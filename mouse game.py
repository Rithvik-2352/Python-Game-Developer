import pgzrun
import random
WIDTH=500
HEIGHT=500
character=Actor("mouse")
character.x = 250
character.y = 250
def draw ():
    screen.fill("blue")
    character.draw ()
def update():
    pass
def on_mouse_down(pos):
    print (pos)
    if character.collidepoint(pos):
        character.x=random.randint (0,500)
        character.y=random.randint (0,500)
pgzrun.go()