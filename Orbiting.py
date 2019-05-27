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
from Point import Point
from common import wrap_angle,print_text
#main program begins
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Orbit Demo")
font=pygame.font.Font(None,18)

#load bitmaps
space=pygame.image.load("pic/space.png").convert()
planet=pygame.image.load("pic/planet2.png").convert_alpha()
ship=pygame.image.load("pic/freelance.png").convert_alpha()
width,height=ship.get_size()
ship=pygame.transform.smoothscale(ship,(width//2,height//2))

radius=250
angle=0.0
pos=Point(0,0)
old_pos=Point(0,0)

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
    #draw planet
    width,height=planet.get_size()
    screen.blit(planet,(400-width/2,300-height/2))
    #screen.blit(ship,(50,50))

    #move the ship
    angle=wrap_angle( angle-0.1)
    pos.x=math.sin(math.radians(angle))*radius
    pos.y=math.cos(math.radians(angle))*radius

    #ratate the ship
    delta_x=(pos.x-old_pos.x)
    delta_y=(pos.y-old_pos.y)
    rangle=math.atan2(delta_y,delta_x)
    rangled=wrap_angle(-math.degrees(rangle))
    scratch_ship=pygame.transform.rotate(ship,rangled)

    #draw the ship
    width,height=scratch_ship.get_size()
    x=400+pos.x-width//2
    y=300+pos.y-height//2
    screen.blit(scratch_ship,(x,y))

    old_pos.x=pos.x
    old_pos.y=pos.y
    print_text(screen,font,0,0,"Orbit:"+"{:.0f}".format(angle))
    print_text(screen,font,0,20,"Rotation:"+"{:.2f}".format(rangle))
    print_text(screen,font,0,40,"Position"+str(pos))
    print_text(screen,font,0,60,"Old Pos:" +str(old_pos))


    pygame.display.update()