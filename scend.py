# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 16:17:30 2020

@author: USER
"""

import time
import random
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

time.sleep(1)

x,y,z=mc.player.getTilePos()

wallet_a=random.randrange(0,10)

wallet_b=random.randrange(0,10)
if wallet_a==4 or wallet_a==8:
    print("4or8")

total=wallet_a+wallet_b

if total>10:
    print("yes")
try:
    blockType=int(input("BLock id:"))
    mc.setBlock(x,y,z,blocktype)
except:
    print("Invalid")