#-*-coding:utf-8-*-
import random
from pyKamipi.pibot import *

# 카미봇 연결
kamibot = KamibotPi('COM3', 57600)

# ------------------------------------------------
# 정밀제어  move_forward_unit
# ------------------------------------------------
kamibot.move_forward_unit(10, "-l") # 10cm
kamibot.delay(1)
kamibot.stop()

kamibot.move_forward_unit(3, "-t") # 3sec
kamibot.delay(1)
kamibot.stop()


kamibot.move_forward_unit(50, "-s") # 50 step
kamibot.delay(1)
kamibot.stop()


# ------------------------------------------------
# 정밀제어  move_right_unit
# ------------------------------------------------
kamibot.move_right_unit(160, "-l") 
kamibot.delay(1)
kamibot.stop()

# ------------------------------------------------
# 정밀제어  move_left_unit
# ------------------------------------------------
kamibot.move_left_unit(160, "-l") 
kamibot.delay(1)
kamibot.stop()


# ------------------------------------------------
# 정밀제어  move_backward_unit
# ------------------------------------------------
kamibot.move_backward_unit(10, "-l") 
kamibot.delay(1)
kamibot.stop()

# ------------------------------------------------
# 정밀제어  turn_continous
# ------------------------------------------------
kamibot.turn_continous("r", 100)
kamibot.delay(1)
kamibot.stop()


# ------------------------------------------------
# 정밀제어  move_step
# ------------------------------------------------
kamibot.move_step("f", 100, "f", 100)
kamibot.delay(1)
kamibot.stop()


# ------------------------------------------------
# 정밀제어  move_time
# ------------------------------------------------
kamibot.move_time("f", 10, "f", 10)
kamibot.delay(1)
kamibot.stop()

# 카미봇 연결 해제 
kamibot.close()

