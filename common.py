#!/usr/bin/env python
# encoding: utf-8
'''
@author: LinJungui
@contact: deamoncao100@gmail.com
@software: garner
@file: common.py
@time: 2019/5/27 0027 8:14
@desc:common function
'''
def print_text(screen,font,x,y,text,color=(255,255,255)):
    imgText=font.render(text,True,color)
    screen.blit(imgText,(x,y))

def wrap_angle(angle):
    return angle % 360