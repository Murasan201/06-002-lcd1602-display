# Troubleshooting Guide

This document contains common issues encountered during development and their solutions.

---

## Table of Contents
- [Installation Issues](#installation-issues)
- [Runtime Errors](#runtime-errors)
- [Hardware Issues](#hardware-issues)

---

## Installation Issues

### Error: ModuleNotFoundError: No module named 'RPLCD'

**Error Details:**
```
Traceback (most recent call last):
  File "/home/pi/work/project/06-002-lcd1602-display/lcd_simple.py", line 15, in <module>
    from RPLCD.i2c import CharLCD
ModuleNotFoundError: No module named 'RPLCD'
```

**Cause:**
Required Python packages (RPLCD and smbus2) are not installed.

**Solution:**
Install the required dependencies using pip:
```bash
pip3 install -r requirements.txt
```

Or install packages individually:
```bash
pip3 install RPLCD>=1.3.0
pip3 install smbus2>=0.4.0
```

**Status:** ✅ Resolved (use virtual environment)

---

### Error: externally-managed-environment

**Error Details:**
```
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
```

**Cause:**
Raspberry Pi OS (Bookworm and later) uses PEP 668 to protect the system Python environment from accidental modifications. Direct installation with pip3 is blocked to prevent system instability.

**Solution (Recommended - Use Virtual Environment):**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install packages
pip install -r requirements.txt

# Run your script
python lcd_simple.py

# Deactivate when done
deactivate
```

**Alternative Solution (Not Recommended):**
```bash
# Override protection (may break system packages)
pip3 install -r requirements.txt --break-system-packages
```

**Alternative Solution (Using apt):**
```bash
# Install via system package manager (if available)
sudo apt install python3-rplcd python3-smbus2
```

**Status:** ✅ Resolved

**Resolution Steps Taken:**
1. Created virtual environment: `python3 -m venv venv`
2. Activated virtual environment: `source venv/bin/activate`
3. Installed packages: `pip install -r requirements.txt`
4. Successfully installed RPLCD-1.4.0 and smbus2-0.5.0
5. Executed lcd_simple.py successfully without errors

---

## Runtime Errors

### Issue: lcd_display.py exits immediately without displaying anything

**Symptoms:**
- Application starts and exits immediately
- No text appears on LCD display
- Display may flash or briefly show text then disappear

**Cause:**
Two issues were identified:
1. **No arguments provided**: Running `python lcd_display.py` without arguments only shows help and exits without displaying anything on the LCD
2. **lcd.close() clearing display**: The `close()` method was calling `lcd.close()`, which clears the LCD display before the user can see it

**Solution:**

The code has been fixed with the following changes:

1. **Modified close() method** (lcd_display.py:128-136):
   - Removed `lcd.close()` call to preserve display
   - Added comment explaining why close is not called
   - Display now persists after program exits

2. **Improved error messaging** (lcd_display.py:224-228):
   - Added clear error message when no arguments provided
   - Added helpful hint to try test mode

**How to use lcd_display.py correctly:**

```bash
# Activate virtual environment first
source venv/bin/activate

# Test mode (recommended for first run)
python lcd_display.py --test

# Display text on line 1
python lcd_display.py "Hello, World!"

# Display text on line 2
python lcd_display.py "Hello" --line 2

# Scroll long text
python lcd_display.py "This is a very long message" --scroll

# Clear display
python lcd_display.py --clear
```

**Status:** ✅ Resolved

**Changes Made:**
- Modified `close()` method to not call `lcd.close()` (preserves display)
- Added error message for missing arguments
- Added hint to use `--test` mode

---

## Hardware Issues

*No hardware issues recorded yet.*

---

## General Troubleshooting Steps

1. **Check I²C is enabled:**
   ```bash
   sudo raspi-config
   # Navigate to: Interface Options → I2C → Enable
   ```

2. **Verify I²C device is detected:**
   ```bash
   i2cdetect -y 1
   # Should show device at 0x27 or 0x3F
   ```

3. **Check Python version:**
   ```bash
   python3 --version
   # Should be Python 3.9 or higher
   ```

4. **Verify file permissions:**
   ```bash
   ls -l *.py
   # Should have execute permissions (chmod +x if needed)
   ```

---

**Last Updated:** 2025-10-25
**Document Version:** 1.2.0
