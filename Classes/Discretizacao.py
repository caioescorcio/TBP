import numpy as np
from Classes.Planeta import Planeta

class Discretizacao:
    
    def rungekutta(y_0, f, n, intervalo_t):
        #discretizacao do intervalo
        delta_t = (intervalo_t[1] - intervalo_t[0])/n

        #inicializacao das variaveis
        t = intervalo_t[0]
        y = y_0
        v_t = [t]
        v_y = [y]

        #loop para calcular os valores de y
        while t < intervalo_t[1]:
            k_1 = delta_t*f(t, y)
            k_2 = delta_t*f(t + delta_t/2, y + k_1/2)
            k_3 = delta_t*f(t +delta_t/2, y + k_2/2)
            k_4 = delta_t*f(t + delta_t, y + k_3)

            y = y + (k_1 + 2*k_2 + 2*k_3 + k_4)/6
            t = t + delta_t
            v_t.append(t)
            v_y.append(y)
            
        return v_t, v_y
    
    def rungekutta_planetas(corpo_1, corpo_2, corpo_3, n, T):
        #discretizacao do intervalo
        delta_t = T/n

        #definicao das funcoes para discretizar
        a1 = lambda c1, c2, c3: c1.ac_rel(c2) + c1.ac_rel(c3)
        a2 = lambda c1, c2, c3: c2.ac_rel(c1) + c2.ac_rel(c3)
        a3 = lambda c1, c2, c3: c3.ac_rel(c2) + c3.ac_rel(c1)
        v = lambda c: c.velocidade
        

        #loop para calcular os valores
        while t < T:

            #para as posicoes
            k = np.zeros(4,6)
            
            k1 = delta_t*v(corpo_1)
            l1 = delta_t*a1(corpo_1, corpo_2, corpo_3)

            k2 = delta_t*(v(corpo_1) + l1/2)
            l2 = delta_t*a1(corpo_1 + k1/2, corpo_2, corpo_3)

           
            


            c1.velocidade = v1_prox
            c2.velocidade = v2_prox
            c3.velocidade = v3_prox 
            c1.posicao    = r1_prox
            c2.posicao    = r2_prox
            c3.posicao    = r3_prox
            
             
            t += delta_t

    def calculaNovaVelocidade(c1, c2, c3, incremento, h):
        cx = Planeta(c1.posicao + incremento*h, c1.massa, c1.velocidade)
        return cx.velocidade + h*(cx.ac_rel(c2) + cx.ac_rel(c3))