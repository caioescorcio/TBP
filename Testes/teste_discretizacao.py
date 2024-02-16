import numpy as np
import matplotlib.pyplot as plt
from Classes.Discretizacao import Discretizacao as disc
from Classes.Plot import Plot as plt

y = lambda x, a: x**2 - 2*x + 1 + 0*a   #funcao teste
d_y = lambda x, a: 2*x - 2 + 0*a        #derivada da funcao teste
i = [-10, 10]                           #intervalo i no qual pretende-se calcular o valor de f(x) 
n = 100                                 #particao


v_x, v_y = disc.rungekutta(y(-10,1), d_y, n, i)
plt.plot(v_x, v_y)