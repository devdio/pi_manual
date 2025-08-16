#-*-coding:utf-8-*-
import random
from pyKamipi.pibot import *

# 카미봇 연결
kamibot = KamibotPi('COM3', 57600)

# ------------------------------------------------
# 라인트레이서
# ------------------------------------------------
kamibot.toggle_linetracer(True, 100)
kamibot.delay(10)
kamibot.toggle_linetracer(False)

# ------------------------------------------------
# 블록 맵보드
# ------------------------------------------------
kamibot.move_forward(1, '-b')
kamibot.move_backward(1)
kamibot.turn_left(1, "-b")
kamibot.turn_right(1, "-b")
kamibot.turn_back(1, "-b")

# ------------------------------------------------
# 라인 맵보드
# ------------------------------------------------
kamibot.move_forward(1)
kamibot.turn_left()
kamibot.turn_right()
kamibot.turn_back()


# 카미봇 연결 해제 
kamibot.close()

