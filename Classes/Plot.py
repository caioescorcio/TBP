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
    
    def plot_tempo(v_t, v_x, v_y):
        fig, ax = plt.subplots()
        line, = ax.plot([], [], 'bo')

        x_buffer = 0.05* (max(v_t) - min(v_t))
        y_buffer = 0.05* (max(v_x) - min(v_x))
        
        def init():
            ax.set_xlim(min(v_t) - x_buffer, max(v_t) + x_buffer)
            ax.set_ylim(min(v_x) - y_buffer, max(v_x) + y_buffer)
            ax.grid(True)
            return line,

        def update(frame):
            line.set_data(v_t[:frame], v_x[:frame])
            ax.set_xlim(min(v_t) - x_buffer, max(v_t) + x_buffer)
            ax.set_ylim(min(v_x) - y_buffer, max(v_x) + y_buffer)
            return line,

        ani = FuncAnimation(fig, update, frames=len(v_t), init_func=init, blit=True, interval=0.05)
        plt.xlabel('v_t')
        plt.ylabel('v_x')
        plt.title('Animated Plot of v_x vs. v_t')
        plt.show()

    def plot_matriz(vetor_posicao):
        fig, ax = plt.subplots()
        line, = ax.plot([], [], 'bo')

        x_buffer = 0.05 * (vetor_posicao[:, 0].max() - vetor_posicao[:, 0].min())
        y_buffer = 0.05 * (vetor_posicao[:, 1].max() - vetor_posicao[:, 1].min())
        
        def init():
            ax.set_xlim(vetor_posicao[:, 0].min() - x_buffer, vetor_posicao[:, 0].max() + x_buffer)
            ax.set_ylim(vetor_posicao[:, 1].min() - y_buffer, vetor_posicao[:, 1].max() + y_buffer)
            ax.grid(True)
            return line,

        def update(frame):
            line.set_data(vetor_posicao[:frame, 0], vetor_posicao[:frame, 1])
            ax.set_xlim(vetor_posicao[:, 0].min() - x_buffer, vetor_posicao[:, 0].max() + x_buffer)
            ax.set_ylim(vetor_posicao[:, 1].min() - y_buffer, vetor_posicao[:, 1].max() + y_buffer)
            return line,

        ani = FuncAnimation(fig, update, frames=len(vetor_posicao), init_func=init, blit=True, interval=50)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Animated Plot of Body Position')
        plt.show()

        def plot_CORPOS(matrices, labels):
            fig, ax = plt.subplots()
            lines = [ax.plot([], [], '-', label=label)[0] for label in labels]
            points = [ax.plot([], [], 'o', color=line.get_color())[0] for line in lines]

            buffers = [(0.05 * (matrix[:, 0].max() - matrix[:, 0].min()),
                        0.05 * (matrix[:, 1].max() - matrix[:, 1].min())) for matrix in matrices]
            
            def init():
                for line, point in zip(lines, points):
                    line.set_data([], [])
                    point.set_data([], [])
                ax.set_xlim(min([matrix[:, 0].min() for matrix in matrices]) - max([buffer[0] for buffer in buffers]),
                            max([matrix[:, 0].max() for matrix in matrices]) + max([buffer[0] for buffer in buffers]))
                ax.set_ylim(min([matrix[:, 1].min() for matrix in matrices]) - max([buffer[1] for buffer in buffers]),
                            max([matrix[:, 1].max() for matrix in matrices]) + max([buffer[1] for buffer in buffers]))
                ax.grid(True)
                ax.legend()
                return lines + points

            def update(frame):
                for line, point, matrix in zip(lines, points, matrices):
                    line.set_data(matrix[:frame, 0], matrix[:frame, 1])
                    point.set_data([matrix[frame-1, 0]], [matrix[frame-1, 1]])

                return lines + points

            ani = FuncAnimation(fig, update, frames=min([len(matrix) for matrix in matrices])+1, init_func=init, blit=True, interval=50)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Animated Plot of Body Position')
            plt.show()
