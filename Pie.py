#!/usr/bin/env python
# encoding: utf-8
'''
@author: LinJungui
@contact: deamoncao100@gmail.com
@software: garner
@file: Pie.py
@time: 2019/5/20 0020 8:19
@desc:Pie game
'''
import math
import pygame,sys
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("The Pie Game - Press 1,2,3,4")
myfont=pygame.font.Font(None,60)

color=200,80,60
width=4
x=300
y=250
radius=200
position=x-radius,y-radius,radius*2,radius*2

piece1=False
piece2=False
piece3=False
piece4=False

def draw_quadrant(s_angle,e_angle,e_line1_pos,e_line2_pos):
    start_angle = math.radians(s_angle)
    end_angle = math.radians(e_angle)
    pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
    pygame.draw.line(screen, color, (x,y), e_line1_pos, width)
    pygame.draw.line(screen, color, (x, y), e_line2_pos, width)


while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
        elif event.type==KEYUP:
            if event.key==pygame.K_ESCAPE:
                sys.exit()
            elif event.key==pygame.K_1:
                piece1=True
            elif event.key==pygame.K_2:
                piece2=True
            elif event.key==pygame.K_3:
                piece3=True
            elif event.key==pygame.K_4:
                piece4=True

    screen.fill((0,0,200))
    textImg1=myfont.render("1",True,color)
    screen.blit(textImg1,(x+radius/2-20,y-radius/2))
    textImg2=myfont.render("2",True,color)
    screen.blit(textImg2,(x-radius/2,y-radius/2))
    textImg3=myfont.render("3",True,color)
    screen.blit(textImg3,(x-radius/2,y+radius/2-20))
    textImg4=myfont.render("4",True,color)
    screen.blit(textImg4,(x+radius/2-20,y+radius/2-20))

    if piece1:draw_quadrant(0,90,(x,y-radius),(x+radius,y))
    if piece2:draw_quadrant(90,180,(x,y-radius),(x-radius,y))
    if piece3:draw_quadrant(180,270,(x-radius,y),(x,y+radius))
    if piece4:draw_quadrant(270,360,(x,y+radius),(x+radius,y))

    if piece1 and piece2 and piece3 and piece4:
        color=0,255,0

    pygame.display.update()


