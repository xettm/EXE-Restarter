import os
import sys
import time
import subprocess
import psutil
import keyboard

#==========================
# 🅲🅾︎🅽🅵🅸🅶
#==========================
KEYBIND = "f8"  # change this to whatever key you want. Read the README for more information
#==========================
# 🅲🅾︎🅳🅴
#===========================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def find_first_exe():
    for file in os.listdir(SCRIPT_DIR):
        if file.lower().endswith(".exe"):
            return os.path.join(SCRIPT_DIR, file)
    return None


def is_exe_running(exe_path):
    exe_name = os.path.basename(exe_path)
    for proc in psutil.process_iter(["name"]):
        try:
            if proc.info["name"] == exe_name:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return False


def close_exe(exe_path):
    exe_name = os.path.basename(exe_path)
    for proc in psutil.process_iter(["name"]):
        try:
            if proc.info["name"] == exe_name:
                proc.terminate()
                proc.wait(timeout=5)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass


def restart_script():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def main():
    exe_path = find_first_exe()

    if not exe_path:
        print("No .exe file found in this folder.")
        return

    print(f"Watching for keybind [{KEYBIND}]")
    print(f"Target exe: {os.path.basename(exe_path)}")

    while True:
        keyboard.wait(KEYBIND)

        print("Keybind pressed!")
        
        if not is_exe_running(exe_path):
            print("Exe is not running. Closing script...")
            sys.exit(0)
        
        print("Closing exe...")
        close_exe(exe_path)

        time.sleep(1)

        print("Reopening exe...")
        subprocess.Popen(exe_path)

        time.sleep(1)

        print("Restarting script...")
        restart_script()


if __name__ == "__main__":
    main()
