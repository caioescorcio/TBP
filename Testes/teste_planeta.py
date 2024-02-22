import numpy as np
from Classes.Planeta import Planeta

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

#massa padrao de todos os planetas
massa = 10**9
v_0 = np.array([0, 0])

corpo_1 = Planeta(np.array([0, 0]), massa, v_0)
corpo_2 = Planeta(np.array([0, 4]), massa, v_0)
corpo_3 = Planeta(np.array([3, 0]), massa, v_0)

d_v1 = lambda c1, c2, c3: c1.ac_rel(c2) + c1.ac_rel(c3)
d_v2 = lambda c1, c2, c3: c2.ac_rel(c1) + c2.ac_rel(c3)
d_v3 = lambda c1, c2, c3: c3.ac_rel(c2) + c3.ac_rel(c1)
d_r1 = lambda c1: c1.velocidade
d_r2 = lambda c2: c2.velocidade
d_r3 = lambda c3: c3.velocidade

print (d_v1(corpo_1, corpo_2, corpo_3), "\n", d_v2(corpo_1, corpo_2, corpo_3), "\n", d_v3(corpo_1, corpo_2, corpo_3), "\n", d_r1(corpo_1), "\n", d_r2(corpo_2), "\n", d_r3(corpo_3))