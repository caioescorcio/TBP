import numpy as np
from funcoes.Planeta import Planeta

v = Planeta(np.array([1, 2, 3]), 1, 1)
b = Planeta(np.array([1, 2, 3]), 1, 1)
print(v.distancia(b))
print(v.ac_rel(b), " \n" )

v = Planeta(np.array([1, 2, 3]), 1, 1)
b = Planeta(np.array([2, 2, 3]), 1, 1)
print(v.distancia(b))
print(v.ac_rel(b), " \n")

v = Planeta(np.array([1, 2, 3]), 1, 1)
b = Planeta(np.array([2, 1, 3]), 1, 1)
print(v.distancia(b))
print(v.ac_rel(b)," \n")