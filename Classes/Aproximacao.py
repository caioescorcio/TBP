import numpy as np

#precisao = casas depois da virgula que se quer a precisao
#a funcao a ser utilizada deve ser PHI(X)
class Aproximacao:

    def MAS(intervalo, funcao, precisao):
        x_0 = intervalo[0]
        x_medio = (intervalo[0] + intervalo[1])/2

        #Metodo do roma para achar o ponto inicial da iteracao, supondo o TPF satisfeito
        if(round(x_medio, precisao) == round(funcao(x_medio), precisao)):
            return x_medio

        if(funcao(x_medio) > x_medio):
            x_0 = intervalo[1]
        
        return round(iteracao(x_0, funcao, precisao), precisao)
            

#funcao para fazer iteracao, recursiva
def iteracao(x, funcao, precisao):
    
    if(round(x, precisao) == round(funcao(x), precisao)):
        return x

    return iteracao(funcao(x), funcao, precisao)