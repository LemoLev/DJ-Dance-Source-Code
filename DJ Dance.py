import pgzrun
import pygame
import random
import sys
import time
#pgzero
WIDTH = 840 # Width of the window
HEIGHT = 630 # Height of the window

TITLE = "DJ Dance by ! LemoLev" # Title of the game
FPS = 30 # Frames per second
#Actors
bg_djk = Actor("bg_djk")
lnna = Actor("lnna", (250, 60))
rnna = Actor("rnna", (593, 60))
dnna = Actor("dnna", (365, 60))
unna = Actor("unna", (470, 60))
gos = Actor('g. o. s.')
notes = [Actor("ln", (250, 690)), Actor("rn", (593, 690)), Actor("un", (470, 690)), Actor("dn", (365, 690))]
nr = random.randint(0, 3)
count = 0
bf = Actor("bflose")
mode = 1
#Music
music.play_once('kpytoi_ihct.wav')
#Drawing
def draw():
    global nr
    bg_djk.draw()
    screen.draw.text(str(count), pos = (10, 10), color = 'white', fontsize = 36)
    lnna.draw()
    rnna.draw()
    dnna.draw()
    unna.draw()
    notes[nr].draw()
    if mode == 4:
        gos.draw()
#Moving
def muf():
    global nr
    global count
    if notes[nr].y < 0:
        notes[nr].y = 690
        nr = random.randint(0, 3)
        count -= 3
    else:
        notes[nr].y -= 13
#Update DT
def update(dt):
    global nr
    global count
    global mode
    muf()
    if count > 50:
        count = 50
    if count < -50:
        music.stop()
        mode = 4
    if mode == 4 and keyboard.r:
        mode = 1
    if mode == 4:
        while mode == 4:
            if count < 0:
                count = 0
            if keyboard.r:
                break
#Arrow Check
def on_key_down(key):
    global nr
    global count
    if ((key == keys.LEFT and nr == 0) or (key == keys.RIGHT and nr == 1) or (key == keys.UP and nr == 2) or (key == keys.DOWN and nr == 3)) and notes[nr].y <100:
        count += 10
        nr = random.randint(0, 3)
        notes[nr].y=690
pgzrun.go()
