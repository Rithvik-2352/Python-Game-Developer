import pgzrun
WIDTH=800
HEIGHT=600
character=Actor("fighter plane")
character.x = 400
character.y = 550
bullets=[]
level=0
rows=0
lives=3
enemies_to_remove=[]
col=0
score=0
game_won = False
enemies=[]
character.dead=False
def lvl ():
    global enemies
    global rows
    global enemies_to_remove
    global col
    enemies=[]
    enemies_to_remove=[] 
    if rows<7:
        rows=1+level
    else:
        rows=7
    if col<7:
        col=4+level
    else:
        col=7
    for x in range (col):
        for y in range (rows):
            character_2=Actor("bee_1")
            character_2.x=250+70*x
            character_2.y=-50+50*y
            enemies.append (character_2)
def draw ():
    global level
    screen.blit("space background", (0,0))
    screen.draw.text ("Score: {}".format (score), (50,280), color=(255,255,255), fontsize=50)
    screen.draw.text ("Lives: {}".format (lives), (50,350), color=(255,255,255), fontsize=40)
    screen.draw.text ("Level: {}".format (level), (50,400), color=(255,255,255), fontsize=40)
    if character.dead==False:
        character.draw ()
        for bullet in bullets:
            bullet.draw ()
        for enemie in enemies:
            enemie.draw ()
    else:
        screen.blit("space background", (0,0))
        screen.draw.text ("Score: {}".format (score), (50,280), color=(255,255,255), fontsize=50)
        screen.draw.text ("Game Over (ship is dead)",(50,350), color=(255,255,255), fontsize=40)
    if game_won:
        screen.draw.text("Game Over (You Win!)", (380, 280), color=(255, 255, 255), fontsize=40)
def update():
    global level
    global lives
    global score
    global enemies_to_remove
    global game_won
    if character.dead or game_won:
        return
    if keyboard.a:
        if character.x>50:
            character.x-=10
    if keyboard.d:
        if character.x<750:
            character.x+=10
    for bullet in bullets:
        bullet.y-=10
    for enemie in enemies:
        if enemie.y<500:
            enemie.y +=1
        else:
            enemies_to_remove.append (enemie)
            lives-=1
        for bullet in bullets:
            if enemie.colliderect (bullet):
                enemies_to_remove.append (enemie)
                bullets.remove (bullet)
                score+=1
        if enemie.colliderect (character):
            enemies_to_remove.append (enemie)
            lives-=1
    if lives<=0:
        character.dead=True
    for enemie in enemies_to_remove:
        if enemie in enemies:
            enemies.remove (enemie)
    if len(enemies)==0:
        if level>=6:
            game_won = True
        else:    
            level+=1
            lvl ()  
def on_key_down(key):
    if key==keys.SPACE:
        character_1=Actor("bullet")
        character_1.x = character.x
        character_1.y = character.y-20
        bullets.append (character_1)

pgzrun.go()
