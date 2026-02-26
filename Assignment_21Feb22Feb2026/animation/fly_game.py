import tkinter as tk
import random
import os

# -----------------------------
# OPTIONAL SOUND (Windows only)
# -----------------------------
try:
    import winsound
    def hit_sound():
        winsound.Beep(800, 120)
except:
    def hit_sound():
        pass


# -----------------------------
# WINDOW SETUP
# -----------------------------
WIDTH = 900
HEIGHT = 600

root = tk.Tk()
root.title("Fly Swatter Game")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="lavender")
canvas.pack()


# -----------------------------
# GAME VARIABLES
# -----------------------------
score = 0
time_left = 60
game_running = True
flies = []

HIGH_SCORE_FILE = "highscore.txt"


# -----------------------------
# HIGH SCORE
# -----------------------------
def load_highscore():
    if os.path.exists(HIGH_SCORE_FILE):
        return int(open(HIGH_SCORE_FILE).read())
    return 0

def save_highscore(val):
    open(HIGH_SCORE_FILE, "w").write(str(val))

high_score = load_highscore()


# -----------------------------
# UI TEXT
# -----------------------------
score_text = canvas.create_text(80, 30, text="Score: 0",
                                font=("Arial", 16, "bold"))

timer_text = canvas.create_text(WIDTH-100, 30, text="Time: 60",
                                font=("Arial", 16, "bold"))

high_text = canvas.create_text(WIDTH//2, 30,
                               text=f"High Score: {high_score}",
                               font=("Arial", 14))


# -----------------------------
# RACKET (HEAD + HANDLE + MESH)
# -----------------------------
racket_head = canvas.create_oval(0,0,80,80,
                                 fill="blue",
                                 outline="black",
                                 width=3)

racket_handle = canvas.create_rectangle(35,80,45,140,
                                        fill="black")

mesh_lines = []
for i in range(-30, 31, 10):
    mesh_lines.append(canvas.create_line(0,0,0,0, fill="white"))
    mesh_lines.append(canvas.create_line(0,0,0,0, fill="white"))


def move_racket(event):
    x = event.x
    y = event.y

    canvas.coords(racket_head, x-40,y-40,x+40,y+40)
    canvas.coords(racket_handle, x-5,y+40,x+5,y+95)

    idx = 0
    for i in range(-30,31,10):
        canvas.coords(mesh_lines[idx], x+i,y-30,x+i,y+30)
        idx += 1
        canvas.coords(mesh_lines[idx], x-30,y+i,x+30,y+i)
        idx += 1

canvas.bind("<Motion>", move_racket)


# -----------------------------
# CREATE FLY
# -----------------------------
def create_fly():
    x = random.randint(50, WIDTH-50)
    y = random.randint(50, HEIGHT-50)

    wing1 = canvas.create_oval(x-12,y-5,x+8,y+5, fill="lightgrey")
    wing2 = canvas.create_oval(x+8,y-5,x+28,y+5, fill="lightgrey")
    body  = canvas.create_oval(x,y,x+18,y+12, fill="black")

    flies.append([wing1, wing2, body, x, y])


for _ in range(4):
    create_fly()


# -----------------------------
# MOVE FLIES FAST
# -----------------------------
def move_flies():
    if not game_running:
        return

    for fly in flies:
        dx = random.randint(-25,25)
        dy = random.randint(-25,25)

        fly[3] = max(20, min(WIDTH-40, fly[3]+dx))
        fly[4] = max(20, min(HEIGHT-40, fly[4]+dy))

        canvas.coords(fly[0], fly[3]-12,fly[4]-5,fly[3]+8,fly[4]+5)
        canvas.coords(fly[1], fly[3]+8,fly[4]-5,fly[3]+28,fly[4]+5)
        canvas.coords(fly[2], fly[3],fly[4],fly[3]+18,fly[4]+12)

    root.after(300, move_flies)


# -----------------------------
# BLOOD SPLASH
# -----------------------------
def blood(x,y):
    for _ in range(15):
        r=random.randint(3,7)
        dx=random.randint(-25,25)
        dy=random.randint(-25,25)
        canvas.create_oval(x+dx,y+dy,x+dx+r,y+dy+r,
                           fill="red", outline="")


# -----------------------------
# SCREEN SHAKE
# -----------------------------
def shake():
    for _ in range(6):
        canvas.move("all", random.randint(-5,5), random.randint(-5,5))
        canvas.update()


# -----------------------------
# SMASH ANIMATION
# -----------------------------
def smash_anim(x,y):
    for i in range(6):
        canvas.create_oval(x-i*5,y-i*5,x+i*5,y+i*5, outline="red")
        canvas.update()


# -----------------------------
# HIT DETECTION (RACKET TOUCH)
# -----------------------------
def click(event):
    global score, flies

    if not game_running:
        return

    rx1, ry1, rx2, ry2 = canvas.coords(racket_head)

    overlapping = canvas.find_overlapping(rx1, ry1, rx2, ry2)

    for fly in flies[:]:
        body_id = fly[2]

        if body_id in overlapping:
            for part in fly[:3]:
                canvas.delete(part)

            flies.remove(fly)

            cx = (rx1+rx2)//2
            cy = (ry1+ry2)//2

            hit_sound()
            blood(cx, cy)
            smash_anim(cx, cy)
            shake()

            score += 1
            canvas.itemconfig(score_text, text=f"Score: {score}")

            create_fly()


canvas.bind("<Button-1>", click)


# -----------------------------
# TIMER
# -----------------------------
def countdown():
    global time_left, game_running, high_score

    if not game_running:
        return

    time_left -= 1
    canvas.itemconfig(timer_text, text=f"Time: {time_left}")

    if time_left <= 0:
        game_running = False

        if score > high_score:
            save_highscore(score)

        canvas.create_text(WIDTH//2, HEIGHT//2,
                           text="GAME OVER",
                           font=("Arial", 40, "bold"),
                           fill="blue")
        return

    root.after(1000, countdown)


# -----------------------------
# START GAME
# -----------------------------
move_flies()
countdown()
root.mainloop()