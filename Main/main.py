import numpy as np
from Classes.Discretizacao import Discretizacao as disc
from Classes.Plot import Plot as plot
from Classes.Planeta import Planeta
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#massa padrao de todos os planetas
massa = 1
v_0 = np.array([0.4662036850, 0.4323657300])
a, b = 3, 4

corpo_1 = Planeta(np.array([-0.97000436, 0.24308753]), massa, v_0)
corpo_2 = Planeta(np.array([0.97000436, -0.24308753]), massa, v_0)
corpo_3 = Planeta(np.array([0, 0]), massa, np.array([-0.93240737, -0.86473146]))
labels = ['Corpo 1', 'Corpo 2', 'Corpo 3']
n = 100
T = 1
discretizacao = disc()
np.set_printoptions(threshold=np.inf)
pos1, pos2, pos3 = discretizacao.rungekutta_planetas(corpo_1, corpo_2, corpo_3, n, T)

fig, ax = plt.subplots()

ax.set_xlim(-a - a / 4, a + a / 4)
ax.set_ylim(-b - b / 4, b + b / 4)

# Create empty lines for the plot
line1, = ax.plot([], [], 'r-', lw=2)
line2, = ax.plot([], [], 'g-', lw=2)
line3, = ax.plot([], [], 'b-', lw=2)

# Create empty scatter plots for the balls
ball1, = ax.plot([], [], 'ro', markersize=5)
ball2, = ax.plot([], [], 'go', markersize=5)
ball3, = ax.plot([], [], 'bo', markersize=5)

# Animation function
def update(frame):
    line1.set_data(pos1[:frame, 0], pos1[:frame, 1])
    line2.set_data(pos2[:frame, 0], pos2[:frame, 1])
    line3.set_data(pos3[:frame, 0], pos3[:frame, 1])
    ball1.set_data(pos1[frame, 0], pos1[frame, 1])
    ball2.set_data(pos2[frame, 0], pos2[frame, 1])
    ball3.set_data(pos3[frame, 0], pos3[frame, 1])
    return line1, line2, line3, ball1, ball2, ball3

# Create the animation
ani = FuncAnimation(fig, update, frames=len(pos1), interval=1, blit=True)

# Show the plot
plt.show()