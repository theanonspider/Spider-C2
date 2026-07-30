"""
Spider-C2 Module : Anti-Debug
Detect debugger presence.
"""

import platform
import sys
import os

class AntiDebugModule:
    def __init__(self):
        self.os_type = platform.system()

    def check(self):
        if self.os_type == "Windows":
            return self._check_windows()
        return {"debugger_detected": False}

    def _check_windows(self):
        try:
            import ctypes
            if ctypes.windll.kernel32.IsDebuggerPresent():
                return {"debugger_detected": True, "method": "IsDebuggerPresent"}
        except:
            pass

        try:
            if sys.gettrace() is not None:
                return {"debugger_detected": True, "method": "sys.gettrace"}
        except:
            pass

        return {"debugger_detected": False}
