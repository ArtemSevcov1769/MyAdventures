import mcpi.minecraft as mine
import time
from random import randint
mc = mine.Minecraft.create()

for i in range(7):
    x, y, z = randint(0, 2999), randint(0, 90), randint(0, 299)
    time.sleep(3)
    mc.player.setTilePos(x, y, z)

