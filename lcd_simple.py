#!/usr/bin/env python3
"""
LCD1602 超シンプル固定表示サンプル
最小限のコードで固定テキストを表示する入門用プログラム

このプログラムは:
- クラスや関数を使わず、最小限のコードで実装
- 固定メッセージを2行表示するだけのシンプル設計
- 初心者がLCD制御の基本を理解するための教材

使用方法:
    python3 lcd_simple.py
"""

from RPLCD.i2c import CharLCD

# ==========================================
# 設定（環境に合わせて変更してください）
# ==========================================
I2C_ADDR = 0x27   # LCDのI²Cアドレス（i2cdetect -y 1で確認）
I2C_PORT = 1      # I²Cポート番号（Raspberry Piは通常1）

# ==========================================
# 表示するメッセージ
# ==========================================
LINE1_TEXT = "Hello, World!"    # 1行目に表示する文字列（16文字まで）
LINE2_TEXT = "Raspberry Pi"     # 2行目に表示する文字列（16文字まで）

# ==========================================
# メイン処理
# ==========================================

# LCDを初期化
lcd = CharLCD(
    i2c_expander='PCF8574',
    address=I2C_ADDR,
    port=I2C_PORT,
    cols=16,
    rows=2,
    charmap='A02',
    auto_linebreaks=True
)

# 画面をクリア
lcd.clear()

# 1行目を表示（カーソル位置を0行0列に設定）
lcd.cursor_pos = (0, 0)
lcd.write_string(LINE1_TEXT)

# 2行目を表示（カーソル位置を1行0列に設定）
lcd.cursor_pos = (1, 0)
lcd.write_string(LINE2_TEXT)

# 完了メッセージ
print("=" * 40)
print("LCD表示完了!")
print("-" * 40)
print(f"1行目: {LINE1_TEXT}")
print(f"2行目: {LINE2_TEXT}")
print("=" * 40)
print("\nプログラムは終了しますが、LCDの表示は保持されます。")
