# KamibotPi ユーザーマニュアル

## 目次
1. [概要](#概要)
2. [インストールと初期設定](#インストールと初期設定)
3. [基本的な使用方法](#基本的な使用方法)
4. [機能別詳細ガイド](#機能別詳細ガイド)
   - [移動制御](#移動制御)
   - [精密制御](#精密制御)
   - [LED制御](#led制御)
   - [センサーの活用](#センサーの活用)
   - [上部モーター制御](#上部モーター制御)
   - [図形描画](#図形描画)
   - [メロディ再生](#メロディ再生)
5. [サンプルコード](#サンプルコード)
6. [トラブルシューティング](#トラブルシューティング)

## 概要

KamibotPiは、シリアル通信を通じてKamibotPiハードウェアと通信し、様々な機能を提供するPythonライブラリです。

### 主な機能
- 移動・回転制御（マップボード・ラインマップボード）
- 精密制御（ステップ・時間・距離単位）
- ライントレーサー機能
- LED色彩制御
- センサー読み取り（ライン・色彩・物体検出）
- 上部ステッピングモーター制御
- 幾何学図形描画
- メロディ再生
- バッテリー・バージョン情報取得

## インストールと初期設定

### 必要パッケージのインストール
```bash
pip install pyserial
```

### ポートの確認
- **Windows**: デバイスマネージャーでCOMポートを確認（例：COM5）
- **Linux/Mac**: `/dev/ttyUSB0` または `/dev/ttyACM0` など

### 基本接続
```python
from kamibotpi import KamibotPi

# ポートと設定での接続
kb = KamibotPi(port="COM5", baud=57600, timeout=2, verbose=True)
kb.init()  # ロボットの初期化
```

## 基本的な使用方法

### 基本テンプレート
```python
from kamibotpi import KamibotPi

# 接続と初期化
kb = KamibotPi(port="COM5", baud=57600, timeout=2, verbose=False)
kb.init()

try:
    # ここにロボット制御コードを書く
    kb.move_forward(2, opt="-l")
    kb.turn_left()
    
finally:
    # プログラム終了
    kb.close()  # 注意：sys.exit(0)が呼ばれます
```

### コンストラクタのパラメータ
- `port`: シリアルポート名（必須）
- `baud`: ボーレート（デフォルト：57600）
- `timeout`: 読み取りタイムアウト秒数（デフォルト：2）
- `verbose`: デバッグ出力の有効化（デフォルト：False）

## 機能別詳細ガイド

### 移動制御

#### マップボード・ラインマップボードでの移動
```python
# 前進（ラインマップボード）
kb.move_forward(2, opt="-l")  # 2マス前進

# 前進（ブロックマップボード）
kb.move_forward(1, opt="-b")  # 1マス前進

# 後退（ブロックマップボードのみ）
kb.move_backward(1)

# 回転
kb.turn_left(value=1, opt="-l")   # 左回転
kb.turn_right(value=1, opt="-l")  # 右回転
kb.turn_back(value=1, opt="-l")   # 180度回転
```

#### 速度制御
```python
# 左右の車輪速度を個別制御
kb.go_forward_speed(120, 120)   # 前進
kb.go_backward_speed(100, 100)  # 後退
kb.go_left_speed(90)            # 左回転
kb.go_right_speed(90)           # 右回転

# 方向と速度の同時制御
kb.go_dir_speed('f', 120, 'b', 110)  # 左前進、右後退

# 停止
kb.stop()
```

#### ライントレーサー
```python
# ライントレーサー開始
kb.toggle_linetracer(True, speed=100)

# ライントレーサー停止
kb.toggle_linetracer(False)
```

### 精密制御

#### ステップ・時間ベースの移動
```python
# ステップベース移動
kb.move_step('f', 400, 'b', 400)  # 左400ステップ前進、右400ステップ後退

# 時間ベース移動
kb.move_time('f', 2, 'f', 2)  # 両輪2秒間前進
```

#### 単位ベース移動
```python
# 距離単位（cm）
kb.move_forward_unit(20, opt='-l', speed=80)   # 20cm前進
kb.move_backward_unit(10, opt='-l', speed=50)  # 10cm後退
kb.move_left_unit(15, opt='-l', speed=70)      # 15cm左移動
kb.move_right_unit(10, opt='-l', speed=60)     # 10cm右移動

# 時間単位（秒）
kb.move_forward_unit(2, opt='-t', speed=80)    # 2秒間前進

# ステップ単位
kb.move_forward_unit(500, opt='-s', speed=60)  # 500ステップ前進
```

#### 連続回転
```python
# 連続回転（停止コマンドまで継続）
kb.turn_continous('l', speed=80)  # 左連続回転
kb.turn_continous('r', speed=80)  # 右連続回転
kb.stop()  # 回転停止
```

### LED制御

#### プリセット色の使用
```python
# インデックスで色設定（0〜7）
kb.turn_led_idx(0)  # 赤
kb.turn_led_idx(1)  # オレンジ
kb.turn_led_idx(2)  # 黄
kb.turn_led_idx(3)  # 緑
kb.turn_led_idx(4)  # 青
kb.turn_led_idx(5)  # 水色
kb.turn_led_idx(6)  # 紫
kb.turn_led_idx(7)  # 白
```

#### RGB直接制御
```python
# RGB値で色設定（0〜255）
kb.turn_led(255, 0, 0)    # 赤
kb.turn_led(0, 255, 0)    # 緑
kb.turn_led(0, 0, 255)    # 青
kb.turn_led(255, 255, 0)  # 黄
kb.turn_led(255, 0, 128)  # ピンク
```

#### プリセット色定数の活用
```python
from kamibotpi import LedColor

kb.turn_led(*LedColor.RED)     # 赤
kb.turn_led(*LedColor.GREEN)   # 緑
kb.turn_led(*LedColor.BLUE)    # 青
```

### センサーの活用

#### ラインセンサー
```python
# ラインセンサー読み取り
left, center, right = kb.get_line_sensor(True)
print(f"ラインセンサー：左={left}、中央={center}、右={right}")

# ライン検出例
if center > 100:  # 閾値は環境に応じて調整
    print("中央にライン検出")
```

#### 物体検出センサー
```python
# 物体検出センサー読み取り
left_obj, right_obj = kb.get_object_detect(True)
print(f"物体検出：左={left_obj}、右={right_obj}")

# 物体検出例
if left_obj > 50 or right_obj > 50:  # 閾値調整が必要
    print("物体を検出しました！")
    kb.stop()
```

#### 色彩センサー
```python
# 色彩センサー読み取り
color = kb.get_color_sensor(True)
print(f"検出された色コード：{color}")

# 色別動作例
if color == 1:  # 色コードはファームウェア定義による
    kb.turn_led_idx(0)  # 赤LED
elif color == 2:
    kb.turn_led_idx(3)  # 緑LED
```

#### バッテリー確認
```python
battery = kb.get_battery()
print(f"バッテリー残量：{battery}")

if battery < 30:  # 例の閾値
    print("バッテリー残量が少ないです！")
```

### 上部モーター制御

#### 角度ベース回転
```python
# 相対角度回転
kb.top_motor_degree('l', value=45, speed=60)   # 左45度
kb.top_motor_degree('r', value=90, speed=80)   # 右90度

# 絶対位置への移動
kb.top_motor_abspos(180, speed=70)  # 絶対180度位置へ
kb.top_motor_abspos(0, speed=50)    # 原点復帰
```

#### 時間・回転数ベース
```python
# 時間ベース回転
kb.top_motor_time('r', value=2, speed=80)  # 2秒間右回転

# 回転数ベース
kb.top_motor_round('l', value=3, speed=40)  # 3回転左

# モーター停止
kb.top_motor_stop()
```

### 図形描画

#### 基本図形
```python
# 多角形
kb.draw_tri(10)      # 正三角形（一辺10cm）
kb.draw_rect(12)     # 正方形（一辺12cm）
kb.draw_penta(8)     # 正五角形（一辺8cm）
kb.draw_hexa(7)      # 正六角形（一辺7cm）
kb.draw_star(10)     # 星形（一辺10cm）
```

#### 円形図形
```python
# 円
kb.draw_circle(6)    # 円（半径6cm）

# 半円
kb.draw_semicircle(5, side='l')  # 左半円（半径5cm）
kb.draw_semicircle(5, side='r')  # 右半円

# 円弧（時間制限付き）
kb.draw_arc(8, time=2)  # 半径8cm、2秒間の円弧
```

### メロディ再生

#### 音の再生
```python
# 特定の音階と時間で再生
kb.melody(scale=60, sec=1)  # 音階60、1秒再生
kb.melody(scale=45, sec=2)  # 音階45、2秒再生

# 簡単なビープ音
kb.beep()  # 短いビープ音

# メロディシーケンス例
melody_sequence = [
    (60, 1), (62, 1), (64, 1), (65, 1),
    (67, 1), (69, 1), (71, 1), (72, 2)
]

for scale, duration in melody_sequence:
    kb.melody(scale=scale, sec=duration)
    kb.delay(0.1)  # 音符間の間隔
```

## サンプルコード

### 基本移動パターン
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5", verbose=False)
kb.init()

try:
    # 正方形描画（ラインマップボード）
    for i in range(4):
        kb.move_forward(2, opt="-l")
        kb.turn_right(opt="-l")
        kb.delay(0.5)
    
    # LED色変更
    colors = [0, 1, 2, 3, 4, 5, 6, 7]
    for color in colors:
        kb.turn_led_idx(color)
        kb.delay(0.5)
        
finally:
    kb.close()
```

### センサーベース障害物回避
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5", verbose=False)
kb.init()

try:
    while True:
        # 物体検出
        left_obj, right_obj = kb.get_object_detect(True)
        
        if left_obj > 50 or right_obj > 50:
            # 障害物検出時
            kb.stop()
            kb.turn_led_idx(0)  # 赤LED
            kb.beep()
            
            # 回避動作
            kb.move_backward_unit(5, opt="-l", speed=50)
            kb.turn_right(opt="-l")
            kb.delay(1)
        else:
            # 前進
            kb.turn_led_idx(3)  # 緑LED
            kb.move_forward_unit(5, opt="-l", speed=70)
            
        kb.delay(0.1)
        
except KeyboardInterrupt:
    print("プログラム中断")
finally:
    kb.close()
```

### ライントレース
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5", verbose=False)
kb.init()

try:
    while True:
        # ラインセンサー読み取り
        left, center, right = kb.get_line_sensor(True)
        
        if center > 100:  # 中央にライン
            kb.go_forward_speed(100, 100)
            kb.turn_led_idx(3)  # 緑
        elif left > 100:  # 左にライン
            kb.go_forward_speed(50, 120)  # 左カーブ
            kb.turn_led_idx(4)  # 青
        elif right > 100:  # 右にライン
            kb.go_forward_speed(120, 50)  # 右カーブ
            kb.turn_led_idx(6)  # 紫
        else:  # ラインなし
            kb.stop()
            kb.turn_led_idx(0)  # 赤
            
        kb.delay(0.05)
        
except KeyboardInterrupt:
    print("プログラム中断")
finally:
    kb.close()
```

### 色反応ロボット
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5", verbose=False)
kb.init()

try:
    while True:
        color = kb.get_color_sensor(True)
        
        if color == 1:  # 赤検出（例）
            kb.turn_led_idx(0)  # 赤LED
            kb.melody(scale=60, sec=1)
            kb.turn_left(opt="-l")
        elif color == 2:  # 緑検出（例）
            kb.turn_led_idx(3)  # 緑LED
            kb.melody(scale=65, sec=1)
            kb.move_forward(1, opt="-l")
        elif color == 3:  # 青検出（例）
            kb.turn_led_idx(4)  # 青LED
            kb.melody(scale=72, sec=1)
            kb.turn_right(opt="-l")
        else:
            kb.turn_led_idx(7)  # 白LED
            
        kb.delay(0.5)
        
except KeyboardInterrupt:
    print("プログラム中断")
finally:
    kb.close()
```

### 図形描画デモ
```python
from kamibotpi import KamibotPi

kb = KamibotPi(port="COM5", verbose=False)
kb.init()

try:
    shapes = [
        ("三角形", lambda: kb.draw_tri(10)),
        ("四角形", lambda: kb.draw_rect(10)),
        ("五角形", lambda: kb.draw_penta(8)),
        ("六角形", lambda: kb.draw_hexa(8)),
        ("円", lambda: kb.draw_circle(6)),
        ("星", lambda: kb.draw_star(8))
    ]
    
    for name, draw_func in shapes:
        print(f"{name}描画開始")
        kb.turn_led_idx(shapes.index((name, draw_func)))
        kb.beep()
        draw_func()
        kb.delay(2)
        
    print("全図形描画完了")
    
finally:
    kb.close()
```

## トラブルシューティング

### よくある問題

#### 1. 接続エラー
```
serial.SerialException: could not open port 'COM5'
```
**解決策**：
- ポート名を確認（Windows：デバイスマネージャー、Linux：`ls /dev/tty*`）
- 他のプログラムがポートを使用していないか確認
- ケーブル接続状態を確認

#### 2. タイムアウトエラー
**症状**：コマンド送信後応答がない
**解決策**：
- `timeout`値を増やす（例：`timeout=5`）
- ボーレートを確認（デフォルト：57600）
- ハードウェアの電源状態を確認

#### 3. 移動が不正確
**解決策**：
- バッテリー残量確認：`kb.get_battery()`
- 床面状態確認（滑り防止）
- モーター速度調整

#### 4. センサー値が異常
**解決策**：
- センサー表面の清掃
- 照明環境の確認（色彩・ラインセンサー）
- 閾値の再調整

### デバッグのコツ

#### 1. Verboseモードの使用
```python
kb = KamibotPi(port="COM5", verbose=True)  # デバッグ出力有効化
```

#### 2. センサー値の監視
```python
while True:
    left_obj, right_obj = kb.get_object_detect(True)
    left_line, center_line, right_line = kb.get_line_sensor(True)
    color = kb.get_color_sensor(True)
    battery = kb.get_battery()
    
    print(f"物体：L={left_obj}、R={right_obj}")
    print(f"ライン：L={left_line}、C={center_line}、R={right_line}")
    print(f"色：{color}、バッテリー：{battery}")
    print("-" * 40)
    
    kb.delay(1)
```

#### 3. 段階別テスト
```python
# 1. 基本接続テスト
kb = KamibotPi(port="COM5", verbose=True)
kb.init()
print("接続成功")

# 2. LEDテスト
kb.turn_led_idx(0)
kb.delay(1)

# 3. 音テスト
kb.beep()

# 4. 簡単な移動テスト
kb.move_forward_unit(5, opt="-l", speed=50)

# 5. センサーテスト
print(kb.get_battery())
```

### パフォーマンス最適化

#### 1. コマンド間の適切な遅延
```python
kb.move_forward(1, opt="-l")
kb.delay(0.1)  # コマンド処理時間確保
kb.turn_left(opt="-l")
```

#### 2. センサーポーリング周期の調整
```python
# 速すぎるポーリングは避ける
while True:
    sensor_data = kb.get_line_sensor(True)
    # 処理ロジック
    kb.delay(0.05)  # 適切な間隔維持
```

#### 3. バッテリー管理
```python
def check_battery(kb):
    battery = kb.get_battery()
    if battery < 20:  # 閾値
        print("バッテリー不足！プログラム終了")
        kb.turn_led_idx(0)  # 赤LED警告
        return False
    return True

# 定期的なバッテリー確認
if not check_battery(kb):
    kb.close()
```

### 安全使用ガイドライン

1. **電源管理**：使用前に十分なバッテリーを確認
2. **動作空間**：ロボットが動く十分なスペースを確保
3. **緊急停止**：`Ctrl+C`でプログラム中断可能
4. **プログラム終了**：必ず`kb.close()`を呼び出し（またはtry-finallyを使用）
5. **センサー清潔性**：定期的なセンサー清掃で精度維持

このマニュアルを参考にして、KamibotPiを安全かつ効果的にご活用ください！
