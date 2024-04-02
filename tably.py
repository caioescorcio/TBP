import argparse
import csv
import os

#!/usr/bin/env python3

# Para chamar diretamente o tably a partir do shell, crie um link simbólico executando
# ln -sf $PWD/tably.py /usr/local/bin/tably



PREAMBLE = r"""\documentclass[11pt, a4paper]{article}
\usepackage{booktabs}
\begin{document}"""

HEADER = r"""\begin{{table}}[htb]
{indent}\centering{caption}{label}
{indent}\begin{{tabular}}{{@{{}}{align}@{{}}}}
{indent}{indent}\toprule"""

FOOTER = r"""{indent}{indent}\bottomrule
{indent}\end{{tabular}}
\end{{table}}"""

LABEL = '\n{indent}\\label{{{label}}}'
CAPTION = '\n{indent}\\caption{{{caption}}}'


class Tably:
    """Objeto que armazena os argumentos analisados.

    Métodos:
        run: seleciona os métodos apropriados para gerar código/arquivos LaTeX
        create_table: para cada arquivo especificado, cria uma tabela LaTeX
        create_row: cria uma linha com base no conteúdo da `line`
        combine_tables: combina todas as tabelas dos arquivos de entrada
        save_single_table: cria e salva uma única tabela LaTeX
        get_units: escreve as unidades como uma linha da tabela LaTeX
    """

    def __init__(self, args):
        """
        Atributos:
            files (string): nome(s) do(s) arquivo(s) .csv
            no_header (bool): se o .csv contém apenas conteúdo, sem um
                cabeçalho (nomes das colunas)
            caption (string): o nome da tabela, impresso acima dela
            label (string): um rótulo pelo qual a tabela pode ser referenciada
            align (string): alinhamento desejado das colunas
            no_indent (bool): deve o código LaTeX ser indentado com 4 espaços por
                bloco de código. Não afeta a aparência final da tabela.
            outfile (string): nome do arquivo onde salvar os resultados.
            separate_outfiles (list): nomes dos arquivos onde cada tabela é salva
            skip (int): número de linhas no .csv para pular
            preamble(bool): criar um preâmbulo
            sep (string): separador de colunas
            units (list): unidades para cada coluna
            fragment (bool): apenas saída de conteúdo no ambiente tabular
            fragment_skip_header (bool): atalho para passar -k 1 -n -f
            replace (bool): substituir arquivo de saída existente se -o for passado
            tex_str (function): escapar caracteres especiais do LaTeX ou não fazer nada
        """
        self.files = args.files
        self.no_header = args.no_header
        self.caption = args.caption
        self.label = args.label
        self.align = args.align
        self.no_indent = args.no_indent
        self.outfile = args.outfile
        self.separate_outfiles = args.separate_outfiles
        self.skip = args.skip
        self.preamble = args.preamble
        self.sep = get_sep(args.sep)
        self.units = args.units
        self.fragment = args.fragment
        self.fragment_skip_header = args.fragment_skip_header
        self.replace = args.replace
        self.tex_str = escape if not args.no_escape else lambda x: x

    def run(self):
        """O método principal.

        Se todas as tabelas precisarem ser colocadas em um único arquivo,
        chama o método `combine_tables` para gerar o código LaTeX
        e em seguida chama a função `save_content` se `outfile` for fornecido;
        caso contrário, imprime no console.
        Se cada tabela precisar ser colocada em um arquivo separado,
        chama o método `save_single_table` para criar e salvar cada tabela separadamente.
        """

        if self.fragment_skip_header:
            self.skip = 1
            self.no_header = True
            self.fragment = True

        if self.fragment:
            self.no_indent = True
            self.label = None
            self.preamble = False

        # se todas as tabelas precisarem ser colocadas em um único arquivo
        if self.outfile or self.separate_outfiles is None:
            final_content = self.combine_tables()
            if not final_content:
                return
            if self.outfile:
                try:
                    save_content(final_content, self.outfile, self.replace)
                except FileNotFoundError:
                    print('{} não é um caminho válido/conhecido. Não foi possível salvar lá.'.format(self.outfile))
            else:
                print(final_content)

        # se -oo for passado (pode ser [])
        if self.separate_outfiles is not None:
            outs = self.separate_outfiles
            if len(outs) == 0:
                outs = [ os.path.splitext(file)[0]+'.tex' for file in self.files ]
            elif os.path.isdir(outs[0]):
                outs = [ os.path.join(outs[0], os.path.splitext(os.path.basename(file))[0])+'.tex' for file in self.files ]
            elif len(outs) != len(self.files):
                print('AVISO: O número de arquivos .csv e o número de arquivos de saída não correspondem!')
            for file, out in zip(self.files, outs):
                self.save_single_table(file, out)

    def create_table(self, file):
        """Cria uma tabela a partir de um arquivo .csv fornecido.

        Este método fornece o procedimento de conversão de um arquivo .csv em uma tabela LaTeX.
        A menos que -f seja especificado, a saída é um ambiente de tabela LaTeX pronto para uso.
        Todos os outros métodos que precisam obter uma tabela LaTeX de um arquivo .csv chamam este método.
        """
        rows = []
        indent = 4*' ' if not self.no_indent else ''

        try:
            with open(file) as infile:
                for i, columns in enumerate(csv.reader(infile, delimiter=self.sep)):
                    if i < self.skip:
                        continue
                    rows.append(self.create_row(columns, indent))
        except FileNotFoundError:
            print("O arquivo {} não existe!!\n".format(file))
            return ''
        if not rows:
            print("Nenhuma tabela criada a partir do arquivo {}. Verifique se o arquivo está vazio "
                  "ou se você usou um valor de pular muito alto.\n".format(file))
            return ''

        if not self.no_header:
            rows.insert(1, r'{0}{0}\midrule'.format(indent))
            if self.units:
                rows[0] = rows[0] + r'\relax' # corrige problema com \[
                units = self.get_units()
                rows.insert(1, r'{0}{0}{1} \\'.format(indent, units))

        content = '\n'.join(rows)
        if not self.fragment:
            header = HEADER.format(
            label=add_label(self.label, indent),
            caption=add_caption(self.caption, indent),
            align=format_alignment(self.align, len(columns)),
            indent=indent,
            )
            footer = FOOTER.format(indent=indent)
            return '\n'.join((header, content, footer))
        else:
            return content

    def create_row(self, line, indent):
        """Cria uma linha com base no conteúdo da `line`"""
        return r'{indent}{indent}{content} \\ \hline'.format(
             indent=indent,
             content=' & '.join(self.tex_str(line)))

    def combine_tables(self):
        """Combina todas as tabelas e adiciona um preâmbulo, se necessário.

        A menos que -oo seja especificado, assim são organizadas as tabelas de entrada.
        """
        all_tables = []
        if self.label and len(self.files) > 1:
            all_tables.append("% não se esqueça de rotular manualmente as tabelas")

        for file in self.files:
            table = self.create_table(file)
            if table:
                all_tables.append(table)
        if not all_tables:
            return None
        if self.preamble:
            all_tables.insert(0, PREAMBLE)
            all_tables.append('\\end{document}\n')
        return '\n\n'.join(all_tables)

    def save_single_table(self, file, out):
        """Cria e salva uma única tabela LaTeX"""
        table = [self.create_table(file)]
        if table:
            if self.preamble:
                table.insert(0, PREAMBLE)
                table.append('\\end{document}\n')
            final_content = '\n\n'.join(table)
            try:
                save_content(final_content, out, self.replace)
            except FileNotFoundError:
                print('{} não é um caminho válido/conhecido. Não foi possível salvar lá.'.format(out))

    def get_units(self):
        """Escreve as unidades como uma linha da tabela LaTeX"""
        formatted_units = []
        for unit in self.tex_str(self.units):
            if unit in '-/0':
                formatted_units.append('')
            else:
                formatted_units.append('[{}]'.format(unit))
        return ' & '.join(formatted_units)


