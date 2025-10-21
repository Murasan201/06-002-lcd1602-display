#!/usr/bin/env python3
"""
LCD1602 初心者向け詳細コメント版
各行の処理を詳しく説明したサンプルコード

学習目的:
- I²C通信の基礎
- LCDの初期化方法
- カーソル位置の制御
- 文字列の表示方法

使用方法:
    python3 lcd_beginner.py
"""

# RPLCDライブラリから、I²C接続用のCharLCDクラスをインポート
from RPLCD.i2c import CharLCD

# ==========================================
# I²C設定
# ==========================================

# LCDモジュールのI²Cアドレス
# i2cdetect -y 1 コマンドで確認できます
# 一般的には 0x27 または 0x3F が使われます
I2C_ADDR = 0x27

# Raspberry PiのI²Cバス番号
# Raspberry Pi 2/3/4/5 では通常 1 を使用
# Raspberry Pi 1 の一部モデルでは 0 の場合もあります
I2C_PORT = 1

# ==========================================
# 表示メッセージ設定
# ==========================================

# 1行目に表示する文字列（最大16文字）
MESSAGE_LINE1 = "Hello, World!"

# 2行目に表示する文字列（最大16文字）
MESSAGE_LINE2 = "LCD1602 Test"

# ==========================================
# LCDの初期化
# ==========================================

# CharLCDオブジェクトを作成してLCDを初期化
lcd = CharLCD(
    # PCF8574系のI²Cエクスパンダを使用
    # PCF8574TもPCF8574も同じ'PCF8574'を指定
    i2c_expander='PCF8574',

    # I²Cアドレスを指定
    address=I2C_ADDR,

    # I²Cポート番号を指定
    port=I2C_PORT,

    # LCDの列数（1行の文字数）
    cols=16,

    # LCDの行数
    rows=2,

    # 文字マップの種類
    # 'A02': 一般的な文字セット（デフォルト）
    # 'A00': 文字化けする場合に試す
    charmap='A02',

    # 自動改行を有効化
    # Trueにすると\nで改行できる
    auto_linebreaks=True
)

# ==========================================
# LCD表示処理
# ==========================================

# 画面をクリア（以前の表示を消去）
lcd.clear()

# 1行目に文字を表示
# cursor_pos = (行, 列) で位置を指定（0始まり）
# (0, 0) は1行目の先頭を意味する
lcd.cursor_pos = (0, 0)
lcd.write_string(MESSAGE_LINE1)

# 2行目に文字を表示
# (1, 0) は2行目の先頭を意味する
lcd.cursor_pos = (1, 0)
lcd.write_string(MESSAGE_LINE2)

# ==========================================
# 完了メッセージ表示
# ==========================================

print("=" * 50)
print("  LCD1602 表示完了")
print("=" * 50)
print(f"  I²Cアドレス: 0x{I2C_ADDR:02X}")
print(f"  I²Cポート  : {I2C_PORT}")
print("-" * 50)
print(f"  1行目: {MESSAGE_LINE1}")
print(f"  2行目: {MESSAGE_LINE2}")
print("=" * 50)
print("\n【注意】")
print("  プログラムは終了しますが、LCDの表示は保持されます。")
print("  表示を消したい場合は、以下のコマンドを実行してください:")
print("  python3 lcd_display.py --clear")
print()
