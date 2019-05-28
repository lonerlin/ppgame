#!/usr/bin/env python
# encoding: utf-8
'''
@author: LinJungui
@contact: deamoncao100@gmail.com
@software: garner
@file: MySprite.py
@time: 2019/5/27 0027 11:17
@desc:MySprite test
'''
import pygame
from pygame.locals import *
class MySprite(pygame.sprite.Sprite):
    def __init__(self,target):
        pygame.sprite.Sprite.__init__(self)
        self.master_image=None
        self.frame=0
        self.old_frame=-1
        self.frame_height=1
        self.frame_width=1
        self.fist_frame=0
        self.last_frame=0
        self.columns=1
        self.last_time=0

    #X property
    def _getx(self):return  self.rect.x
    def _setx(self,value):self.rect.x=value
    X=property(_getx,_setx)

    #Y property
    def _gety(self):return  self.rect.y
    def _sety(self,value):self.rect.y=value
    Y=property(_gety,_sety)

    #position property
    def _getpos(self):return self.rect.topleft
    def _setpos(self,pos):self.rect.topleft=pos
    position=property(_getpos,_setpos)

    def load(self,filename,width,height,columns):
        self.master_image=pygame.image.load(filename).convert_alpha()
        self.frame_width=width
        self.frame_height=height
        self.rect=Rect(0,0,width,height)
        self.columns=columns

    def update(self, currect_time,rate=30):
        if currect_time>self.last_time+rate:
            self.frame+=1
        if self.frame>self.last_frame:
            self.frame=self.fist_frame
        self.last_time=currect_time
        #build curret frame only if it changed
        if self.frame!=self.old_frame:
            frame_x=(self.frame%self.columns)*self.frame_width
            frame_y=(self.frame//self.columns)*self.frame_height
            rect=Rect(frame_x,frame_y,self.frame_width,self.frame_height)
            self.image=self.master_image.subsurface(rect)
            self.old_frame=self.frame

    def __str__(self):
        return str(self.frame)+","+str(self.fist_frame) +\
            ","+str(self.last_frame)+","+str(self.frame_width)+\
            ","+str(self.frame_height)+","+str(self.columns)+","+str(self.rect)

