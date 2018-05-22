# -*- coding: utf-8 -*-
"""
Created on Sat May 19 11:45:24 2018

@author: Ignacio Paillalef
"""
from tkinter import *

from random import randrange


# ========== GLOBAL variables ==========
Cx, Cy = 500, 500 # Dimensions Canvas

x1, y1 = Cx//2, Cy//2 + 50 # Position intiale
dx, dy = 0, 20 # Vitesse

Size = abs(dx + dy)

flag = False
# ========== fonctions ==========

# Mouvement constant
def moveConst():
    global x1, y1, dx, dy, flag
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
    delPomme()
    #if abs(y1 - 250) == 0 or abs(y1 + Size - 250) == 0:
    if touch(obs1):        
        can.delete(ALL)
        text = can.create_text(Cx // 4, Cy // 2, font="Helvatica 28", text='GAME OVER!', anchor=NW)
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

# Mouvement Joueur
def up(*ignore):
    global dx, dy
    if len(body) > 0:
        if dy <= 0:
            dx, dy = 0, -Size
    else:
        if dy >= 0:
            dx, dy = 0, -Size
def down(*ignore):
    global dx, dy
    if len(body) > 0:
        if dy >= 0:
            dx, dy = 0, Size
    else:
        if dy <= 0:
            dx, dy = 0, Size
def left(*ignore):
    global dx, dy
    if len(body) > 0:
        if dx <= 0:
            dx, dy = -Size, 0
    else:
        if dx >= 0:
            dx, dy = -Size, 0
def right(*ignore):
    global dx, dy
    if len(body) > 0:
        if dx >= 0:
            dx, dy = Size, 0
    else:
        if dx <= 0:
            dx, dy = Size, 0
            
# Fonctions du corps du SNAKE
body = []         
def create():
    global snake, body, dx, dy
    pS = can.coords(snake)
    # LEFT
    if dx < 0:
        body += [can.create_rectangle(pS[0] + Size, pS[1], pS[2] + Size, pS[3], width = 2, fill = COLORS[randrange(479)])]
    # RIGHT
    if dx > 0:
        body += [can.create_rectangle(pS[0] - Size, pS[1], pS[2] - Size, pS[3], width = 2, fill = COLORS[randrange(479)])]
    # DOWN
    if dy > 0:
        body += [can.create_rectangle(pS[0], pS[1] - Size, pS[2], pS[3] - Size, width = 2, fill = COLORS[randrange(479)])]
    # UP
    if dy < 0:
        body += [can.create_rectangle(pS[0], pS[1] + Size, pS[2], pS[3] + Size, width = 2, fill = COLORS[randrange(479)])]

def follow(xF, yF):
    global body
    for i in range(len(body)):
        posP = can.coords(body[i])
        can.coords(body[i], xF, yF, xF + Size, yF + Size)
        xF, yF = posP[0], posP[1] 
        
def touch(chose):
    coordsC = can.coords(chose)
    coordsS = can.coords(snake)
    Xs, Ys = (coordsS[0] + coordsS[2])/2, (coordsS[1] + coordsS[3])/2
    Xc, Yc = (coordsC[0] + coordsC[2])/2, (coordsC[1] + coordsC[3])/2
    if abs(Xs - Xc) < Size and abs(Ys - Yc) < Size:
        can.delete(chose)
        return True
    return False

def delPomme():
    global pomme, snake, Size, score, text
    if touch(pomme):
        can.delete(pomme)
        ranX = randrange(Size, Cx)
        ranY = randrange(Size, Cy)
        pomme = can.create_oval(ranX, ranY, ranX + Size, ranY + Size, fill='red')
        create()
        # experiment
        score += 1
        can.delete(text)
        text = can.create_text(Cx // 2, 20, font="Helvatica 28", text=score, anchor=NW)
        
# ========== MAIN PROGRAM ==========
fen = Tk()
fen.title("Snake")

can = Canvas(fen, bg = 'dark grey', height = Cx, width = Cy)
can.pack(side = LEFT, padx = 5, pady = 5)

# SNAKE
snake = can.create_rectangle(x1, y1, x1 + Size, y1 + Size, width = 2, fill = 'green')

fen.bind("<Up>", up)
fen.bind("<Down>", down)
fen.bind("<Left>", left)
fen.bind("<Right>", right)

# Pomme
ranX = randrange(Size, Cx-Size)
ranY = randrange(Size, Cy-Size)
pomme = can.create_oval(ranX, ranY, ranX + Size, ranY + Size, fill='red')


# Marqueur avec les points
score = 0
text = can.create_text(Cx // 2, 20, font="Helvatica 28", text=score, anchor=NW)

# Obstacles
obs1 = can.create_rectangle(230, Cy//2, 270, Cy//2 + 10, fill='black')

# Boutons
btn1 = Button(fen, text='Start', command = start)     # Commencer mouvement
btn1.pack()

btn2 = Button(fen, text='Stop', command = stop)     # Arreter mouvement
btn2.pack()

# TODO: Pour quoi ça?
can.focus_set()

fen.mainloop()

COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']