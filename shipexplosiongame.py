import pgzrun
import random
WIDTH=512
HEIGHT=544
character = Actor("ship")
character.x = 256
character.y = 256
Images = ["blueenemy", "redenemy", "greyenemy", "greenenemy"]
enemies = []
def draw ():
    screen.blit("map",(0,0))
    character.draw ()
    for enemy in enemies:
        enemy.draw ()
        animate (enemy, pos=character.pos, angle=enemy.angle_to(character.pos)-90, duration=3)
def update():
    pass
def on_mouse_down (pos):
    animate (character, pos=pos, angle=character.angle_to(pos)-90, duration=1, tween = "bounce_end")
def spawn_enemy ():
    img = random.choice (Images)
    enemy = Actor(img)
    if img == "greenenemy":
        enemy.x = 90
        enemy.y = 80
    elif img == "redenemy":
        enemy.x = 90
        enemy.y = 415
    elif img == "blueenemy":
        enemy.x = 415
        enemy.y = 80
    elif img == "greyenemy":
        enemy.x = 420
        enemy.y = 415
    enemies.append (enemy)
clock.schedule_interval (spawn_enemy,2)
pgzrun.go()
