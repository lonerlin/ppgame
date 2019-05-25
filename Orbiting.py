#!/usr/bin/env python
# encoding: utf-8
'''
@author: LinJungui
@contact: deamoncao100@gmail.com
@software: garner
@file: Orbiting.py
@time: 2019/5/25 0025 10:37
@desc:Orbiting Spaceship
'''
import random,math,pygame,sys
from pygame.locals import *

#main program begins
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Orbit Demo")

#load bitmaps
space=pygame.image.load("pic/space.png").convert()
planet=pygame.image.load("pic/planet2.png").convert_alpha()
ship=pygame.image.load("pic/freelance.png").convert_alpha()
width,height=ship.get_size()
ship=pygame.transform.smoothscale(ship,(width//2,height//2))
#repeating loop
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
    keys=pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    #draw background
    screen.blit(space,(0,0))
    width,height=planet.get_size()
    screen.blit(planet,(400-width/2,300-height/2))
    screen.blit(ship,(50,50))
    pygame.display.update()