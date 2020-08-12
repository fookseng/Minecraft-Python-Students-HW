# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 13:50:38 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
import random
import time
mc=Minecraft.create()
pos=mc.player.getPos()
while True:
    
    x=pos.x+random.uniform(-20,20)
    z=pos.z+random.uniform(-20,20)
    y=pos.y+30
    mc.spawnEntity(x,y,z, 20)
    mc.spawnEntity(x,y,z, 20)
    mc.spawnEntity(x,y,z, 20)
    mc.spawnEntity(x,y,z,20)
    mc.spawnEntity(x,y,z, 20)
    mc.spawnEntity(x,y,z,20)
    mc.spawnEntity(x,y,z, 20)
    mc.spawnEntity(x,y,z, 20)
    time.sleep(0.0000001)