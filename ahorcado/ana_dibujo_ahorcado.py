# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 18:43:10 2020

@author: Ana Caviedes
"""
import pylab as pl
from PIL import Image, ImageDraw



image = Image.new('RGB', (500, 500))
draw = ImageDraw.Draw(image)

shape1 = [(400, 500), (400, 100)] 
draw.line(shape1, fill =255, width = 10) 
shape2 = [(400, 100), (200, 100)] 
draw.line(shape2, fill =255, width = 10) 
shape3 = [(200, 100), (200, 150)] 
draw.line(shape3, fill =255, width = 10) 
draw.ellipse((200-30, 170-30, 200+30, 170+30), fill=(255,0,0,0))
shape4 = [(200, 200), (200, 380)] 
draw.line(shape4, fill =255, width = 10) 
shape5 = [(200, 380), (100, 500)] 
draw.line(shape5, fill =255, width = 10) 
shape6 = [(200, 380), (300, 500)] 
draw.line(shape6, fill =255, width = 10) 
shape7 = [(200, 280), (100, 300)] 
draw.line(shape7, fill =255, width = 10)
shape7 = [(200, 280), (300, 300)] 
draw.line(shape7, fill =255, width = 10)

pl.imshow(image)




