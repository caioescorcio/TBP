import numpy as np
from Classes.Planeta import Planeta
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Discretizacao:
    
    def __init__(self):
        pass
        
    
    def rungekutta(self, y_0, f, n, intervalo_t):
        #discretizacao do intervalo
        h = (intervalo_t[1] - intervalo_t[0])/n

        #inicializacao das variaveis
        t = intervalo_t[0]
        y = y_0
        v_t = [t]
        v_y = [y]

        #loop para calcular os valores de y
        while t < intervalo_t[1]:
            k_1 = h*f(t, y)
            k_2 = h*f(t + h/2, y + k_1/2)
            k_3 = h*f(t +h/2, y + k_2/2)
            k_4 = h*f(t + h, y + k_3)

            y = y + (k_1 + 2*k_2 + 2*k_3 + k_4)/6
            t = t + h
            v_t.append(t)
            v_y.append(y)
            
        return v_t, v_y
    
    
    def rungekutta_planetas(self, corpo_1, corpo_2, corpo_3, n, T):

        def nova_ac(corpo_atual, corpo_outro_1, corpo_outro_2, h, k):
            corpo_aux = Planeta(corpo_atual.posicao + k*h, corpo_atual.massa, corpo_atual.velocidade)
            return corpo_aux.ac_rel(corpo_outro_1) + corpo_aux.ac_rel(corpo_outro_2)
        
        #discretizacao do intervalo
        h = T/n
        
        #array de corpos
        corpos = np.array([corpo_1, corpo_2, corpo_3])

        #definicao das funcoes para discretizar
        a1 = lambda c1, c2, c3: c1.ac_rel(c2) + c1.ac_rel(c3)
        a2 = lambda c1, c2, c3: c2.ac_rel(c1) + c2.ac_rel(c3)
        a3 = lambda c1, c2, c3: c3.ac_rel(c2) + c3.ac_rel(c1)
        v = lambda c: c.velocidade
        pos1 = np.array([corpo_1.posicao[0],corpo_1.posicao[1]])
        pos2 = np.array([corpo_2.posicao[0],corpo_2.posicao[1]])
        pos3 = np.array([corpo_3.posicao[0],corpo_3.posicao[1]])
        
        #array de termos do RK para posicao e velocidade (3 corpos, 4 passos no RK, 2 componentes para posicao e velocidade)
        #k guarda valores de posicao e l valores de velocidade
        
        t = 0
        #loop para calcular os valores
        while t < T:

            #corpo 1
            kr1_1 = v(corpo_1)
            kv1_1 = a1(corpo_1, corpo_2, corpo_3)

            kr2_1 = v(corpo_1) + h*kv1_1/2
            kv2_1 = nova_ac(corpo_1, corpo_2, corpo_3, h/2, kr1_1)

            kr3_1 = v(corpo_1) + h*kv2_1/2
            kv3_1 = nova_ac(corpo_1, corpo_2, corpo_3, h/2, kr2_1)

            kr4_1 = v(corpo_1) + h*kv3_1
            kv4_1 = nova_ac(corpo_1, corpo_2, corpo_3, h, kr3_1)

            corpo_1.posicao    = corpo_1.posicao + h*(kr1_1 +2*kr2_1 + 2*kr3_1 + kr4_1)/6
            corpo_1.velocidade = corpo_1.velocidade +h*(kv1_1 +2*kv2_1 + 2*kv3_1 + kv4_1)/6
            pos1 = np.vstack([pos1, corpo_1.posicao])

            #corpo 2
            kr1_2 = v(corpo_2)
            kv1_2 = a2(corpo_1, corpo_2, corpo_3)

            kr2_2 = v(corpo_2) + h*kv1_2/2
            kv2_2 = nova_ac(corpo_2, corpo_1, corpo_3, h/2, kr1_2)

            kr3_2 = v(corpo_2) + h*kv2_2/2
            kv3_2 = nova_ac(corpo_2, corpo_1, corpo_3, h/2, kr2_2)

            kr4_2 = v(corpo_2) + h*kv3_2
            kv4_2 = nova_ac(corpo_2, corpo_1, corpo_3, h, kr3_2)

            corpo_2.posicao    = corpo_2.posicao + h*(kr1_2 +2*kr2_2 + 2*kr3_2 + kr4_2)/6
            corpo_2.velocidade = corpo_2.velocidade +h*(kv1_2 +2*kv2_2 + 2*kv3_2 + kv4_2)/6
            pos2 = np.vstack([pos2, corpo_2.posicao])

            #corpo 3
            kr1_3 = v(corpo_3)
            kv1_3 = a3(corpo_1, corpo_2, corpo_3)

            kr2_3 = v(corpo_3) + h*kv1_3/2
            kv2_3 = nova_ac(corpo_3, corpo_1, corpo_2, h/2, kr1_3)

            kr3_3 = v(corpo_3) + h*kv2_3/2
            kv3_3 = nova_ac(corpo_3, corpo_1, corpo_2, h/2, kr2_3)

            kr4_3 = v(corpo_3) + h*kv3_3
            kv4_3 = nova_ac(corpo_3, corpo_1, corpo_2, h, kr3_3)

            corpo_3.posicao    = corpo_3.posicao + h*(kr1_3 +2*kr2_3 + 2*kr3_3 + kr4_3)/6
            corpo_3.velocidade = corpo_3.velocidade +h*(kv1_3 +2*kv2_3 + 2*kv3_3 + kv4_3)/6
            pos3 = np.vstack([pos3, corpo_3.posicao])

            t += h
            
        return pos1, pos2, pos3

