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

text

3. **Commit** : `Update README complete`

---

## PDF : `Spider-C2_V1.md`

1. Retourne à la **racine**
2. **Add file** → **Create new file**
3. Nom : `Spider-C2_V1.md`
4. Colle :

```markdown
# 🕷️ SPIDER-C2 V1 — DOCUMENTATION OFFICIELLE

> **Framework Command & Control modulaire pour tests de sécurité autorisés.**
> Version publique — Open Source — Usage éducatif

---

## 📊 FICHE TECHNIQUE

| Élément | Détail |
|---------|--------|
| **Nom** | Spider-C2 |
| **Version** | 1.0 (Publique) |
| **Type** | Framework C2 modulaire |
| **Licence** | MIT (usage éducatif uniquement) |
| **Langage** | Python 3 |
| **Plateforme** | Multi-plateforme |
| **Interface** | Web Dashboard (Flask) |
| **Modules** | 11 |
| **Dépôt** | github.com/theanonspider/Spider-C2 |

---

## 🧩 MODULES

### 🖥️ Server
- Flask web dashboard
- API REST pour agents
- Authentification admin

### 🤖 Agent
- Client multi-OS (Windows/Linux/macOS)
- Check-in automatique
- Exécution de commandes

### 🔐 Crypto
- Chiffrement AES-256
- Communication sécurisée

### 🔄 Persistence
- Windows : Registre Run
- Linux : Cron job
- macOS : LaunchAgent

### 📊 SysInfo
- Hostname, OS, IP, architecture
- Processeur, RAM

### 📸 Screenshot
- Capture d'écran Windows/Linux/macOS
- Encodage base64

### ⌨️ Keylogger
- Capture frappes clavier
- Windows/Linux

### 💻 Shell
- Exécution de commandes à distance
- Mode interactif

### 📁 File Manager
- Upload de fichiers
- Download de fichiers
- Liste de répertoires

### 🛡️ Anti-VM
- Détection VMware, VirtualBox, QEMU
- Vérification RAM, drivers

### 🔍 Anti-Debug
- IsDebuggerPresent
- sys.gettrace

---

## 🔐 SÉCURITÉ

| Mécanisme | Description |
|-----------|-------------|
| **Token** | Fichier `spiderc2.token` obligatoire |
| **Authentification** | Login/password dashboard |
| **Chiffrement** | AES-256 |

---

## ⚙️ INSTALLATION

```bash
git clone https://github.com/theanonspider/Spider-C2.git
cd Spider-C2
pip install -r requirements.txt
🚀 UTILISATION

bash
# Token obligatoire
echo "SPIDER_C2_AUTHORIZED" > spiderc2.token

# Démarrer le serveur
python spiderc2.py server

# Générer un agent
python spiderc2.py generate --type windows

# Lister les agents
python spiderc2.py list
🎨 DASHBOARD WEB

URL : http://localhost:8080
Login : admin / SpiderC2-2024!
⚠️ AVERTISSEMENT

Cet outil est fourni à des fins exclusivement éducatives et défensives.
Toute utilisation sans autorisation écrite est ILLÉGALE.

👤 AUTEUR

@theanonspider — Cybersécurité éthique

Document généré le 30 juillet 2026
