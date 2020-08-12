# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:56:55 2020

@author: USER
"""
block=mc.getBlock(x,y,z)
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
    hits=mc.event.pollProjectileHits()
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        mc.setBlock(x,y,z,36)
        mc.postToChat("恭喜你獵到了"+str(block)
for i in range(5,10,5):
    print(i)