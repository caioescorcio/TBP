import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def generate_trajectory(amplitude, frequency, phase_shift, num_points):
    t = np.linspace(0, 10, num_points)  # tempo de 0 a 10 segundos
    x = amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)
    y = amplitude * np.cos(2 * np.pi * frequency * t + phase_shift)
    return np.column_stack((x, y))

def plot_tempo(matrices, labels):
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

# Gerando trajetórias usando funções sinusoidais
amplitude1, frequency1, phase_shift1 = 3, 0.5, 0
amplitude2, frequency2, phase_shift2 = 4, 0.3, np.pi/2
amplitude3, frequency3, phase_shift3 = 2, 0.8, np.pi

positions1 = generate_trajectory(amplitude1, frequency1, phase_shift1, 100)
positions2 = generate_trajectory(amplitude2, frequency2, phase_shift2, 120)
positions3 = generate_trajectory(amplitude3, frequency3, phase_shift3, 150)

# Definindo os rótulos para cada corpo
labels = ['Corpo 1', 'Corpo 2', 'Corpo 3']

# Chamando a função para animar as posições com legendas
plot_tempo([positions1, positions2, positions3], labels)
