import numpy as np
from Classes.Planeta import Planeta

class Discretizacao:
    
    def rungekutta(y_0, f, n, intervalo_t):
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
    
    def calculaNovaVelocidade(c1, c2, c3, incremento, h, k, l, i):
        cx = Planeta(c1.posicao + incremento*k[i], c1.massa, c1.velocidade[i] + incremento*l[i])
        cx_1 = Planeta(c2.posicao + incremento*k[(i+1)%3], c2.massa, c2.velocidade + incremento*l[(i+1)%3])
        cx_2 = Planeta(c3.posicao + incremento*k[(i+2)%3], c3.massa, c3.velocidade + incremento*l[(i+2)%3])
        return cx.velocidade + h*(cx.ac_rel(c2) + cx.ac_rel(c3))
    
    def rungekutta_planetas(corpo_1, corpo_2, corpo_3, n, T):
        #discretizacao do intervalo
        h = T/n
        
        #array de corpos
        corpos = np.array([corpo_1, corpo_2, corpo_3])

        #definicao das funcoes para discretizar
        a1 = lambda c1, c2, c3: c1.ac_rel(c2) + c1.ac_rel(c3)
        a2 = lambda c1, c2, c3: c2.ac_rel(c1) + c2.ac_rel(c3)
        a3 = lambda c1, c2, c3: c3.ac_rel(c2) + c3.ac_rel(c1)
        a = [a1, a2, a3]
        v = lambda c: c.velocidade
        
        #array de termos do RK para posicao e velocidade
        k = np.zeros(3,4)
        l = np.zeros(3,4)

        #loop para calcular os valores
        while t < T:
            
            #K1
            for i in range(3):
                k[i,0] = h*v(corpos[i])
            for i in range(3):
                l[i,0] = h*a(corpos[i], corpos[(i+1)%3], corpos[(i+2)%3])
            
            #K2
            for i in range(3):
                k[i,1] = h*(v(corpos[i]) + (l[i,0])/2)
            for i in range(3):
                l[i,1] = h*calculaNovaVelocidade(corpos[i], corpos[(i+1)%3], corpos[(i+2)%3], 0.5, h, k, l, 0)
            
            #K3
            for i in range(3):
                k[i,2] = h*(v(corpos[i]) + (l[i,1])/2)
            for i in range(3):
                l[i,2] = h*calculaNovaVelocidade(corpos[i], corpos[(i+1)%3], corpos[(i+2)%3], 0.5, h, k, l, 1)
            
            #K4
            for i in range(3):
                k[i,3] = h*(v(corpos[i]) + l[i,2])
            for i in range(3):
                l[i,3] = h*calculaNovaVelocidade(corpos[i], corpos[(i+1)%3], corpos[(i+2)%3], 1, h, k, l, 2)
               
            #Atualizando os valores    
            for i in range(3):
                corpos[i].posicao = corpos[i].posicao + (k[i,0] + 2*k[i,1] + 2*k[i,2] + k[i,3])/6
                corpos[i].velocidade = corpos[i].velocidade + (l[i,0] + 2*l[i,1] + 2*l[i,2] + l[i,3])/6

             
            t += h
            
        return corpos[0], corpos[1], corpos[2]

