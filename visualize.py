import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 

data = np.load('handover2.npy', allow_pickle = True)
panda0_ee = data.item()['panda0_ee']
panda1_ee = data.item()['panda1_ee']
goal = data.item()['goal']
obj_init = data.item()['obj_init_pos']

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
for g in goal.reshape(-1, 3):
    ax.scatter(*g, marker = 'x')
for o in obj_init.reshape(-1, 3):
    ax.scatter(*o)
ax.scatter(*np.moveaxis(panda0_ee, 0, 1))
ax.scatter(*np.moveaxis(panda1_ee, 0, 1))

graph0,  = ax.plot(*panda0_ee[0], "ro", markersize=8)
graph1,  = ax.plot(*panda1_ee[0], "yo", markersize=8)

def update_graph(i):
    graph0.set_data(panda0_ee[i][0], panda0_ee[i][1])
    graph0.set_3d_properties(panda0_ee[i][2])
    graph1.set_data(panda1_ee[i][0], panda1_ee[i][1])
    graph1.set_3d_properties(panda1_ee[i][2])

ani = FuncAnimation(fig, update_graph, len(panda0_ee), interval=40)

plt.show()