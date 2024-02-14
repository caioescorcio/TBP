# TBP
Abordagem em python do problema dos 3 corpos (Three Body Problem) para a disciplina de MAP3122
\documentclass[12pt]{article}
\usepackage{graphicx} % Required for inserting images
\usepackage{fancyhdr} %para colocar um termo no final da página
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage[colorlinks=true,linkcolor=blue,urlcolor=blue]{hyperref}
\pagestyle{fancy}
\newcommand\tab{\hspace*{0.5cm}}
\title{\textbf{Relatório Parcial}}
 
\author{\\Caio Escórcio Lima Dourado \\NUSP: 13680313\and \\Victor Pedreira dos Santos Pepe\\NUSP: 13000000}
\date{21.01.2024}
\fancyhf{}


\cfoot{MAP3122 -- Cursos Coopeerativos -- 2024}
\renewcommand{\headrulewidth}{0pt}

\begin{document}
\begin{titlepage}
\centering
{\fontsize{24}{14}\selectfont \textbf{ Relatório Parcial} }\par
\vspace{0.4cm}
MAP3122 -- Cursos Cooperativos\par
{21.01.2024}\par
\vspace{1cm}

\includegraphics[width=0.9\textwidth]{minerva.jpeg}
\vspace{1cm}

\textbf{Caio Escórcio Lima Dourado}\par
NUSP: 13680313\par
\vspace{0.5cm}

\textbf{Victor Pedreira dos Santos Pepe}\par
NUSP: 13679565
\end{titlepage}
\newpage
\section{Introdução}
\hspace{0.6cm}Johannes Kepler, físico famoso pela elaboração das Leis de Kepler da Astronomia, como bem se sabe, dedicou a maior parte da sua vida ao estudo dos corpos celestes e de suas propriedades. Contudo, seja pela tecnologia da época ou até mesmo pela complexidade matemática que envolve o estudo dos astros, muitos de seus problemas  ficaram em aberto para as próximas gerações.\par
Um grande exemplo de problema não solucionado por Kepler é o Problema dos Dois Corpos, que envolvia a análise do movimento de planetas sujeitos aos campos gravitacionais um do outro. Tal problema, apesar de ter sido proposto e estudado pelo astrônomo em 1609, foi solucionado somente cerca de 78 anos depois, em 1687, graças outro tão famoso físico, Isaac Newton.\par
Assim, tomando como inspiração esse problema quase secular e a relação de movimento Terra-Sol-Lua, surgiu, por volta dos anos 1700, postulado pelo próprio Newton, uma nuance do que seria a ser Problema dos Três Corpos. À época, os objetivos de Newton foram apenas de tentar achar uma estabilidade de movimento entre os corpos do nosso sistema solar, o que não gerou muitas conclusões inovadoras ao considerarmos as suas outras contribuições para a matemática de sua época.\par
Contudo, com as novas leis físicas impostas por Newton, diversos cientistas do mundo inteiro, agora armados como o Cálculo e com as Leis de Newton, estavam dispostos a explorar as lacunas deixadas pelo físico, entre elas, o Problema dos Três Corpos. Assim, com o passar dos anos, tal desafio tornou-se mais e mais famoso no meios científicos, passando pelas mãos de matemáticos como D'Alembert e Poincaré, até chegar à proposição que temos hoje.\par
Fato é, esse problema se perpetuou desde o início da teoria gravitacional até os dias de hoje e, afirmativamente, é objeto de estudo de diversas áreas matemáticas, como busca-se mostrar neste documento.
\newpage
\section{Modelagem Matemática}
\hspace{0.6cm}O Problema dos Três Corpos (\textit{Three-Body Problem}, TBP) atualmente envolve diversas áreas matemática, como Equações Diferenciais, Geometria Euclidiana e até mesmo Caos. Sua proposição mais famosa consiste em um sistema de 3 corpos de mesma massa, esféricos e pontuais, localizados nos vértices de um triângulo pitagórico com lados de 3, de 4 e de 5 unidades arbitrariamente grandes quando comparadas ao raio dos corpos -- \textit{condições iniciais} do sistema -- que são atraídos gravitacionalmente uns pelos outros seguindo a Lei de Newton para Gravitação:\par
\vspace{0.4cm}

