"""
Spider-C2 Module : SysInfo
Collect system information.
"""

import platform
import socket
import os
import json
from datetime import datetime

class SysInfoModule:
    def __init__(self):
        pass

    def collect(self):
        info = {
            "timestamp": datetime.now().isoformat(),
            "hostname": platform.node(),
            "os": platform.platform(),
            "os_version": platform.version(),
            "architecture": platform.machine(),
            "processor": platform.processor(),
            "python_version": platform.python_version(),
            "username": os.getlogin(),
            "ip": self._get_ip()
        }
        return json.dumps(info, indent=2)

    def _get_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
