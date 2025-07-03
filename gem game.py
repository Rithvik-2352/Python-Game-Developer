import pgzrun
import random
WIDTH=500
HEIGHT=500
character=Actor("wreck it ralph")
character.x = 250
character.y = 250
score=0
gems=[]
for i in range (7):
      character_2=Actor("gem")
      gems.append (character_2)
      character_2.x = random.randint (10,490)
      character_2.y = random.randint (10,490)
def draw ():
    screen.fill("black")
    screen.draw.text ("Score:{}".format (score), (250,480), color=(255,255,255))
    character.draw ()
    for gem in gems:
          gem.draw ()
def update():
    global score
    if keyboard.a:
            if character.x>20:
                character.x-=3
    if keyboard.d:
            if character.x<480:
                character.x+=3
    if keyboard.w:
            if character.y>20:
                character.y-=3
    if keyboard.s:
            if character.y<480:
                character.y+=3
    for gem in gems:
          if character.colliderect(gem):
                gems.remove (gem)
                score+=1
    
pgzrun.go()