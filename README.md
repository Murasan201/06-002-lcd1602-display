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
- LCD1602 display module with I²C backpack (PCF8574/PCF8574T)
- Jumper wires (Male-Male)
- 10kΩ potentiometer (for contrast adjustment, if not integrated on the module)
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

2. **Create and activate a virtual environment (Recommended):**

   ⚠️ **Important**: Raspberry Pi OS (Bookworm and later) requires using a virtual environment for Python package installation to protect the system Python environment.

   ```bash
   # Create virtual environment
   python3 -m venv venv

   # Activate virtual environment
   source venv/bin/activate
   ```

   **Note**: You need to activate the virtual environment every time you open a new terminal session:
   ```bash
   source venv/bin/activate
   ```

   To deactivate when done:
   ```bash
   deactivate
   ```

3. **Install dependencies:**
   ```bash
   # Make sure virtual environment is activated first
   pip install -r requirements.txt
   ```

   **Alternative (Not Recommended)**: If you choose not to use a virtual environment, you can install system-wide with:
   ```bash
   pip3 install -r requirements.txt --break-system-packages
   ```

4. **Enable I²C on Raspberry Pi:**
   ```bash
   sudo raspi-config
   # Navigate to Interface Options → I2C → Enable
   ```

5. **Verify I²C connection:**
   ```bash
   sudo i2cdetect -y 1
   ```

## Hardware Setup

### I²C Connection (Default)

| LCD1602 I²C Module | Raspberry Pi 5 |
|-------------------|----------------|
| VCC               | 5V (Pin 2) or 3.3V (Pin 1)* |
| GND               | GND (Pin 6)    |
| SDA               | SDA (Pin 3)    |
| SCL               | SCL (Pin 5)    |

**Important Voltage Level Notes:**

⚠️ **Critical: I²C Voltage Compatibility**

- Raspberry Pi I²C bus operates at **3.3V logic level**
- Many PCF8574 modules have pull-up resistors connected to VCC
- **Safe Options:**
  1. **Recommended for beginners**: Power PCF8574 module with **3.3V** (Pin 1). Most PCF8574/PCF8574T chips support 2.5V-6V operation.
  2. **Advanced option**: Use 5V power with a **logic level converter** to protect Raspberry Pi GPIO pins from 5V signals on I²C lines.

- **Never** connect 5V-pulled I²C lines directly to Raspberry Pi GPIO without level conversion
- LCD backlight may be dimmer at 3.3V but is safer for direct connection
- Some modules have separate power pins for logic and backlight - check your module datasheet

### Contrast Adjustment

Most I²C modules have an integrated potentiometer on the backpack board. Rotate the potentiometer with a small screwdriver until characters are clearly visible. If your module doesn't have one, connect a 10kΩ potentiometer to the V0 pin.

## Usage

### Quick Start (Beginner Example)

⚠️ **Important**: Always activate the virtual environment before running Python scripts:
```bash
source venv/bin/activate
```

#### Ultra-Simple Fixed Display (`lcd_simple.py`)
The absolute minimum code to display fixed text - perfect for first-time users:
```bash
# Activate virtual environment first
source venv/bin/activate

# Edit lcd_simple.py to change LINE1_TEXT and LINE2_TEXT if desired
python lcd_simple.py
```
**Best for**: First-time users who want to see results immediately with minimal configuration

### Basic Usage (Full Application)

**Note**: Make sure to activate the virtual environment first!

```bash
# Activate virtual environment
source venv/bin/activate

# Run test mode (recommended for first run)
python lcd_display.py --test

# Display text on line 1
python lcd_display.py "Hello World"

# Display text on line 2
python lcd_display.py "Hello Pi" --line 2

# Enable scrolling for long text
python lcd_display.py "This is a very long message that will scroll" --scroll

# Clear the display
python lcd_display.py --clear
```

### Advanced Options

