import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Polygon
from matplotlib.widgets import Button, Slider

# -----------------------
# FAN SETTINGS
# -----------------------
num_blades = 4
length = 1.5
width = 0.5

angle_value = 0
speed = 2          # starting speed
running = True     # fan ON initially

# -----------------------
# CREATE GRAPH
# -----------------------
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')

# -----------------------
# CREATE BLADES
# -----------------------
blades = []
for i in range(num_blades):
    blade = Polygon([[0,0],[0,0],[0,0]], color="red")
    ax.add_patch(blade)
    blades.append(blade)

# -----------------------
# ROTATION FUNCTION
# -----------------------
def rotate(x, y, angle):
    new_x = x*math.cos(angle) - y*math.sin(angle)
    new_y = x*math.sin(angle) + y*math.cos(angle)
    return new_x, new_y

# -----------------------
# ANIMATION UPDATE
# -----------------------
def update(frame):
    global angle_value

    if running:
        angle_value += speed   # rotate based on speed

    base_angle = math.radians(angle_value)

    for i in range(num_blades):
        angle = base_angle + i*(2*math.pi/num_blades)

        p1 = (0, 0)
        p2 = (length, width/2)
        p3 = (length, -width/2)

        r1 = rotate(*p1, angle)
        r2 = rotate(*p2, angle)
        r3 = rotate(*p3, angle)

        blades[i].set_xy([r1, r2, r3])

# -----------------------
# ON / OFF BUTTON
# -----------------------
def toggle(event):
    global running
    running = not running

button_ax = plt.axes([0.7, 0.05, 0.15, 0.07])
button = Button(button_ax, "ON / OFF")
button.on_clicked(toggle)

# -----------------------
# SPEED SLIDER
# -----------------------
def change_speed(val):
    global speed
    speed = val

slider_ax = plt.axes([0.2, 0.1, 0.4, 0.03])
slider = Slider(slider_ax, "Speed", 0, 10, valinit=speed)
slider.on_changed(change_speed)

# -----------------------
# RUN ANIMATION
# -----------------------
ani = FuncAnimation(fig, update, interval=40)

plt.show()