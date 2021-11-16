# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import turtle
import math
import random
def branch(length):
    t.fd(length)
    return
    
t = turtle

t.speed(255)
t.up()
t.goto(0,-200)
t.down()
t.left(90)
def branch(l,angle):
    if l<1:
        # t.circle(l)
        return
    else:
        t.pensize(l//20)
        r = random.random()
        g = random.random()
        b = random.random()
        t.pencolor((r,g,b))    
        t.fd(l)
        t.left(angle)
        branch(2/3*l,angle)
        t.right(2*angle)
        branch(2/3*l,angle)
        t.left(angle)
        t.backward(l)
    
branch(200,30)
turtle.done()