\begin{equation*}
\overrightarrow{F} = -{\frac{G\cdot m_1\cdot m_2}{r^2}\cdot \hat{r}}
\end{equation*}
\vspace{0.4cm}

onde:
\vspace{0.4cm}

\begin{itemize}
\item G é uma constante;
\item r é a distância entre os planetas;
\item m1 e m2 são as massas dos planetas 1 e 2, respectivamente;
\end{itemize}\vspace{1cm}
\hspace{0.6cm}Assim, uma vez que:
\vspace{0.4cm}

\begin{equation*}
    \overrightarrow{F_x} = m_x\ddot{r_x}\cdot \hat{r_x}
\end{equation*}
\vspace{0.4cm}

E, levando em consideração o plano vetorial bidimensional em que os corpos se encontram, bem como a interação gravitacional par a par temos os seguinte sistema diferencial:
\vspace{0.4cm}

\begin{equation*}
    \begin{cases}
       \ddot{\overrightarrow{r_1}} = -Gm_2\frac{\overrightarrow{r_1}-\overrightarrow{r_2}}{|\overrightarrow{r_1}-\overrightarrow{r_2}|^3} -Gm_3\frac{\overrightarrow{r_1}-\overrightarrow{r_3}}{\left|\overrightarrow{r_1}-\overrightarrow{r_3}\right|^3} \\
       \\
      \ddot{\overrightarrow{r_2}} = -Gm_1\frac{\overrightarrow{r_2}-\overrightarrow{r_1}}{|\overrightarrow{r_2}-\overrightarrow{r_1}|^3} -Gm_3\frac{\overrightarrow{r_2}-\overrightarrow{r_3}}{\left|\overrightarrow{r_2}-\overrightarrow{r_3}\right|^3}  \\
      \\
      \ddot{\overrightarrow{r_3}} = -Gm_1\frac{\overrightarrow{r_3}-\overrightarrow{r_1}}{|\overrightarrow{r_3}-\overrightarrow{r_1}|^3} -Gm_2\frac{\overrightarrow{r_3}-\overrightarrow{r_2}}{\left|\overrightarrow{r_3}-\overrightarrow{r_2}\right|^3}
      
    \end{cases}       
\end{equation*}

    \vspace{0.4cm}

Assim, a partir da análise de diversos trabalhos de pesquisa que envolvem o TBP, percebeu-se que, dependendo das condições iniciais escolhidas, a abordagem do problema tomaria configurações caóticas, fato que será descorrido em tópicos posteriores. Portanto, uma vez que o propósito deste relatório é essencialmente a análise de equações diferenciais a partir de métodos numéricos para compará-las com resultados previstos, optou-se por escolher uma configuração que obedecesse tal critério de previsibilidade. Então, considerando os inúmeros estudos envolvendo condições iniciais clássicas -- triângulo pitagórico `3-4-5' -- e seus resultados não-caóticos, escolheu-se para essa análise as seguintes circunstâncias:
\vspace{0.4cm}
    
  \begin{equation*}
        \begin{cases}
        \overrightarrow{r_1}_{(0)} = (0, 0, 0);\\
      
        \overrightarrow{r_2}_{(0)} = (4, 0, 0);\\
      
        \overrightarrow{r_3}_{(0)} = (0, 3, 0);\\
        \end{cases}
  \end{equation*}
    
      \vspace{0.4cm}
      
\hspace{0.6cm}Vale destacar que:
\vspace{0.4cm}

\begin{equation*}
\begin{cases}

    |\overrightarrow{r_1{}_2}| = |\overrightarrow{r_2{}_1}| = 4;\\

    |\overrightarrow{r_1{}_3}| = |\overrightarrow{r_3{}_1}| = 3;\\

    |\overrightarrow{r_2{}_3}| = |\overrightarrow{r_3{}_2}| = 5;\\
    
\end{cases}
\end{equation*}
\vspace{0.4cm}

\hspace{0.6cm}Formando o triângulo `3-4-5', e:
\vspace{0.4cm}

\begin{equation*}
    m_1 = m_2 = m_3 = m = 1;