```bash
# Activate virtual environment first
source venv/bin/activate

# Specify I²C address (if different from default 0x27)
python lcd_display.py "Hello" --address 0x3F

# Specify I²C port (if different from default 1)
python lcd_display.py "Hello" --port 0

# Change character map if characters appear garbled
python lcd_display.py "Hello" --charmap A00

# Display help
python lcd_display.py --help
```

## Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `text` | Text string to display | - |
| `--line` | Display line (1 or 2) | 1 |
| `--scroll` | Enable scrolling for long text | False |
| `--address` | I²C address (hex format) | 0x27 |
| `--port` | I²C port number | 1 |
| `--charmap` | Character map (A02 or A00) | A02 |
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

📋 **For detailed troubleshooting information, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md)**

### Common Issues

1. **"LCD initialization error"**
   - Check I²C wiring connections
   - Verify I²C is enabled: `sudo raspi-config`
   - Check I²C address: `sudo i2cdetect -y 1`
   - Ensure proper voltage level (3.3V recommended for direct connection)

2. **"Permission denied"**
   - Run with proper permissions: `sudo python3 lcd_display.py`
   - Add user to i2c group: `sudo usermod -a -G i2c $USER`

3. **"Module not found" error**
   - Make sure virtual environment is activated: `source venv/bin/activate`
   - Install requirements: `pip install -r requirements.txt`
   - Check Python version: `python3 --version`
   - See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for detailed solutions

4. **Display shows garbled characters**
   - **First try**: Change character map with `--charmap A00`
   - Adjust contrast using the potentiometer on the I²C backpack
   - Check power supply stability
   - Verify wiring connections

5. **No display output**
   - Check LCD power connections (VCC, GND)
   - Verify I²C communication with `i2cdetect`
   - Try different I²C address (0x27 or 0x3F)
   - Verify voltage level is appropriate for your module

6. **Backlight is off**
   - Some modules have inverted backlight logic
   - The software enables backlight by default
   - Check if your module has a backlight jumper

7. **Program exits immediately / Display disappears**
   - Make sure you're providing arguments to `lcd_display.py`
   - Try test mode first: `python lcd_display.py --test`
   - The display should persist after program exits
   - See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for detailed solution

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
├── lcd_display.py                    # Main application (full-featured with scrolling)
├── lcd_simple.py                     # Ultra-simple fixed display (beginner-friendly)
├── requirements.txt                  # Python dependencies
├── README.md                        # This file (English)
├── TROUBLESHOOTING.md               # Troubleshooting guide
├── LICENSE                          # License file
├── CLAUDE.md                        # Project rules and guidelines
├── .gitignore                       # Git ignore file (excludes venv/)
├── venv/                            # Virtual environment (not tracked in git)
└── 06-002_LCD文字表示アプリ_要件定義書.md  # Requirements specification (Japanese)
```

### File Comparison

| File | Complexity | Features | Best For |
|------|------------|----------|----------|
| `lcd_simple.py` | ⭐ Very Simple | Fixed 2-line display only | Absolute beginners, quick testing |
| `lcd_display.py` | ⭐⭐⭐⭐ Advanced | Full features: scrolling, line selection, test mode, CLI args | Production use, advanced features |

## Learning Path

### Recommended Order for Beginners

1. **Start with `lcd_simple.py`**
   - Understand the minimal code structure
   - Learn basic I²C configuration
   - See immediate results with fixed text display
   - Perfect for first-time hardware interface programming

2. **Explore `lcd_display.py`**
   - Advanced features (scrolling, command-line arguments)
   - Comprehensive error handling
   - Test mode for debugging
   - Real-world application structure
   - Production-ready code patterns

3. **Read the source code**
   - Both files include detailed Japanese comments
   - Understand cursor positioning, text display, and I²C communication
   - Learn best practices for hardware control applications

## Educational Goals

This project is designed to teach:

- I²C communication protocol fundamentals
- LCD1602 module control techniques with PCF8574T expander
- Python hardware interface programming
- Error handling in embedded applications
- Command-line argument processing
- Voltage level shifting for safe GPIO operation

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
**Last Updated**: October 25, 2025