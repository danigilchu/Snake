from tkinter import *
from random import randrange

global x,y,x1,x2,coord
x,y,x1,x2=10,10,100,100
coord = [x, y, x1, x2]

def creation_pomme():
    rayon=10
    global posx, posy
    posx=randrange(10,690,1)
    posy=randrange(10,690,1)
    pomme=canvas1.create_oval(posx-rayon,posy-rayon,posx+rayon,posy+rayon,
                          fill='red')

    
def mouvement(event):
        if event.keysym == 'Up':
            canvas1.move(rect, 0,-5)
        if event.keysym == 'Up' and 'Right':
            canvas1.move(rect, 5,-5)
        if event.keysym == 'Up' and 'Left':
            canvas1.move(rect, -5,-5)
        if event.keysym == 'Down':
            canvas1.move(rect, 0,5)
        if event.keysym == 'Down' and 'Right':
            canvas1.move(rect, 5,5)
        if event.keysym == 'Down' and 'Left':
            canvas1.move(rect, -5,5)
        if event.keysym == 'Right':
            canvas1.move(rect, 5,0)
            auto1()
            creation_pomme()
        if event.keysym == 'Left':
            canvas1.move(rect, -5,0)
            #window.after(1000,mouvement)

            
def auto1():    # Mouvement automatique vers la droite
    global rect, coord
    coord[0]= coord[0] + 5
    coord[2]=coord[2] + 5
    print(coord[0],coord[2])
    canvas1.coords(rect, coord[0], coord[1], coord[2], coord[3])
    window.after(100, auto1)

def auto2():
    global rect, coord
    coord[0]= coord[0] + 5
    coord[2]=coord[2] + 5
    print(coord[0],coord[2])
    canvas1.coords(rect, coord[0], coord[1], coord[2], coord[3])
    window.after(100, auto)


window = Tk()
window.geometry("800x800")

#canvas et dessin (rectangle)
canvas1=Canvas(window, height = 700, width = 700)
canvas1.grid(row=0, column=0, sticky=W)
coord = [x, y, x1, x2]
rect = canvas1.create_rectangle(*coord, outline="aquamarine", fill="cyan")



#Associer les touches à la fonction
window.bind_all('<Up>', mouvement)
window.bind_all('<Down>', mouvement)
window.bind_all('<Left>', mouvement)
window.bind_all('<Right>', mouvement)
window.mainloop()
