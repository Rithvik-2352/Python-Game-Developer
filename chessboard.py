import pgzrun
WIDTH=500
HEIGHT=500
def draw ():
    screen.fill("black")
    x=93.75
    y=31.25
    for i in range (4):
        for i in range (4):
            r = Rect((0,0),(62.5,62.5))
            r.center =(x,y)
            screen.draw.filled_rect (r,(255,255,255))
            x+=125
        y+=62.5
        x=31.25
        for i in range (5):
            r = Rect((0,0),(62.5,62.5))
            r.center =(x,y)
            screen.draw.filled_rect (r,(255,255,255))
            x+=125
        y+=62.5
        x=93.75
        
def update():
    pass
pgzrun.go()