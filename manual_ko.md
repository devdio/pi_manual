# KamibotPi API 문서

KamibotPi 로봇을 제어하기 위한 Python 라이브러리의 완전한 API 참조 문서입니다.

## 목차

- [초기화 및 연결](#초기화-및-연결)
- [기본 동작](#기본-동작)
- [맵보드 이동](#맵보드-이동)
- [속도 제어](#속도-제어)
- [정밀 제어](#정밀-제어)
- [LED 제어](#led-제어)
- [탑 모터 제어](#탑-모터-제어)
- [센서](#센서)
- [도형 그리기](#도형-그리기)
- [사운드](#사운드)
- [유틸리티](#유틸리티)

---

## 파이썬 가상환경 만들기
- VSCode 설치 및 파이썬 플러그인 설치

- [Miniconda 다운로드]()에서 Miniconda를 다운로드받아서 설치합니다.
- 파이썬 3.10 버전을 사용하는 가상환경 만들기
```
conda create -n [가상환경 이름] python==3.10
```
- 가상환경 활성화
```
conda activate [가상환경 이름]
```
- 카미봇파이용 라이브러리 설치
```
pip install pyKamipi
```


## 초기화 및 연결

### `KamibotPi(port, baud, timeout, verbose)`

KamibotPi 객체를 생성하고 시리얼 포트로 연결합니다.

**매개변수:**
- `port` (str): 시리얼 포트 경로 (예: '/dev/ttyUSB0', 'COM3')
- `baud` (int, optional): 통신 속도, 기본값 57600
- `timeout` (int, optional): 시리얼 통신 타임아웃(초), 기본값 2
- `verbose` (bool, optional): 디버그 메시지 출력 여부, 기본값 False

**예제:**
```python
robot = KamibotPi(port='COM8', baud=57600, timeout=2, verbose=False)
```

---

### `close()`

시리얼 연결을 종료하고 프로그램을 종료합니다.

**매개변수:** 없음

**반환값:** 없음

**예제:**
```python
robot.close()
```

---

### `disconnect()`

시리얼 연결만 종료합니다 (프로그램은 종료하지 않음).

**매개변수:** 없음

**반환값:** 없음

**예제:**
```python
robot.disconnect()
```

---

## 기본 동작

### `delay(sec)`

지정된 시간(초) 동안 대기합니다.

**매개변수:**
- `sec` (float): 대기할 시간(초)

**반환값:** 없음

**예제:**
```python
robot.delay(2)  # 2초 대기
robot.delay(0.5)  # 0.5초 대기
```

---

### `delayms(ms)` / `wait(ms)`

지정된 시간(밀리초) 동안 대기합니다.

**매개변수:**
- `ms` (int): 대기할 시간(밀리초)

**반환값:** 없음

**예제:**
```python
robot.delayms(500)  # 500ms 대기
robot.wait(1000)  # 1000ms(1초) 대기
```

---

### `stop()`

로봇의 모든 이동을 즉시 정지합니다.

**매개변수:** 없음

**반환값:** 없음

**예제:**
```python
robot.stop()
```

---

### `init()`

로봇을 초기화합니다.

**매개변수:** 없음

**반환값:** 없음

**예제:**
```python
robot.init()
```

---

## 맵보드 이동

### `move_forward(value, opt)`

로봇을 앞으로 이동시킵니다.

**매개변수:**
- `value` (int): 이동할 칸 수
- `opt` (str, optional): 맵보드 타입
  - `'-l'`: 라인맵보드 (기본값)
  - `'-b'`: 블록맵보드

**반환값:** 없음

**예제:**
```python
robot.move_forward(1, '-l')  # 라인맵보드에서 1칸 전진
robot.move_forward(3, '-b')  # 블록맵보드에서 3칸 전진
```

---

### `move_backward(value)`

로봇을 뒤로 이동시킵니다. (블록맵보드에서만 동작)

**매개변수:**
- `value` (int): 이동할 칸 수

**반환값:** 없음

**예제:**
```python
robot.move_backward(2)  # 2칸 후진
```

---

### `turn_left(value, opt)`

로봇을 왼쪽으로 회전시킵니다.

**매개변수:**
- `value` (int, optional): 회전 횟수, 기본값 1 (라인맵보드에서는 무시됨)
- `opt` (str, optional): 맵보드 타입
  - `'-l'`: 라인맵보드 (기본값)
  - `'-b'`: 블록맵보드

**반환값:** 없음

**예제:**
```python
robot.turn_left(1, '-l')  # 라인맵보드에서 왼쪽으로 회전
robot.turn_left(2, '-b')  # 블록맵보드에서 왼쪽으로 2번 회전
```

---

### `turn_right(value, opt)`

로봇을 오른쪽으로 회전시킵니다.

**매개변수:**
- `value` (int, optional): 회전 횟수, 기본값 1 (라인맵보드에서는 무시됨)
- `opt` (str, optional): 맵보드 타입
  - `'-l'`: 라인맵보드 (기본값)
  - `'-b'`: 블록맵보드

**반환값:** 없음

**예제:**
```python
robot.turn_right(1, '-l')  # 라인맵보드에서 오른쪽으로 회전
robot.turn_right(3, '-b')  # 블록맵보드에서 오른쪽으로 3번 회전
```

---

### `turn_back(value, opt)`

로봇을 뒤로 회전시킵니다 (180도 회전).

**매개변수:**
- `value` (int, optional): 회전 횟수, 기본값 1 (라인맵보드에서는 무시됨)
- `opt` (str, optional): 맵보드 타입
  - `'-l'`: 라인맵보드 (기본값)
  - `'-b'`: 블록맵보드

**반환값:** 없음

**예제:**
```python
robot.turn_back(1, '-l')  # 라인맵보드에서 뒤로 회전
robot.turn_back(2, '-b')  # 블록맵보드에서 뒤로 2번 회전
```

---

### `toggle_linetracer(mode, speed)`

라인트레이서 기능을 켜거나 끕니다.

**매개변수:**
- `mode` (bool): 라인트레이서 모드
  - `True`: 켜기
  - `False`: 끄기
- `speed` (int, optional): 라인트레이서 속도 (0-255), 기본값 100

**반환값:** 없음

**예제:**
```python
robot.toggle_linetracer(True, 100)  # 속도 100으로 라인트레이서 시작
robot.toggle_linetracer(False)  # 라인트레이서 종료
```

---

## 속도 제어

### `go_dir_speed(ldir, lspeed, rdir, rspeed)`

왼쪽, 오른쪽 바퀴의 방향과 속도를 개별적으로 제어합니다.

**매개변수:**
- `ldir` (str): 왼쪽 바퀴 회전 방향
  - `'f'`: 앞으로
  - `'b'`: 뒤로
- `lspeed` (int): 왼쪽 바퀴 속도 (0-255)
- `rdir` (str): 오른쪽 바퀴 회전 방향
  - `'f'`: 앞으로
  - `'b'`: 뒤로
- `rspeed` (int): 오른쪽 바퀴 속도 (0-255)

**반환값:** 없음

**예제:**
```python
robot.go_dir_speed('f', 100, 'f', 100)  # 양쪽 바퀴 앞으로 속도 100
robot.go_dir_speed('f', 150, 'b', 150)  # 왼쪽 앞으로, 오른쪽 뒤로
```

---

### `go_forward_speed(lspeed, rspeed)`

지정된 속도로 앞으로 이동합니다.

**매개변수:**
- `lspeed` (int): 왼쪽 바퀴 속도 (0-255)
- `rspeed` (int): 오른쪽 바퀴 속도 (0-255)

**반환값:** 없음

**예제:**
```python
robot.go_forward_speed(100, 100)  # 양쪽 바퀴 속도 100으로 전진
robot.go_forward_speed(150, 100)  # 오른쪽으로 약간 휘면서 전진
```

---

### `go_backward_speed(lspeed, rspeed)`

지정된 속도로 뒤로 이동합니다.

**매개변수:**
- `lspeed` (int): 왼쪽 바퀴 속도 (0-255)
- `rspeed` (int): 오른쪽 바퀴 속도 (0-255)

**반환값:** 없음

**예제:**
```python
robot.go_backward_speed(100, 100)  # 양쪽 바퀴 속도 100으로 후진
```

---

### `go_left_speed(speed)`

지정된 속도로 왼쪽으로 회전합니다.

**매개변수:**
- `speed` (int): 회전 속도 (0-255)

**반환값:** 없음

**예제:**
```python
robot.go_left_speed(80)  # 속도 80으로 왼쪽 회전
```

---

### `go_right_speed(speed)`

지정된 속도로 오른쪽으로 회전합니다.

**매개변수:**
- `speed` (int): 회전 속도 (0-255)

**반환값:** 없음

**예제:**
```python
robot.go_right_speed(80)  # 속도 80으로 오른쪽 회전
```

---

## 정밀 제어

### `move_step(ldir, lstep, rdir, rstep)`

스텝 단위로 정밀하게 이동합니다.

**매개변수:**
- `ldir` (str): 왼쪽 바퀴 회전 방향 ('f': 앞, 'b': 뒤)
- `lstep` (int): 왼쪽 바퀴 스텝 수
- `rdir` (str): 오른쪽 바퀴 회전 방향 ('f': 앞, 'b': 뒤)
- `rstep` (int): 오른쪽 바퀴 스텝 수

**반환값:** 없음

**예제:**
```python
robot.move_step('f', 100, 'f', 100)  # 양쪽 100스텝 전진
robot.move_step('f', 200, 'b', 200)  # 제자리 회전
```

---

### `move_time(ldir, lsec, rdir, rsec)`

시간 단위로 이동합니다.

**매개변수:**
- `ldir` (str): 왼쪽 바퀴 회전 방향 ('f': 앞, 'b': 뒤)
- `lsec` (int): 왼쪽 바퀴 동작 시간(초)
- `rdir` (str): 오른쪽 바퀴 회전 방향 ('f': 앞, 'b': 뒤)
- `rsec` (int): 오른쪽 바퀴 동작 시간(초)

**반환값:** 없음

**예제:**
```python
robot.move_time('f', 2, 'f', 2)  # 양쪽 2초간 전진
robot.move_time('f', 1, 'b', 1)  # 1초간 제자리 회전
```

---

### `move_forward_unit(value, opt, speed)`

단위를 지정하여 앞으로 이동합니다.

**매개변수:**
- `value` (int): 이동할 값
- `opt` (str, optional): 단위 타입
  - `'-l'`: cm (기본값)
  - `'-t'`: 초
  - `'-s'`: 스텝
- `speed` (int, optional): 이동 속도 (0-255), 기본값 50

**반환값:** 없음

**예제:**
```python
robot.move_forward_unit(10, '-l', 50)  # 10cm 전진
robot.move_forward_unit(2, '-t', 100)  # 2초간 전진
robot.move_forward_unit(500, '-s', 80)  # 500스텝 전진
```

---

### `move_backward_unit(value, opt, speed)`

단위를 지정하여 뒤로 이동합니다.

**매개변수:**
- `value` (int): 이동할 값
- `opt` (str, optional): 단위 타입 ('-l': cm, '-t': 초, '-s': 스텝), 기본값 '-l'
- `speed` (int, optional): 이동 속도 (0-255), 기본값 50

**반환값:** 없음

**예제:**
```python
robot.move_backward_unit(10, '-l', 50)  # 10cm 후진
```

---

### `turn_left_speed(value, speed)`

각도를 지정하여 왼쪽으로 제자리 회전합니다.

**매개변수:**
- `value` (int, optional): 회전 각도, 기본값 90
- `speed` (int, optional): 회전 속도 (0-255), 기본값 50

**반환값:** 없음

**예제:**
```python
robot.turn_left_speed(90, 50)  # 90도 왼쪽 회전
robot.turn_left_speed(180, 80)  # 180도 왼쪽 회전
```

---

### `turn_right_speed(value, speed)`

각도를 지정하여 오른쪽으로 제자리 회전합니다.

**매개변수:**
- `value` (int, optional): 회전 각도, 기본값 90
- `speed` (int, optional): 회전 속도 (0-255), 기본값 50

**반환값:** 없음

**예제:**
```python
robot.turn_right_speed(90, 50)  # 90도 오른쪽 회전
robot.turn_right_speed(45, 30)  # 45도 오른쪽 회전
```

---

### `move_left_unit(value, opt, speed)`

단위를 지정하여 왼쪽으로 이동합니다.

**매개변수:**
- `value` (int): 이동할 값
- `opt` (str, optional): 단위 타입 ('-l': cm, '-t': 초, '-s': 스텝), 기본값 '-l'
- `speed` (int, optional): 이동 속도 (0-255), 기본값 50

**반환값:** 없음

**예제:**
```python
robot.move_left_unit(5, '-l', 50)  # 5cm 왼쪽으로 이동
```

---

### `move_right_unit(value, opt, speed)`

단위를 지정하여 오른쪽으로 이동합니다.

**매개변수:**
- `value` (int): 이동할 값
- `opt` (str, optional): 단위 타입 ('-l': cm, '-t': 초, '-s': 스텝), 기본값 '-l'
- `speed` (int, optional): 이동 속도 (0-255), 기본값 50

**반환값:** 없음

**예제:**
```python
robot.move_right_unit(5, '-l', 50)  # 5cm 오른쪽으로 이동
```

---

## LED 제어

### `turn_led(rval, gval, bval)`

RGB 값으로 LED 색상을 설정합니다.

**매개변수:**
- `rval` (int): Red 값 (0-255)
- `gval` (int): Green 값 (0-255)
- `bval` (int): Blue 값 (0-255)

**반환값:** 없음

**예제:**
```python
robot.turn_led(255, 0, 0)  # 빨간색
robot.turn_led(0, 255, 0)  # 녹색
robot.turn_led(255, 255, 0)  # 노란색
robot.turn_led(0, 0, 0)  # LED 끄기
```

---

### `turn_led_idx(idx)`

인덱스로 미리 정의된 LED 색상을 설정합니다.

**매개변수:**
- `idx` (int): 색상 인덱스 (0-8)
  - 0: 빨강 (red)
  - 1: 주황 (orange)
  - 2: 노랑 (yellow)
  - 3: 녹색 (green)
  - 4: 파랑 (blue)
  - 5: 하늘색 (skyblue)
  - 6: 보라 (purple)
  - 7: 흰색 (white)

**반환값:** 없음

**예제:**
```python
robot.turn_led_idx(0)  # 빨간색
robot.turn_led_idx(3)  # 녹색
robot.turn_led_idx(7)  # 흰색
```

---

## 탑 모터 제어

### `top_motor_degree(dir, value, speed)`

지정된 각도만큼 탑 모터를 회전시킵니다.

**매개변수:**
- `dir` (str): 회전 방향
  - `'l'`: 왼쪽
  - `'r'`: 오른쪽
- `value` (int, optional): 회전 각도, 기본값 90
- `speed` (int, optional): 회전 속도 (0-255), 기본값 50

**반환값:** 없음

**예제:**
```python
robot.top_motor_degree('r', 90, 50)  # 오른쪽으로 90도 회전
robot.top_motor_degree('l', 180, 80)  # 왼쪽으로 180도 회전
```

---

### `top_motor_abspos(degree, speed)`

탑 모터를 절대 각도 위치로 이동시킵니다.

**매개변수:**
- `degree` (int, optional): 절대 각도 위치 (0-65000), 기본값 0
- `speed` (int, optional): 회전 속도 (0-255), 기본값 50

**반환값:** 없음

**예제:**
```python
robot.top_motor_abspos(0, 50)  # 0도 위치로 이동
robot.top_motor_abspos(180, 80)  # 180도 위치로 이동
```

---

### `top_motor_time(dir, value, speed)`

지정된 시간 동안 탑 모터를 회전시킵니다.

**매개변수:**
- `dir` (str): 회전 방향 ('l': 왼쪽, 'r': 오른쪽)
- `value` (int, optional): 회전 시간(초), 기본값 3
- `speed` (int, optional): 회전 속도 (0-255), 기본값 50

**반환값:** 없음

**예제:**
```python
robot.top_motor_time('r', 2, 50)  # 오른쪽으로 2초간 회전
robot.top_motor_time('l', 5, 80)  # 왼쪽으로 5초간 회전
```

---

### `top_motor_round(dir, value, speed)`

지정된 회전수만큼 탑 모터를 회전시킵니다.

**매개변수:**
- `dir` (str): 회전 방향 ('l': 왼쪽, 'r': 오른쪽)
- `value` (int, optional): 회전 수, 기본값 1
- `speed` (int, optional): 회전 속도 (0-255), 기본값 50

**반환값:** 없음

**예제:**
```python
robot.top_motor_round('r', 2, 50)  # 오른쪽으로 2바퀴 회전
robot.top_motor_round('l', 1, 100)  # 왼쪽으로 1바퀴 회전
```

---

### `top_motor_stop()`

탑 모터의 회전을 즉시 정지시킵니다.

**매개변수:** 없음

**반환값:** 없음

**예제:**
```python
robot.top_motor_stop()
```

---

## 센서

### `get_object_detect(opt)`

물체 감지 센서를 동작시키고 값을 읽습니다.

**매개변수:**
- `opt` (bool, optional): 센서 동작 모드
  - `True`: 센서 동작 (기본값)
  - `False`: 센서 정지

**반환값:** 
- `tuple`: (left_object, right_object) - 왼쪽, 오른쪽 물체 감지 값

**예제:**
```python
left, right = robot.get_object_detect(True)
print(f"왼쪽: {left}, 오른쪽: {right}")
```

---

### `get_line_sensor(opt)`

라인 센서를 동작시키고 값을 읽습니다.

**매개변수:**
- `opt` (bool, optional): 센서 동작 모드
  - `True`: 센서 동작 (기본값)
  - `False`: 센서 정지

**반환값:**
- `tuple`: (right_line, center_line, left_line) - 오른쪽, 중앙, 왼쪽 라인 감지 값

**예제:**
```python
right, center, left = robot.get_line_sensor(True)
print(f"오른쪽: {right}, 중앙: {center}, 왼쪽: {left}")
```

---

### `get_color_sensor(opt)`

컬러 센서를 동작시키고 색상 인덱스를 읽습니다.

**매개변수:**
- `opt` (bool, optional): 센서 동작 모드
  - `True`: 센서 동작 (기본값)
  - `False`: 센서 정지

**반환값:**
- `int`: 색상 인덱스 값

**예제:**
```python
color = robot.get_color_sensor(True)
print(f"색상 인덱스: {color}")
```

---

### `get_color_elements(opt)`

컬러 센서를 동작시키고 RGB 값을 읽습니다.

**매개변수:**
- `opt` (bool, optional): 센서 동작 모드
  - `True`: 센서 동작 (기본값)
  - `False`: 센서 정지

**반환값:**
- `tuple`: (r, g, b) - Red, Green, Blue 값

**예제:**
```python
r, g, b = robot.get_color_elements(True)
print(f"RGB: ({r}, {g}, {b})")
```

---

### `get_battery()`

배터리 잔량을 읽습니다.

**매개변수:** 없음

**반환값:**
- `int`: 배터리 값

**예제:**
```python
battery = robot.get_battery()
print(f"배터리: {battery}")
```

---

### `get_version()`

펌웨어 버전 정보를 읽습니다.

**매개변수:** 없음

**반환값:** 없음

**예제:**
```python
robot.get_version()
```

---

## 도형 그리기

### `draw_tri(len)`

삼각형을 그립니다.

**매개변수:**
- `len` (int): 삼각형 한 변의 길이(cm)

**반환값:** 없음

**예제:**
```python
robot.draw_tri(10)  # 한 변이 10cm인 삼각형
```

---

### `draw_rect(len)`

사각형을 그립니다.

**매개변수:**
- `len` (int): 사각형 한 변의 길이(cm)

**반환값:** 없음

**예제:**
```python
robot.draw_rect(10)  # 한 변이 10cm인 사각형
```

---

### `draw_penta(len)`

오각형을 그립니다.

**매개변수:**
- `len` (int): 오각형 한 변의 길이(cm)

**반환값:** 없음

**예제:**
```python
robot.draw_penta(8)  # 한 변이 8cm인 오각형
```

---

### `draw_hexa(len)`

육각형을 그립니다.

**매개변수:**
- `len` (int): 육각형 한 변의 길이(cm)

**반환값:** 없음

**예제:**
```python
robot.draw_hexa(7)  # 한 변이 7cm인 육각형
```

---

### `draw_star(len)`

별 모양을 그립니다.

**매개변수:**
- `len` (int): 별 한 변의 길이(cm)

**반환값:** 없음

**예제:**
```python
robot.draw_star(10)  # 한 변이 10cm인 별
```

---

### `draw_circle(len)`

원을 그립니다.

**매개변수:**
- `len` (int): 원의 반지름(cm)

**반환값:** 없음

**예제:**
```python
robot.draw_circle(5)  # 반지름 5cm인 원
```

---

### `draw_semicircle(len, side)`

반원을 그립니다.

**매개변수:**
- `len` (int): 반원의 반지름(cm)
- `side` (str, optional): 반원 방향
  - `'l'`: 왼쪽 (기본값)
  - `'r'`: 오른쪽

**반환값:** 없음

**예제:**
```python
robot.draw_semicircle(5, 'l')  # 왼쪽 반원
robot.draw_semicircle(5, 'r')  # 오른쪽 반원
```

---

### `draw_arc(radius, value, mode)`

원호를 그립니다.

**매개변수:**
- `radius` (int): 원호의 반지름(cm)
- `value` (int, optional): 시간(초) 또는 각도, 기본값 1
- `mode` (int, optional): 단위 모드
  - `0`: 시간(초) 기준 (기본값)
  - `1`: 각도 기준

**반환값:** 없음

**예제:**
```python
robot.draw_arc(10, 2, 0)  # 반지름 10cm, 2초간 원호
robot.draw_arc(10, 90, 1)  # 반지름 10cm, 90도 원호
```

---

## 사운드

### `melody(scale, sec)`

지정된 음계와 시간으로 소리를 냅니다.

**매개변수:**
- `scale` (int, optional): 음계 (0-83), 기본값 45
- `sec` (int, optional): 소리 지속 시간(초), 기본값 1

**반환값:** 없음

**예제:**
```python
robot.melody(45, 1)  # 음계 45를 1초간 재생
robot.melody(60, 0.5)  # 음계 60을 0.5초간 재생
```

---

### `beep()`

짧은 "삐" 소리를 냅니다.

**매개변수:** 없음

**반환값:** 없음

**예제:**
```python
robot.beep()  # 짧은 비프음
```

---

## 유틸리티

### `angle3p(p1, p2, p3)` (정적 메서드)

3개의 점으로 이루어진 각도를 계산합니다 (시계 반대방향).

**매개변수:**
- `p1` (tuple): 첫 번째 점 (x1, y1)
- `p2` (tuple): 중심점 (x2, y2)
- `p3` (tuple): 세 번째 점 (x3, y3)

**반환값:**
- `float`: 각도(도 단위)

**예제:**
```python
angle = KamibotPi.angle3p((0, 0), (1, 0), (1, 1))
print(f"각도: {angle}도")
```

---

### `remap(value, source_range, target_range)`

값을 한 범위에서 다른 범위로 재매핑합니다.

**매개변수:**
- `value` (float): 재매핑할 값
- `source_range` (tuple): 소스 범위 (min, max)
- `target_range` (tuple): 타겟 범위 (min, max)

**반환값:**
- `float`: 재매핑된 값

**예제:**
```python
# 0-100 범위의 50을 0-10 범위로 변환
result = robot.remap(50, (0, 100), (0, 10))
print(result)  # 5.0

# 0-10 범위의 5를 0-100 범위로 변환
result = robot.remap(5, (0, 10), (0, 100))
print(result)  # 50.0
```

---

### `diff_color(color1, color2)` (전역 함수)

두 RGB 색상 간의 유클리드 거리를 계산합니다.

**매개변수:**
- `color1` (tuple): 첫 번째 색상 (r, g, b)
- `color2` (tuple): 두 번째 색상 (r, g, b)

**반환값:**
- `float`: 색상 간 거리 (0에 가까울수록 유사)

**예제:**
```python
from kamibotpi import diff_color

color1 = (255, 0, 0)  # 빨강
color2 = (255, 100, 0)  # 주황
distance = diff_color(color1, color2)
print(f"색상 차이: {distance}")
```


