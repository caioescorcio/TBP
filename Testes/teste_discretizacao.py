import numpy as np
import matplotlib.pyplot as plt
from Classes.Discretizacao import Discretizacao as disc
from Classes.Plot import Plot as plot

y = lambda x, a: x**2 - 2*x + 1 + 0*a   #funcao teste ("y")
d_y = lambda x, a: 2*x - 2 + 0*a        #derivada da funcao teste ("y")
z = lambda x, a: np.exp(x) + 0*a   #funcao teste ("y")
d_z = lambda x, a: np.exp(x) - 3 + 0*a        #derivada da funcao teste ("y")
i = [-10, 10]                         #intervalo i no qual pretende-se calcular o valor de f(x) 
n = 100                                 #particao


v_t, v_y = disc.rungekutta(y(-10,1), d_y, n, i)
v_t, v_z = disc.rungekutta(z(-10, 1), d_z, n, i) 

vetor_posicao = np.column_stack((v_y, v_z))

plot.plot(v_t, v_y)
plot.plot_tempo(v_t, v_y, v_z)

plot.plot(v_t, v_z)
plot.plot_tempo(v_t, v_z, v_y)

plot.plot_matriz(vetor_posicao)
