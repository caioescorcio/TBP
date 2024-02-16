import numpy as np
from Classes.Discretizacao import Discretizacao as disc

y = lambda x, a: x**2 - 2*x + 1 + 0*a   #funcao teste
d_y = lambda x, a: 2*x - 2 + 0*a        #derivada da funcao teste
i = [-10, 10]                           #intervalo i no qual pretende-se calcular o valor de f(x) 
n = 100                                 #particao


disc.rungekutta(y(-10,1), d_y, n, i)