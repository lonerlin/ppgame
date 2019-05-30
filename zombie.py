#!/usr/bin/env python
# encoding: utf-8
'''
@author: LinJungui
@contact: deamoncao100@gmail.com
@software: garner
@file: zombie.py
@time: 2019/5/29 0029 17:05
@desc:Zombie Mob Game
'''
import itertools,sys,time,random,math,pygame
from pygame.locals import *
from common import *
from MySprite import MySprite
from Point import Point

def calc_velocity(direction,vel=1.0):
    velocity=Point(0,0)
    if direction==0:
        velocity.y=-vel
    elif direction==2:
        velocity.x=vel
    elif direction==4:
        velocity.y=vel
    elif direction==6:
        velocity.x=-vel
    return velocity

def reverse_direction(sprite):
    if sprite.direction==0:
        sprite.direction=4
    elif sprite.direction==2:
        sprite.direction=6
    elif sprite.direction == 4:
        sprite.direction = 0
    elif sprite.direction == 6:
        sprite.direction = 2
def add_zombie():
    zombie = MySprite(screen)
    zombie.load("pic/zombie walk.png", 96, 96, 8)
    zombie.position = random.randint(0, 700), random.randint(0, 500)
    zombie.direction = random.randint(0, 3) * 2
    zombie_group.add(zombie)

pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Zombie Mob")
font=pygame.font.Font(None,36)
timer=pygame.time.Clock()
pygame.time.set_timer(USEREVENT+1,3000)
#create sprite groups
player_group=pygame.sprite.Group()
zombie_group=pygame.sprite.Group()
health_group=pygame.sprite.Group()

#create the player sprite
player=MySprite(screen)
player.load("pic/farmer walk.png",96,96,8)
player.position=80,80
player.direction=4
player_group.add(player)

#create the zombie sprite
zombie_image=pygame.image.load("pic/zombie walk.png").convert_alpha()
for n in range(0,10):
    add_zombie()

#create heath sprite
health=MySprite(screen)
health.load("pic/health.png",32,32,1)
health.position=400,300
health_group.add(health)

game_over=False
player_moving=False
player_health=100

#repeating loop
while True:
    timer.tick(30)
    ticks=pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type==QUIT:sys.exit()
        if event.type==USEREVENT+1:add_zombie()
    keys=pygame.key.get_pressed()
    if keys[K_ESCAPE]:sys.exit()
    elif keys[K_UP] or keys[K_w]:
        player.direction=0
        player_moving=True
    elif keys[K_RIGHT] or keys[K_d]:
        player.direction=2
        player_moving = True
    elif keys[K_DOWN] or keys[K_s]:
        player.direction = 4
        player_moving = True
    elif keys[K_LEFT] or keys[K_a]:
        player.direction =6
        player_moving = True
    else:
        player_moving=False

    if not game_over:
        player.first_frame=player.direction*player.columns
        player.last_frame=player.first_frame+player.columns-1
        if player.frame<player.first_frame:
            player.frame=player.first_frame
        if not player_moving:
            player.frame=player.first_frame=player.last_frame
        else:
            player.velocity=calc_velocity(player.direction,1.5)
            player.velocity.x*=1.5
            player.velocity.y*=1.5

        player_group.update(ticks,50)

        if player_moving:
            player.X+=player.velocity.x
            player.Y+=player.velocity.y
            if player.X<0:player.X=0
            if player.Y<0:player.Y=0
            if player.X>700:player.X=700
            if player.Y>500:player.Y=500

        zombie_group.update(ticks, 50)

        for z in zombie_group:
            z.first_frame=z.direction*z.columns
            z.last_frame=z.first_frame+z.columns-1
            if z.frame<z.first_frame:
                z.frame=z.first_frame
            z.velocity=calc_velocity(z.direction)

            z.X+=z.velocity.x
            z.Y+=z.velocity.y
            if z.X<0 or z.X>700 or z.Y<0 or z.Y>500:
                reverse_direction(z)


            attacker=None
            attacker=pygame.sprite.spritecollideany(player,zombie_group)
            if attacker!=None:
                if pygame.sprite.collide_circle_ratio(0.5)(player,attacker):
                    player_health-=10
                    if attacker.X<player.X:
                        attacker.X-=10
                    elif attacker.X>player.X:
                        attacker.X+=10
                    else:
                        attacker=None


        health_group.update(ticks,50)

        if pygame.sprite.collide_circle_ratio(0.5)(player,health):
            player_health+=30
            if player_health>100:player_health=100
            health.X=random.randint(0,700)
            health.Y=random.randint(0,500)

        if player_health<=0:
            game_over=True

        screen.fill((50,50,100))

        health_group.draw(screen)
        zombie_group.draw(screen)
        player_group.draw(screen)

        pygame.draw.rect(screen,(50,150,50,180),Rect(300,570,player_health*2,25))
        pygame.draw.rect(screen,(100,200,100,180),Rect(300,570,200,25),2)

        if game_over:
            print_text(screen,font,300,100,"GAME OVER")

        pygame.display.update()





