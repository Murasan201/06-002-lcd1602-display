#!/usr/bin/env python3
"""
LCD文字表示アプリ
LCD1602モジュールに文字列を表示するPythonアプリケーション
要件定義書: 06-002_LCD文字表示アプリ_要件定義書.md
"""

import argparse
import time
import sys
from RPLCD.i2c import CharLCD

class LCDDisplay:
    """
    LCD1602ディスプレイを制御するクラス
    初心者向けに機能を整理し、簡潔な実装にしています
    """
    
    def __init__(self, i2c_address=0x27, i2c_port=1, charmap='A02'):
        """
        LCDディスプレイの初期化

        Args:
            i2c_address (int): I²Cアドレス（通常0x27または0x3F）
            i2c_port (int): I²Cポート番号（Raspberry Pi 5では通常1）
            charmap (str): 文字マップ（'A02'または'A00'、文字化け時は切り替え）
        """
        try:
            # RPLCDライブラリを使用してPCF8574T搭載のI²C接続LCDを初期化
            # PCF8574TはPCF8574の低電圧版で、指定は'PCF8574'でOK
            self.lcd = CharLCD(
                i2c_expander='PCF8574',  # PCF8574Tもこの指定で動作
                address=i2c_address,
                port=i2c_port,
                cols=16, rows=2,
                charmap=charmap,         # 文字化け時はA00に変更
                auto_linebreaks=True
            )
            # バックライトを明示的に有効化（一部基板で必要）
            self.lcd.backlight_enabled = True
            print(f"LCD初期化完了: I²Cアドレス 0x{i2c_address:02X}, charmap={charmap}")
        except Exception as e:
            print(f"LCD初期化エラー: {e}")
            print("接続とI²Cアドレスを確認してください")
            print("ヒント: i2cdetect -y 1 でアドレスを確認")
            sys.exit(1)
    
    def clear_display(self):
        """
        画面をクリアする
        """
        try:
            self.lcd.clear()
            print("画面をクリアしました")
        except Exception as e:
            print(f"画面クリアエラー: {e}")
    
    def display_text(self, text, line=1):
        """
        指定した行に文字列を表示する

        Args:
            text (str): 表示する文字列
            line (int): 表示行（1または2）
        """
        try:
            # 行の指定（1行目: (0,0), 2行目: (1,0)）
            if line == 1:
                self.lcd.cursor_pos = (0, 0)
            elif line == 2:
                self.lcd.cursor_pos = (1, 0)
            else:
                print("エラー: 行は1または2を指定してください")
                return

            # 16文字以内の場合はそのまま表示
            if len(text) <= 16:
                # 行をクリアしてから表示（古い文字を消すため）
                self.lcd.write_string(' ' * 16)  # スペース16個で行全体をクリア
                self.lcd.cursor_pos = (line - 1, 0)
                self.lcd.write_string(text)
                print(f"第{line}行に表示: {text}")
            else:
                # 16文字を超える場合はスクロール表示
                self.scroll_text(text, line)

        except Exception as e:
            print(f"文字表示エラー: {e}")
    
    def scroll_text(self, text, line=1, scroll_delay=0.3):
        """
        長い文字列をスクロール表示する

        Args:
            text (str): 表示する文字列
            line (int): 表示行（1または2）
            scroll_delay (float): スクロール間隔（秒）
        """
        try:
            print(f"第{line}行でスクロール表示開始: {text}")

            # 文字列の末尾にスペースを追加してループしやすくする
            scroll_text = text + "    "

            # スクロール表示（文字列を一周表示）
            for i in range(len(scroll_text)):
                # 表示する16文字の部分を取得
                display_part = scroll_text[i:i+16]

                # 16文字に満たない場合は先頭から補完（ループ表示のため）
                if len(display_part) < 16:
                    display_part += scroll_text[:16-len(display_part)]

                # 指定行に表示（1行目: (0,0), 2行目: (1,0)）
                if line == 1:
                    self.lcd.cursor_pos = (0, 0)
                else:
                    self.lcd.cursor_pos = (1, 0)

                self.lcd.write_string(display_part)
                time.sleep(scroll_delay)

            print("スクロール表示完了")

        except Exception as e:
            print(f"スクロール表示エラー: {e}")
    
    def close(self):
        """
        LCDリソースをクリーンアップする

        注意: lcd.close()を呼ぶと表示が消える場合があるため、
        このメソッドでは何もしません。表示は保持されます。
        """
        # lcd.close()を呼ぶと表示が消えるため、意図的に呼ばない
        print("LCD表示を保持したまま終了します")

