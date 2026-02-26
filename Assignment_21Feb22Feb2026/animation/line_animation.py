import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

vx, vy = 1, 0

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)

def rotate(x, y, theta):
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    return x*cos_t - y*sin_t, x*sin_t + y*cos_t

# initialize line (important)
def init():
    line.set_data([], [])
    return line,

def update(frame):
    theta = math.radians(frame)
    xr, yr = rotate(vx, vy, theta)
    line.set_data([0, xr], [0, yr])
    return line,

ani = FuncAnimation(
    fig,
    update,
    frames=range(0, 360, 2),
    init_func=init,
    interval=50,
    blit=False
)

plt.show()

    
