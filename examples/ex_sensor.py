#-*-coding:utf-8-*-
import random
from pyKamipi.pibot import *

# 카미봇 연결
kamibot = KamibotPi('COM3', 57600)

# ------------------------------------------------
# 물체감지 get_object_detect
# ------------------------------------------------
left, right = kamibot.get_object_detect()
print(f"left={left}, right={right}")
kamibot.delay(1)
kamibot.get_object_detect(False)


# ------------------------------------------------
# 라인센서 get_line_sensor
# ------------------------------------------------
left, center, right = kamibot.get_line_sensor()
print(f"left={left}, center={center}, right={right}")
kamibot.delay(1)

# ------------------------------------------------
# 컬러센서 get_color_sensor
# ------------------------------------------------
color = kamibot.get_color_sensor()
print(f"color={color}")
kamibot.delay(1)
kamibot.get_color_sensor(False)

# ------------------------------------------------
# 배터리 get_battery
# ------------------------------------------------
battery = kamibot.get_battery()
print(f"battery={battery}")
kamibot.delay(1)


# ------------------------------------------------
# 멜로디  melody
# ------------------------------------------------
kamibot.melody(45, 1)
kamibot.delay(1)

kamibot.beep()
kamibot.delay(1)


# 카미봇 연결 해제 
kamibot.close()

