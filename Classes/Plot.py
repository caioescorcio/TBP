import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
class Plot:
    def plot(v_x, v_y):
        plt.plot(v_x, v_y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Gráfico de y em função de x')
        plt.grid(True)
        plt.show()
    
    def plot_tempo(v_x, v_y):
        fig, ax = plt.subplots()
        line, = ax.plot([], [], 'bo')

        x_buffer = 0.05* (max(v_x) - min(v_x))
        y_buffer = 0.05* (max(v_y) - min(v_y))
        
        def init():
            ax.set_xlim(min(v_x) - x_buffer, max(v_x) + x_buffer)
            ax.set_ylim(min(v_y) - y_buffer, max(v_y) + y_buffer)
            ax.grid(True)
            return line,

        def update(frame):
            line.set_data(v_x[:frame], v_y[:frame])
            ax.set_xlim(min(v_x) - x_buffer, max(v_x) + x_buffer)
            ax.set_ylim(min(v_y) - y_buffer, max(v_y) + y_buffer)
            return line,

        ani = FuncAnimation(fig, update, frames=len(v_x), init_func=init, blit=True, interval=0.05)
        plt.xlabel('v_x')
        plt.ylabel('v_y')
        plt.title('Animated Plot of v_y vs. v_x')
        plt.show()
