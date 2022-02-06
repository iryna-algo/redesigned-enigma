from pygame import *

clock = time.Clock()
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")

background = transform.scale(image.load("background.jpg"), (win_width, win_height))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

game = True
while game:
    clock.tick(60)
    window.blit(background, (0, 0))
    display.update()

    for e in event.get():
        if e.type == QUIT:
            game = False