def main():
    """
    メイン関数：コマンドライン引数を処理してLCD表示を実行
    """
    # ==========================================
    # コマンドライン引数の設定
    # ==========================================
    parser = argparse.ArgumentParser(
        description="LCD1602文字表示アプリ - Raspberry Pi用",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  python3 lcd_display.py "Hello World"           # 1行目に表示
  python3 lcd_display.py "Hello" --line 2        # 2行目に表示
  python3 lcd_display.py "Very long text message" --scroll  # スクロール表示
  python3 lcd_display.py --clear                 # 画面クリア
  python3 lcd_display.py --test                  # テスト表示
        """
    )

    # 引数の定義
    parser.add_argument('text', nargs='?', default='',
                       help='表示する文字列')
    parser.add_argument('--line', type=int, choices=[1, 2], default=1,
                       help='表示行を指定 (1または2、デフォルト: 1)')
    parser.add_argument('--scroll', action='store_true',
                       help='16文字を超える場合のスクロール表示を有効化')
    parser.add_argument('--address', type=str, default='0x27',
                       help='I²Cアドレス (デフォルト: 0x27)')
    parser.add_argument('--port', type=int, default=1,
                       help='I²Cポート番号 (デフォルト: 1)')
    parser.add_argument('--charmap', type=str, choices=['A00', 'A02'], default='A02',
                       help='文字マップ (デフォルト: A02、文字化け時はA00)')
    parser.add_argument('--clear', action='store_true',
                       help='画面をクリアして終了')
    parser.add_argument('--test', action='store_true',
                       help='テスト表示を実行')
    
    args = parser.parse_args()

    # ==========================================
    # I²Cアドレスの変換（文字列から整数へ）
    # ==========================================
    try:
        if args.address.startswith('0x'):
            i2c_addr = int(args.address, 16)  # 16進数として変換（例: "0x27" → 39）
        else:
            i2c_addr = int(args.address)      # 10進数として変換
    except ValueError:
        print(f"エラー: 無効なI²Cアドレス '{args.address}'")
        sys.exit(1)

    # ==========================================
    # LCDディスプレイの初期化
    # ==========================================
    lcd_display = LCDDisplay(i2c_address=i2c_addr, i2c_port=args.port, charmap=args.charmap)

    try:
        # ==========================================
        # 実行モードに応じた処理
        # ==========================================
        if args.clear:
            # 画面クリアモード
            lcd_display.clear_display()
        
        elif args.test:
            # テストモード（動作確認用の表示シーケンスを実行）
            print("テスト表示を開始します...")
            lcd_display.clear_display()
            time.sleep(1)

            # 1行目にテスト文字列
            lcd_display.display_text("LCD Test Line 1", 1)
            time.sleep(2)

            # 2行目にテスト文字列
            lcd_display.display_text("LCD Test Line 2", 2)
            time.sleep(2)

            # スクロールテスト（長い文字列の表示確認）
            lcd_display.display_text("This is a very long scrolling message for testing", 1)
            time.sleep(1)

            print("テスト表示完了")
        
        elif args.text:
            # 通常の文字表示モード
            if args.scroll or len(args.text) > 16:
                # スクロール表示（16文字を超える場合または--scrollオプション指定時）
                lcd_display.scroll_text(args.text, args.line)
            else:
                # 通常表示（16文字以内の場合）
                lcd_display.display_text(args.text, args.line)
        else:
            # 引数なしの場合はヘルプを表示
            print("エラー: 表示するテキストが指定されていません\n")
            parser.print_help()
            print("\nヒント: テストモードを試してください:")
            print("  python3 lcd_display.py --test")
    
    except KeyboardInterrupt:
        print("\n\n割り込み信号を受信しました。終了処理を実行中...")

    except Exception as e:
        print(f"実行エラー: {e}")

    finally:
        # ==========================================
        # リソースのクリーンアップ（終了処理）
        # ==========================================
        # 必ずリソースをクリーンアップ（例外発生時も実行される）
        lcd_display.close()
        print("アプリケーションを終了しました")

if __name__ == "__main__":
    main()