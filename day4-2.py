# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:32:37 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
x,y,z = mc.player.getTilePos()
for i in range(20):
    r = random.randrange(1,5)

    if r == 1: #往右生成4個
        mc.setBlocks(x,y,z,x+4,y,z,41)
        x = x+4
    elif r ==2 : #往左生成4個
        mc.setBlocks(x,y,z,x-4,y,z,46)
        x = x-4
    elif r ==3: #往前生成4個
        mc.setBlocks(x,y,z,x,y,z+4,137)
        z = z+4
    elif r == 4:#往後生成4個
        mc.setBlocks(x,y,z,x,y,z-4,56)
        z = z-4
 #題目：增加上下兩個方向 
        
