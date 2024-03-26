import numpy as np
from Classes.Planeta import Planeta

massa = 1
G = 1

class Discretizacao:
    
    def __init__(self):
        pass
    
    #f(t, y) para o caso dos planetas
    def f(self, t, y): #y_k[i]
        #funcao para calcular a aceleracao
        a1 = lambda c1, c2, c3: c1.ac_rel(c2) + c1.ac_rel(c3)
        a2 = lambda c1, c2, c3: c2.ac_rel(c1) + c2.ac_rel(c3)
        a3 = lambda c1, c2, c3: c3.ac_rel(c2) + c3.ac_rel(c1)

        #Criando os planetas
        planeta_1 = Planeta(np.array([y[0], y[1]]), massa, np.array([y[6], y[7]]))
        planeta_2 = Planeta(np.array([y[2], y[3]]), massa, np.array([y[8], y[9]]))
        planeta_3 = Planeta(np.array([y[4], y[5]]), massa, np.array([y[10], y[11]]))

        #declara o vetor de retorno
        k = np.array([0.0, 0.0,
                      0.0, 0.0,
                      0.0, 0.0,
                      0.0, 0.0,
                      0.0, 0.0,
                      0.0, 0.0])

        #derivada da posicao = velocidade
        k[0], k[1] = planeta_1.velocidade[0], planeta_1.velocidade[1] 
        k[2], k[3] = planeta_2.velocidade[0], planeta_2.velocidade[1] 
        k[4], k[5] = planeta_3.velocidade[0], planeta_3.velocidade[1] 

        #derivada da velocidade = aceleracao
        k[6], k[7] = a1(planeta_1, planeta_2, planeta_3)
        k[8], k[9] = a2(planeta_1, planeta_2, planeta_3)
        k[10], k[11] = a3(planeta_1, planeta_2, planeta_3)

        return k

    #phi generico
    def phi(self, t, y, h, TBP):
        
        if TBP:
            func = self.f
        else:
            func = self.f_manufaturada
        #declarando phi do Runge-Kutta
        k_1 = h*func(t, y)
        k_2 = h*func(t + h/2, y + k_1/2)
        k_3 = h*func(t + h/2, y + k_2/2)
        k_4 = h*func(t + h, y + k_3)

        return (k_1 + 2*k_2 + 2*k_3 + k_4)/6

    def f_manufaturada(self, t, y): 
        """f = y' ; y = e^(3t)*sin(5t) - 5; y(0) = -5"""
        return np.exp(3*t)*3*np.sin(5*t) + 5*np.exp(3*t)*np.cos(5*t)
    
    def exata_manufaturada(self, t):
        """y = e^(3t)*sin(5t) - 5"""
        return np.exp(3*t)*np.sin(5*t) - 5

    #metodo de discretizacao
    def calcula(self, n, intervalo_t, dim, TBP):
        #discretizacao do intervalo
        h = (intervalo_t[1] - intervalo_t[0])/n

        if TBP:
            #PLANETAS
            #inicializacao das variaveis
            i = 0
            t_k = np.zeros((30*n+1, 1))
            y_k = np.zeros((30*n+1, dim))
            
            #inicializacao das condicoes iniciais
            t_k[0] = intervalo_t[0]
            y_k[0] = np.array([
                -0.97000436, 0.24308753,        #R_1: 0, 1
                0.97000436, -0.24308753,        #R_2: 2, 3
                0, 0,                           #R_3: 4, 5

                0.4662036850, 0.4323657300,     #V_1: 6, 7
                0.4662036850, 0.4323657300,     #V_2: 8, 9
                -0.93240737, -0.86473146        #V_3: 10, 11
            ])  
            #loop para calcular valores de y        
            for i in range(30*n):
                y_k[i+1] = y_k[i] + self.phi(t_k[i], y_k[i], h, TBP)
                t_k[i+1] = t_k[i] + h
            
        else:
            #MANUFATURA
            t_k = np.zeros((n+1, 1))
            y_k = np.zeros((n+1, dim))
            y_k[0] = np.array([-5])
        #loop para calcular os valores de y
            for i in range(n):
                y_k[i+1] = y_k[i] + self.phi(t_k[i], y_k[i], h, TBP)
                t_k[i+1] = t_k[i] + h
        
        return y_k, t_k
    
    def converte(self, n, TBP):
        """n: numero de passos
           TBP: True se for para os planetas, False se for para a manufatura"""
        if TBP:
            #PLANETAS
            y_k, t_k = self.calcula(n, [0, 1], 12, TBP)
            pos1 = np.array([y_k[0][0], y_k[0][1]])
            pos2 = np.array([y_k[0][2], y_k[0][3]])
            pos3 = np.array([y_k[0][4], y_k[0][5]])
            for i in range(30*n):
                pos1 = np.vstack([pos1, np.array([y_k[i][0], y_k[i][1]])])
                pos2 = np.vstack([pos2, np.array([y_k[i][2], y_k[i][3]])])
                pos3 = np.vstack([pos3, np.array([y_k[i][4], y_k[i][5]])])
            return pos1, pos2, pos3, t_k
        
        else:
            #MANUFATURA
            y_k, t_k = self.calcula(n, [0, 2], 1, TBP)
            i = 1
            return y_k, t_k
    
    def rungekutta_planetas(self, corpo_1, corpo_2, corpo_3, n, T):

        def nova_ac(corpo_atual, corpo_outro_1, corpo_outro_2, h, k, k1, k2):
            corpo_aux = Planeta(corpo_atual.posicao + k*h, corpo_atual.massa, corpo_atual.velocidade)
            corpo_aux1 = Planeta(corpo_outro_1.posicao + k1*h, corpo_outro_1.massa, corpo_outro_1.velocidade)
            corpo_aux2 = Planeta(corpo_outro_2.posicao + k2*h, corpo_outro_2.massa, corpo_outro_2.velocidade)
            
            return corpo_aux.ac_rel(corpo_aux1) + corpo_aux.ac_rel(corpo_aux2)
        
        #discretizacao do intervalo
        h = T/n
        
        #array de corpos
        corpos = np.array([corpo_1, corpo_2, corpo_3])

        #definicao das funcoes para discretizar
        a1 = lambda c1, c2, c3: c1.ac_rel(c2) + c1.ac_rel(c3)
        a2 = lambda c1, c2, c3: c2.ac_rel(c1) + c2.ac_rel(c3)
        a3 = lambda c1, c2, c3: c3.ac_rel(c2) + c3.ac_rel(c1)
        v = lambda c: c.velocidade
        pos1 = np.array(corpo_1.posicao)
        pos2 = np.array(corpo_2.posicao)
        pos3 = np.array(corpo_3.posicao)
        
        #array de termos do RK para posicao e velocidade (3 corpos, 4 passos no RK, 2 componentes para posicao e velocidade)
        #k guarda valores de posicao e l valores de velocidade
        
        t = 0
        #loop para calcular os valores
        while t < 30*T:

            #K1
            kr1_1 = v(corpo_1)
            kv1_1 = a1(corpo_1, corpo_2, corpo_3)
            
            kr1_2 = v(corpo_2)
            kv1_2 = a2(corpo_1, corpo_2, corpo_3)
            
            kr1_3 = v(corpo_3)
            kv1_3 = a3(corpo_1, corpo_2, corpo_3)

            #K2
            kr2_1 = v(corpo_1) + h*kv1_1/2
            kv2_1 = nova_ac(corpo_1, corpo_2, corpo_3, h/2, kr1_1, kr1_2, kr1_3)

            kr2_2 = v(corpo_2) + h*kv1_2/2
            kv2_2 = nova_ac(corpo_2, corpo_1, corpo_3, h/2, kr1_2, kr1_1, kr1_3)

            kr2_3 = v(corpo_3) + h*kv1_3/2
            kv2_3 = nova_ac(corpo_3, corpo_1, corpo_2, h/2, kr1_3, kr1_1, kr1_2)

            #K3
            kr3_1 = v(corpo_1) + h*kv2_1/2
            kv3_1 = nova_ac(corpo_1, corpo_2, corpo_3, h/2, kr2_1, kr2_2, kr2_3)

            kr3_2 = v(corpo_2) + h*kv2_2/2
            kv3_2 = nova_ac(corpo_2, corpo_1, corpo_3, h/2, kr2_2, kr2_1, kr2_3)
            
            kr3_3 = v(corpo_3) + h*kv2_3/2
            kv3_3 = nova_ac(corpo_3, corpo_1, corpo_2, h/2, kr2_3, kr2_1, kr2_2)

            #K4
            kr4_1 = v(corpo_1) + h*kv3_1
            kv4_1 = nova_ac(corpo_1, corpo_2, corpo_3, h, kr3_1, kr3_2, kr3_3)

            kr4_2 = v(corpo_2) + h*kv3_2
            kv4_2 = nova_ac(corpo_2, corpo_1, corpo_3, h, kr3_2, kr3_1, kr3_3)

            kr4_3 = v(corpo_3) + h*kv3_3
            kv4_3 = nova_ac(corpo_3, corpo_1, corpo_2, h, kr3_3, kr3_1, kr3_2)

            corpo_1.posicao    = corpo_1.posicao + h*(kr1_1 +2*kr2_1 + 2*kr3_1 + kr4_1)/6
            corpo_1.velocidade = corpo_1.velocidade +h*(kv1_1 +2*kv2_1 + 2*kv3_1 + kv4_1)/6
            pos1 = np.vstack([pos1, corpo_1.posicao])

            corpo_2.posicao    = corpo_2.posicao + h*(kr1_2 +2*kr2_2 + 2*kr3_2 + kr4_2)/6
            corpo_2.velocidade = corpo_2.velocidade +h*(kv1_2 +2*kv2_2 + 2*kv3_2 + kv4_2)/6
            pos2 = np.vstack([pos2, corpo_2.posicao])

            corpo_3.posicao    = corpo_3.posicao + h*(kr1_3 +2*kr2_3 + 2*kr3_3 + kr4_3)/6
            corpo_3.velocidade = corpo_3.velocidade +h*(kv1_3 +2*kv2_3 + 2*kv3_3 + kv4_3)/6
            pos3 = np.vstack([pos3, corpo_3.posicao])

            t += h
            
        return pos1, pos2, pos3

