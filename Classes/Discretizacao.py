import numpy as np

class Discretizacao:
    
    def rungekutta(y_0, f, n, intervalo_t):
        #discretizacao do intervalo
        delta_t = (intervalo_t[1] - intervalo_t[0])/n

        #inicializacao das variaveis
        t = intervalo_t[0]
        y = y_0
        

        #loop para calcular os valores de y
        while t < intervalo_t[1]:
            print(round(y, 2),"\t",round(t, 2))
            k_1 = delta_t*f(t, y)
            k_2 = delta_t*f(t + delta_t/2, y + k_1/2)
            k_3 = delta_t*f(t +delta_t/2, y + k_2/2)
            k_4 = delta_t*f(t + delta_t, y + k_3)

            y = y + (k_1 + 2*k_2 + 2*k_3 + k_4)/6
            t = t + delta_t


 