import pygame
import random
import math
from pygame import mixer

#intialize the pygame

pygame.init()
#create the screen
screen=pygame.display.set_mode((1200,600))
#background
bg=pygame.image.load('bg.png')
#background sound
mixer.music.load("Taki Taki.mp3")
mixer.music.play(-1)


#title and icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#player
playerImg=pygame.image.load('player.png')
playerx=170
playery=520
playerx_change=0

#enemy
enemyImg=[]
enemyx=[]
enemyy=[]
enemyx_change=[]
enemyy_change=[]

num_of_enemies=15

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0,1134))
    enemyy.append(random.randint(0,300))
    enemyx_change.append(9)
    enemyy_change.append(40)
#reaady=you can't see the bullet on screen
#fire -bullet is currently moving
bulletImg=pygame.image.load('bullet.png')
bulletx=0
bullety=520
bulletx_change=0
bullety_change=10
bullet_state="ready"

#score
score_value=0
font=pygame.font.Font('freesansbold.ttf',40)
textx=10
texty=10
xs=10
ys=45
xp=10
yp=80

#Game over text
over_font=pygame.font.Font('freesansbold.ttf',70)


def show_score(x,y):
    score=font.render("Score:"+str(score_value),True,(0,255,255))
    screen.blit(score,(x,y))
def highscore(x,y):
    score=font.render("High Score:"+str(hi),True,(0,255,255))
    screen.blit(score,(x,y))
def Playername(x,y):
    score=font.render("Player:"+str(ply),True,(0,255,255))
    screen.blit(score,(x,y))
def game_over_text(x,y):
    over_text=over_font.render("GAME OVER",True,(0,255,255))
    screen.blit(over_text,(460,320))
def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))

    
def iscollision(enemyx,enemy,bulletx,bullety):
    dis=math.sqrt(math.pow(enemyx[i]-bulletx,2)+math.pow(enemyy[i]-bullety,2))
    if dis<27:
        return True
    else:
        return False
#game loop
running=True
with open("hi.txt","r") as f:
        hi=f.read()
#with open("player.txt","r") as f:
#       a=f.read()
#       ply=str(input("Player Name:"))
        
while running:
    
    
    #rgb-red,green,blue
    screen.fill((0,0,0))
    #background image
    screen.blit(bg,(0,0))
    
    
    for event in pygame.event.get():
    
        if event.type== pygame.QUIT:
            running=False
            with open("hi.txt","w") as f:
                f.write(str(hi))
            #with open("player.txt","w") as f:
            #    f.write(str(ply))
        #if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                playerx_change=-15
            if event.key== pygame.K_RIGHT:
                playerx_change=15
            if event.key== pygame.K_SPACE:
                if bullet_state=="ready":
                    bullet_sound=mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletx=playerx
                    fire_bullet(playerx,bullety)
        
        if event.type == pygame.KEYUP:
            if event.key== pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerx_change=0
    #5= 5+0.1 =>5=5-0.1
    #5= 5+0.1
    playerx +=playerx_change
    player(playerx,playery)
    if playerx<=0:
        playerx=0
    elif playerx>=1136:
        playerx=1136

    #enemy movement
    for i in range(num_of_enemies):
        #Game Over
        if enemyy[i]>470:
            for j in range(num_of_enemies):
                enemyy[j]=2000
            game_over_text(550,450)
            break
            
        enemyx[i]+=enemyx_change[i]
    
        if enemyx[i]<=0:
            enemyx_change[i]=7
            enemyy[i]+=enemyy_change[i]
        elif enemyx[i]>=1136:
            enemyx_change[i]=-7
            enemyy[i]+=enemyy_change[i]
    #collision
        collision=iscollision(enemyx,enemyy,bulletx,bullety)
        if collision:
            explosion_sound=mixer.Sound('explosion.wav')
            explosion_sound.play()
            bullety=520
            bullet_state="ready"

            score_value+=1
            if score_value>int(hi):
                hi=score_value
            enemyx[i]=random.randint(0, 1200)
            enemyy[i]=random.randint(0,300)
        enemy(enemyx[i],enemyy[i],i)
    #bullet movement
    if bullety<=0:
        bullety=520
        bullet_state="ready"
            
    if bullet_state =="fire":
        fire_bullet(bulletx,bullety)
        bullety-=bullety_change
    
    
    player(playerx,playery)
    show_score(textx,texty)
    highscore(xs,ys)
    #Playername(xp,yp)
    pygame.display.update()




