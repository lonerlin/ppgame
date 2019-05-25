#!/usr/bin/env python
# encoding: utf-8
'''
@author: LinJungui
@contact: deamoncao100@gmail.com
@software: garner
@file: analog_clock.py
@time: 2019/5/23 0023 16:13
@desc:Analog clock
'''
import sys,random,math,pygame
from pygame.locals import *
from datetime import datetime,date,time

def print_text(font,x,y,text,color=(255,255,255)):
    imgText=font.render(text,True,color)
    screen.blit(imgText,(x,y))

def wrap_angle(angle):
    return angle % 360
def draw_hand(screen,color,hand_angle,pos_x,pos_y,length,width):
    angle=wrap_angle(hand_angle*30-90)
    angle=math.radians(angle)
    x=math.cos(angle)*length
    y=math.sin(angle)*length
    target=(pos_x+x,pos_y+y)
    pygame.draw.line(screen,color,(pos_x,pos_y),target,width)

#main program begins
pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("Analog Clock Demo")

font =pygame.font.Font(None,36)
orange=220,180,0
white=255,255,255
yellow=255,255,0
pink=255,100,100

pos_x=300
pos_y=250
radius=250
angle=360

#repeating loop
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
    keys=pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    screen.fill((0, 0, 100))

    #draw one step around the circle
    pygame.draw.circle(screen,white,(pos_x,pos_y),radius,6)

    #draw the clock number 1-12
    for n in range(1,13):
        angle=math.radians(n*(360/12)-90)
        x=math.cos(angle)*(radius-20)-10
        y=math.sin(angle)*(radius-20)-10
        print_text(font,pos_x+x,pos_y+y,str(n))

    #get the time of day
    today=datetime.today()
    hours=today.hour%12
    minutes=today.minute
    second=today.second

    #draw the hours hand
    draw_hand(screen,pink,hours,pos_x,pos_y,170,25)
    draw_hand(screen,orange,minutes,pos_x,pos_y,190,12)
    draw_hand(screen,yellow,second,pos_x,pos_y,210,6)

    #cover the center
    pygame.draw.circle(screen,white,(pos_x,pos_y),20)
    print_text(font,0,0,str(hours)+":"+str(minutes)+":"+str(second))

    pygame.display.update()


