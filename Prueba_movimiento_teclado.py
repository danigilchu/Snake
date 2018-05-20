# -*- coding: utf-8 -*-
"""
Created on Sat May 19 11:45:24 2018

@author: Ignacio Paillalef, Ali mehdi, Daniel Gil
"""
from tkinter import *
from random import randrange
# ========== GLOBAL variables ==========
Cx, Cy = 500, 500 # Dimensions Canvas

x1, y1 = Cx//2, Cy//2 # Position intiale
dx, dy = 0, 10 # Vitesse

flag = False


# ========== fonctions ==========

# Mouvement constant
def moveConst():
    global x1, y1, dx, dy, flag
    x1, y1 = x1 + dx, y1 + dy
    # Passe a l'autre cote
    if x1 > Cx:
        x1 = 0
    if y1 > Cy:
        y1 = 0
    if x1 < 0:
        x1 = Cx
    if y1 < 0:
        y1 = Cy
    can.coords(snake, x1, y1, x1 + 30, y1 + 30)
    if flag:
        fen.after(100, moveConst)
# Arreter mouvement constant
def stop():
    global flag
    flag = False
# Demarrer mouvement constant
def start():
    global flag
    if not flag:
        flag = True
        moveConst()
        creation_pomme()
# Mouvement Joueur
def up(*ignore):
    global dx, dy
    if dy >= 0:
        dx, dy = 0, -10
def down(*ignore):
    global dx, dy
    if dy <= 0:
        dx, dy = 0, 10
def left(*ignore):
    global dx, dy
    if dx >= 0:
        dx, dy = -10, 0
def right(*ignore):
    global dx, dy
    if dx <= 0:
        dx, dy = 10, 0
# Nourriture et le fait de manger
def creation_pomme():
    rayon=10
    global posx, posy,x1
    posx=randrange(10,490,1)
    posy=randrange(10,490,1)
    pomme=can.create_oval(posx-rayon,posy-rayon,posx+rayon,posy+rayon,
                          fill='red')
    if(posx+10 == x1 or posx-10 == x1 or posy+10 == x1 or posy-10 == x1 ):
        can.delete(pomme)
        creation_pomme()



# ========== MAIN PROGRAM ==========


fen = Tk()
fen.title("Snake")

can = Canvas(fen, bg = 'dark grey', height = Cx, width = Cy)
can.pack(side = LEFT, padx = 5, pady = 5)

# SNAKE
snake = can.create_rectangle(x1, y1, x1 + 30, y1 + 30, width = 2, fill = 'red')
fen.bind("<Up>", up)            # Bouttons déplacement
fen.bind("<Down>", down)
fen.bind("<Left>", left)
fen.bind("<Right>", right)

# Boutons
btn1 = Button(fen, text='Start', command = start)     # Commencer mouvement
btn1.pack()

btn2 = Button(fen, text='Stop', command = stop)     # Arreter mouvement
btn2.pack()

# TODO: Pour quoi ça?
can.focus_set()

fen.mainloop()
