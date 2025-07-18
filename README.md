# LCD1602 Display Application

A Python application for controlling LCD1602 displays via I²C communication on Raspberry Pi. This project serves as educational material for beginners learning I²C communication protocols and LCD control.

## Features

- ✨ Simple text display on LCD1602 (16x2 characters)
- 🔄 Horizontal scrolling for long text
- 📍 Line selection (Line 1 or Line 2)
- 🧹 Screen clear functionality
- 🔧 I²C address configuration
- 🧪 Built-in test mode
- 📚 Beginner-friendly with comprehensive Japanese comments

## Hardware Requirements

- Raspberry Pi 5 (or compatible models)
- LCD1602 display module with I²C backpack
- Jumper wires (Male-Male)
- 10kΩ potentiometer (for contrast adjustment)
- Breadboard
- 5V power supply (official Raspberry Pi adapter recommended)

## Software Requirements

- **OS**: Raspberry Pi OS (latest recommended)
- **Python**: 3.9 or higher
- **Libraries**: See `requirements.txt`

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Murasan201/06-002-lcd1602-display.git
   cd 06-002-lcd1602-display
   ```

2. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Enable I²C on Raspberry Pi:**
   ```bash
   sudo raspi-config
   # Navigate to Interface Options → I2C → Enable
   ```

4. **Verify I²C connection:**
   ```bash
   sudo i2cdetect -y 1
   ```

## Hardware Setup

### I²C Connection (Default)

| LCD1602 I²C Module | Raspberry Pi 5 |
|-------------------|----------------|
| VCC               | 5V (Pin 2)     |
| GND               | GND (Pin 6)    |
| SDA               | SDA (Pin 3)    |
| SCL               | SCL (Pin 5)    |

### Contrast Adjustment

Connect a 10kΩ potentiometer to the V0 pin of the LCD module for contrast adjustment.

## Usage

### Basic Usage

```bash
# Display text on line 1
python3 lcd_display.py "Hello World"

# Display text on line 2
python3 lcd_display.py "Hello Pi" --line 2

# Enable scrolling for long text
python3 lcd_display.py "This is a very long message that will scroll" --scroll

# Clear the display
python3 lcd_display.py --clear

# Run test mode
python3 lcd_display.py --test
```

### Advanced Options

```bash
# Specify I²C address (if different from default 0x27)
python3 lcd_display.py "Hello" --address 0x3F

# Specify I²C port (if different from default 1)
python3 lcd_display.py "Hello" --port 0

# Display help
python3 lcd_display.py --help
```

## Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `text` | Text string to display | - |
| `--line` | Display line (1 or 2) | 1 |
| `--scroll` | Enable scrolling for long text | False |
| `--address` | I²C address (hex format) | 0x27 |
| `--port` | I²C port number | 1 |
| `--clear` | Clear display and exit | False |
| `--test` | Run test display sequence | False |

## Safety Considerations

⚠️ **Important Safety Guidelines:**

1. **Power Off**: Always power off your Raspberry Pi before connecting/disconnecting hardware
2. **Correct Wiring**: Double-check all connections before powering on
3. **Voltage Levels**: Ensure proper voltage levels (3.3V for GPIO, 5V for LCD power)
4. **I²C Address**: Verify the correct I²C address using `i2cdetect` before running the application
5. **Contrast Adjustment**: Adjust the potentiometer carefully to avoid damaging the display

## Troubleshooting

### Common Issues

1. **"LCD initialization error"**
   - Check I²C wiring connections
   - Verify I²C is enabled: `sudo raspi-config`
   - Check I²C address: `sudo i2cdetect -y 1`

2. **"Permission denied"**
   - Run with proper permissions: `sudo python3 lcd_display.py`
   - Add user to i2c group: `sudo usermod -a -G i2c $USER`

3. **"Module not found" error**
   - Install requirements: `pip3 install -r requirements.txt`
   - Check Python version: `python3 --version`

4. **Display shows garbled characters**
   - Adjust contrast using the potentiometer
   - Check power supply stability
   - Verify wiring connections

5. **No display output**
   - Check LCD power connections (VCC, GND)
   - Verify I²C communication with `i2cdetect`
   - Try different I²C address (0x27 or 0x3F)

### Testing I²C Connection

```bash
# Scan for I²C devices
sudo i2cdetect -y 1

# Expected output should show device at address 0x27 or 0x3F
#      0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
# 00:          -- -- -- -- -- -- -- -- -- -- -- -- --
# 10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 20: -- -- -- -- -- -- -- 27 -- -- -- -- -- -- -- --
# 30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
```

## Project Structure

```
06-002-lcd1602-display/
├── lcd_display.py                    # Main application
├── requirements.txt                  # Python dependencies
├── README.md                        # This file
├── LICENSE                          # License file
├── CLAUDE.md                        # Project rules and guidelines
└── 06-002_LCD文字表示アプリ_要件定義書.md  # Requirements specification (Japanese)
```

## Educational Goals

This project is designed to teach:

- I²C communication protocol fundamentals
- LCD1602 module control techniques
- Python hardware interface programming
- Error handling in embedded applications
- Command-line argument processing

## Contributing

This is an educational project. Feel free to:

- Report issues or bugs
- Suggest improvements for beginners
- Add support for other LCD modules
- Improve documentation

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## References

- [RPLCD Library Documentation](https://rplcd.readthedocs.io/)
- [Raspberry Pi I²C Documentation](https://www.raspberrypi.org/documentation/hardware/raspberrypi/i2c/)
- [LCD1602 Datasheet](https://www.sparkfun.com/datasheets/LCD/HD44780.pdf)

---

**Document ID**: 06-002  
**Target Audience**: Programming beginners, Raspberry Pi enthusiasts, Electronics learners  
**Difficulty Level**: Beginner to Intermediate  
**Last Updated**: July 2025