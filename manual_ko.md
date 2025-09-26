# KamibotPi 사용자 매뉴얼

## 목차
1. [개요](#개요)
2. [설치 및 초기 설정](#설치-및-초기-설정)
3. [기본 사용법](#기본-사용법)
4. [기능별 상세 가이드](#기능별-상세-가이드)
   - [이동 제어](#이동-제어)
   - [정밀 제어](#정밀-제어)
   - [LED 제어](#led-제어)
   - [센서 활용](#센서-활용)
   - [상단 모터 제어](#상단-모터-제어)
   - [도형 그리기](#도형-그리기)
   - [멜로디 재생](#멜로디-재생)
5. [예제 코드](#예제-코드)
6. [문제 해결](#문제-해결)

## 개요

KamibotPi는 직렬(Serial) 통신을 통해 KamibotPi 하드웨어와 통신하여 다양한 기능을 제공하는 Python 라이브러리입니다.

### 주요 기능
- 이동/회전 제어 (맵보드/라인맵보드)
- 정밀 제어 (스텝/시간/거리 단위)
- 라인트레이서
- LED 색상 제어
- 센서 읽기 (라인/컬러/물체)
- 상단 스텝퍼 모터 제어
- 도형 그리기
- 멜로디 재생
- 배터리/버전 조회

## 설치 및 초기 설정
### Kamibot용 드라이버 설치
```./drivers/CDM21228_Setup.zip``` 파일을 다운로드 받아서, 압축을 푼 후 설치한다. 설치는 윈도우즈의 관리자 권한으로 설치해야 합니다.
```
CDM21228_Setup.exe 파일 설치 
```
### VSCode 설치
```
https://code.visualstudio.com/download
```
VSCode 프로그램을 다운로드 받아서 설치 

### 파이썬 가상환경 만들기
가상환경은 Miniconda 를 사용해서 python 3.10을 사용합니다.
```bash
conda create -n [가상환경 이름] python==3.10
```
### 가상환경 활성화
```
conda activate [가상 환경 이름]
```
파이썬의 버전을 확인합니다.
```
python --version
```

### 필요 패키지 설치
카미봇 파이용 파이썬 라이브러리 설치 
```bash
pip install pyKamipi
```

### 카미봇파이용 동글의 포트 확인
- **Windows**: 장치 관리자에서 COM 포트 확인 (예: COM5)

### 기본 연결
```python
from kamibotpi import KamibotPi

# 포트와 설정으로 연결
kb = KamibotPi(port="COM8", baud=57600, timeout=2, verbose=True)
kb.init()  # 로봇 초기화
```
> `port`: 직렬 포트 이름 (필수)  
> `baud`: 보오 레이트 (기본값: 57600)  
> `timeout`: 읽기 타임아웃 초 (기본값: 2)  
> `verbose`: 디버그 출력 여부 (기본값: False)  
  
## 기본 사용법

### 기본 템플릿
```python
#-*-coding:utf-8-*-
from pyKamipi.pibot import *


# 카미봇 연결
robot = KamibotPi('COM8', 57600)
robot.init()  # 로봇 초기화

try:
    # 여기에 로봇 제어 코드 작성
    robot.go_dir_speed("f", 50, "f", 50)
    robot.delayms(1000)
    robot.stop()
    
finally:
    # 프로그램 종료
    robot.close()  # 주의: sys.exit(0) 호출됨


```



## 기능별 상세 가이드

### 이동 제어

#### 맵보드/라인맵보드 이동
```python
# 전진 (라인맵보드)
kb.move_forward(2, opt="-l")  # 2칸 전진

# 전진 (블록맵보드)
kb.move_forward(1, opt="-b")  # 1칸 전진

# 후진 (블록맵보드만 지원)
kb.move_backward(1)

# 회전
kb.turn_left(value=1, opt="-l")   # 왼쪽 회전
kb.turn_right(value=1, opt="-l")  # 오른쪽 회전
kb.turn_back(value=1, opt="-l")   # 180도 회전
```

#### 속도 제어
```python
# 좌우 바퀴 속도 개별 제어
kb.go_forward_speed(120, 120)   # 전진
kb.go_backward_speed(100, 100)  # 후진
kb.go_left_speed(90)            # 왼쪽 회전
kb.go_right_speed(90)           # 오른쪽 회전

# 방향과 속도 동시 제어
kb.go_dir_speed('f', 120, 'b', 110)  # 좌측 전진, 우측 후진

# 정지
kb.stop()
```

#### 라인트레이서
```python
# 라인트레이서 시작
kb.toggle_linetracer(True, speed=100)

# 라인트레이서 정지
kb.toggle_linetracer(False)
```

### 정밀 제어

#### 스텝/시간 기반 이동
```python
# 스텝 단위 이동
kb.move_step('f', 400, 'b', 400)  # 좌측 전진 400스텝, 우측 후진 400스텝

# 시간 단위 이동
kb.move_time('f', 2, 'f', 2)  # 양쪽 2초 전진
```

#### 단위 기반 이동
```python
# 거리 단위 (cm)
kb.move_forward_unit(20, opt='-l', speed=80)   # 20cm 전진
kb.move_backward_unit(10, opt='-l', speed=50)  # 10cm 후진
kb.move_left_unit(15, opt='-l', speed=70)      # 15cm 좌측 이동
kb.move_right_unit(10, opt='-l', speed=60)     # 10cm 우측 이동

# 시간 단위 (초)
kb.move_forward_unit(2, opt='-t', speed=80)    # 2초 전진

# 스텝 단위
kb.move_forward_unit(500, opt='-s', speed=60)  # 500스텝 전진
```

#### 연속 회전
```python
# 지속 회전 (정지 명령까지 계속)
kb.turn_continous('l', speed=80)  # 왼쪽 연속 회전
kb.turn_continous('r', speed=80)  # 오른쪽 연속 회전
kb.stop()  # 회전 정지
```

### LED 제어

#### 프리셋 색상 사용
```python
# 인덱스로 색상 설정 (0~7)
kb.turn_led_idx(0)  # 빨강
kb.turn_led_idx(1)  # 주황
kb.turn_led_idx(2)  # 노랑
kb.turn_led_idx(3)  # 초록
kb.turn_led_idx(4)  # 파랑
kb.turn_led_idx(5)  # 하늘색
kb.turn_led_idx(6)  # 보라
kb.turn_led_idx(7)  # 흰색
```

#### RGB 직접 제어
```python
# RGB 값으로 색상 설정 (0~255)
kb.turn_led(255, 0, 0)    # 빨강
kb.turn_led(0, 255, 0)    # 초록
kb.turn_led(0, 0, 255)    # 파랑
kb.turn_led(255, 255, 0)  # 노랑
kb.turn_led(255, 0, 128)  # 핑크
```

#### 프리셋 색상 상수 활용
```python
from kamibotpi import LedColor

kb.turn_led(*LedColor.RED)     # 빨강
kb.turn_led(*LedColor.GREEN)   # 초록
kb.turn_led(*LedColor.BLUE)    # 파랑
```

### 센서 활용

#### 라인 센서
```python
# 라인 센서 읽기
left, center, right = kb.get_line_sensor(True)
print(f"라인 센서: 좌={left}, 중앙={center}, 우={right}")

# 라인 감지 예제
if center > 100:  # 임계값은 환경에 따라 조정
    print("중앙에 라인 감지됨")
```

#### 물체 감지 센서
```python
# 물체 감지 센서 읽기
left_obj, right_obj = kb.get_object_detect(True)
print(f"물체 감지: 좌={left_obj}, 우={right_obj}")

# 물체 감지 예제
if left_obj > 50 or right_obj > 50:  # 임계값 조정 필요
    print("물체 감지됨!")
    kb.stop()
```

#### 컬러 센서
```python
# 컬러 센서 읽기
color = kb.get_color_sensor(True)
print(f"감지된 색상 코드: {color}")

# 색상별 동작 예제
if color == 1:  # 색상 코드는 펌웨어 정의에 따름
    kb.turn_led_idx(0)  # 빨간 LED
elif color == 2:
    kb.turn_led_idx(3)  # 초록 LED
```

#### 배터리 확인
```python
battery = kb.get_battery()
print(f"배터리 잔량: {battery}")

if battery < 30:  # 임계값 예시
    print("배터리 부족!")
```

### 상단 모터 제어

#### 각도 기반 회전
```python
# 상대 각도 회전
kb.top_motor_degree('l', value=45, speed=60)   # 왼쪽 45도
kb.top_motor_degree('r', value=90, speed=80)   # 오른쪽 90도

# 절대 위치로 이동
kb.top_motor_abspos(180, speed=70)  # 절대 180도 위치로
kb.top_motor_abspos(0, speed=50)    # 원점으로 복귀
```

#### 시간/회전수 기반
```python
# 시간 기반 회전
kb.top_motor_time('r', value=2, speed=80)  # 2초 동안 우측 회전

# 회전수 기반
kb.top_motor_round('l', value=3, speed=40)  # 3바퀴 좌측 회전

# 모터 정지
kb.top_motor_stop()
```

### 도형 그리기

#### 기본 도형
```python
# 다각형
kb.draw_tri(10)      # 정삼각형 (한 변 10cm)
kb.draw_rect(12)     # 정사각형 (한 변 12cm)
kb.draw_penta(8)     # 정오각형 (한 변 8cm)
kb.draw_hexa(7)      # 정육각형 (한 변 7cm)
kb.draw_star(10)     # 별 모양 (한 변 10cm)
```

#### 원형 도형
```python
# 원
kb.draw_circle(6)    # 원 (반지름 6cm)

# 반원
kb.draw_semicircle(5, side='l')  # 왼쪽 반원 (반지름 5cm)
kb.draw_semicircle(5, side='r')  # 오른쪽 반원

# 원호 (시간 제한)
kb.draw_arc(8, time=2)  # 반지름 8cm, 2초 동안 원호
```

### 멜로디 재생

#### 음 재생
```python
# 특정 음계와 시간으로 재생
kb.melody(scale=60, sec=1)  # 음계 60, 1초 재생
kb.melody(scale=45, sec=2)  # 음계 45, 2초 재생

# 간단한 삐 소리
kb.beep()  # 짧은 삐 소리

# 멜로디 시퀀스 예제
melody_sequence = [
    (60, 1), (62, 1), (64, 1), (65, 1),
    (67, 1), (69, 1), (71, 1), (72, 2)
]

for scale, duration in melody_sequence:
    kb.melody(scale=scale, sec=duration)
    kb.delay(0.1)  # 음 사이 간격
```

## 예제 코드

### 기본 이동 패턴
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5", verbose=False)
kb.init()

try:
    # 정사각형 그리기 (라인맵보드)
    for i in range(4):
        kb.move_forward(2, opt="-l")
        kb.turn_right(opt="-l")
        kb.delay(0.5)
    
    # LED 색상 변경
    colors = [0, 1, 2, 3, 4, 5, 6, 7]
    for color in colors:
        kb.turn_led_idx(color)
        kb.delay(0.5)
        
finally:
    kb.close()
```

### 센서 기반 장애물 회피
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5", verbose=False)
kb.init()

try:
    while True:
        # 물체 감지
        left_obj, right_obj = kb.get_object_detect(True)
        
        if left_obj > 50 or right_obj > 50:
            # 장애물 감지시
            kb.stop()
            kb.turn_led_idx(0)  # 빨간 LED
            kb.beep()
            
            # 회피 동작
            kb.move_backward_unit(5, opt="-l", speed=50)
            kb.turn_right(opt="-l")
            kb.delay(1)
        else:
            # 전진
            kb.turn_led_idx(3)  # 초록 LED
            kb.move_forward_unit(5, opt="-l", speed=70)
            
        kb.delay(0.1)
        
except KeyboardInterrupt:
    print("프로그램 중단")
finally:
    kb.close()
```

### 라인 추적
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5", verbose=False)
kb.init()

try:
    while True:
        # 라인 센서 읽기
        left, center, right = kb.get_line_sensor(True)
        
        if center > 100:  # 중앙에 라인
            kb.go_forward_speed(100, 100)
            kb.turn_led_idx(3)  # 초록
        elif left > 100:  # 왼쪽에 라인
            kb.go_forward_speed(50, 120)  # 좌회전
            kb.turn_led_idx(4)  # 파랑
        elif right > 100:  # 오른쪽에 라인
            kb.go_forward_speed(120, 50)  # 우회전
            kb.turn_led_idx(6)  # 보라
        else:  # 라인 없음
            kb.stop()
            kb.turn_led_idx(0)  # 빨강
            
        kb.delay(0.05)
        
except KeyboardInterrupt:
    print("프로그램 중단")
finally:
    kb.close()
```

### 컬러 반응 로봇
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5", verbose=False)
kb.init()

try:
    while True:
        color = kb.get_color_sensor(True)
        
        if color == 1:  # 빨강 감지 (예시)
            kb.turn_led_idx(0)  # 빨간 LED
            kb.melody(scale=60, sec=1)
            kb.turn_left(opt="-l")
        elif color == 2:  # 초록 감지 (예시)
            kb.turn_led_idx(3)  # 초록 LED
            kb.melody(scale=65, sec=1)
            kb.move_forward(1, opt="-l")
        elif color == 3:  # 파랑 감지 (예시)
            kb.turn_led_idx(4)  # 파란 LED
            kb.melody(scale=72, sec=1)
            kb.turn_right(opt="-l")
        else:
            kb.turn_led_idx(7)  # 흰색 LED
            
        kb.delay(0.5)
        
except KeyboardInterrupt:
    print("프로그램 중단")
finally:
    kb.close()
```

### 도형 그리기 데모
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5", verbose=False)
kb.init()

try:
    shapes = [
        ("삼각형", lambda: kb.draw_tri(10)),
        ("사각형", lambda: kb.draw_rect(10)),
        ("오각형", lambda: kb.draw_penta(8)),
        ("육각형", lambda: kb.draw_hexa(8)),
        ("원", lambda: kb.draw_circle(6)),
        ("별", lambda: kb.draw_star(8))
    ]
    
    for name, draw_func in shapes:
        print(f"{name} 그리기 시작")
        kb.turn_led_idx(shapes.index((name, draw_func)))
        kb.beep()
        draw_func()
        kb.delay(2)
        
    print("모든 도형 그리기 완료")
    
finally:
    kb.close()
```

## 문제 해결

### 자주 발생하는 문제

#### 1. 연결 오류
```
serial.SerialException: could not open port 'COM5'
```
**해결책**:
- 포트 이름 확인 (Windows: 장치 관리자, Linux: `ls /dev/tty*`)
- 다른 프로그램이 포트를 사용하고 있는지 확인
- 케이블 연결 상태 확인

#### 2. 타임아웃 오류
**증상**: 명령 전송 후 응답이 없음
**해결책**:
- `timeout` 값을 늘려보기 (예: `timeout=5`)
- 보오 레이트 확인 (기본값: 57600)
- 하드웨어 전원 상태 확인

#### 3. 움직임이 부정확함
**해결책**:
- 배터리 잔량 확인: `kb.get_battery()`
- 바닥 표면 상태 확인 (미끄러짐 방지)
- 모터 속도 조정

#### 4. 센서값이 이상함
**해결책**:
- 센서 표면 청소
- 조명 환경 확인 (컬러/라인 센서)
- 임계값 재조정

### 디버깅 팁

#### 1. Verbose 모드 사용
```python
kb = KamibotPi(port="COM5", verbose=True)  # 디버그 출력 활성화
```

#### 2. 센서값 모니터링
```python
while True:
    left_obj, right_obj = kb.get_object_detect(True)
    left_line, center_line, right_line = kb.get_line_sensor(True)
    color = kb.get_color_sensor(True)
    battery = kb.get_battery()
    
    print(f"물체: L={left_obj}, R={right_obj}")
    print(f"라인: L={left_line}, C={center_line}, R={right_line}")
    print(f"색상: {color}, 배터리: {battery}")
    print("-" * 40)
    
    kb.delay(1)
```

#### 3. 단계별 테스트
```python
# 1. 기본 연결 테스트
kb = KamibotPi(port="COM5", verbose=True)
kb.init()
print("연결 성공")

# 2. LED 테스트
kb.turn_led_idx(0)
kb.delay(1)

# 3. 소리 테스트
kb.beep()

# 4. 간단한 이동 테스트
kb.move_forward_unit(5, opt="-l", speed=50)

# 5. 센서 테스트
print(kb.get_battery())
```

### 성능 최적화

#### 1. 명령 간 적절한 지연
```python
kb.move_forward(1, opt="-l")
kb.delay(0.1)  # 명령 처리 시간 확보
kb.turn_left(opt="-l")
```

#### 2. 센서 폴링 주기 조정
```python
# 너무 빠른 폴링은 피하기
while True:
    sensor_data = kb.get_line_sensor(True)
    # 처리 로직
    kb.delay(0.05)  # 적절한 간격 유지
```

#### 3. 배터리 관리
```python
def check_battery(kb):
    battery = kb.get_battery()
    if battery < 20:  # 임계값
        print("배터리 부족! 프로그램 종료")
        kb.turn_led_idx(0)  # 빨간 LED로 경고
        return False
    return True

# 주기적으로 배터리 확인
if not check_battery(kb):
    kb.close()
```

### 안전 사용 수칙

1. **전원 관리**: 사용 전 충분한 배터리 확인
2. **동작 공간**: 로봇이 움직일 충분한 공간 확보
3. **긴급 정지**: `Ctrl+C`로 프로그램 중단 가능
4. **프로그램 종료**: 항상 `kb.close()` 호출 (또는 try-finally 사용)
5. **센서 청결**: 정기적인 센서 청소로 정확도 유지

이 매뉴얼을 참고하여 KamibotPi를 안전하고 효과적으로 활용하시기 바랍니다!
