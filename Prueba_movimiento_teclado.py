from tkinter import *

x = 10
y = 10
a = 100
b = 100

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
        if event.keysym == 'Left':
            canvas1.move(rect, -5,0)

window = Tk()
window.geometry("400x200")

#canvas et dessin (rectangle)
canvas1=Canvas(window, height = 200, width = 400)
canvas1.grid(row=0, column=0, sticky=W)
coord = [x, y, a, b]
rect = canvas1.create_rectangle(*coord, outline="aquamarine", fill="cyan")

#Associer les touches à la fonction
window.bind_all('<Up>', mouvement)
window.bind_all('<Down>', mouvement)
window.bind_all('<Left>', mouvement)
window.bind_all('<Right>', mouvement)
window.mainloop()
