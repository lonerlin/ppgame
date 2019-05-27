#!/usr/bin/env python
# encoding: utf-8
'''
@author: LinJungui
@contact: deamoncao100@gmail.com
@software: garner
@file: Point.py
@time: 2019/5/27 0027 7:55
@desc:Class Point
'''
class Point(object):
    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    def getx(self):
        return self.__x
    def setx(self,x):
        self.__x=x
    x=property(getx,setx)

    def gety(self):
        return self.__y
    def sety(self,y):
        self.__y=y
    y=property(gety,sety)

    def __str__(self):
        return "{X:" +"{:.0f}".format(self.__x) +\
            ",Y:" +"{:.0f}".format(self.__y)+"}"