# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 15:32:54 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
def plantTree(x,y,z):
    mc.setBlock(x-1,y+3,z-1,x+1,y+5,z+1,18)
    mc.setBlocks(x,y,z,x,y+4,z,18)
for i in range(10):
    plantTree(x+i,y,z)