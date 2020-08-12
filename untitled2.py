# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:50:43 2020

@author: USER
"""

import time
import random
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
time.sleep(1)
x,y,z=mc.player.getTilePos()
while True:
    colour=random.randrange(0,16)
    mc.setBlocks(x+25,y-1,z+25,x-25,y-1,z-25,95,colour)
    time.sleep(0.5)