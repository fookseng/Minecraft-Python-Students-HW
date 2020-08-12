# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:37:15 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
for i in range(20):
    mc.setBlock(x+i,y-1,z+i,1)