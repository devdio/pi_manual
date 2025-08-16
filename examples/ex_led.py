#-*-coding:utf-8-*-
import random
from pyKamipi.pibot import *

# 카미봇 연결
kamibot = KamibotPi('COM3', 57600)

# ------------------------------------------------
# LED
# ------------------------------------------------
kamibot.turn_led(255, 0, 0)
kamibot.delay(1)
kamibot.turn_led(0, 255, 0)
kamibot.delay(1)
kamibot.turn_led(0, 0, 255)
kamibot.delay(1)


for i in range(8):
    kamibot.turn_led_idx(i)
    kamibot.delay(0.5)

for i in range(10):
    kamibot.turn_led(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    kamibot.delay(0.5)

for i in range(100):
    kamibot.turn_led(255, 0, 0)
    kamibot.turn_led(0, 0, 255)


# 카미봇 연결 해제 
kamibot.close()

