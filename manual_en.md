# KamibotPi API Documentation

Complete API reference documentation for the Python library to control KamibotPi robots.

## Table of Contents

- [Initialization and Connection](#initialization-and-connection)
- [Basic Operations](#basic-operations)
- [Map Board Movement](#map-board-movement)
- [Speed Control](#speed-control)
- [Precision Control](#precision-control)
- [LED Control](#led-control)
- [Top Motor Control](#top-motor-control)
- [Sensors](#sensors)
- [Drawing Shapes](#drawing-shapes)
- [Sound](#sound)
- [Utilities](#utilities)

---

## Initialization and Connection

### `KamibotPi(port, baud, timeout, verbose)`

Creates a KamibotPi object and connects via serial port.

**Parameters:**
- `port` (str): Serial port path (e.g., '/dev/ttyUSB0', 'COM3')
- `baud` (int, optional): Communication speed, default 57600
- `timeout` (int, optional): Serial communication timeout (seconds), default 2
- `verbose` (bool, optional): Enable debug messages, default False

**Example:**
```python
robot = KamibotPi(port='/dev/ttyUSB0', baud=57600, timeout=2, verbose=False)
```

---

### `close()`

Closes the serial connection and exits the program.

**Parameters:** None

**Returns:** None

**Example:**
```python
robot.close()
```

---

### `disconnect()`

Closes only the serial connection (does not exit the program).

**Parameters:** None

**Returns:** None

**Example:**
```python
robot.disconnect()
```

---

## Basic Operations

### `delay(sec)`

Waits for the specified time in seconds.

**Parameters:**
- `sec` (float): Time to wait in seconds

**Returns:** None

**Example:**
```python
robot.delay(2)  # Wait 2 seconds
robot.delay(0.5)  # Wait 0.5 seconds
```

---

### `delayms(ms)` / `wait(ms)`

Waits for the specified time in milliseconds.

**Parameters:**
- `ms` (int): Time to wait in milliseconds

**Returns:** None

**Example:**
```python
robot.delayms(500)  # Wait 500ms
robot.wait(1000)  # Wait 1000ms (1 second)
```

---

### `stop()`

Immediately stops all robot movement.

**Parameters:** None

**Returns:** None

**Example:**
```python
robot.stop()
```

---

### `init()`

Initializes the robot.

**Parameters:** None

**Returns:** None

**Example:**
```python
robot.init()
```

---

## Map Board Movement

### `move_forward(value, opt)`

Moves the robot forward.

**Parameters:**
- `value` (int): Number of cells to move
- `opt` (str, optional): Map board type
  - `'-l'`: Line map board (default)
  - `'-b'`: Block map board

**Returns:** None

**Example:**
```python
robot.move_forward(1, '-l')  # Move forward 1 cell on line map
robot.move_forward(3, '-b')  # Move forward 3 cells on block map
```

---

### `move_backward(value)`

Moves the robot backward. (Works only on block map board)

**Parameters:**
- `value` (int): Number of cells to move

**Returns:** None

**Example:**
```python
robot.move_backward(2)  # Move backward 2 cells
```

---

### `turn_left(value, opt)`

Turns the robot left.

**Parameters:**
- `value` (int, optional): Number of turns, default 1 (ignored on line map)
- `opt` (str, optional): Map board type
  - `'-l'`: Line map board (default)
  - `'-b'`: Block map board

**Returns:** None

**Example:**
```python
robot.turn_left(1, '-l')  # Turn left on line map
robot.turn_left(2, '-b')  # Turn left 2 times on block map
```

---

### `turn_right(value, opt)`

Turns the robot right.

**Parameters:**
- `value` (int, optional): Number of turns, default 1 (ignored on line map)
- `opt` (str, optional): Map board type
  - `'-l'`: Line map board (default)
  - `'-b'`: Block map board

**Returns:** None

**Example:**
```python
robot.turn_right(1, '-l')  # Turn right on line map
robot.turn_right(3, '-b')  # Turn right 3 times on block map
```

---

### `turn_back(value, opt)`

Turns the robot 180 degrees.

**Parameters:**
- `value` (int, optional): Number of turns, default 1 (ignored on line map)
- `opt` (str, optional): Map board type
  - `'-l'`: Line map board (default)
  - `'-b'`: Block map board

**Returns:** None

**Example:**
```python
robot.turn_back(1, '-l')  # Turn back on line map
robot.turn_back(2, '-b')  # Turn back 2 times on block map
```

---

### `toggle_linetracer(mode, speed)`

Turns the line tracer function on or off.

**Parameters:**
- `mode` (bool): Line tracer mode
  - `True`: On
  - `False`: Off
- `speed` (int, optional): Line tracer speed (0-255), default 100

**Returns:** None

**Example:**
```python
robot.toggle_linetracer(True, 100)  # Start line tracer at speed 100
robot.toggle_linetracer(False)  # Stop line tracer
```

---

## Speed Control

### `go_dir_speed(ldir, lspeed, rdir, rspeed)`

Controls left and right wheel direction and speed individually.

**Parameters:**
- `ldir` (str): Left wheel rotation direction
  - `'f'`: Forward
  - `'b'`: Backward
- `lspeed` (int): Left wheel speed (0-255)
- `rdir` (str): Right wheel rotation direction
  - `'f'`: Forward
  - `'b'`: Backward
- `rspeed` (int): Right wheel speed (0-255)

**Returns:** None

**Example:**
```python
robot.go_dir_speed('f', 100, 'f', 100)  # Both wheels forward at speed 100
robot.go_dir_speed('f', 150, 'b', 150)  # Left forward, right backward
```

---

### `go_forward_speed(lspeed, rspeed)`

Moves forward at the specified speed.

**Parameters:**
- `lspeed` (int): Left wheel speed (0-255)
- `rspeed` (int): Right wheel speed (0-255)

**Returns:** None

**Example:**
```python
robot.go_forward_speed(100, 100)  # Move forward at speed 100
robot.go_forward_speed(150, 100)  # Curve slightly right while moving forward
```

---

### `go_backward_speed(lspeed, rspeed)`

Moves backward at the specified speed.

**Parameters:**
- `lspeed` (int): Left wheel speed (0-255)
- `rspeed` (int): Right wheel speed (0-255)

**Returns:** None

**Example:**
```python
robot.go_backward_speed(100, 100)  # Move backward at speed 100
```

---

### `go_left_speed(speed)`

Turns left at the specified speed.

**Parameters:**
- `speed` (int): Rotation speed (0-255)

**Returns:** None

**Example:**
```python
robot.go_left_speed(80)  # Turn left at speed 80
```

---

### `go_right_speed(speed)`

Turns right at the specified speed.

**Parameters:**
- `speed` (int): Rotation speed (0-255)

**Returns:** None

**Example:**
```python
robot.go_right_speed(80)  # Turn right at speed 80
```

---

## Precision Control

### `move_step(ldir, lstep, rdir, rstep)`

Moves precisely in step units.

**Parameters:**
- `ldir` (str): Left wheel rotation direction ('f': forward, 'b': backward)
- `lstep` (int): Left wheel step count
- `rdir` (str): Right wheel rotation direction ('f': forward, 'b': backward)
- `rstep` (int): Right wheel step count

**Returns:** None

**Example:**
```python
robot.move_step('f', 100, 'f', 100)  # Move forward 100 steps
robot.move_step('f', 200, 'b', 200)  # Rotate in place
```

---

### `move_time(ldir, lsec, rdir, rsec)`

Moves in time units.

**Parameters:**
- `ldir` (str): Left wheel rotation direction ('f': forward, 'b': backward)
- `lsec` (int): Left wheel operation time (seconds)
- `rdir` (str): Right wheel rotation direction ('f': forward, 'b': backward)
- `rsec` (int): Right wheel operation time (seconds)

**Returns:** None

**Example:**
```python
robot.move_time('f', 2, 'f', 2)  # Move forward for 2 seconds
robot.move_time('f', 1, 'b', 1)  # Rotate in place for 1 second
```

---

### `move_forward_unit(value, opt, speed)`

Moves forward with specified units.

**Parameters:**
- `value` (int): Value to move
- `opt` (str, optional): Unit type
  - `'-l'`: cm (default)
  - `'-t'`: seconds
  - `'-s'`: steps
- `speed` (int, optional): Movement speed (0-255), default 50

**Returns:** None

**Example:**
```python
robot.move_forward_unit(10, '-l', 50)  # Move forward 10cm
robot.move_forward_unit(2, '-t', 100)  # Move forward for 2 seconds
robot.move_forward_unit(500, '-s', 80)  # Move forward 500 steps
```

---

### `move_backward_unit(value, opt, speed)`

Moves backward with specified units.

**Parameters:**
- `value` (int): Value to move
- `opt` (str, optional): Unit type ('-l': cm, '-t': seconds, '-s': steps), default '-l'
- `speed` (int, optional): Movement speed (0-255), default 50

**Returns:** None

**Example:**
```python
robot.move_backward_unit(10, '-l', 50)  # Move backward 10cm
```

---

### `turn_left_speed(value, speed)`

Rotates left in place by specified angle.

**Parameters:**
- `value` (int, optional): Rotation angle, default 90
- `speed` (int, optional): Rotation speed (0-255), default 50

**Returns:** None

**Example:**
```python
robot.turn_left_speed(90, 50)  # Turn left 90 degrees
robot.turn_left_speed(180, 80)  # Turn left 180 degrees
```

---

### `turn_right_speed(value, speed)`

Rotates right in place by specified angle.

**Parameters:**
- `value` (int, optional): Rotation angle, default 90
- `speed` (int, optional): Rotation speed (0-255), default 50

**Returns:** None

**Example:**
```python
robot.turn_right_speed(90, 50)  # Turn right 90 degrees
robot.turn_right_speed(45, 30)  # Turn right 45 degrees
```

---

### `move_left_unit(value, opt, speed)`

Moves left with specified units.

**Parameters:**
- `value` (int): Value to move
- `opt` (str, optional): Unit type ('-l': cm, '-t': seconds, '-s': steps), default '-l'
- `speed` (int, optional): Movement speed (0-255), default 50

**Returns:** None

**Example:**
```python
robot.move_left_unit(5, '-l', 50)  # Move left 5cm
```

---

### `move_right_unit(value, opt, speed)`

Moves right with specified units.

**Parameters:**
- `value` (int): Value to move
- `opt` (str, optional): Unit type ('-l': cm, '-t': seconds, '-s': steps), default '-l'
- `speed` (int, optional): Movement speed (0-255), default 50

**Returns:** None

**Example:**
```python
robot.move_right_unit(5, '-l', 50)  # Move right 5cm
```

---

## LED Control

### `turn_led(rval, gval, bval)`

Sets LED color with RGB values.

**Parameters:**
- `rval` (int): Red value (0-255)
- `gval` (int): Green value (0-255)
- `bval` (int): Blue value (0-255)

**Returns:** None

**Example:**
```python
robot.turn_led(255, 0, 0)  # Red
robot.turn_led(0, 255, 0)  # Green
robot.turn_led(255, 255, 0)  # Yellow
robot.turn_led(0, 0, 0)  # Turn off LED
```

---

### `turn_led_idx(idx)`

Sets LED color with predefined color index.

**Parameters:**
- `idx` (int): Color index (0-8)
  - 0: Red
  - 1: Orange
  - 2: Yellow
  - 3: Green
  - 4: Blue
  - 5: Sky blue
  - 6: Purple
  - 7: White

**Returns:** None

**Example:**
```python
robot.turn_led_idx(0)  # Red
robot.turn_led_idx(3)  # Green
robot.turn_led_idx(7)  # White
```

---

## Top Motor Control

### `top_motor_degree(dir, value, speed)`

Rotates the top motor by specified angle.

**Parameters:**
- `dir` (str): Rotation direction
  - `'l'`: Left
  - `'r'`: Right
- `value` (int, optional): Rotation angle, default 90
- `speed` (int, optional): Rotation speed (0-255), default 50

**Returns:** None

**Example:**
```python
robot.top_motor_degree('r', 90, 50)  # Rotate right 90 degrees
robot.top_motor_degree('l', 180, 80)  # Rotate left 180 degrees
```

---

### `top_motor_abspos(degree, speed)`

Moves the top motor to an absolute angle position.

**Parameters:**
- `degree` (int, optional): Absolute angle position (0-65000), default 0
- `speed` (int, optional): Rotation speed (0-255), default 50

**Returns:** None

**Example:**
```python
robot.top_motor_abspos(0, 50)  # Move to 0 degree position
robot.top_motor_abspos(180, 80)  # Move to 180 degree position
```

---

### `top_motor_time(dir, value, speed)`

Rotates the top motor for specified time.

**Parameters:**
- `dir` (str): Rotation direction ('l': left, 'r': right)
- `value` (int, optional): Rotation time (seconds), default 3
- `speed` (int, optional): Rotation speed (0-255), default 50

**Returns:** None

**Example:**
```python
robot.top_motor_time('r', 2, 50)  # Rotate right for 2 seconds
robot.top_motor_time('l', 5, 80)  # Rotate left for 5 seconds
```

---

### `top_motor_round(dir, value, speed)`

Rotates the top motor by specified number of rotations.

**Parameters:**
- `dir` (str): Rotation direction ('l': left, 'r': right)
- `value` (int, optional): Number of rotations, default 1
- `speed` (int, optional): Rotation speed (0-255), default 50

**Returns:** None

**Example:**
```python
robot.top_motor_round('r', 2, 50)  # Rotate right 2 times
robot.top_motor_round('l', 1, 100)  # Rotate left 1 time
```

---

### `top_motor_stop()`

Immediately stops the top motor rotation.

**Parameters:** None

**Returns:** None

**Example:**
```python
robot.top_motor_stop()
```

---

## Sensors

### `get_object_detect(opt)`

Activates the object detection sensor and reads values.

**Parameters:**
- `opt` (bool, optional): Sensor operation mode
  - `True`: Activate sensor (default)
  - `False`: Stop sensor

**Returns:** 
- `tuple`: (left_object, right_object) - Left and right object detection values

**Example:**
```python
left, right = robot.get_object_detect(True)
print(f"Left: {left}, Right: {right}")
```

---

### `get_line_sensor(opt)`

Activates the line sensor and reads values.

**Parameters:**
- `opt` (bool, optional): Sensor operation mode
  - `True`: Activate sensor (default)
  - `False`: Stop sensor

**Returns:**
- `tuple`: (right_line, center_line, left_line) - Right, center, left line detection values

**Example:**
```python
right, center, left = robot.get_line_sensor(True)
print(f"Right: {right}, Center: {center}, Left: {left}")
```

---

### `get_color_sensor(opt)`

Activates the color sensor and reads color index.

**Parameters:**
- `opt` (bool, optional): Sensor operation mode
  - `True`: Activate sensor (default)
  - `False`: Stop sensor

**Returns:**
- `int`: Color index value

**Example:**
```python
color = robot.get_color_sensor(True)
print(f"Color index: {color}")
```

---

### `get_color_elements(opt)`

Activates the color sensor and reads RGB values.

**Parameters:**
- `opt` (bool, optional): Sensor operation mode
  - `True`: Activate sensor (default)
  - `False`: Stop sensor

**Returns:**
- `tuple`: (r, g, b) - Red, Green, Blue values

**Example:**
```python
r, g, b = robot.get_color_elements(True)
print(f"RGB: ({r}, {g}, {b})")
```

---

### `get_battery()`

Reads the battery level.

**Parameters:** None

**Returns:**
- `int`: Battery value

**Example:**
```python
battery = robot.get_battery()
print(f"Battery: {battery}")
```

---

### `get_version()`

Reads firmware version information.

**Parameters:** None

**Returns:** None

**Example:**
```python
robot.get_version()
```

---

## Drawing Shapes

### `draw_tri(len)`

Draws a triangle.

**Parameters:**
- `len` (int): Length of one side of the triangle (cm)

**Returns:** None

**Example:**
```python
robot.draw_tri(10)  # Draw a triangle with 10cm sides
```

---

### `draw_rect(len)`

Draws a rectangle.

**Parameters:**
- `len` (int): Length of one side of the rectangle (cm)

**Returns:** None

**Example:**
```python
robot.draw_rect(10)  # Draw a rectangle with 10cm sides
```

---

### `draw_penta(len)`

Draws a pentagon.

**Parameters:**
- `len` (int): Length of one side of the pentagon (cm)

**Returns:** None

**Example:**
```python
robot.draw_penta(8)  # Draw a pentagon with 8cm sides
```

---

### `draw_hexa(len)`

Draws a hexagon.

**Parameters:**
- `len` (int): Length of one side of the hexagon (cm)

**Returns:** None

**Example:**
```python
robot.draw_hexa(7)  # Draw a hexagon with 7cm sides
```

---

### `draw_star(len)`

Draws a star shape.

**Parameters:**
- `len` (int): Length of one side of the star (cm)

**Returns:** None

**Example:**
```python
robot.draw_star(10)  # Draw a star with 10cm sides
```

---

### `draw_circle(len)`

Draws a circle.

**Parameters:**
- `len` (int): Radius of the circle (cm)

**Returns:** None

**Example:**
```python
robot.draw_circle(5)  # Draw a circle with 5cm radius
```

---

### `draw_semicircle(len, side)`

Draws a semicircle.

**Parameters:**
- `len` (int): Radius of the semicircle (cm)
- `side` (str, optional): Semicircle direction
  - `'l'`: Left (default)
  - `'r'`: Right

**Returns:** None

**Example:**
```python
robot.draw_semicircle(5, 'l')  # Draw left semicircle
robot.draw_semicircle(5, 'r')  # Draw right semicircle
```

---

### `draw_arc(radius, value, mode)`

Draws an arc.

**Parameters:**
- `radius` (int): Radius of the arc (cm)
- `value` (int, optional): Time (seconds) or angle, default 1
- `mode` (int, optional): Unit mode
  - `0`: Time (seconds) based (default)
  - `1`: Angle based

**Returns:** None

**Example:**
```python
robot.draw_arc(10, 2, 0)  # Arc with 10cm radius for 2 seconds
robot.draw_arc(10, 90, 1)  # Arc with 10cm radius for 90 degrees
```

---

## Sound

### `melody(scale, sec)`

Plays a sound with specified scale and duration.

**Parameters:**
- `scale` (int, optional): Musical scale (0-83), default 45
- `sec` (int, optional): Sound duration (seconds), default 1

**Returns:** None

**Example:**
```python
robot.melody(45, 1)  # Play scale 45 for 1 second
robot.melody(60, 0.5)  # Play scale 60 for 0.5 seconds
```

---

### `beep()`

Makes a short beep sound.

**Parameters:** None

**Returns:** None

**Example:**
```python
robot.beep()  # Short beep
```

---

## Utilities

### `angle3p(p1, p2, p3)` (Static Method)

Calculates the angle formed by three points (counterclockwise).

**Parameters:**
- `p1` (tuple): First point (x1, y1)
- `p2` (tuple): Center point (x2, y2)
- `p3` (tuple): Third point (x3, y3)

**Returns:**
- `float`: Angle in degrees

**Example:**
```python
angle = KamibotPi.angle3p((0, 0), (1, 0), (1, 1))
print(f"Angle: {angle} degrees")
```

---

### `remap(value, source_range, target_range)`

Remaps a value from one range to another.

**Parameters:**
- `value` (float): Value to remap
- `source_range` (tuple): Source range (min, max)
- `target_range` (tuple): Target range (min, max)

**Returns:**
- `float`: Remapped value

**Example:**
```python
# Convert 50 from 0-100 range to 0-10 range
result = robot.remap(50, (0, 100), (0, 10))
print(result)  # 5.0

# Convert 5 from 0-10 range to 0-100 range
result = robot.remap(5, (0, 10), (0, 100))
print(result)  # 50.0
```

---

### `diff_color(color1, color2)` (Global Function)

Calculates the Euclidean distance between two RGB colors.

**Parameters:**
- `color1` (tuple): First color (r, g, b)
- `color2` (tuple): Second color (r, g, b)

**Returns:**
- `float`: Distance between colors (closer to 0 means more similar)

**Example:**
```python
from kamibotpi import diff_color

color1 = (255, 0, 0)  # Red
color2 = (255, 100, 0)  # Orange
distance = diff_color(color1, color2)
print(f"Color difference: {distance}")
```

---

## Constants and Classes

### LED Color Constants

You can use predefined LED colors:

```python
from kamibotpi import LedColor

robot.turn_led(*LedColor.RED)      # Red
robot.turn_led(*LedColor.ORANGE)   # Orange
robot.turn_led(*LedColor.YELLOW)   # Yellow
robot.turn_led(*LedColor.GREEN)    # Green
robot.turn_led(*LedColor.BLUE)     # Blue
robot.turn_led(*LedColor.SKYBLUE)  # Sky blue
robot.turn_led(*LedColor.PURPLE)   # Purple
robot.turn_led(*LedColor.WHITE)    # White
robot.turn_led(*LedColor.OFF)      # Off
```

---

## Complete Examples

### Basic Usage Example

```python
from kamibotpi import KamibotPi
import time

# Connect to robot
robot = KamibotPi(port='/dev/ttyUSB0', baud=57600)

# Turn LED red
robot.turn_led(255, 0, 0)
robot.delay(1)

# Move forward 2 cells
robot.move_forward(2, '-l')

# Turn right
robot.turn_right(1, '-l')

# Draw a triangle
robot.draw_tri(10)

# Make a sound
robot.beep()

# Close connection
robot.close()
```

---

### Sensor Usage Example

```python
from kamibotpi import KamibotPi

robot = KamibotPi(port='/dev/ttyUSB0')

# Object detection
left_obj, right_obj = robot.get_object_detect(True)
print(f"Object detection - Left: {left_obj}, Right: {right_obj}")

# Line sensor
right_line, center_line, left_line = robot.get_line_sensor(True)
print(f"Line detection - Right: {right_line}, Center: {center_line}, Left: {left_line}")

# Color detection
r, g, b = robot.get_color_elements(True)
print(f"Color: RGB({r}, {g}, {b})")

# Battery check
battery = robot.get_battery()
print(f"Battery: {battery}")

robot.disconnect()
```

---

### Precision Control Example

```python
from kamibotpi import KamibotPi

robot = KamibotPi(port='/dev/ttyUSB0')

# Move forward 10cm
robot.move_forward_unit(10, '-l', 50)

# Turn right 90 degrees
robot.turn_right_speed(90, 50)

# Move backward 5cm
robot.move_backward_unit(5, '-l', 50)

# Precise movement in steps
robot.move_step('f', 500, 'f', 500)

robot.close()
```

---

### Top Motor Control Example

```python
from kamibotpi import KamibotPi

robot = KamibotPi(port='/dev/ttyUSB0')

# Rotate right 90 degrees
robot.top_motor_degree('r', 90, 50)
robot.delay(1)

# Rotate left 180 degrees
robot.top_motor_degree('l', 180, 50)
robot.delay(1)

# Return to 0 degree position
robot.top_motor_abspos(0, 50)

# Rotate 2 times
robot.top_motor_round('r', 2, 80)

robot.close()
```

---

### Line Tracer Example

```python
from kamibotpi import KamibotPi

robot = KamibotPi(port='/dev/ttyUSB0')

# Start line tracer (speed 100)
robot.toggle_linetracer(True, 100)

# Run for 5 seconds
robot.delay(5)

# Stop line tracer
robot.toggle_linetracer(False)

robot.close()
```

---

## Important Notes

1. **Serial Port**: You must specify the correct serial port. On Linux, common ports are `/dev/ttyUSB0`, `/dev/ttyACM0`, etc. On Windows, use `COM3`, `COM4`, etc.

2. **Permission Issues**: On Linux, you may need serial port access permissions:
   ```bash
   sudo usermod -a -G dialout $USER
   ```

3. **Speed Range**: Motor speed uses the 0-255 range. Very low speeds may not move the motors.

4. **Battery**: Low battery can prevent the robot from operating normally. Check regularly with `get_battery()`.

5. **Sequential Execution**: When executing multiple commands consecutively, use `delay()` to allow time for previous actions to complete.

6. **Return Packets**: All commands receive return packets from the robot. Sensor values are updated through these return packets.

---

## Troubleshooting

### Connection Failed
```python
# Check ports
import serial.tools.list_ports
ports = serial.tools.list_ports.comports()
for port in ports:
    print(port.device)
```

### Robot Not Responding
- Check battery
- Verify serial cable connection
- Use correct baud rate (default 57600)

### Sensor Values Not Updating
- Confirm sensor function called with `opt=True`
- Verify return packets are being received properly (debug with `verbose=True`)

---

## License and Support

This library is a Python interface for controlling KamibotPi robots.

**Developer Support:** If issues occur, check debug messages with the `verbose=True` option.

```python
robot = KamibotPi(port='/dev/ttyUSB0', verbose=True)
```
