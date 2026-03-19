import pgzrun
import random
WIDTH=512
HEIGHT=544
character = Actor("ship")
character.x = 256
character.y = 256
Images = ["blueenemy", "redenemy", "greyenemy", "greenenemy"]
enemies = []
attackmode = False
powerup = 0
lives = 3
game = True
enemylives = 0
speed = 0
def draw ():
    screen.blit("map",(0,0))
    screen.draw.text (f"Lives:{lives}",(10,5),color="black")
    screen.draw.text(f"Powerup:{powerup}",(410,5),color="black")
    if game==True:
        character.draw ()
        global speed
        for enemy in enemies:
            enemy.draw ()
            if enemy.image=="blueenemy":
                speed=0.5
            elif enemy.image=="redenemy":
                speed=1
            elif enemy.image=="greenenemy":
                speed=1.3
            elif enemy.image=="greyenemy":
                speed=1.6
            animate (enemy, pos=character.pos, angle=enemy.angle_to(character.pos)-90, duration=speed)
    elif game==False:
        screen.draw.text("Game Over",(230,240))
    elif game=="Win":
        screen.draw.text("You Win!",(230,240))
def update():
    global powerup, lives, game
    if lives>0:
        game=True
    elif lives==0:
        game=False
    elif lives==10:
        game="Win"
    if powerup==10:
        powerup=0
        lives+=1
    for enemy in enemies:
        global enemylives
        if enemy.colliderect (character):
            if attackmode == True:
                if enemy.image=="blueenemy":
                   enemylives-=1
                elif enemy.image=="redenemy":
                   enemylives-=1
                elif enemy.image=="greenenemy":
                   enemylives-=1
                elif enemy.image=="greyenemy":
                   enemylives-=1
                if enemylives<=0:
                    powerup+=1
                    enemies.remove (enemy)
                else:
                    enemy.x=random.randint(0,512)
                    enemy.y=random.randint(0,544)
            elif attackmode == False:
                lives-=1
                enemies.remove (enemy)
def stop_attackmode ():
    global attackmode
    attackmode = False
def on_mouse_down (pos):
    global attackmode
    attackmode = True
    animate (character, pos=pos, angle=character.angle_to(pos)-90, duration=1, tween = "bounce_end", on_finished=stop_attackmode)
def spawn_enemy ():
    img = random.choice (Images)
    enemy = Actor(img)
    global enemylives
    if img == "greenenemy":
        enemylives=3
        enemy.x = 90
        enemy.y = 80
    elif img == "redenemy":
        enemylives=2
        enemy.x = 90
        enemy.y = 415
    elif img == "blueenemy":
        enemylives=4
        enemy.x = 415
        enemy.y = 80
    elif img == "greyenemy":
        enemylives=1
        enemy.x = 420
        enemy.y = 415
    enemies.append (enemy)
clock.schedule_interval (spawn_enemy,1)
pgzrun.go()
