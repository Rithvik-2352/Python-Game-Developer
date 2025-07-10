import pgzrun
WIDTH=900
HEIGHT=650
r=Rect (0,10,870,50)
r_1=Rect (50,70, 650,100)
r_2=Rect (750,70,100,100)
r_3=Rect (50,200,300,200)
r_4=Rect (400,200,300,200)
r_5=Rect (50,430,300,200)
r_6=Rect (400,430,300,200)
r_7=Rect (750,200,100,200)
r_8=Rect (750,430,100,200)
timeleft=10
def draw ():
    global timeleft
    screen.fill("black")
    screen.draw.filled_rect (r,(0,0,0))
    titletext= "Welcome to Trivia"
    screen.draw.textbox (titletext, r, color = (255,255,255))
    screen.draw.filled_rect (r_1,(0,190,255))
    screen.draw.filled_rect (r_2,(0,190,255))
    screen.draw.textbox (str(timeleft), r_2, color=(0,0,0))
    screen.draw.filled_rect (r_3,(255,140,0))
    screen.draw.filled_rect (r_4,(255,140,0))
    screen.draw.filled_rect (r_5,(255,140,0))
    screen.draw.filled_rect (r_6,(255,140,0))
    screen.draw.filled_rect (r_7,(0,255,50))
    screen.draw.textbox (("Skip"), r_7, color = (0,0,0), angle=-90)
    screen.draw.filled_rect (r_8,(255,0,0))
    screen.draw.textbox (("Reset"), r_8, color = (0,0,0), angle=-90)
def update():
    pass
pgzrun.go()