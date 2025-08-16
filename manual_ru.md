# Руководство пользователя KamibotPi

## Содержание
1. [Обзор](#обзор)
2. [Установка и начальная настройка](#установка-и-начальная-настройка)
3. [Основы использования](#основы-использования)
4. [Подробное руководство по функциям](#подробное-руководство-по-функциям)
   - [Управление движением](#управление-движением)
   - [Точное управление](#точное-управление)
   - [Управление светодиодами](#управление-светодиодами)
   - [Использование датчиков](#использование-датчиков)
   - [Управление верхним мотором](#управление-верхним-мотором)
   - [Рисование фигур](#рисование-фигур)
   - [Воспроизведение мелодий](#воспроизведение-мелодий)
5. [Примеры кода](#примеры-кода)
6. [Решение проблем](#решение-проблем)

## Обзор

KamibotPi — это библиотека Python для управления роботом KamibotPi через последовательное (Serial) соединение, предоставляющая множество функций.

### Основные возможности
- Управление движением/поворотами (на игровом поле/линейном поле)
- Точное управление (по шагам/времени/расстоянию)
- Следование по линии
- Управление цветом светодиодов
- Чтение датчиков (линии/цвета/объектов)
- Управление верхним шаговым мотором
- Рисование геометрических фигур
- Воспроизведение мелодий
- Проверка батареи/версии

## Установка и начальная настройка

### Установка драйвера для Kamibot
Загрузите файл ```./drivers/CDM21228_Setup.zip```, распакуйте архив и установите.
```
Установите файл CDM21228_Setup.exe 
```

### Установка VSCode
```
https://code.visualstudio.com/download
```
Загрузите и установите программу VSCode

### Создание виртуальной среды Python
```bash
pythonn -m venv .venv
```

### Активация виртуальной среды
```
# Powershell
./venv/Scrpts/activate.ps1

# CommandLine
./venv/Scrpts/activate.bat
```

### Установка необходимых пакетов
Установка библиотеки Python для KamibotPi
```bash
pip install pyKamipi
```

### Определение порта адаптера KamibotPi
- **Windows**: Проверьте COM-порт в диспетчере устройств (например: COM5)

### Базовое подключение
```python
from kamibotpi import KamibotPi

# Подключение с настройками порта
kb = KamibotPi(port="COM5", baud=57600, timeout=2, verbose=True)
kb.init()  # Инициализация робота
```

## Основы использования

### Базовый шаблон
```python
from kamibotpi import KamibotPi

# Подключение и инициализация
kb = KamibotPi(port="COM5", baud=57600, timeout=2, verbose=False)
kb.init()

try:
    # Здесь пишите код управления роботом
    kb.move_forward(2, opt="-l")
    kb.turn_left()
    
finally:
    # Завершение программы
    kb.close()  # Внимание: вызывает sys.exit(0)
```

### Параметры конструктора
- `port`: Имя последовательного порта (обязательно)
- `baud`: Скорость передачи данных (по умолчанию: 57600)
- `timeout`: Таймаут чтения в секундах (по умолчанию: 2)
- `verbose`: Включить отладочный вывод (по умолчанию: False)

## Подробное руководство по функциям

### Управление движением

#### Движение по игровому/линейному полю
```python
# Движение вперед (линейное поле)
kb.move_forward(2, opt="-l")  # Движение на 2 клетки вперед

# Движение вперед (блочное поле)
kb.move_forward(1, opt="-b")  # Движение на 1 клетку вперед

# Движение назад (только блочное поле)
kb.move_backward(1)

# Повороты
kb.turn_left(value=1, opt="-l")   # Поворот влево
kb.turn_right(value=1, opt="-l")  # Поворот вправо
kb.turn_back(value=1, opt="-l")   # Поворот на 180 градусов
```

#### Управление скоростью
```python
# Индивидуальное управление скоростью левого и правого колес
kb.go_forward_speed(120, 120)   # Движение вперед
kb.go_backward_speed(100, 100)  # Движение назад
kb.go_left_speed(90)            # Поворот влево
kb.go_right_speed(90)           # Поворот вправо

# Одновременное управление направлением и скоростью
kb.go_dir_speed('f', 120, 'b', 110)  # Левое колесо вперед, правое назад

# Остановка
kb.stop()
```

#### Следование по линии
```python
# Запуск следования по линии
kb.toggle_linetracer(True, speed=100)

# Остановка следования по линии
kb.toggle_linetracer(False)
```

### Точное управление

#### Движение на основе шагов/времени
```python
# Движение по шагам
kb.move_step('f', 400, 'b', 400)  # Левое колесо 400 шагов вперед, правое 400 шагов назад

# Движение по времени
kb.move_time('f', 2, 'f', 2)  # Оба колеса 2 секунды вперед
```

#### Движение на основе единиц измерения
```python
# Единицы расстояния (см)
kb.move_forward_unit(20, opt='-l', speed=80)   # 20 см вперед
kb.move_backward_unit(10, opt='-l', speed=50)  # 10 см назад
kb.move_left_unit(15, opt='-l', speed=70)      # 15 см влево
kb.move_right_unit(10, opt='-l', speed=60)     # 10 см вправо

# Единицы времени (секунды)
kb.move_forward_unit(2, opt='-t', speed=80)    # 2 секунды вперед

# Единицы шагов
kb.move_forward_unit(500, opt='-s', speed=60)  # 500 шагов вперед
```

#### Непрерывное вращение
```python
# Непрерывное вращение (до команды остановки)
kb.turn_continous('l', speed=80)  # Непрерывное вращение влево
kb.turn_continous('r', speed=80)  # Непрерывное вращение вправо
kb.stop()  # Остановка вращения
```

### Управление светодиодами

#### Использование предустановленных цветов
```python
# Установка цвета по индексу (0~7)
kb.turn_led_idx(0)  # Красный
kb.turn_led_idx(1)  # Оранжевый
kb.turn_led_idx(2)  # Желтый
kb.turn_led_idx(3)  # Зеленый
kb.turn_led_idx(4)  # Синий
kb.turn_led_idx(5)  # Голубой
kb.turn_led_idx(6)  # Фиолетовый
kb.turn_led_idx(7)  # Белый
```

#### Прямое управление RGB
```python
# Установка цвета значениями RGB (0~255)
kb.turn_led(255, 0, 0)    # Красный
kb.turn_led(0, 255, 0)    # Зеленый
kb.turn_led(0, 0, 255)    # Синий
kb.turn_led(255, 255, 0)  # Желтый
kb.turn_led(255, 0, 128)  # Розовый
```

#### Использование предустановленных цветовых констант
```python
from kamibotpi import LedColor

kb.turn_led(*LedColor.RED)     # Красный
kb.turn_led(*LedColor.GREEN)   # Зеленый
kb.turn_led(*LedColor.BLUE)    # Синий
```

### Использование датчиков

#### Датчик линии
```python
# Чтение датчика линии
left, center, right = kb.get_line_sensor(True)
print(f"Датчик линии: лев={left}, центр={center}, прав={right}")

# Пример обнаружения линии
if center > 100:  # Пороговое значение настраивается в зависимости от условий
    print("Линия обнаружена в центре")
```

#### Датчик объектов
```python
# Чтение датчика объектов
left_obj, right_obj = kb.get_object_detect(True)
print(f"Обнаружение объектов: лев={left_obj}, прав={right_obj}")

# Пример обнаружения объекта
if left_obj > 50 or right_obj > 50:  # Необходимо настроить пороговое значение
    print("Объект обнаружен!")
    kb.stop()
```

#### Датчик цвета
```python
# Чтение датчика цвета
color = kb.get_color_sensor(True)
print(f"Обнаруженный код цвета: {color}")

# Пример действий в зависимости от цвета
if color == 1:  # Код цвета зависит от определения в прошивке
    kb.turn_led_idx(0)  # Красный светодиод
elif color == 2:
    kb.turn_led_idx(3)  # Зеленый светодиод
```

#### Проверка батареи
```python
battery = kb.get_battery()
print(f"Уровень заряда батареи: {battery}")

if battery < 30:  # Пример порогового значения
    print("Низкий заряд батареи!")
```

### Управление верхним мотором

#### Вращение на основе угла
```python
# Относительное вращение на угол
kb.top_motor_degree('l', value=45, speed=60)   # 45 градусов влево
kb.top_motor_degree('r', value=90, speed=80)   # 90 градусов вправо

# Движение в абсолютную позицию
kb.top_motor_abspos(180, speed=70)  # В абсолютную позицию 180 градусов
kb.top_motor_abspos(0, speed=50)    # Возврат в исходную позицию
```

#### На основе времени/оборотов
```python
# Вращение на основе времени
kb.top_motor_time('r', value=2, speed=80)  # 2 секунды вращения вправо

# На основе количества оборотов
kb.top_motor_round('l', value=3, speed=40)  # 3 оборота влево

# Остановка мотора
kb.top_motor_stop()
```

### Рисование фигур

#### Основные фигуры
```python
# Многоугольники
kb.draw_tri(10)      # Равносторонний треугольник (сторона 10 см)
kb.draw_rect(12)     # Квадрат (сторона 12 см)
kb.draw_penta(8)     # Правильный пятиугольник (сторона 8 см)
kb.draw_hexa(7)      # Правильный шестиугольник (сторона 7 см)
kb.draw_star(10)     # Звезда (сторона 10 см)
```

#### Круглые фигуры
```python
# Круг
kb.draw_circle(6)    # Круг (радиус 6 см)

# Полукруг
kb.draw_semicircle(5, side='l')  # Левый полукруг (радиус 5 см)
kb.draw_semicircle(5, side='r')  # Правый полукруг

# Дуга (с ограничением по времени)
kb.draw_arc(8, time=2)  # Радиус 8 см, дуга в течение 2 секунд
```

### Воспроизведение мелодий

#### Воспроизведение звуков
```python
# Воспроизведение с определенной нотой и длительностью
kb.melody(scale=60, sec=1)  # Нота 60, 1 секунда воспроизведения
kb.melody(scale=45, sec=2)  # Нота 45, 2 секунды воспроизведения

# Простой звуковой сигнал
kb.beep()  # Короткий звуковой сигнал

# Пример последовательности мелодии
melody_sequence = [
    (60, 1), (62, 1), (64, 1), (65, 1),
    (67, 1), (69, 1), (71, 1), (72, 2)
]

for scale, duration in melody_sequence:
    kb.melody(scale=scale, sec=duration)
    kb.delay(0.1)  # Интервал между нотами
```

## Примеры кода

### Базовый паттерн движения
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5", verbose=False)
kb.init()

try:
    # Рисование квадрата (линейное поле)
    for i in range(4):
        kb.move_forward(2, opt="-l")
        kb.turn_right(opt="-l")
        kb.delay(0.5)
    
    # Изменение цвета светодиода
    colors = [0, 1, 2, 3, 4, 5, 6, 7]
    for color in colors:
        kb.turn_led_idx(color)
        kb.delay(0.5)
        
finally:
    kb.close()
```

### Обход препятствий на основе датчиков
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5", verbose=False)
kb.init()

try:
    while True:
        # Обнаружение объектов
        left_obj, right_obj = kb.get_object_detect(True)
        
        if left_obj > 50 or right_obj > 50:
            # При обнаружении препятствия
            kb.stop()
            kb.turn_led_idx(0)  # Красный светодиод
            kb.beep()
            
            # Действие обхода
            kb.move_backward_unit(5, opt="-l", speed=50)
            kb.turn_right(opt="-l")
            kb.delay(1)
        else:
            # Движение вперед
            kb.turn_led_idx(3)  # Зеленый светодиод
            kb.move_forward_unit(5, opt="-l", speed=70)
            
        kb.delay(0.1)
        
except KeyboardInterrupt:
    print("Программа прервана")
finally:
    kb.close()
```

### Следование по линии
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5", verbose=False)
kb.init()

try:
    while True:
        # Чтение датчика линии
        left, center, right = kb.get_line_sensor(True)
        
        if center > 100:  # Линия в центре
            kb.go_forward_speed(100, 100)
            kb.turn_led_idx(3)  # Зеленый
        elif left > 100:  # Линия слева
            kb.go_forward_speed(50, 120)  # Поворот влево
            kb.turn_led_idx(4)  # Синий
        elif right > 100:  # Линия справа
            kb.go_forward_speed(120, 50)  # Поворот вправо
            kb.turn_led_idx(6)  # Фиолетовый
        else:  # Нет линии
            kb.stop()
            kb.turn_led_idx(0)  # Красный
            
        kb.delay(0.05)
        
except KeyboardInterrupt:
    print("Программа прервана")
finally:
    kb.close()
```

### Робот, реагирующий на цвет
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5", verbose=False)
kb.init()

try:
    while True:
        color = kb.get_color_sensor(True)
        
        if color == 1:  # Обнаружение красного (пример)
            kb.turn_led_idx(0)  # Красный светодиод
            kb.melody(scale=60, sec=1)
            kb.turn_left(opt="-l")
        elif color == 2:  # Обнаружение зеленого (пример)
            kb.turn_led_idx(3)  # Зеленый светодиод
            kb.melody(scale=65, sec=1)
            kb.move_forward(1, opt="-l")
        elif color == 3:  # Обнаружение синего (пример)
            kb.turn_led_idx(4)  # Синий светодиод
            kb.melody(scale=72, sec=1)
            kb.turn_right(opt="-l")
        else:
            kb.turn_led_idx(7)  # Белый светодиод
            
        kb.delay(0.5)
        
except KeyboardInterrupt:
    print("Программа прервана")
finally:
    kb.close()
```

### Демонстрация рисования фигур
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5", verbose=False)
kb.init()

try:
    shapes = [
        ("Треугольник", lambda: kb.draw_tri(10)),
        ("Квадрат", lambda: kb.draw_rect(10)),
        ("Пятиугольник", lambda: kb.draw_penta(8)),
        ("Шестиугольник", lambda: kb.draw_hexa(8)),
        ("Круг", lambda: kb.draw_circle(6)),
        ("Звезда", lambda: kb.draw_star(8))
    ]
    
    for name, draw_func in shapes:
        print(f"{name} - начинаем рисовать")
        kb.turn_led_idx(shapes.index((name, draw_func)))
        kb.beep()
        draw_func()
        kb.delay(2)
        
    print("Рисование всех фигур завершено")
    
finally:
    kb.close()
```

## Решение проблем

### Часто возникающие проблемы

#### 1. Ошибка подключения
```
serial.SerialException: could not open port 'COM5'
```
**Решение**:
- Проверьте имя порта (Windows: Диспетчер устройств, Linux: `ls /dev/tty*`)
- Убедитесь, что порт не используется другой программой
- Проверьте состояние подключения кабеля

#### 2. Ошибка таймаута
**Симптомы**: Нет ответа после отправки команды
**Решение**:
- Увеличьте значение `timeout` (например: `timeout=5`)
- Проверьте скорость передачи данных (по умолчанию: 57600)
- Проверьте состояние питания оборудования

#### 3. Неточное движение
**Решение**:
- Проверьте уровень заряда батареи: `kb.get_battery()`
- Проверьте состояние поверхности пола (предотвратите скольжение)
- Отрегулируйте скорость мотора

#### 4. Странные значения датчиков
**Решение**:
- Очистите поверхность датчиков
- Проверьте условия освещения (датчики цвета/линии)
- Перенастройте пороговые значения

### Советы по отладке

#### 1. Использование режима Verbose
```python
kb = KamibotPi(port="COM5", verbose=True)  # Включить отладочный вывод
```

#### 2. Мониторинг значений датчиков
```python
while True:
    left_obj, right_obj = kb.get_object_detect(True)
    left_line, center_line, right_line = kb.get_line_sensor(True)
    color = kb.get_color_sensor(True)
    battery = kb.get_battery()
    
    print(f"Объекты: Л={left_obj}, П={right_obj}")
    print(f"Линия: Л={left_line}, Ц={center_line}, П={right_line}")
    print(f"Цвет: {color}, Батарея: {battery}")
    print("-" * 40)
    
    kb.delay(1)
```

#### 3. Пошаговое тестирование
```python
# 1. Тест базового подключения
kb = KamibotPi(port="COM5", verbose=True)
kb.init()
print("Подключение успешно")

# 2. Тест светодиода
kb.turn_led_idx(0)
kb.delay(1)

# 3. Тест звука
kb.beep()

# 4. Тест простого движения
kb.move_forward_unit(5, opt="-l", speed=50)

# 5. Тест датчиков
print(kb.get_battery())
```

### Оптимизация производительности

#### 1. Подходящая задержка между командами
```python
kb.move_forward(1, opt="-l")
kb.delay(0.1)  # Обеспечение времени обработки команды
kb.turn_left(opt="-l")
```

#### 2. Регулировка периода опроса датчиков
```python
# Избегайте слишком быстрого опроса
while True:
    sensor_data = kb.get_line_sensor(True)
    # Логика обработки
    kb.delay(0.05)  # Поддержание подходящего интервала
```

#### 3. Управление батареей
```python
def check_battery(kb):
    battery = kb.get_battery()
    if battery < 20:  # Пороговое значение
        print("Низкий заряд батареи! Завершение программы")
        kb.turn_led_idx(0)  # Предупреждение красным светодиодом
        return False
    return True

# Периодическая проверка батареи
if not check_battery(kb):
    kb.close()
```

### Правила безопасного использования

1. **Управление питанием**: Проверьте достаточный заряд батареи перед использованием
2. **Рабочее пространство**: Обеспечьте достаточное пространство для движения робота
3. **Экстренная остановка**: Можно прервать программу с помощью `Ctrl+C`
4. **Завершение программы**: Всегда вызывайте `kb.close()` (или используйте try-finally)
5. **Чистота датчиков**: Регулярная очистка датчиков для поддержания точности

Пожалуйста, используйте этот справочник для безопасного и эффективного использования KamibotPi!
