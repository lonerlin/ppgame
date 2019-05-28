#!/usr/bin/env python
# encoding: utf-8
'''
@author: LinJungui
@contact: deamoncao100@gmail.com
@software: garner
@file: spriteTest.py
@time: 2019/5/27 0027 9:15
@desc:test sprite
'''
import pygame,sys
from pygame.locals import *
from MySprite import MySprite
from common import print_text

pygame.init()
screen=pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("Sprite Animation Demo")
font=pygame.font.Font(None,18)
framerate=pygame.time.Clock()

#crete the dragon sprite
dragon=MySprite(screen)
dragon.load("pic/dragon.png",260,150,3)
group=pygame.sprite.Group()
group.add(dragon)

while True:
    framerate.tick(30)
    ticks=pygame.time.get_ticks()

    for even in pygame.event.get():
        if even.type==pygame.QUIT:sys.exit()
    key=pygame.key.get_pressed()
    if key[K_ESCAPE]:sys.exit()

    screen.fill((0,0,100))
    group.update(ticks)
    group.draw(screen)
    print_text(screen,font,0,0,"Sprite:"+str(dragon))
    pygame.display.update()