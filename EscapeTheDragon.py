#!/usr/bin/env python
# encoding: utf-8
'''
@author: LinJungui
@contact: deamoncao100@gmail.com
@software: garner
@file: EscapeTheDragon.py
@time: 2019/5/28 0028 16:22
@desc:Escape the dragon
'''

import sys,time,random,math,pygame
from pygame.locals import *
from common import print_text
from MySprite import MySprite

def reset_arrow():
    y=random.randint(250,350)
    arrow.position=800,y

#main program begins
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Escape The dragon Game")
font=pygame.font.Font(None,18)
framerate=pygame.time.Clock()

bg=pygame.image.load("pic/background.png").convert_alpha()

group=pygame.sprite.Group()

dragon=MySprite(screen)
dragon.load("pic/dragon.png",260,150,3)
dragon.position=100,230
group.add(dragon)

player=MySprite(screen)
player.load("pic/caveman.png",50,64,8)
player.first_frame=1
player.last_frame=7
player.position=400,300
group.add(player)

arrow=MySprite(screen)
arrow.load("pic/flame.png",40,16,1)
arrow.position=800,320
group.add(arrow)

arrow_vel=8.0
game_over=False
you_win=False
player_jumping=False
jump_vel=0.0
player_start_y=player.Y

#repeating loop

while True:
    framerate.tick(30)
    ticks=pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type==QUIT:sys.exit()
    keys=pygame.key.get_pressed()
    if keys[K_ESCAPE]:sys.exit()
    elif keys[K_SPACE]:
        if not player_jumping:
            player_jumping=True
        jump_vel=-8.0

    #update the arrow
    if not game_over:
        arrow.X-=arrow_vel
        if arrow.X<-40:reset_arrow()

    if pygame.sprite.collide_rect(arrow,player):
        reset_arrow()
        player.X-=10

    if pygame.sprite.collide_rect(arrow,dragon):
        reset_arrow()
        dragon.X-=10

    if pygame.sprite.collide_rect(player,dragon):
        game_over=True

    if dragon.X<-10:
        you_win=True
        game_over=True

    if player_jumping:
        player.Y+=jump_vel
        jump_vel+=0.5
        if player.Y>player_start_y:
            player_jumping=False
            player.Y=player_start_y
            jump_vel=0.0

    screen.blit(bg,(0,0))
    if not game_over:
        group.update(ticks,50)
    group.draw(screen)
    print_text(screen,font,350,560,"Press SPACE to jump!")

    if game_over:
        print_text(screen,font,360,100,"GAME OVER")
        if you_win:
            print_text(screen,font,330,130,"YOU BEAT THE DRAGON!")
        else:
            print_text(screen,font,330,130,"THE DRAGON GOT YOU!")

    pygame.display.update()


