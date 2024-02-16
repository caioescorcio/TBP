import numpy as np
import matplotlib.pyplot as plt

class Plot:
    def plot(v_x, v_y):
        plt.plot(v_x, v_y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Gráfico de y em função de x')
        plt.grid(True)
        plt.show()