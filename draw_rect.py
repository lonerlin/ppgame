#!/usr/bin/env python
# encoding: utf-8
'''
@author: LinJungui
@contact: deamoncao100@gmail.com
@software: garner
@file: draw_rect.py
@time: 2019/5/20 0020 8:11
@desc:draw rect
'''
import pygame,sys
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("画矩形")
pos_x=300
pos_y=250
vel_x=2
vel_y=1

while True:
    for even in pygame.event.get():
        if even.type in(QUIT,KEYDOWN):
            sys.exit()
    screen.fill((0,0,200))

    pos_x+=vel_x
    pos_y+=vel_y

    if pos_x>500 or pos_x< 0 :
       vel_x=-vel_x
    if pos_y>600 or pos_y<0:
        vel_y=-vel_y
    color=255,255,0
    width=0
    pos=pos_x,pos_y,100,100
    pygame.draw.rect(screen,color,pos,width)

    pygame.display.update()