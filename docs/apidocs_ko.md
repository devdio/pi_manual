# KamibotPi API 레퍼런스

## 목차
1. [클래스 개요](#클래스-개요)
2. [생성자](#생성자)
3. [연결 관리](#연결-관리)
4. [기본 이동 제어](#기본-이동-제어) : 맵보드를 사용하는 함수들 
5. [속도 제어](#속도-제어)
6. [정밀 제어](#정밀-제어)
7. [LED 제어](#led-제어)
8. [상단 모터 제어](#상단-모터-제어)
9. [센서 제어](#센서-제어)
10. [도형 그리기](#도형-그리기)
11. [멜로디 재생](#멜로디-재생)
12. [유틸리티 함수](#유틸리티-함수)
13. [상수 및 열거형](#상수-및-열거형)

---

## 클래스 개요

### `class KamibotPi`
KamibotPi 로봇을 제어하기 위한 메인 클래스입니다. 시리얼 통신을 통해 로봇과 통신하며 다양한 기능을 제공합니다.

---

## 생성자

### `__init__(port=None, baud=57600, timeout=2, verbose=False)`
KamibotPi 객체를 초기화하고 시리얼 연결을 설정합니다.

**매개변수:**
- `port` (str): 시리얼 포트 이름 (필수)
- `baud` (int): 보오 레이트 (기본값: 57600)
- `timeout` (int): 읽기 타임아웃 (초) (기본값: 2)
- `verbose` (bool): 디버그 출력 활성화 (기본값: False)

**예외:**
- `ValueError`: 포트가 지정되지 않은 경우
- `serial.SerialException`: 시리얼 포트 연결 실패

**예제:**
```python
kb = KamibotPi(port="COM5", baud=57600, timeout=2, verbose=True)
```

---

## 연결 관리

### `init()`
로봇을 초기화합니다.

**반환값:** `None`

**예제:**
```python
kb.init()
```

### `close()`
시리얼 연결을 닫고 프로그램을 종료합니다.

**반환값:** `None` (실제로는 `sys.exit(0)` 호출)

**예제:**
```python
kb.close()
```

### `disconnect()`
시리얼 연결을 닫습니다 (프로그램 종료 없음).

**반환값:** `None`

**예제:**
```python
kb.disconnect()
```

---

## 기본 이동 제어

### `move_forward(value, opt="-l")`
앞으로 지정된 칸 수만큼 이동합니다.

**매개변수:**
- `value` (int): 이동할 칸 수
- `opt` (str): 맵 보드 타입 ("-l": 라인맵보드, "-b": 블록맵보드)

**반환값:** `None`

**예제:**
```python
kb.move_forward(2, opt="-l")  # 라인맵보드에서 2칸 전진
kb.move_forward(1, opt="-b")  # 블록맵보드에서 1칸 전진
```

### `move_backward(value)`
뒤로 지정된 칸 수만큼 이동합니다 (블록맵보드 전용).

**매개변수:**
- `value` (int): 이동할 칸 수

**반환값:** `None`

**예제:**
```python
kb.move_backward(1)
```

### `turn_left(value=1, opt='-l')`
왼쪽으로 회전합니다.

**매개변수:**
- `value` (int): 회전 횟수 (블록맵보드에서만 유효)
- `opt` (str): 맵 보드 타입 ("-l": 라인맵보드, "-b": 블록맵보드)

**반환값:** `None`

**예제:**
```python
kb.turn_left(value=2, opt="-b")  # 블록맵보드에서 2번 좌회전
kb.turn_left(opt="-l")           # 라인맵보드에서 좌회전
```

### `turn_right(value=1, opt='-l')`
오른쪽으로 회전합니다.

**매개변수:**
- `value` (int): 회전 횟수 (블록맵보드에서만 유효)
- `opt` (str): 맵 보드 타입 ("-l": 라인맵보드, "-b": 블록맵보드)

**반환값:** `None`

**예제:**
```python
kb.turn_right(value=1, opt="-l")
```

### `turn_back(value=1, opt='-l')`
180도 회전합니다.

**매개변수:**
- `value` (int): 회전 횟수 (블록맵보드에서만 유효)
- `opt` (str): 맵 보드 타입 ("-l": 라인맵보드, "-b": 블록맵보드)

**반환값:** `None`

**예제:**
```python
kb.turn_back(opt="-l")
```

### `stop()`
로봇의 이동을 정지합니다.

**반환값:** `None`

**예제:**
```python
kb.stop()
```

---

## 속도 제어

### `go_dir_speed(ldir, lspeed, rdir, rspeed)`
좌우 바퀴의 방향과 속도를 개별적으로 제어합니다.

**매개변수:**
- `ldir` (str): 왼쪽 바퀴 방향 ("f": 전진, "b": 후진)
- `lspeed` (int): 왼쪽 바퀴 속도
- `rdir` (str): 오른쪽 바퀴 방향 ("f": 전진, "b": 후진)
- `rspeed` (int): 오른쪽 바퀴 속도

**반환값:** `None`

**예제:**
```python
kb.go_dir_speed("f", 120, "b", 110)  # 좌측 전진, 우측 후진
```

### `go_forward_speed(lspeed, rspeed)`
지정된 속도로 전진합니다.

**매개변수:**
- `lspeed` (int): 왼쪽 바퀴 속도
- `rspeed` (int): 오른쪽 바퀴 속도

**반환값:** `None`

**예제:**
```python
kb.go_forward_speed(120, 120)
```

### `go_backward_speed(lspeed, rspeed)`
지정된 속도로 후진합니다.

**매개변수:**
- `lspeed` (int): 왼쪽 바퀴 속도
- `rspeed` (int): 오른쪽 바퀴 속도

**반환값:** `None`

**예제:**
```python
kb.go_backward_speed(100, 100)
```

### `go_left_speed(speed)`
지정된 속도로 왼쪽으로 회전합니다.

**매개변수:**
- `speed` (int): 회전 속도

**반환값:** `None`

**예제:**
```python
kb.go_left_speed(90)
```

### `go_right_speed(speed)`
지정된 속도로 오른쪽으로 회전합니다.

**매개변수:**
- `speed` (int): 회전 속도

**반환값:** `None`

**예제:**
```python
kb.go_right_speed(90)
```

---

## 정밀 제어

### `move_step(ldir, lstep, rdir, rstep)`
스텝 단위로 정밀한 이동을 수행합니다.

**매개변수:**
- `ldir` (str): 왼쪽 바퀴 방향 ("f": 전진, "b": 후진)
- `lstep` (int): 왼쪽 바퀴 스텝 수
- `rdir` (str): 오른쪽 바퀴 방향 ("f": 전진, "b": 후진)
- `rstep` (int): 오른쪽 바퀴 스텝 수

**반환값:** `None`

**예제:**
```python
kb.move_step("f", 400, "b", 400)
```

### `move_time(ldir, lsec, rdir, rsec)`
시간 단위로 정밀한 이동을 수행합니다.

**매개변수:**
- `ldir` (str): 왼쪽 바퀴 방향 ("f": 전진, "b": 후진)
- `lsec` (int): 왼쪽 바퀴 구동 시간 (초)
- `rdir` (str): 오른쪽 바퀴 방향 ("f": 전진, "b": 후진)
- `rsec` (int): 오른쪽 바퀴 구동 시간 (초)

**반환값:** `None`

**예제:**
```python
kb.move_time("f", 2, "f", 2)
```

### `move_forward_unit(value=10, opt="-l", speed=50)`
단위 기반으로 앞으로 이동합니다.

**매개변수:**
- `value` (int): 이동 값
- `opt` (str): 단위 타입 ("-l": cm, "-t": 초, "-s": 스텝)
- `speed` (int): 이동 속도

**반환값:** `None`

**예제:**
```python
kb.move_forward_unit(20, opt="-l", speed=80)  # 20cm 전진
kb.move_forward_unit(2, opt="-t", speed=60)   # 2초 전진
kb.move_forward_unit(500, opt="-s", speed=50) # 500스텝 전진
```

### `move_backward_unit(value=10, opt="-l", speed=50)`
단위 기반으로 뒤로 이동합니다.

**매개변수:**
- `value` (int): 이동 값
- `opt` (str): 단위 타입 ("-l": cm, "-t": 초, "-s": 스텝)
- `speed` (int): 이동 속도

**반환값:** `None`

**예제:**
```python
kb.move_backward_unit(10, opt="-l", speed=50)
```

### `move_left_unit(value=10, opt="-l", speed=50)`
단위 기반으로 왼쪽으로 이동합니다.

**매개변수:**
- `value` (int): 이동 값
- `opt` (str): 단위 타입 ("-l": cm, "-t": 초, "-s": 스텝)
- `speed` (int): 이동 속도

**반환값:** `None`

**예제:**
```python
kb.move_left_unit(15, opt="-l", speed=70)
```

### `move_right_unit(value=10, opt="-l", speed=50)`
단위 기반으로 오른쪽으로 이동합니다.

**매개변수:**
- `value` (int): 이동 값
- `opt` (str): 단위 타입 ("-l": cm, "-t": 초, "-s": 스텝)
- `speed` (int): 이동 속도

**반환값:** `None`

**예제:**
```python
kb.move_right_unit(10, opt="-l", speed=60)
```

### `turn_left_speed(value=90, speed=50)`
지정된 각도로 왼쪽 제자리 회전합니다.

**매개변수:**
- `value` (int): 회전 각도
- `speed` (int): 회전 속도

**반환값:** `None`

**예제:**
```python
kb.turn_left_speed(45, speed=60)
```

### `turn_right_speed(value=90, speed=50)`
지정된 각도로 오른쪽 제자리 회전합니다.

**매개변수:**
- `value` (int): 회전 각도
- `speed` (int): 회전 속도

**반환값:** `None`

**예제:**
```python
kb.turn_right_speed(90, speed=50)
```

### `turn_continous(dir="l", speed=100)`
지정된 방향으로 계속 회전합니다.

**매개변수:**
- `dir` (str): 회전 방향 ("l": 왼쪽, "r": 오른쪽)
- `speed` (int): 회전 속도

**반환값:** `None`

**예제:**
```python
kb.turn_continous("r", speed=80)
kb.stop()  # 회전 정지
```

---

## LED 제어

### `turn_led(rval, gval, bval)`
RGB 값으로 LED 색상을 설정합니다.

**매개변수:**
- `rval` (int): Red 값 (0-255)
- `gval` (int): Green 값 (0-255)
- `bval` (int): Blue 값 (0-255)

**반환값:** `None`

**예제:**
```python
kb.turn_led(255, 0, 0)    # 빨간색
kb.turn_led(0, 255, 0)    # 초록색
kb.turn_led(255, 255, 0)  # 노란색
```

### `turn_led_idx(idx)`
프리셋 인덱스로 LED 색상을 설정합니다.

**매개변수:**
- `idx` (int): 색상 인덱스 (0-8)
  - 0: off (꺼짐)
  - 1: red (빨간색)
  - 2: orange (주황색)
  - 3: yellow (노란색)
  - 4: green (초록색)
  - 5: blue (파란색)
  - 6: skyblue (하늘색)
  - 7: purple (보라색)
  - 8: white (흰색)

**반환값:** `None`

**예제:**
```python
kb.turn_led_idx(1)  # 빨간색
kb.turn_led_idx(4)  # 초록색
```

---

## 상단 모터 제어

### `top_motor_degree(dir, value=90, speed=50)`
상단 모터를 지정된 각도만큼 회전시킵니다.

**매개변수:**
- `dir` (str): 회전 방향 ("l": 왼쪽, "r": 오른쪽)
- `value` (int): 회전 각도
- `speed` (int): 회전 속도

**반환값:** `None`

**예제:**
```python
kb.top_motor_degree("l", value=45, speed=60)
kb.top_motor_degree("r", value=90, speed=80)
```

### `top_motor_abspos(degree=0, speed=50)`
상단 모터를 절대 위치로 이동시킵니다.

**매개변수:**
- `degree` (int): 목표 절대 각도 (최대 65000)
- `speed` (int): 회전 속도

**반환값:** `None`

**예제:**
```python
kb.top_motor_abspos(180, speed=70)  # 180도 위치로
kb.top_motor_abspos(0, speed=50)    # 원점으로 복귀
```

### `top_motor_time(dir, value=3, speed=50)`
상단 모터를 지정된 시간 동안 회전시킵니다.

**매개변수:**
- `dir` (str): 회전 방향 ("l": 왼쪽, "r": 오른쪽)
- `value` (int): 회전 시간 (초)
- `speed` (int): 회전 속도

**반환값:** `None`

**예제:**
```python
kb.top_motor_time("r", value=2, speed=80)
```

### `top_motor_round(dir, value=1, speed=50)`
상단 모터를 지정된 회전수만큼 회전시킵니다.

**매개변수:**
- `dir` (str): 회전 방향 ("l": 왼쪽, "r": 오른쪽)
- `value` (int): 회전수
- `speed` (int): 회전 속도

**반환값:** `None`

**예제:**
```python
kb.top_motor_round("l", value=3, speed=40)
```

### `top_motor_stop()`
상단 모터의 회전을 정지시킵니다.

**반환값:** `None`

**예제:**
```python
kb.top_motor_stop()
```

---

## 센서 제어

### `get_object_detect(opt=True)`
물체 감지 센서를 동작시키고 값을 읽어옵니다.

**매개변수:**
- `opt` (bool): 센서 동작 여부 (True: 동작, False: 정지)

**반환값:** `tuple(int, int)` - (왼쪽 감지값, 오른쪽 감지값)

**예제:**
```python
left_obj, right_obj = kb.get_object_detect(True)
print(f"왼쪽: {left_obj}, 오른쪽: {right_obj}")
```

### `get_line_sensor(opt=True)`
라인 감지 센서를 동작시키고 값을 읽어옵니다.

**매개변수:**
- `opt` (bool): 센서 동작 여부 (True: 동작, False: 정지)

**반환값:** `tuple(int, int, int)` - (왼쪽, 중앙, 오른쪽 라인 감지값)

**참고:** 반환값에서 좌우가 뒤바뀌어 있음 (하드웨어 보정)

**예제:**
```python
left, center, right = kb.get_line_sensor(True)
print(f"라인 센서 - 왼쪽: {left}, 중앙: {center}, 오른쪽: {right}")
```

### `get_color_sensor(opt=True)`
컬러 센서를 동작시키고 색상 인덱스를 읽어옵니다.

**매개변수:**
- `opt` (bool): 센서 동작 여부 (True: 동작, False: 정지)

**반환값:** `int` - 색상 인덱스

**예제:**
```python
color = kb.get_color_sensor(True)
print(f"감지된 색상: {color}")
```

### `get_color_elements(opt=True)`
컬러 센서를 동작시키고 RGB 값을 읽어옵니다.

**매개변수:**
- `opt` (bool): 센서 동작 여부 (True: 동작, False: 정지)

**반환값:** `tuple(int, int, int)` - (R, G, B) 값

**예제:**
```python
r, g, b = kb.get_color_elements(True)
print(f"RGB: ({r}, {g}, {b})")
```

### `get_battery()`
배터리 잔량을 읽어옵니다.

**반환값:** `int` - 배터리 잔량

**예제:**
```python
battery = kb.get_battery()
print(f"배터리: {battery}")
```

### `get_version()`
펌웨어 버전 정보를 요청합니다.

**반환값:** `None`

**예제:**
```python
kb.get_version()
```

### `toggle_linetracer(mode, speed=100)`
라인트레이서 기능을 켜거나 끕니다.

**매개변수:**
- `mode` (bool): 기능 활성화 여부 (True: 켜기, False: 끄기)
- `speed` (int): 라인트레이서 속도

**반환값:** `None`

**예제:**
```python
kb.toggle_linetracer(True, speed=120)   # 라인트레이서 켜기
kb.toggle_linetracer(False)             # 라인트레이서 끄기
```

---

## 도형 그리기

### `draw_tri(len)`
삼각형을 그립니다.

**매개변수:**
- `len` (int): 삼각형 한 변의 길이 (cm)

**반환값:** `None`

**예제:**
```python
kb.draw_tri(10)
```

### `draw_rect(len)`
사각형을 그립니다.

**매개변수:**
- `len` (int): 사각형 한 변의 길이 (cm)

**반환값:** `None`

**예제:**
```python
kb.draw_rect(12)
```

### `draw_penta(len)`
오각형을 그립니다.

**매개변수:**
- `len` (int): 오각형 한 변의 길이 (cm)

**반환값:** `None`

**예제:**
```python
kb.draw_penta(8)
```

### `draw_hexa(len)`
육각형을 그립니다.

**매개변수:**
- `len` (int): 육각형 한 변의 길이 (cm)

**반환값:** `None`

**예제:**
```python
kb.draw_hexa(7)
```

### `draw_star(len)`
별 모양을 그립니다.

**매개변수:**
- `len` (int): 별 한 변의 길이 (cm)

**반환값:** `None`

**예제:**
```python
kb.draw_star(10)
```

### `draw_circle(len)`
원을 그립니다.

**매개변수:**
- `len` (int): 원의 반지름 (cm)

**반환값:** `None`

**예제:**
```python
kb.draw_circle(6)
```

### `draw_semicircle(len, side="l")`
반원을 그립니다.

**매개변수:**
- `len` (int): 원의 반지름 (cm)
- `side` (str): 반원 방향 ("l": 왼쪽, "r": 오른쪽)

**반환값:** `None`

**예제:**
```python
kb.draw_semicircle(5, side="l")
kb.draw_semicircle(5, side="r")
```

### `draw_arc(radius, value=1, mode=0)`
원호를 그립니다.

**매개변수:**
- `radius` (int): 원의 반지름 (cm)
- `value` (int): 모드에 따른 값 (시간 또는 각도)
- `mode` (int): 모드 (0: 시간 기반, 1: 각도 기반)

**반환값:** `None`

**예제:**
```python
kb.draw_arc(8, value=2, mode=0)   # 2초 동안 원호
kb.draw_arc(8, value=90, mode=1)  # 90도 원호
```

---

## 멜로디 재생

### `melody(scale=45, sec=1)`
지정된 음계와 시간으로 소리를 재생합니다.

**매개변수:**
- `scale` (int): 음계 (0-83)
- `sec` (int): 재생 시간 (초)

**반환값:** `None`

**예제:**
```python
kb.melody(scale=60, sec=1)
kb.melody(scale=45, sec=2)
```

### `beep()`
짧은 삐 소리를 재생합니다.

**반환값:** `None`

**예제:**
```python
kb.beep()
```

---

## 유틸리티 함수

### `delay(sec)`
지정된 시간만큼 대기합니다.

**매개변수:**
- `sec` (float): 대기 시간 (초)

**반환값:** `None`

**예제:**
```python
kb.delay(0.5)
```

### `delayms(ms)`
지정된 시간만큼 대기합니다 (밀리초 단위).

**매개변수:**
- `ms` (int): 대기 시간 (밀리초)

**반환값:** `None`

**예제:**
```python
kb.delayms(500)  # 500ms 대기
```

### `wait(ms)`
`delayms()`의 별칭입니다.

**매개변수:**
- `ms` (int): 대기 시간 (밀리초)

**반환값:** `None`

**예제:**
```python
kb.wait(1000)  # 1초 대기
```

### `angle3p(p1, p2, p3)` (정적 메서드)
3점 사이의 각도를 계산합니다.

**매개변수:**
- `p1` (tuple): 첫 번째 점 (x1, y1)
- `p2` (tuple): 두 번째 점 (x2, y2)
- `p3` (tuple): 세 번째 점 (x3, y3)

**반환값:** `float` - 시계 반대방향 각도 (도)

**예제:**
```python
angle = KamibotPi.angle3p((0, 0), (1, 0), (1, 1))
```

### `remap(value, source_range, target_range)`
값을 한 범위에서 다른 범위로 매핑합니다.

**매개변수:**
- `value` (float): 매핑할 값
- `source_range` (tuple): 원본 범위 (min, max)
- `target_range` (tuple): 대상 범위 (min, max)

**반환값:** `float` - 매핑된 값

**예제:**
```python
mapped = kb.remap(50, (0, 100), (0, 10))  # 결과: 5.0
```

---

## 상수 및 열거형

### `class CommandType`
펌웨어 명령 타입 상수들을 정의합니다.

**주요 상수:**
- `FORCE_STOP = 0x01`
- `MOVE_FORWARD_BLOCK = 0x02`
- `MOVE_BACKWARD_BLOCK = 0x03`
- `TURN_LEFT_BLOCK = 0x04`
- `TURN_RIGHT_BLOCK = 0x05`
- 기타 다수의 명령 타입...

### `class ModeType`
작동 모드 타입 상수들을 정의합니다.

**주요 상수:**
- `MAPBOARD = 0x01`
- `CONTROL = 0x02`
- `RGB = 0x03`
- `TOP_STEPPER = 0x04`
- `OBJECT_DETECTER = 0x05`
- `LINE_DETECTOR = 0x06`
- `COLOR_DETECTOR = 0x07`
- 기타 다수의 모드 타입...

### `class PacketIndex`
송신 패킷의 바이트 오프셋을 정의합니다.

**주요 상수:**
- `START = 0`
- `LENGTH = 1`
- `HWID = 2`
- `HWTYPE = 3`
- `COMMANDTYPE = 4`
- 기타 패킷 필드들...

### `class RETURN_PACKET`
수신 패킷의 바이트 오프셋을 정의합니다.

**주요 상수:**
- `START = 0`
- `LENGTH = 1`
- `BATTERY = 7`
- `LEFT_OBJECT = 8`
- `RIGHT_OBJECT = 9`
- 기타 리턴 패킷 필드들...

### `LED` (딕셔너리)
미리 정의된 LED 색상들을 포함합니다.

**색상:**
- `"off"`: [0, 0, 0] - 꺼짐
- `"red"`: [255, 0, 0] - 빨간색
- `"orange"`: [255, 165, 0] - 주황색
- `"yellow"`: [255, 255, 0] - 노란색
- `"green"`: [0, 255, 0] - 초록색
- `"blue"`: [0, 0, 255] - 파란색
- `"skyblue"`: [0, 255, 255] - 하늘색
- `"purple"`: [139, 0, 255] - 보라색
- `"white"`: [255, 255, 255] - 흰색

**예제:**
```python
kb.turn_led(*LED["red"])     # 빨간색으로 설정
kb.turn_led(*LED["green"])   # 초록색으로 설정
```

### `LED_COLOR` (리스트)
LED 색상들의 배열로, 인덱스로 접근할 수 있습니다.

**인덱스:**
- `0`: off (꺼짐)
- `1`: red (빨간색)
- `2`: orange (주황색)
- `3`: yellow (노란색)
- `4`: green (초록색)
- `5`: blue (파란색)
- `6`: skyblue (하늘색)
- `7`: purple (보라색)
- `8`: white (흰색)

**예제:**
```python
kb.turn_led(*LED_COLOR[1])  # 빨간색
kb.turn_led(*LED_COLOR[4])  # 초록색
```

### `class LedColor`
LED 색상 상수들을 정의하는 클래스입니다.

**상수:**
- `OFF = [0, 0, 0]`
- `RED = [255, 0, 0]`
- `ORANGE = [255, 165, 0]`
- `YELLOW = [255, 255, 0]`
- `GREEN = [0, 255, 0]`
- `BLUE = [0, 0, 255]`
- `SKYBLUE = [0, 255, 255]`
- `PURPLE = [139, 0, 255]`
- `WHITE = [255, 255, 255]`

**예제:**
```python
from kamibotpi import LedColor
kb.turn_led(*LedColor.RED)
kb.turn_led(*LedColor.BLUE)
```

### 기타 상수

#### 명령 타입
- `COMMANDTYPE_WRITE = 0x01` - 쓰기 명령
- `COMMANDTYPE_READ = 0x02` - 읽기 명령
- `COMMANDTYPE_RETURN = 0x03` - 반환 명령

#### 하드웨어 타입
- `HWTYPE_BOTPI = 0x00` - KamibotPi 하드웨어
- `HWTYPE_XBLOCK = 0x10` - XBlock 하드웨어

#### 기본 설정
- `DEFAULT_MOTOR_SPEED = 0x96` (150) - 기본 모터 속도

---

## 사용 예제

### 기본 사용법
```python
from kamibotpi import KamibotPi

# 연결 및 초기화
kb = KamibotPi(port="COM5", verbose=False)
kb.init()

try:
    # 기본 이동
    kb.move_forward(2, opt="-l")
    kb.turn_right()
    
    # LED 제어
    kb.turn_led_idx(1)  # 빨간색
    
    # 센서 읽기
    battery = kb.get_battery()
    print(f"배터리: {battery}")
    
finally:
    kb.close()
```

### 센서 기반 제어
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5")
kb.init()

try:
    while True:
        # 물체 감지
        left_obj, right_obj = kb.get_object_detect(True)
        
        if left_obj > 50 or right_obj > 50:
            # 장애물 발견
            kb.stop()
            kb.turn_led_idx(1)  # 빨간색
            kb.beep()
            
            # 회피 동작
            kb.move_backward_unit(5, opt="-l")
            kb.turn_right()
        else:
            # 전진
            kb.turn_led_idx(4)  # 초록색
            kb.move_forward_unit(10, opt="-l")
            
        kb.delay(0.1)
        
except KeyboardInterrupt:
    print("프로그램 중단")
finally:
    kb.close()
```

### 정밀 제어 예제
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5")
kb.init()

try:
    # 스텝 기반 정밀 이동
    kb.move_step("f", 400, "f", 400)  # 양쪽 400스텝 전진
    kb.delay(1)
    
    # 시간 기반 정밀 이동
    kb.move_time("f", 2, "b", 2)  # 좌측 2초 전진, 우측 2초 후진
    kb.delay(1)
    
    # 단위 기반 정밀 이동
    kb.move_forward_unit(20, opt="-l", speed=80)  # 20cm 전진
    kb.turn_left_speed(90, speed=60)              # 90도 좌회전
    
finally:
    kb.close()
```

### 도형 그리기 예제
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5")
kb.init()

try:
    # 기본 도형들
    kb.draw_tri(10)      # 삼각형
    kb.delay(2)
    
    kb.draw_rect(12)     # 사각형
    kb.delay(2)
    
    kb.draw_circle(8)    # 원
    kb.delay(2)
    
    kb.draw_star(10)     # 별
    kb.delay(2)
    
    # 반원 그리기
    kb.draw_semicircle(6, side="l")  # 왼쪽 반원
    kb.delay(2)
    
    # 원호 그리기
    kb.draw_arc(8, value=2, mode=0)  # 2초 동안 원호
    
finally:
    kb.close()
```

### 멜로디 재생 예제
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5")
kb.init()

try:
    # 도레미 연주
    scales = [60, 62, 64, 65, 67, 69, 71, 72]
    
    for scale in scales:
        kb.melody(scale=scale, sec=1)
        kb.delay(0.1)  # 음 사이 간격
    
    # 간단한 멜로디
    melody = [
        (60, 0.5), (64, 0.5), (67, 0.5), (72, 1.0),
        (67, 0.5), (64, 0.5), (60, 1.0)
    ]
    
    for scale, duration in melody:
        kb.melody(scale=scale, sec=duration)
        kb.delay(0.1)
    
    # 효과음
    kb.beep()  # 삐 소리
    
finally:
    kb.close()
```

### 상단 모터 제어 예제
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5")
kb.init()

try:
    # 상대 각도 회전
    kb.top_motor_degree("r", value=90, speed=60)   # 오른쪽 90도
    kb.delay(2)
    
    kb.top_motor_degree("l", value=180, speed=60)  # 왼쪽 180도
    kb.delay(2)
    
    # 절대 위치로 이동
    kb.top_motor_abspos(0, speed=50)  # 원점으로 복귀
    kb.delay(2)
    
    # 시간 기반 회전
    kb.top_motor_time("r", value=3, speed=80)  # 3초 동안 우회전
    kb.delay(3)
    
    # 회전수 기반
    kb.top_motor_round("l", value=2, speed=40)  # 2바퀴 좌회전
    kb.delay(5)
    
    # 정지
    kb.top_motor_stop()
    
finally:
    kb.close()
```

---

## 오류 처리

### 일반적인 예외 처리
```python
from kamibotpi import KamibotPi
import serial

try:
    kb = KamibotPi(port="COM5", baud=57600, timeout=2)
    kb.init()
    
    # 로봇 제어 코드
    kb.move_forward(2)
    
except ValueError as e:
    print(f"포트 설정 오류: {e}")
except serial.SerialException as e:
    print(f"시리얼 통신 오류: {e}")
except KeyboardInterrupt:
    print("사용자가 프로그램을 중단했습니다.")
except Exception as e:
    print(f"예상치 못한 오류: {e}")
finally:
    if 'kb' in locals():
        kb.close()
```

### 센서 값 검증
```python
def safe_sensor_read(kb):
    """안전한 센서 읽기 함수"""
    try:
        left_obj, right_obj = kb.get_object_detect(True)
        
        # 센서 값 유효성 검사
        if left_obj is None or right_obj is None:
            print("센서 값을 읽을 수 없습니다.")
            return None, None
            
        # 값 범위 검사 (0-255 범위 가정)
        if not (0 <= left_obj <= 255) or not (0 <= right_obj <= 255):
            print("센서 값이 유효 범위를 벗어났습니다.")
            return None, None
            
        return left_obj, right_obj
        
    except Exception as e:
        print(f"센서 읽기 오류: {e}")
        return None, None

# 사용 예제
kb = KamibotPi(port="COM5")
kb.init()

left_obj, right_obj = safe_sensor_read(kb)
if left_obj is not None and right_obj is not None:
    print(f"물체 감지: 왼쪽={left_obj}, 오른쪽={right_obj}")
else:
    print("센서 읽기 실패")
```

---

## 성능 최적화 팁

### 1. 적절한 지연 시간 사용
```python
# 명령 간 적절한 지연
kb.move_forward(1)
kb.delay(0.1)  # 명령 처리 시간 확보
kb.turn_left()
```

### 2. 센서 폴링 주기 조정
```python
# 너무 빠른 폴링 방지
while True:
    sensor_data = kb.get_line_sensor(True)
    # 처리 로직
    kb.delay(0.05)  # 적절한 간격 유지
```

### 3. 배터리 모니터링
```python
def monitor_battery(kb, threshold=20):
    """배터리 모니터링 함수"""
    battery = kb.get_battery()
    if battery < threshold:
        kb.turn_led_idx(1)  # 빨간색 경고
        kb.beep()
        print(f"배터리 부족: {battery}")
        return False
    return True

# 주기적 배터리 확인
if not monitor_battery(kb):
    print("배터리 부족으로 프로그램을 종료합니다.")
    kb.close()
```

---

## 디버깅 도구

### Verbose 모드 활용
```python
# 디버깅을 위한 verbose 모드 활성화
kb = KamibotPi(port="COM5", verbose=True)

# 센서 값 실시간 모니터링
def debug_sensors(kb, duration=10):
    """센서 값 디버깅 함수"""
    start_time = time.time()
    
    while time.time() - start_time < duration:
        # 모든 센서 값 읽기
        left_obj, right_obj = kb.get_object_detect(True)
        left_line, center_line, right_line = kb.get_line_sensor(True)
        color = kb.get_color_sensor(True)
        battery = kb.get_battery()
        
        # 포매팅된 출력
        print(f"시간: {time.time() - start_time:.1f}s")
        print(f"물체: L={left_obj:3d}, R={right_obj:3d}")
        print(f"라인: L={left_line:3d}, C={center_line:3d}, R={right_line:3d}")
        print(f"색상: {color:3d}, 배터리: {battery:3d}")
        print("-" * 40)
        
        kb.delay(0.5)

# 사용 예제
debug_sensors(kb, duration=30)  # 30초 동안 센서 모니터링
```

이 API 레퍼런스는 KamibotPi 라이브러리의 모든 공개 메서드와 상수들을 상세히 설명하고 있습니다. 각 함수의 매개변수, 반환값, 그리고 실용적인 사용 예제를 포함하여 개발자들이 쉽게 활용할 수 있도록 구성되어 있습니다.
