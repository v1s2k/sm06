import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

t_obsl1 = np.linspace(1, 5, num=100)
t_obsl2 = np.linspace(1, 5, num=100)

t_obsl1_grid, t_obsl2_grid = np.meshgrid(t_obsl1, t_obsl2)
lmbd1 = 0.1
lmbd2 = 0.2
mu1 = 1/t_obsl1_grid
mu2 = 1/t_obsl2_grid



y1 = lmbd1 / mu1
y2 = lmbd2 / mu2
y = y1 + y2

tque1 = y1 / (mu1 * (1 - y1))
tsys1 = tque1 + t_obsl1_grid

tque2 = ((mu2 / mu1) * (y1 / (1 - y)) + y) / (1 - y)
tsys2 = tque2 + t_obsl2_grid

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(t_obsl1_grid, t_obsl2_grid, tsys1, cmap='viridis')
ax.set_xlabel('t_obsl1')
ax.set_ylabel('t_obsl2')
ax.set_zlabel('время пребывания в отключенном состоянии потребителей I категории составит')
ax.set_title('Система 1')
plt.show()

fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
ax2.plot_surface(t_obsl1_grid, t_obsl2_grid, tsys2, cmap='viridis')
ax2.set_xlabel('t_obsl1')
ax2.set_ylabel('t_obsl2')
ax2.set_zlabel('время пребывания не обладающей приоритетом')
ax2.set_title('Система  2')

plt.show()