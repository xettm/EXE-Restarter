# EXE Restarter

A simple Python script that automatically restarts an executable file with a keyboard keybind.

## Features

- **Auto-detects .exe files** - Automatically finds and targets the first .exe file in the same directory
- **Keyboard trigger** - Press the configured keybind (default: **F8**) to restart the exe
- **Auto-close on exit** - If the exe is not running when you press the keybind, the script closes automatically
- **Fast restart** - Quickly closes and reopens the exe on demand

## Requirements

Install the required Python packages:

```bash
pip install psutil keyboard
```

## How to Use

1. Place the script in the same folder as your .exe file
2. Run the script:
   ```bash
   python exe_restarter.py
   ```
3. Press **F8** (or your configured keybind) to restart the exe
4. If the exe is not running, the script will close

## Configuration

Edit the `KEYBIND` variable at the top of the script to change the trigger key:

```python
KEYBIND = "f8"  # change this to whatever key you want
```

Common keybinds: `f1`, `f2`, ... `f12`, `space`, `enter`, `esc`, `shift`, `ctrl`, `alt`

## How It Works

1. Scans the script directory for .exe files
2. Waits for the configured keybind to be pressed
3. Checks if the exe is currently running:
   - If **not running**: Closes the script
   - If **running**: Terminates it, waits 1 second, restarts it, and restarts the script
