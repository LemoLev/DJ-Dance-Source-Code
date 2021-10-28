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
lbd = Actor("lbd", (250, 60))
rbd = Actor("rbd", (593, 60))
dbd = Actor("nbd", (365, 60))
ubd = Actor("ubd", (470, 60))
gos = Actor('g.o.s.')
ws = Actor("w.s.")
tys = Actor("try_again")
notes = [Actor("ln", (250, 690)), Actor("rn", (593, 690)), Actor("un", (470, 690)), Actor("dn", (365, 690))]
nr = random.randint(0, 3)
count = 0
bf = Actor("bflose")
mode = 1
hitted = 0
#Music
music.play_once('kpytoi_ihct.wav')
#Drawing
def draw():
    global nr
    global mode
    global hitted
    if music.is_playing("ns"):
        bg_djk.draw()
        screen.draw.text("Score: " + str(count), center = (420, 12), color = 'white', fontsize = 36)
        lnna.draw()
        rnna.draw()
        dnna.draw()
        unna.draw()
        notes[nr].draw()
        if hitted == 1:
           lbd.draw()
           if notes[nr].y <600:
               hitted = 0
        if hitted == 2:
           rbd.draw()
           if notes[nr].y <600:
               hitted = 0
        if hitted == 3:
           ubd.draw()
           if notes[nr].y <600:
               hitted = 0
        if hitted == 4:
           dbd.draw()
           if notes[nr].y <600:
               hitted = 0
    if not music.is_playing("o|oo|o") and count > 0:
        mode = 2
        ws.draw()
    if not music.is_playing("o|oo|o") and count < 0 and mode != 4:
        tys.draw()
        mode = 3
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
        mode = 4
        music.stop()
    if mode == 4 and keyboard.r:
        mode = 1
        count = 0
        music.play_once("kpytoi_ihct.wav")
    if mode == 3 and keyboard.r:
        mode = 1
        count = 0
        music.play_once("kpytoi_ihct.wav")
    if mode == 2 and keyboard.r:
        mode = 1
        count = 0
        music.play_once("kpytoi_ihct.wav")
#Arrow Check
def on_key_down(key):
    global nr
    global count
    global hitted
    if ((key == keys.LEFT and nr == 0) or (key == keys.RIGHT and nr == 1) or (key == keys.UP and nr == 2) or (key == keys.DOWN and nr == 3)) and notes[nr].y <100:
        count += 10
        nr = random.randint(0, 3)
        notes[nr].y=690
        if key == keys.LEFT:
            hitted = 1
        if key == keys.RIGHT:
            hitted = 2
            rbd.draw()
        if key == keys.UP:
            hitted = 3
            ubd.draw()
        if key == keys.DOWN:
            hitted = 4
            dbd.draw()
pgzrun.go()
