import pgzrun
import random
WIDTH=800
HEIGHT=600
mode=int(input("What difficulty would you like to choose; 1/easy, 2/medium, or 3/hard?"))
if mode == 1:
    nos=5
elif mode == 2:
    nos=10
elif mode == 3:
  nos=20
names=[]
lines=[]
next=0
for i in range (nos):
    sat=Actor("sattelite")
    sat.x = random.randint (50,750)
    sat.y = random.randint (50,550)
    names.append (sat)
def draw ():
    screen.blit("spacebackground",(0,0))
    num=1
    for name in names:
        name.draw ()
        screen.draw.text (f'{num}',(name.x-10, name.y+15))
        num+=1
    for line in lines:
        screen.draw.line(line[0],line[1],(0,100,255))    
def update():
    pass
def on_mouse_down(pos):
    global next,lines
    if next<nos:
        if names [next].collidepoint(pos):
            if next:
                lines.append ((names[next-1].pos,names[next].pos))
            next+=1
            print (lines)
        else:
            next=0
            lines=[]   
pgzrun.go()