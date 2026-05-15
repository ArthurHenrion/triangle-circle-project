from lib_math import *
import turtle as t
import keyboard as key
import time

# --- Configuration initiale des points ---
ax, ay = 0, 150
bx, by = -200, -100
cx, cy = 200, -100

selection = 1
last_space_state = False

print("Commandes :")
print("- ESPACE : Changer de point sélectionné")
print("- FLÈCHES : Déplacer le point")
print("- ESC : Quitter")

while True:
    t.clear()
    
    try:
        tri = Triangle(ax, ay, bx, by, cx, cy)
        tri.trace()
    except:
        pass

    t.penup()
    current_pt = [(ax, ay), (bx, by), (cx, cy)][selection-1]
    t.goto(current_pt[0], current_pt[1] - 10)
    t.pencolor("red")
    t.pendown()
    t.circle(10)
    t.pencolor("black")
    t.penup()

    t.update()

    current_space_state = key.is_pressed('space')
    
    if current_space_state and not last_space_state:
        selection = selection + 1 if selection < 3 else 1
    last_space_state = current_space_state

    speed = 5
    dx, dy = 0, 0
    if key.is_pressed('up'):    dy = speed
    if key.is_pressed('down'):  dy = -speed
    if key.is_pressed('left'):  dx = -speed
    if key.is_pressed('right'): dx = speed

    if selection == 1:
        ax += dx; ay += dy
    elif selection == 2:
        bx += dx; by += dy
    elif selection == 3:
        cx += dx; cy += dy
    
    time.sleep(0.01)
    if key.is_pressed('esc'):
        break

t.done()
