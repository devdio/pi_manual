# KamibotPi User Manual

## Table of Contents
1. [Overview](#overview)
2. [Installation and Initial Setup](#installation-and-initial-setup)
3. [Basic Usage](#basic-usage)
4. [Detailed Feature Guide](#detailed-feature-guide)
   - [Movement Control](#movement-control)
   - [Precision Control](#precision-control)
   - [LED Control](#led-control)
   - [Sensor Usage](#sensor-usage)
   - [Top Motor Control](#top-motor-control)
   - [Shape Drawing](#shape-drawing)
   - [Melody Playback](#melody-playback)
5. [Code Examples](#code-examples)
6. [Troubleshooting](#troubleshooting)

## Overview

KamibotPi is a Python library that communicates with KamibotPi hardware via serial communication, providing various functions for robot control.

### Key Features
- Movement/rotation control (map board/line map board)
- Precision control (step/time/distance units)
- Line tracer functionality
- LED color control
- Sensor reading (line/color/object detection)
- Top stepper motor control
- Geometric shape drawing
- Melody playback
- Battery/version information

## Installation and Initial Setup

### Required Package Installation
```bash
pip install pyserial
```

### Port Identification
- **Windows**: Check COM port in Device Manager (e.g., COM5)
- **Linux/Mac**: `/dev/ttyUSB0` or `/dev/ttyACM0`, etc.

### Basic Connection
```python
from kamibotpi import KamibotPi

# Connect with port and settings
kb = KamibotPi(port="COM5", baud=57600, timeout=2, verbose=True)
kb.init()  # Initialize robot
```

## Basic Usage

### Basic Template
```python
from kamibotpi import KamibotPi

# Connection and initialization
kb = KamibotPi(port="COM5", baud=57600, timeout=2, verbose=False)
kb.init()

try:
    # Write robot control code here
    kb.move_forward(2, opt="-l")
    kb.turn_left()
    
finally:
    # Program termination
    kb.close()  # Warning: calls sys.exit(0)
```

### Constructor Parameters
- `port`: Serial port name (required)
- `baud`: Baud rate (default: 57600)
- `timeout`: Read timeout in seconds (default: 2)
- `verbose`: Enable debug output (default: False)

## Detailed Feature Guide

### Movement Control

#### Map Board/Line Map Board Movement
```python
# Forward movement (line map board)
kb.move_forward(2, opt="-l")  # Move 2 cells forward

# Forward movement (block map board)
kb.move_forward(1, opt="-b")  # Move 1 cell forward

# Backward movement (block map board only)
kb.move_backward(1)

# Rotations
kb.turn_left(value=1, opt="-l")   # Turn left
kb.turn_right(value=1, opt="-l")  # Turn right
kb.turn_back(value=1, opt="-l")   # Turn 180 degrees
```

#### Speed Control
```python
# Individual left and right wheel speed control
kb.go_forward_speed(120, 120)   # Move forward
kb.go_backward_speed(100, 100)  # Move backward
kb.go_left_speed(90)            # Turn left
kb.go_right_speed(90)           # Turn right

# Simultaneous direction and speed control
kb.go_dir_speed('f', 120, 'b', 110)  # Left forward, right backward

# Stop
kb.stop()
```

#### Line Tracer
```python
# Start line tracer
kb.toggle_linetracer(True, speed=100)

# Stop line tracer
kb.toggle_linetracer(False)
```

### Precision Control

#### Step/Time-Based Movement
```python
# Step-based movement
kb.move_step('f', 400, 'b', 400)  # Left 400 steps forward, right 400 steps backward

# Time-based movement
kb.move_time('f', 2, 'f', 2)  # Both wheels 2 seconds forward
```

#### Unit-Based Movement
```python
# Distance units (cm)
kb.move_forward_unit(20, opt='-l', speed=80)   # 20cm forward
kb.move_backward_unit(10, opt='-l', speed=50)  # 10cm backward
kb.move_left_unit(15, opt='-l', speed=70)      # 15cm left
kb.move_right_unit(10, opt='-l', speed=60)     # 10cm right

# Time units (seconds)
kb.move_forward_unit(2, opt='-t', speed=80)    # 2 seconds forward

# Step units
kb.move_forward_unit(500, opt='-s', speed=60)  # 500 steps forward
```

#### Continuous Rotation
```python
# Continuous rotation (until stop command)
kb.turn_continous('l', speed=80)  # Continuous left rotation
kb.turn_continous('r', speed=80)  # Continuous right rotation
kb.stop()  # Stop rotation
```

### LED Control

#### Using Preset Colors
```python
# Set color by index (0~7)
kb.turn_led_idx(0)  # Red
kb.turn_led_idx(1)  # Orange
kb.turn_led_idx(2)  # Yellow
kb.turn_led_idx(3)  # Green
kb.turn_led_idx(4)  # Blue
kb.turn_led_idx(5)  # Sky blue
kb.turn_led_idx(6)  # Purple
kb.turn_led_idx(7)  # White
```

#### Direct RGB Control
```python
# Set color with RGB values (0~255)
kb.turn_led(255, 0, 0)    # Red
kb.turn_led(0, 255, 0)    # Green
kb.turn_led(0, 0, 255)    # Blue
kb.turn_led(255, 255, 0)  # Yellow
kb.turn_led(255, 0, 128)  # Pink
```

#### Using Preset Color Constants
```python
from kamibotpi import LedColor

kb.turn_led(*LedColor.RED)     # Red
kb.turn_led(*LedColor.GREEN)   # Green
kb.turn_led(*LedColor.BLUE)    # Blue
```

### Sensor Usage

#### Line Sensor
```python
# Read line sensor
left, center, right = kb.get_line_sensor(True)
print(f"Line sensor: Left={left}, Center={center}, Right={right}")

# Line detection example
if center > 100:  # Threshold value adjustable based on environment
    print("Line detected in center")
```

#### Object Detection Sensor
```python
# Read object detection sensor
left_obj, right_obj = kb.get_object_detect(True)
print(f"Object detection: Left={left_obj}, Right={right_obj}")

# Object detection example
if left_obj > 50 or right_obj > 50:  # Adjust threshold as needed
    print("Object detected!")
    kb.stop()
```

#### Color Sensor
```python
# Read color sensor
color = kb.get_color_sensor(True)
print(f"Detected color code: {color}")

# Color-based action example
if color == 1:  # Color code depends on firmware definition
    kb.turn_led_idx(0)  # Red LED
elif color == 2:
    kb.turn_led_idx(3)  # Green LED
```

#### Battery Check
```python
battery = kb.get_battery()
print(f"Battery level: {battery}")

if battery < 30:  # Example threshold
    print("Low battery!")
```

### Top Motor Control

#### Angle-Based Rotation
```python
# Relative angle rotation
kb.top_motor_degree('l', value=45, speed=60)   # 45 degrees left
kb.top_motor_degree('r', value=90, speed=80)   # 90 degrees right

# Move to absolute position
kb.top_motor_abspos(180, speed=70)  # Move to absolute 180 degrees
kb.top_motor_abspos(0, speed=50)    # Return to origin
```

#### Time/Revolution-Based
```python
# Time-based rotation
kb.top_motor_time('r', value=2, speed=80)  # 2 seconds right rotation

# Revolution-based
kb.top_motor_round('l', value=3, speed=40)  # 3 revolutions left

# Stop motor
kb.top_motor_stop()
```

### Shape Drawing

#### Basic Shapes
```python
# Polygons
kb.draw_tri(10)      # Equilateral triangle (10cm side)
kb.draw_rect(12)     # Square (12cm side)
kb.draw_penta(8)     # Regular pentagon (8cm side)
kb.draw_hexa(7)      # Regular hexagon (7cm side)
kb.draw_star(10)     # Star shape (10cm side)
```

#### Circular Shapes
```python
# Circle
kb.draw_circle(6)    # Circle (6cm radius)

# Semicircle
kb.draw_semicircle(5, side='l')  # Left semicircle (5cm radius)
kb.draw_semicircle(5, side='r')  # Right semicircle

# Arc (time-limited)
kb.draw_arc(8, time=2)  # 8cm radius, 2 seconds arc
```

### Melody Playback

#### Sound Playback
```python
# Play with specific scale and duration
kb.melody(scale=60, sec=1)  # Scale 60, 1 second playback
kb.melody(scale=45, sec=2)  # Scale 45, 2 seconds playback

# Simple beep sound
kb.beep()  # Short beep

# Melody sequence example
melody_sequence = [
    (60, 1), (62, 1), (64, 1), (65, 1),
    (67, 1), (69, 1), (71, 1), (72, 2)
]

for scale, duration in melody_sequence:
    kb.melody(scale=scale, sec=duration)
    kb.delay(0.1)  # Interval between notes
```

## Code Examples

### Basic Movement Pattern
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5", verbose=False)
kb.init()

try:
    # Draw a square (line map board)
    for i in range(4):
        kb.move_forward(2, opt="-l")
        kb.turn_right(opt="-l")
        kb.delay(0.5)
    
    # Change LED colors
    colors = [0, 1, 2, 3, 4, 5, 6, 7]
    for color in colors:
        kb.turn_led_idx(color)
        kb.delay(0.5)
        
finally:
    kb.close()
```

### Sensor-Based Obstacle Avoidance
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5", verbose=False)
kb.init()

try:
    while True:
        # Object detection
        left_obj, right_obj = kb.get_object_detect(True)
        
        if left_obj > 50 or right_obj > 50:
            # When obstacle detected
            kb.stop()
            kb.turn_led_idx(0)  # Red LED
            kb.beep()
            
            # Avoidance action
            kb.move_backward_unit(5, opt="-l", speed=50)
            kb.turn_right(opt="-l")
            kb.delay(1)
        else:
            # Move forward
            kb.turn_led_idx(3)  # Green LED
            kb.move_forward_unit(5, opt="-l", speed=70)
            
        kb.delay(0.1)
        
except KeyboardInterrupt:
    print("Program interrupted")
finally:
    kb.close()
```

### Line Following
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5", verbose=False)
kb.init()

try:
    while True:
        # Read line sensor
        left, center, right = kb.get_line_sensor(True)
        
        if center > 100:  # Line in center
            kb.go_forward_speed(100, 100)
            kb.turn_led_idx(3)  # Green
        elif left > 100:  # Line on left
            kb.go_forward_speed(50, 120)  # Turn left
            kb.turn_led_idx(4)  # Blue
        elif right > 100:  # Line on right
            kb.go_forward_speed(120, 50)  # Turn right
            kb.turn_led_idx(6)  # Purple
        else:  # No line
            kb.stop()
            kb.turn_led_idx(0)  # Red
            
        kb.delay(0.05)
        
except KeyboardInterrupt:
    print("Program interrupted")
finally:
    kb.close()
```

### Color-Responsive Robot
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5", verbose=False)
kb.init()

try:
    while True:
        color = kb.get_color_sensor(True)
        
        if color == 1:  # Red detected (example)
            kb.turn_led_idx(0)  # Red LED
            kb.melody(scale=60, sec=1)
            kb.turn_left(opt="-l")
        elif color == 2:  # Green detected (example)
            kb.turn_led_idx(3)  # Green LED
            kb.melody(scale=65, sec=1)
            kb.move_forward(1, opt="-l")
        elif color == 3:  # Blue detected (example)
            kb.turn_led_idx(4)  # Blue LED
            kb.melody(scale=72, sec=1)
            kb.turn_right(opt="-l")
        else:
            kb.turn_led_idx(7)  # White LED
            
        kb.delay(0.5)
        
except KeyboardInterrupt:
    print("Program interrupted")
finally:
    kb.close()
```

### Shape Drawing Demo
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5", verbose=False)
kb.init()

try:
    shapes = [
        ("Triangle", lambda: kb.draw_tri(10)),
        ("Square", lambda: kb.draw_rect(10)),
        ("Pentagon", lambda: kb.draw_penta(8)),
        ("Hexagon", lambda: kb.draw_hexa(8)),
        ("Circle", lambda: kb.draw_circle(6)),
        ("Star", lambda: kb.draw_star(8))
    ]
    
    for name, draw_func in shapes:
        print(f"Starting to draw {name}")
        kb.turn_led_idx(shapes.index((name, draw_func)))
        kb.beep()
        draw_func()
        kb.delay(2)
        
    print("All shape drawing completed")
    
finally:
    kb.close()
```

## Troubleshooting

### Common Issues

#### 1. Connection Error
```
serial.SerialException: could not open port 'COM5'
```
**Solution**:
- Check port name (Windows: Device Manager, Linux: `ls /dev/tty*`)
- Ensure no other program is using the port
- Check cable connection status

#### 2. Timeout Error
**Symptoms**: No response after sending command
**Solution**:
- Increase `timeout` value (e.g., `timeout=5`)
- Check baud rate (default: 57600)
- Check hardware power status

#### 3. Inaccurate Movement
**Solution**:
- Check battery level: `kb.get_battery()`
- Check floor surface condition (prevent slipping)
- Adjust motor speed

#### 4. Strange Sensor Values
**Solution**:
- Clean sensor surfaces
- Check lighting conditions (color/line sensors)
- Readjust threshold values

### Debugging Tips

#### 1. Use Verbose Mode
```python
kb = KamibotPi(port="COM5", verbose=True)  # Enable debug output
```

#### 2. Monitor Sensor Values
```python
while True:
    left_obj, right_obj = kb.get_object_detect(True)
    left_line, center_line, right_line = kb.get_line_sensor(True)
    color = kb.get_color_sensor(True)
    battery = kb.get_battery()
    
    print(f"Objects: L={left_obj}, R={right_obj}")
    print(f"Line: L={left_line}, C={center_line}, R={right_line}")
    print(f"Color: {color}, Battery: {battery}")
    print("-" * 40)
    
    kb.delay(1)
```

#### 3. Step-by-Step Testing
```python
# 1. Basic connection test
kb = KamibotPi(port="COM5", verbose=True)
kb.init()
print("Connection successful")

# 2. LED test
kb.turn_led_idx(0)
kb.delay(1)

# 3. Sound test
kb.beep()

# 4. Simple movement test
kb.move_forward_unit(5, opt="-l", speed=50)

# 5. Sensor test
print(kb.get_battery())
```

### Performance Optimization

#### 1. Appropriate Delays Between Commands
```python
kb.move_forward(1, opt="-l")
kb.delay(0.1)  # Ensure command processing time
kb.turn_left(opt="-l")
```

#### 2. Adjust Sensor Polling Period
```python
# Avoid too fast polling
while True:
    sensor_data = kb.get_line_sensor(True)
    # Processing logic
    kb.delay(0.05)  # Maintain appropriate interval
```

#### 3. Battery Management
```python
def check_battery(kb):
    battery = kb.get_battery()
    if battery < 20:  # Threshold value
        print("Low battery! Terminating program")
        kb.turn_led_idx(0)  # Red LED warning
        return False
    return True

# Periodic battery check
if not check_battery(kb):
    kb.close()
```

### Safe Usage Guidelines

1. **Power Management**: Check sufficient battery before use
2. **Operating Space**: Ensure adequate space for robot movement
3. **Emergency Stop**: Can interrupt program with `Ctrl+C`
4. **Program Termination**: Always call `kb.close()` (or use try-finally)
5. **Sensor Cleanliness**: Regular sensor cleaning for accuracy maintenance

Please refer to this manual for safe and effective use of KamibotPi!
