from asyncio import protocols
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 
import pickle

# for file in ['handover1_inhand_joint', 'handover1_joint']:
#     data = np.load(f'{file}.npy', allow_pickle=True).item()
#     with open(f'{file}.pkl', 'wb') as f:
#         pickle.dump(data, f, protocol=2)
# exit()

with open('/Users/reedpan/Downloads/trajectory/handover1_rearrange1/re1_hand1_1.pkl', 'rb') as f:
    data = pickle.load(f)
panda0_ee = data['panda0_ee_new']
panda1_ee = data['panda1_ee_new']
goal = data['goal']
obj_init = data['obj_init_pos']

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