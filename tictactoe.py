import pgzrun
import random
WIDTH=600
HEIGHT=600
currentTurn="X"
board=[""]*9
gameover = False
def draw ():
    screen.fill("white")
    screen.draw.line ((200,0),(200,600),"black")
    screen.draw.line ((400,0),(400,600),"black")
    screen.draw.line ((0,200),(600,200),"black")
    screen.draw.line ((0,400),(600,400),"black")
    screen.draw.text (f"Turn:{currentTurn}",(270,10),color="black")
    for i in range (9):
        x = (i%3)*200 + 25
        y = (i//3)*200 + 25
        if board [i] == "X":
            screen.blit ("tictactoe x",(x,y))
        elif board [i] == "O":
            screen.blit ("tictactoe o",(x,y))

def update():
    pass
def on_mouse_down(pos):
    global currentTurn, gameover
    if "" not in board:
        gameover = True
    else:
        x,y = pos
        col = x//200
        row = y//200
        index = 3*row + col
        if board [index] == "":
            board [index] = currentTurn
            if currentTurn == "X":
                currentTurn = "O"
            else:
                currentTurn = "X"
        print (board)
pgzrun.go()