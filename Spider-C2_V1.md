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
