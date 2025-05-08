import pgzrun
import random
WIDTH=500
HEIGHT=500
character=Actor("alien")
character2=Actor("darth vader")
character.x = 250
character.y = 250
character2.x=250
character2.y=250
def draw ():
    screen.fill("blue")
    character.draw ()
    character2.draw ()
def update():
    pass
def on_mouse_down(pos):
    print (pos)
    if character.collidepoint(pos): 
        character2.x=random.randint (0,500)
        character2.y=random.randint (0,500)
    
pgzrun.go()