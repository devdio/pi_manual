## Template

```python
from pyKamipi.pibot import *

robot = KamibotPi('COM8', 57600)
robot.init()

try:
    # YOUR CODE
    print("Program started")


except KeyboardInterrupt:
    print("Program stopped by user")
    
finally:
    robot.stop()
    robot.close()

```

## Line Follower Robot
```
from pyKamipi.pibot import *

robot = KamibotPi('COM8', 57600)
robot.init()

try:
    # YOUR CODE
    right, center, left = robot.get_line_sensor(True)
    print(f"Right: {right}, Center: {center}, Left: {left}")

    if center == 1:
      robot.go_dir_speed("f", 50, "f", 50)
    elif left == 1:
        pass
    elif right == 1:
        pass

except KeyboardInterrupt:
    print("Program stopped by user")
    
finally:
    robot.stop()
    robot.close()
```
