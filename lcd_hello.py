#!/usr/bin/env python3
"""
LCD1602 最小サンプルコード（PCF8574T対応）
入門者向けの最もシンプルな実装例

使用方法:
    python3 lcd_hello.py

事前準備:
    1. I²Cを有効化: sudo raspi-config → Interface Options → I2C → Enable
    2. I²Cアドレスを確認: i2cdetect -y 1
    3. 必要に応じて下記のI2C_ADDRを変更
"""

from RPLCD.i2c import CharLCD

# ====================================
# 環境に合わせて変更してください
# ====================================
I2C_ADDR = 0x27   # i2cdetectで見つかった値（通常0x27または0x3F）
I2C_PORT = 1      # Raspberry PiのI²Cバス番号（通常1）

# ====================================
# LCDの初期化（PCF8574T対応）
# ====================================
lcd = CharLCD(
    i2c_expander='PCF8574',  # PCF8574TもこのexpanderでOK
    address=I2C_ADDR,
    port=I2C_PORT,
    cols=16, rows=2,         # 16文字×2行
    charmap='A02',           # 文字化け時は'A00'に変更
    auto_linebreaks=True
)

# ====================================
# 画面をクリアして文字を表示
# ====================================
lcd.clear()
lcd.write_string('Hello, world!\nRaspberry Pi')

print("LCD表示完了!")
print("プログラムは終了しますが、表示は保持されます")

# 注意: lcd.close()を呼ぶと表示が消える場合があるため、ここでは呼ばない
