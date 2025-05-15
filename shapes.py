import pgzrun
import random
WIDTH=500
HEIGHT=500
size=500
def draw ():
    global size
    screen.fill("black")
    for i in range (20):
        r_1=random.randint (0,255)
        g=random.randint (0,255)
        b=random.randint (0,255)
        r = Rect((0,0),(size,size))
        r.center =(250,250)
        screen.draw.filled_rect (r,(r_1,g,b))
        size-=20
        #r_1-=5
        #g+=5
        #b-=0
#def update():
   # pass
pgzrun.go()