# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:22:51 2020

@author: USER
"""

import time
from mcpi.minecraft import Minecraft
a=1
import random
mc=Minecraft.create()
mc.executeCommand("clear WillySu")
time.sleep(5)
x,y,z=mc.player.getTilePos()
mc.setBlocks(x+25,y-2,z+25,x-25,y-2,z-25,41)
mc.setBlocks(x+25,y-1,z+25,x-25,y-1,z-25,166)
mc.setBlocks(x+25,y+3,z+25,x-25,y+3,z-25,166)
mc.setBlocks(x+25,y+4,z+25,x-25,y+4,z-25,169)
mc.setBlocks(x+25,y+5,z+25,x-25,y+5,z-25,10)
mc.executeCommand("gamemode survival WillySu")
mc.executeCommand("give WillySu minecraft:iron_sword")
mc.executeCommand("give WillySu minecraft:bow")
mc.executeCommand("give WillySu minecraft:arrow 64")
mc.executeCommand("give WillySu minecraft:diamond_sword minecraft:sharpness")
mc.executeCommand("give WillySu minecraft:cooked_fish 64")
#import time
pos=mc.player.getPos()
while True:
    if a==1:
        x=pos.x+random.uniform(-20,20)
        z=pos.z+random.uniform(-20,20)
        y=pos.y
        mc.spawnEntity(x,y,z,54)
        a=+1
        time.sleep(2)
        if a==10:
            time.sleep(2)
            
           
           #time.sleep(1)
            x=pos.x+random.uniform(-20,20)
            z=pos.z+random.uniform(-20,20)
            y=pos.y
            mc.spawnEntity(x,y,z,54)
            mc.spawnEntity(x,y,z,54)
            a=+1
            if a==20:
                
                time.sleep(3)
                x=pos.x+random.uniform(-20,20)
                z=pos.z+random.uniform(-20,20)
                y=pos.y
                mc.spawnEntity(x,y,z,54)
                mc.spawnEntity(x,y,z,54)
                mc.spawnEntity(x,y,z,51)
                mc.spawnEntity(x,y,z,34)
                a=a+1
                if a==30:
                   mc.setBlocks(x+25,y+5,z+25,x-25,y+5,z-25,0)
                   mc.spawnEntity(x,y,z,99)
                   mc.spawnEntity(x,y,z,99)
                   mc.spawnEntity(x,y,z,99)
                   mc.spawnEntity(x,y,z,99)
                   

                   

