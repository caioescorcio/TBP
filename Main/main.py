import numpy as np
from Classes.Discretizacao import Discretizacao as disc
from Classes.Planeta import Planeta
from Classes.Splines import CubicSpline
#from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import plotly.graph_objects as go


#massa padrao de todos os planetas
massa = 1
v_0 = np.array([0.4662036850, 0.4323657300])
a, b = 3, 4

labels = ['Corpo 1', 'Corpo 2', 'Corpo 3']
n = 1000
T = 1
discretizacao = disc()
np.set_printoptions(threshold=np.inf)
pos1, pos2, pos3, t = discretizacao.converte(100*30, True)

fig, ax = plt.subplots()

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

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

# Create empty scatter plots for the balls
ball1, = ax.plot([], [], 'ro', markersize=5)
ball2, = ax.plot([], [], 'go', markersize=5)
ball3, = ax.plot([], [], 'bo', markersize=5)

# Animation function
def update(frame):
    line1.set_data(pos1[:frame, 0], pos1[:frame, 1])
    line2.set_data(pos2[:frame, 0], pos2[:frame, 1])
    line3.set_data(pos3[:frame, 0], pos3[:frame, 1])
    ball1.set_data([pos1[frame, 0]], [pos1[frame, 1]])
    ball2.set_data([pos2[frame, 0]], [pos2[frame, 1]])
    ball3.set_data([pos3[frame, 0]], [pos3[frame, 1]])

    return line1, line2, line3, ball1, ball2, ball3

# Create the animation
ani = FuncAnimation(fig, update, frames=len(pos1), interval=1, blit=True)
plt.show()

#SPLINE CUBICO
pos_stack = np.array( [pos1, pos2, pos3] )
t = np.linspace(0, 30*T, len(pos1[:,0]))
t_plot = np.arange(0, 30*T,  T/(20*n))
csx = np.array(list(map( lambda pos: CubicSpline(t, pos[:, 0]), pos_stack)))
csy = np.array(list(map( lambda pos: CubicSpline(t, pos[:, 1]), pos_stack)))

# Create figure
fig = go.Figure()

# Add real values
fig.add_trace(go.Scatter(x=pos1[:, 0], y=pos1[:, 1], mode='lines', name='Real Pos1'))
# fig.add_trace(go.Scatter(x=pos2[:, 0], y=pos2[:, 1], mode='lines', name='Real Pos2'))
# fig.add_trace(go.Scatter(x=pos3[:, 0], y=pos3[:, 1], mode='lines', name='Real Pos3'))

# # Add spline predictions
# for i in range(len(pos_stack)):
#     fig.add_trace(go.Scatter(x=csx[i](t_plot), y=csy[i](t_plot), mode='lines', name=f'Spline Pos{i+1}'))
fig.add_trace(go.Scatter(x=csx[0](t_plot)[0:], y=csy[0](t_plot)[0:], mode='lines', name=f'Spline Pos 1'))

# Set layout
fig.update_layout(
    title='Movimento de tres bolas',
    xaxis_title='X (m)',
    yaxis_title='Y (m)',
    legend_title='Legend',
    showlegend=True
)

fig.show()


