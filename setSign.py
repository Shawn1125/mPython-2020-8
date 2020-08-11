from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z,=mc.player.getPos()
mc.setSign(x,y,z,63,0,"嘿","嘿嘿","嘿嘿嘿","嘿嘿嘿嘿") 