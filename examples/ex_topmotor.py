#-*-coding:utf-8-*-
import random
from pyKamipi.pibot import *

# 카미봇 연결
kamibot = KamibotPi('COM3', 57600)

# ------------------------------------------------
# 탑모터 제어  top_motor_degree
# ------------------------------------------------
# kamibot.top_motor_degree("l", 180)
# kamibot.delay(1)

# kamibot.top_motor_degree("r", 180)
# kamibot.delay(1)


# ------------------------------------------------
# 탑모터 제어  top_motor_abspos
# ------------------------------------------------
# kamibot.top_motor_abspos(0)
# kamibot.delay(1)

# kamibot.top_motor_abspos(90)
# kamibot.delay(1)

# kamibot.top_motor_abspos(180)
# kamibot.delay(1)

# ------------------------------------------------
# 탑모터 제어  top_motor_time
# ------------------------------------------------
# kamibot.top_motor_time("l", 10)
# kamibot.delay(1)
# kamibot.top_motor_time("r", 10)
# kamibot.delay(1)


# ------------------------------------------------
# 탑모터 제어  top_motor_round
# ------------------------------------------------
kamibot.top_motor_round("l", 1)
kamibot.delay(1)



# 카미봇 연결 해제 
kamibot.close()

