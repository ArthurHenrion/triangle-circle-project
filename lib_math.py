from math import *
import turtle as t

t.pensize(1)
t.speed(0)
t.hideturtle()
t.tracer(0, 0)

def draw_circle(cx, cy, r):
    t.penup()
    t.goto(cx + r, cy)
    t.pendown()
    for i in range(101):
        angle = i * (2 * pi / 100)
        t.goto(cx + cos(angle) * r, cy + sin(angle) * r)
    t.penup()

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3
        
        # --- calcul la longueurn de chaques côtés du triangle --- #
        # Les 3 côtés sont calculer avec theoreme de  pythagore, side_1 = x1,y1 -> x2,y2
        #                                                        side_2 = x2,y2 -> x3,y3
        #                                                        side_3 = x3,y3 -> x1,y1
        
        a = sqrt((x2 - x3)**2 + (y2 - y3)**2)
        b = sqrt((x1 - x3)**2 + (y1 - y3)**2)
        c = sqrt((x1 - x2)**2 + (y1 - y2)**2)
        
        self.side1, self.side2, self.side3 = a, b, c
        p = a + b + c # Périmètre
        
        # --- calcul du centre du cercle inscrit de ce trianfgle --- #

        self.centre_x = (a * x1 + b * x2 + c * x3) / p
        self.centre_y = (a * y1 + b * y2 + c * y3) / p
        
        # --- calcul du rayon cercle inscrit de notre triangle --- #
        #     rayon = Aire / Demi-périmètre
        
        s = p / 2 # Demi-périmètre
        aire = sqrt(s * (s - a) * (s - b) * (s - c))
        self.rayon = aire / s
        
    def trace(self, draw_tri = True, draw_incircle = True):
        if draw_tri:
            t.penup()
            t.goto(self.x1, self.y1)
            t.pendown()
            t.goto(self.x2, self.y2)
            t.goto(self.x3, self.y3)
            t.goto(self.x1, self.y1)
            t.penup()
        
        if draw_incircle:
            draw_circle(self.centre_x, self.centre_y, self.rayon)
        
        t.update()
    