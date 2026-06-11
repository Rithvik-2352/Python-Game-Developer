import pgzrun
WIDTH = 600
HEIGHT = 600
currentTurn = "X"
board = [""] * 9
gameover = False
winner = None

def draw():
    screen.fill("white")
    screen.draw.line ((200,0),(200,600),"black")
    screen.draw.line ((400,0),(400,600),"black")
    screen.draw.line ((0,200),(600,200),"black")
    screen.draw.line ((0,400),(600,400),"black")

    for i in range(9):
        x = (i % 3) * 200 + 25
        y = (i // 3) * 200 + 25
        if board[i] == "X":
            screen.blit("tictactoe x", (x, y))
        elif board[i] == "O":
            screen.blit("tictactoe o", (x, y))
    if winner is not None:
        screen.draw.text(f"Winner: {winner}", (270, 10), color="black")
    elif gameover:
        screen.draw.text(f"Draw!", (270, 10), color="black")
    else:
        screen.draw.text(f"Turn: {currentTurn}", (270, 10), color="black")
    if winner is not None or gameover:
        screen.draw.text(f"Press R to restart", (270, 300), color="black")
def update():
    pass
def on_key_down(key):
    global currentTurn, board, gameover, winner
    
    if key == keys.R:
        if winner is not None or gameover:
            currentTurn = "X"
            board = [""] * 9
            gameover = False
            winner = None
def check_winner():
    global winner, gameover
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [2, 4, 6], [0, 4, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8]]
    for combo in winning_combinations:
        a, b, c = combo
        if board[a] != "" and (board[a] == board[b] == board[c]):
            winner = board[a]
            return
    if "" not in board:
        gameover = True

def on_mouse_down(pos):
    global currentTurn, gameover, winner
    
    # Don't allow moves if game is over
    if winner is not None or gameover:
        return
    
    x, y = pos
    col = x // 200
    row = y // 200
    
    # Validate click is within grid bounds
    if col < 0 or col > 2 or row < 0 or row > 2:
        return
    
    index = 3 * row + col
    
    # Only allow move if cell is empty
    if board[index] == "":
        board[index] = currentTurn
        check_winner()
        if currentTurn == "X":
            currentTurn = "O"
        else:
            currentTurn = "X"
        print(board)
pgzrun.go()