\end{equation*}
\vspace{0.4cm}

Para $\overrightarrow{r_1}$, $\overrightarrow{r_2}$ e $\overrightarrow{r_3}$ vetores do plano $\mathbb{R}^3$ com unidade de medida de distância arbitrária muito maiores que o raio esférico dos corpos -- a fim de garantir a sua característica pontual. Por sua vez, as massas $m_1$, $m_2$ e $m_3$ possuem todas massas escalares reais $m$, também em unidades arbitrárias, para garantir a proporcionalidade das forças e assim atender os critérios para evitar o caos.\par
Adicionalmente, tem-se que também atribuir condições iniciais nulas de velocidade ($\dot{\vec{r}}$) a fim de se ter puramente o movimento das forças gravitacionais, então:
\vspace{0.4cm}

    \begin{equation*}
        \dot{\overrightarrow{r_1}}_{(0)} = \dot{\overrightarrow{r_2}}_{(0)} = \dot{\overrightarrow{r_3}}_{(0)} = (0, 0, 0);
    \end{equation*}
    \vspace{0.4cm}
    
Em unidades arbitrárias de velocidade.
\vspace{0.4cm}

\begin{center}
    ------------------------------------------------------------------------------------------
\end{center}
\vspace{0.4cm}

Para adaptar o TBP para uma forma legível para discretização, são necessárias algumas tranformações de variáveis já que, essencialmente, esse problema contém configurações de EDO's de segunda ordem (acelerações). Transformações essas que, por comodidade, envolvem o seguinte modelo:
\vspace{0.4cm}

\begin{equation*}
    \ddot{y} = \frac{d\dot{y}}{dt} = \frac{d(f(y, t))}{dt} = F(y,t)
\end{equation*}

\begin{equation*}\rightarrow
\begin{cases}
        \dot{y} = h\\

        \dot{h} = F(y,t) \\
\end{cases}
\end{equation*}
\vspace{0.4cm}

Que aumenta o número de variáveis do sistema. Portanto, ao aplicar essa tranformação em cada um dos eixos x, y e z do $\mathbb{R}^3$ nos vetores que descrevem os movimentos dos corpos, temos:
\vspace{0.4cm}

\begin{equation*}
    \begin{cases}
        \dot{\overrightarrow{r_1}} = \overrightarrow{v_1}\\ 
        \dot{\overrightarrow{r_2}} = \overrightarrow{v_2}\\ 
        \dot{\overrightarrow{r_3}} = \overrightarrow{v_3}\\ \\
        \dot{\overrightarrow{v_1}} = -Gm_2\frac{\overrightarrow{r_1}-\overrightarrow{r_2}}{|\overrightarrow{r_1}-\overrightarrow{r_2}|^3} -Gm_3\frac{\overrightarrow{r_1}-\overrightarrow{r_3}}{\left|\overrightarrow{r_1}-\overrightarrow{r_3}\right|^3} \\
        \\
        \dot{\overrightarrow{v_2}} = -Gm_1\frac{\overrightarrow{r_2}-\overrightarrow{r_1}}{|\overrightarrow{r_2}-\overrightarrow{r_1}|^3} -Gm_3\frac{\overrightarrow{r_2}-\overrightarrow{r_3}}{\left|\overrightarrow{r_2}-\overrightarrow{r_3}\right|^3}  \\
        \\
        \dot{\overrightarrow{v_3}} = -Gm_1\frac{\overrightarrow{r_3}-\overrightarrow{r_1}}{|\overrightarrow{r_3}-\overrightarrow{r_1}|^3} -Gm_2\frac{\overrightarrow{r_3}-\overrightarrow{r_2}}{\left|\overrightarrow{r_3}-\overrightarrow{r_2}\right|^3}
    \end{cases}
\end{equation*}
\vspace{0.4cm}

Vale ressaltar que, apesar de todos os vetores possuírem dimensionalidade 3, o fato deles pertencerem inicalmente ao mesmo triângulo no plano $z=0$ e inexistirem forças externas atuando no eixo z do sistema -- vide 1ª lei de Newton -- pode-se considerar o sistema como bidimensional. 
 \newpage
 \section{Bibliografia}
