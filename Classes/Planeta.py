import numpy as np

#Definicao de variaveis globais
G = 1 #fonte: https://pt.wikipedia.org/wiki/Constante_gravitacional_universal 6,6743 × 10-11

class Planeta:
    
    #Construtor do planeta   
    #Cada planeta possui posicao, massa e velocidade como caracteristicas instrinsecas
    def __init__ (self, posicao:np.array, massa:int, velocidade:np.array):
        self.posicao = posicao
        self.massa = massa
        self.velocidade = velocidade
        
    #Mede a distancia entre dois planetas (funcao estatica)
    def distancia (planeta_1, planeta_2):
        delta = planeta_1.posicao - planeta_2.posicao
        d = np.sqrt(delta.dot(delta)) #raiz do produto escalar entre duas distancias vetoriais
        
        return d #retorna a distancia escalar entre dois vetores
    
    #Calcula a aceleracao causada em um planeta por outro planeta
    def ac_rel (self, planeta_outro):
        ac = np.array([0, 0])
        if(np.any(self.posicao != planeta_outro.posicao) and self.distancia(planeta_outro) > 0.26):
            ac = ((-1)*G*(planeta_outro.massa)*np.subtract(self.posicao, planeta_outro.posicao))/(Planeta.distancia(self, planeta_outro)**3) #ac_rel 1 para 2 = -G*(R_1 - R_2)/d^3
        else:
            self.velocidade, planeta_outro.velocidade = planeta_outro.velocidade, self.velocidade #colisao
            
        return ac
    
    # def ac_rel (self, planeta_outro):
    #     ac = np.array([0, 0])
    #     if(np.any(self.posicao != planeta_outro.posicao)):
    #         ac = ((-1)*G*(planeta_outro.massa)*np.subtract(self.posicao, planeta_outro.posicao))/(Planeta.distancia(self, planeta_outro)**3) #ac_rel 1 para 2 = -G*(R_1 - R_2)/d^3
    #     if(self.distancia(planeta_outro) < 0.2):
    #         self.velocidade, planeta_outro.velocidade = planeta_outro.velocidade, self.velocidade
    #         ac = -ac
            
    #     return ac


