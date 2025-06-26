import pgzrun
WIDTH=800
HEIGHT=600
character=Actor("fighter plane")
character.x = 400
character.y = 550
bullets=[]
level=1
enemies=[]
rows=3+level
col=4+level
for x in range (col):
    for y in range (rows):
        character_2=Actor("bee_1")
        character_2.x=250+70*x
        character_2.y=-50+50*y
        enemies.append (character_2)
def draw ():
    screen.blit("spacebackground", (0,0))
    character.draw ()
    for bullet in bullets:
        bullet.draw ()
    for enemie in enemies:
        enemie.draw ()
def update():
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
            enemies.remove (enemie)
def on_key_down(key):
    if key==keys.SPACE:
        character_1=Actor("bullet")
        character_1.x = character.x
        character_1.y = character.y-20
        bullets.append (character_1)

pgzrun.go()