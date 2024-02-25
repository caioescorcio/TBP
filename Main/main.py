import numpy as np
from Classes.Discretizacao import Discretizacao as disc
from Classes.Plot import Plot as plot
from Classes.Planeta import Planeta

#massa padrao de todos os planetas
massa = 10**9
v_0 = np.array([0, 0])

corpo_1 = Planeta(np.array([0, 0]), massa, v_0)
corpo_2 = Planeta(np.array([0, 4]), massa, v_0)
corpo_3 = Planeta(np.array([3, 0]), massa, v_0)

n = 100
T = 1000

print(disc.rungekutta_planetas(corpo_1, corpo_2, corpo_3, n, T))