import pgzrun
import random
WIDTH=500
HEIGHT=500
character=Actor("mouse")
character_1=Actor("bee")
character.x = 250
character.y = 250
character_1.x = 250
character_1.y = 250
def draw ():
    screen.fill("blue")
    character.draw ()
    character_1.draw ()
def update():
    pass
def on_mouse_down(pos):
    print (pos)
    if character.collidepoint(pos) or character_1.collidepoint(pos):
        character.x=random.randint (0,500)
        character.y=random.randint (0,500)
        character_1.x=random.randint (0,500)
        character_1.y=random.randint (0,500)
pgzrun.go()