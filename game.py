from curses import window
from pygame import *
import os 

window = display.set_mode((700, 500))
display.set_caption("Догонялки")
clock = time.Clock()

background = transform.scale(image.load("background.jpg"), (700,500))
sprite1 = transform.scale(image.load("hero.png"), (100, 100))

game = True
x = 100
y = 100
while game:
    clock.tick(60)
    window.blit(background, (0, 0))
    window.blit(sprite1, (x, y))
    display.update()

    key_pressed = key.get_pressed()
    if key_pressed[K_UP]:
        y -=10
    if key_pressed[K_DOWN]:
        y +=10    
    if key_pressed[K_LEFT]:
        x -=10    
    if key_pressed[K_RIGHT]:
        x +=10    

    for e in event.get():
        if e.type == QUIT:
            game = False