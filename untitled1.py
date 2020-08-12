# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:17:06 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
y=63
z=106
x=59
mc.setblock(x,y,z,20)
mc.setblock(x+1,y,z,20)
mc.setblock(x+2,y,z,20)
mc.setblock(x,y-1,z,20)
mc.setblock(x,y-2,z,20)
mc.setblock(x+2,y-1,z,20)
mc.setblock(x+2,y-2,z,20)
mc.setblock(x+1,y-2,z,20)

mc.setblock(x,y,z+1,20)
mc.setblock(x+1,y,z+1,20)
mc.setblock(x+2,y,z+1,20)
mc.setblock(x,y-1,z+1,20)
mc.setblock(x,y-2,z+1,20)
mc.setblock(x+2,y-1,z+1,20)
mc.setblock(x+2,y-2,z+1,20)
mc.setblock(x+1,y-2,z+1,20)

mc.setblock(x,y,z+2,20)
mc.setblock(x+1,y,z+2,20)
mc.setblock(x+2,y,z+2,20)
mc.setblock(x,y-1,z+2,20)
mc.setblock(x,y-2,z+2,20)
mc.setblock(x+2,y-1,z+2,20)
mc.setblock(x+2,y-2,z+2,20)
mc.setblock(x+1,y-2,z+2,20)

mc.setblock(x,y,z+3,20)
mc.setblock(x+1,y,z+3,20)
mc.setblock(x+2,y,z+3,20)
mc.setblock(x,y-1,z+3,20)
mc.setblock(x,y-2,z+3,20)
mc.setblock(x+2,y-1,z+3,20)
mc.setblock(x+2,y-2,z+3,20)
mc.setblock(x+1,y-2,z+3,20)

mc.setblock(x,y,z+4,20)
mc.setblock(x+1,y,z+4,20)
mc.setblock(x+2,y,z+4,20)
mc.setblock(x,y-1,z+4,20)
mc.setblock(x,y-2,z+4,20)
mc.set block(x+2,y-1,z+4,20)
mc.set block(x+2,y-2,z+4,20)
mc.set block(x+1,y-2,z+4,20)