A bibliografia utilizada até agora foi:
 \begin{itemize}
     \item \href{https://www.feis.unesp.br/#!/departamentos/fisica-e-quimica/grupo-de-pesquisa/gaais/grandes-cientista/johannes-kleper/}{UNESP: História de Newton}
     \item \href{https://www.feis.unesp.br/#!/departamentos/fisica-e-quimica/grupo-de-pesquisa/gaais/grandes-cientista/isaac-newton/}{UNESP: História de Kepler}
     \item \href{https://en.wikipedia.org/wiki/Three-body_problem}{Wikipedia: Three-Body Problem} 
     \item \href{https://en.wikipedia.org/wiki/Poincar%C3%A9_and_the_Three-Body_Problem}{Wikipedia: Poincaré and the Three-Body Problem}
     \item \href{https://www.google.com/search?q=simulation+three+body+problem&sca_esv=597544494&ei=lhigZeG_Ea7e1sQPvt2AmAk&udm=&oq=simulaton+of+three+bod&gs_lp=Egxnd3Mtd2l6LXNlcnAiFnNpbXVsYXRvbiBvZiB0aHJlZSBib2QqAggAMgYQABgWGB5IpLEBUOYaWI2iAXAQeACQAQSYAecBoAGpKqoBBjAuMzYuMrgBAcgBAPgBAagCCsICBxAhGAoYoAHCAgUQIRigAcICFhAAGAMYjwEY5QIY6gIYtAIYjAPYAQHCAhYQLhgDGI8BGOUCGOoCGLQCGIwD2AEBwgIIEC4YsQMYgATCAhEQLhiABBixAxiDARjHARjRA8ICCBAuGIAEGLEDwgIIEAAYgAQYsQPCAgsQABiABBixAxiDAcICDhAAGIAEGIoFGLEDGIMBwgIXEC4YsQMYgAQYlwUY3AQY3gQY4ATYAQLCAgoQABiABBiKBRhDwgIFEAAYgATCAg4QLhiABBjHARivARiOBcICCxAuGIAEGMcBGK8BwgIHEAAYgAQYCsICHRAuGIAEGMcBGK8BGI4FGJcFGNwEGN4EGOAE2AECwgITEC4YChiDARjHARixAxjRAxiABMICBRAuGIAEwgIKEAAYgAQYChixA8ICEBAAGIAEGIoFGEMYsQMYgwHCAggQLhiABBjUAsICDRAuGIAEGAoYxwEY0QPCAgkQABiABBgNGArCAgcQABiABBgNwgIHEC4YgAQYDcICCBAAGB4YDRgPwgIGEAAYHhgNwgIJEAAYgAQYDRgTwgIIEAAYHhgNGBPCAgoQABgeGA0YDxgTwgIIEAAYFhgeGBPCAgoQABgFGB4YDRgTwgIKEAAYCBgeGA0YE8ICChAAGBYYHhgTGArCAgwQABgFGB4YDRgPGBPCAgoQABgWGB4YDxgTwgIFECEYnwXiAwQYASBBiAYBugYECAEYCroGBggCEAEYFA&sclient=gws-wiz-serp#fpstate=ive&vld=cid:186afdfa,vid:cev3g826iIQ,st:0}{Material da disciplina: Three-Body Problem: A Precise Simulation}
     \item \href{https://www.wolframscience.com/reference/notes/972d/}{Stephen Wolfram, A New Kind of Science -- Notes for Chapter 7: Mechanisms in Programs and Nature; Section: Chaos Theory and Randomness from Initial Conditions}
     \item \href{https://articles.adsabs.harvard.edu/pdf/1967AJ.....72..876S}{Artigos Harvard: The Complete Solution of a General Problem of Three Bodies; Victor Szebehely and C. Frederick Peters}
     \item \href{https://plato.stanford.edu/entries/chaos/}{Stanford Encyclopedia of Philosophy -- Chaos, 2008}
     \item \href{https://cmup.fc.up.pt/cmup/relatividade/3Corpos/3corpos.html}{Oliveira, V., Cruz, I. -- O Problema dos Três Corpos}
 \end{itemize}


\end{document}
