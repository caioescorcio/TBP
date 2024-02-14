import numpy as np

#precisao = casas depois da virgula que se quer a precisao

def MAS(intervalo:np.array[2], funcao, precisao):
    x_0 = intervalo[0]
    x_medio = (intervalo[0] + intervalo[1])/2


    #Metodo do roma para achar o ponto inicial da iteracao, supondo o TPF satisfeito
    if(funcao(x_medio)%(10**(-precisao)) == x_medio%(10**(-precisao))):
        return x_medio

    if(funcao(x_medio) > x_medio):
        x_0 = intervalo[1]
    
    return iteracao(x_0, funcao, precisao)
    
    
#funcao para fazer iteracao, recursiva
def iteracao(x, funcao, precisao):
    
    if(x%(10**(-precisao)) == funcao(x)%(10**(-precisao))):
        return x
    return iteracao(funcao(x), funcao, precisao)