def get_sep(sep):
    if sep.lower() in ['t', 'tab', '\\t']:
        return '\t'
    elif sep.lower() in ['s', 'semi', ';']:
        return ';'
    elif sep.lower() in ['c', 'comma', ',']:
        return ','
    else:
        return sep


def escape(line):
    """Escapa caracteres especiais do LaTeX prefixando-os com uma barra invertida"""
    for char in '#$%&_}{':
        line = [column.replace(char, '\\'+char) for column in line]
    return line


def format_alignment(align, length):
    """Garante que o alinhamento fornecido seja válido:
    1. o comprimento do alinhamento é 1 ou o mesmo que o número de colunas
    2. os caracteres válidos são `l`, `c` e `r`

    Se houver um caractere inválido, todas as colunas são definidas como alinhamento centralizado.
    Se o comprimento do alinhamento for muito longo, ele é reduzido para caber no número de colunas.
    Se o comprimento do alinhamento for muito curto, ele é preenchido com `c` para as colunas faltantes.
    """
    if any(ch not in 'lcr' for ch in align):
        align = 'c'

    if len(align) == 1:
        return length * align
    elif len(align) == length:
        return align
    else:
        return '{:c<{l}.{l}}'.format(align, l=length)


def add_label(label, indent):
    """Cria um rótulo para a tabela"""
    return LABEL.format(label=label, indent=indent) if label else ''


def add_caption(caption, indent):
    """Cria uma legenda para a tabela"""
    return CAPTION.format(caption=caption, indent=indent) if caption else ''


