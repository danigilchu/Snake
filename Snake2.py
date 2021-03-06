# -*- coding: utf-8 -*-
"""
Created on Sat May 19 11:45:24 2018
@author: Ignacio Paillalef, Ali mehdi, Daniel Gil
"""
from tkinter import *
from random import *
import os
from time import *
# ========== GLOBAL variables ==========
Cx, Cy = 500, 500 # Dimensions Canvas

x1, y1 = Cx//2, Cy//2 # Position intiale
dx, dy = 0, 20 # Vitesse

Size = abs(dx + dy)

flag = False
# ========== fonctions ==========

# Mouvement constant
def moveConst():
    global x1, y1, dx, dy, flag,score
    xF, yF = x1, y1
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
    can.coords(snake, x1, y1, x1 + Size, y1 + Size)
    if flag:
        fen.after(100, moveConst)

        if len(body) > 0:
            follow(xF, yF)
# Arreter mouvement constant
def stop():
    global flag
    flag = False
# Demarrer mouvement constant
def start():
    global flag,snake
    if not flag:
        flag = True
        moveConst()
        creation_pomme()

# Mouvement Joueur
def up(*ignore):
    global dx, dy
    if dy >= 0:
        dx, dy = 0, -Size
def down(*ignore):
    global dx, dy
    if dy <= 0:
        dx, dy = 0, Size
def left(*ignore):
    global dx, dy
    if dx >= 0:
        dx, dy = -Size, 0
def right(*ignore):
    global dx, dy
    if dx <= 0:
        dx, dy = Size, 0

# Fonctions du corps du SNAKE
body = []
def create(*ignore):
    global snake, body, dx, dy
    pS = can.coords(snake)
    # LEFT
    if dx < 0:
        body += [can.create_rectangle(pS[0] + Size, pS[1], pS[2] + Size, pS[3], width = 2, fill = 'yellow')]
    # RIGHT
    if dx > 0:
        body += [can.create_rectangle(pS[0] - Size, pS[1], pS[2] - Size, pS[3], width = 2, fill = 'blue')]
    # DOWN
    if dy > 0:
        body += [can.create_rectangle(pS[0], pS[1] - Size, pS[2], pS[3] - Size, width = 2, fill = 'green')]
    # UP
    if dy < 0:
        body += [can.create_rectangle(pS[0], pS[1] + Size, pS[2], pS[3] + Size, width = 2, fill = 'orange')]
# Nourriture et le fait de manger
pomme = []
def creation_pomme():
    rayon=10
    global posx, posy,x1
    posx=randrange(10,490,1)
    posy=randrange(10,490,1)
    pomme=can.create_oval(posx-rayon,posy-rayon,posx+rayon,posy+rayon,
                          fill='red')
    print (posx,posy)
    print (pseudo_recupere)
    #if(posx+10 > x1 or posx-10 == x1 or posy+10 == x1 or posy-10 == x1 ) or flag == False:
    #if(posx-x1 >= 0 or posx-x1+30<=0 or posy-y1 >=0 or posy-y1+30 <=0) or flag == False:
##    if x1 == 300:
##        can.delete(pomme)
##        creation_pomme()
def delPomme(*ignore):
    global pomme
    can.delete()
    creation_pomme()
def follow(xF, yF):
    global body
    for i in range(len(body)):
        posP = can.coords(body[i])
        can.coords(body[i], xF, yF, xF + Size, yF + Size)
        xF, yF = posP[0], posP[1]

def afficher(event):

    pseudo1=pseudo.get()
    chaine.configure(text = "Bienvenu " + str(pseudo1))
    donnees=open("donnees.txt","w")
    donnees.write(pseudo.get())
    donnees.close()
    return pseudo1
    
# ========== MAIN PROGRAM ==========
score=clock()
fenetre = Tk()
pseudo = Entry(fenetre)
pseudo.bind("<Return>", afficher)

chaine = Label(fenetre)

pseudo.pack()
chaine.pack()

fenetre.mainloop()

fen = Tk()
fen.title("Snake")


can = Canvas(fen, bg = 'dark grey', height = Cx, width = Cy)
can.pack(side = LEFT, padx = 5, pady = 5)


# SNAKE
snake = can.create_rectangle(x1, y1, x1 + Size, y1 + Size, width = 2, fill = 'red')

fen.bind("<Up>", up)
fen.bind("<Down>", down)
fen.bind("<Left>", left)
fen.bind("<Right>", right)

fen.bind("<Tab>", delPomme)

# Creer corps
fen.bind("<Tab>", create)

# Boutons
btn1 = Button(fen, text='Start', command = start)     # Commencer mouvement
btn1.pack()

btn2 = Button(fen, text='Stop', command = stop)     # Arreter mouvement
btn2.pack()
with open('donnees.txt','r',) as donnees:
    pseudo_recupere=donnees.read()
mylabel1 = Label(fen, text=str(pseudo_recupere))
mylabel2 = Label(fen, text=str(score))
mylabel1.pack()
mylabel2.pack()

#TODO: Pour quoi ça?
can.focus_set()

fen.mainloop()
