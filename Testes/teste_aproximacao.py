import numpy as np
from Classes.Aproximacao import Aproximacao as ap

f = lambda x: (x**2 + 3)/12 #funcao teste, com uma raiz no intervalo I 
i = [-10, 10] #intervalo i no qual pretende-se calcular o valor de f(x) = x
p = 5 #precisao de 3 casas apos a virgula


print(ap.MAS(i, f, p))