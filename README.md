# 🕷️ Spider-C2

> **Modular Command & Control framework for authorized security testing.**
> For Red Team operations and penetration testing.

---

## 📖 Description

Spider-C2 is a modular Command & Control framework designed for security professionals. It allows operators to manage multiple agents, execute commands remotely, and collect data from compromised systems during authorized engagements.

---

## ⚠️ Warning

**This tool is for authorized use only.** Always obtain written permission before deployment.

---

## ⚙️ Installation

```bash
git clone https://github.com/theanonspider/Spider-C2.git
cd Spider-C2
pip install -r requirements.txt

🚀 Usage

bash
# Create authorization token (required)
echo "SPIDER_C2_AUTHORIZED" > spiderc2.token

# Start C2 server
python spiderc2.py server

# Generate agent
python spiderc2.py generate --type windows

# List connected agents
python spiderc2.py list
🧩 Modules

Module	Description
server	Flask web dashboard + API
agent	Multi-OS client agent
crypto	AES-256 encryption
persistence	Windows/Linux/macOS persistence
sysinfo	System information collection
screenshot	Screen capture
keylogger	Keyboard input capture
shell	Remote command execution
file_manager	Upload/download files
anti_vm	VM detection
anti_debug	Debugger detection
🎨 Web Dashboard

Access the dashboard at http://localhost:8080

Login : admin / SpiderC2-2024!
Agents : real-time connected agents list
Commands : send commands to agents
👤 Author

@theanonspider
