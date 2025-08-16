#-*-coding:utf-8-*-
import random
from pyKamipi.pibot import *

# 카미봇 연결
kamibot = KamibotPi('COM3', 57600)

# ------------------------------------------------
# 콘트롤모드 go_dir_speed
# ------------------------------------------------
kamibot.go_dir_speed("f", 100, "f", 100)
kamibot.delay(1)

kamibot.go_dir_speed("b", 100, "f", 100)
kamibot.delay(1)

kamibot.go_dir_speed("f", 100, "b", 100)
kamibot.delay(1)

kamibot.go_dir_speed("b", 100, "b", 100)
kamibot.delay(1)
kamibot.stop()

# ------------------------------------------------
# 콘트롤모드 go_forward_speed
# ------------------------------------------------
kamibot.go_forward_speed(50, 50)
kamibot.delay(1)

kamibot.go_forward_speed(100, 50)
kamibot.delay(1)
kamibot.stop()

# ------------------------------------------------
# 콘트롤모드 go_backward_speed
# ------------------------------------------------
kamibot.go_backward_speed(50, 50)
kamibot.delay(1)

kamibot.go_backward_speed(100, 50)
kamibot.delay(1)
kamibot.stop()

# ------------------------------------------------
# 콘트롤모드 go_left_speed
# ------------------------------------------------
kamibot.go_left_speed(50)
kamibot.delay(1)

kamibot.go_left_speed(100)
kamibot.delay(1)
kamibot.stop()

# ------------------------------------------------
# 콘트롤모드 go_right_speed
# ------------------------------------------------
kamibot.go_right_speed(50)
kamibot.delay(1)

kamibot.go_right_speed(100)
kamibot.delay(1)
kamibot.stop()

# 카미봇 연결 해제 
kamibot.close()

