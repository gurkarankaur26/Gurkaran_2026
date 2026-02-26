import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Polygon, Circle

num_blades = 4
blade_length = 1.4
blade_width = 0.4

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.grid()

# create fan hub (center circle)
hub = Circle((0, 0), 0.15, color='black')
ax.add_patch(hub)

# create blade patches
blades = []
for _ in range(num_blades):
    poly = Polygon([[0, 0], [0, 0], [0, 0]], color='red')
    ax.add_patch(poly)
    blades.append(poly)

# rotation helper
def rotate(x, y, theta):
    c = math.cos(theta)
    s = math.sin(theta)
    return x*c - y*s, x*s + y*c

def update(frame):
    base_angle = math.radians(frame)

    for i, blade in enumerate(blades):
        angle = base_angle + i * (2*math.pi / num_blades)

        # triangle blade shape (before rotation)
        p1 = (0, 0)
        p2 = (blade_length, blade_width/2)
        p3 = (blade_length, -blade_width/2)

        # rotate each point
        rp1 = rotate(*p1, angle)
        rp2 = rotate(*p2, angle)
        rp3 = rotate(*p3, angle)

        blade.set_xy([rp1, rp2, rp3])

    return blades

ani = FuncAnimation(fig, update, frames=range(0, 360, 5), interval=40)

plt.show()