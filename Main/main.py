import numpy as np
from Classes.Discretizacao import Discretizacao as disc
from Classes.Plot import Plot as plot
from Classes.Planeta import Planeta
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#massa padrao de todos os planetas
massa = 10**8
v_0 = np.array([0, 0])

corpo_1 = Planeta(np.array([0, 0]), massa, v_0)
corpo_2 = Planeta(np.array([3*1000, 0]), massa, v_0)
corpo_3 = Planeta(np.array([0, 4*1000]), massa, v_0)
labels = ['Corpo 1', 'Corpo 2', 'Corpo 3']
n = 1500
T = 20
discretizacao = disc()
np.set_printoptions(threshold=np.inf)
pos1, pos2, pos3 = discretizacao.rungekutta_planetas(corpo_1, corpo_2, corpo_3, n, T)


# Create a figure and axis
fig, ax = plt.subplots()

# Set the limits of the plot
ax.set_xlim(min(pos1[:, 0].min(), pos2[:, 0].min(), pos3[:, 0].min()),
            max(pos1[:, 0].max(), pos2[:, 0].max(), pos3[:, 0].max()))
ax.set_ylim(min(pos1[:, 1].min(), pos2[:, 1].min(), pos3[:, 1].min()),
            max(pos1[:, 1].max(), pos2[:, 1].max(), pos3[:, 1].max()))

# Create empty lines for the plot
line1, = ax.plot([], [], 'r-', lw=2)
line2, = ax.plot([], [], 'g-', lw=2)
line3, = ax.plot([], [], 'b-', lw=2)

# Animation function
def update(frame):
    line1.set_data(pos1[:frame, 0], pos1[:frame, 1])
    line2.set_data(pos2[:frame, 0], pos2[:frame, 1])
    line3.set_data(pos3[:frame, 0], pos3[:frame, 1])
    return line1, line2, line3

# Create the animation
ani = FuncAnimation(fig, update, frames=len(pos1), interval=1, blit=True)

# Show the plot
plt.show()
