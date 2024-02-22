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
        d_v1 = lambda c1, c2, c3: c1.ac_rel(c2) + c1.ac_rel(c3)
        d_v2 = lambda c1, c2, c3: c2.ac_rel(c1) + c2.ac_rel(c3)
        d_v3 = lambda c1, c2, c3: c3.ac_rel(c2) + c3.ac_rel(c1)
        d_r1 = lambda c1: c1.posicao
        d_r2 = lambda c2: c2.posicao
        d_r3 = lambda c3: c3.posicao

        #loop para calcular os valores
        while t < T:

            k_1 = delta_t*d_v1(corpo_1, corpo_2, corpo_3)
            k_2 = delta_t*f(t + delta_t/2, y + k_1/2)
            k_3 = delta_t*f(t +delta_t/2, y + k_2/2)
            k_4 = delta_t*f(t + delta_t, y + k_3)

            v1_prox = corpo_1.velocidade + (k_1 + 2*k_2 + 2*k_3 + k_4)/6


            c1.velocidade = v1_prox
            c2.velocidade = v2_prox
            c3.velocidade = v3_prox 
            c1.posicao    = r1_prox
            c2.posicao    = r2_prox
            c3.posicao    = r3_prox
            
             
            t += delta_t
 