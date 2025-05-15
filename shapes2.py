import pgzrun
import random
WIDTH=500
HEIGHT=500
rad=250
def draw ():
    global rad
    screen.fill("black")
    for i in range (25):
        r=random.randint (0,255)
        g=random.randint (0,255)
        b=random.randint (0,255)
        screen.draw.filled_circle ((250,250),rad,(r,g,b))
        rad-=20
#def update():
   # pass
pgzrun.go()