# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 14:07:56 2020

@author: USER
"""
import time
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
print(mc.player.getTilePos())
x=50
y=100
z=100
mc.player.setTilePos(x,y,z)
time.sleep(1)