def save_content(content, outfile, replace):
    """Salva o conteúdo em um arquivo.

    Se um arquivo existente for fornecido, o conteúdo é anexado ao final
    do arquivo por padrão. Se -r for passado, o arquivo é substituído.
    """
    if replace:
        with open(outfile, 'w') as out:
            out.writelines(content)
        print('O conteúdo foi escrito em', outfile)
    else:
        with open(outfile, 'a') as out:
            out.writelines(content)
        print('O conteúdo foi anexado a', outfile)



def arg_parser():
    """Analisa os argumentos da linha de comando e fornece --help"""
    parser = argparse.ArgumentParser(description="Cria tabelas LaTeX a partir de arquivos .csv")

    parser.add_argument(
        'files',
        nargs='+',
        help='Arquivo(s) .csv contendo os dados que você deseja exportar.'
    )
    parser.add_argument(
        '-a', '--align',
        default='c',
        help='Alinhamento das colunas da tabela. '
             'Use `l`, `c` e `r` para esquerda, centro e direita. '
             'Um único caractere para todas as colunas ou um caractere por coluna. '
             'Padrão: c'
    )
    parser.add_argument(
        '-c', '--caption',
        help='Legenda da tabela. '
             'Padrão: Nenhum'
    )
    parser.add_argument(
        '-i', '--no-indent',
        action='store_true',
        help='Passe isso se você não quiser indentar o código fonte LaTeX '
             'com 4 espaços por bloco. Nenhuma diferença no resultado final (pdf). '
             'Padrão: False'
    )
    parser.add_argument(
        '-k', '--skip',
        type=int,
        default=0,
        help='Número de linhas no .csv para pular. Padrão: 0'
    )
    parser.add_argument(
        '-l', '--label',
        help='Rótulo da tabela, para referenciá-la. Padrão: Nenhum'
    )
    parser.add_argument(
        '-n', '--no-header',
        action='store_true',
        help='Por padrão, a primeira linha do .csv é usada como cabeçalho da tabela. '
             'Passe esta opção se não houver cabeçalho. Padrão: False'
    )
    parser.add_argument(
        '-o', '--outfile',
        help='Escolha um arquivo de saída para salvar os resultados. '
             'Os resultados são anexados ao arquivo (adicionados após a última linha). '
             'Padrão: Nenhum, imprime no console.'
    )
    parser.add_argument(
        '-oo', '--separate-outfiles',
        metavar='PATH',
        nargs='*',
        help='Quando vários arquivos .csv precisam ser processados, '
             'passe -oo para salvar cada tabela individual em um arquivo .tex separado. '
             'Para especificar cada arquivo de saída individualmente, '
             'passe uma lista de nomes de arquivos após -oo. '
             'Alternativamente, passe um diretório que armazenará todos os arquivos de saída. '
             'Se nenhum nome de arquivo/diretório for passado após -oo, '
             'serão usados os nomes de arquivos .csv (com extensão .tex).'
    )
    parser.add_argument(
        '-p', '--preamble',
        action='store_true',
        help='Se selecionado, cria um documento .tex completo (incluindo o preâmbulo) '
             'pronto para ser compilado como .pdf. Útil ao tentar fazer um relatório rápido. '
             'Padrão: False'
    )
    parser.add_argument(
        '-s', '--sep',
        default=',',
        help=r'Escolha um separador entre colunas. Se um arquivo estiver separado por tabulação, '
             r'passe `t` ou `tab`. Se um arquivo estiver separado por ponto e vírgula, '
             r'passe `s`, `semi` ou `\;`.'
             r'Padrão: `,` (separado por vírgula)'
    )
    parser.add_argument(
        '-u', '--units',
        nargs='+',
        help='Forneça unidades para cada coluna. Se a coluna não tiver unidade, denote-a '
             'passando `-`, `/` ou `0`. Se `--no-header` for usado, '
             'este argumento será ignorado.'
    )
    parser.add_argument(
        '-e', '--no-escape',
        action='store_true',
        help='Se selecionado, não escape caracteres especiais do LaTeX.'
    )
    parser.add_argument(
        '-f', '--fragment',
        action='store_true',
        help='Se selecionado, apenas saída de conteúdo dentro do ambiente tabular '
             '(sem preâmbulo, ambiente de tabela, etc.).'
    )
    parser.add_argument(
        '-ff', '--fragment-skip-header',
        action='store_true',
        help='Equivalente a passar -k 1 -n -f '
             '(suprimir cabeçalho quando eles estão na primeira linha do .csv e passar -f).'
    )
    parser.add_argument(
        '-r', '--replace',
        action='store_true',
        help='Se selecionado e -o ou -oo for passado, substitui qualquer arquivo de saída existente.'
    )
    return parser.parse_args()


def main():
    options = arg_parser()
    tably = Tably(options)
    tably.run()


if __name__ == '__main__':
    main()
