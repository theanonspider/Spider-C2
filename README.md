# 🕷️ Spider-C2 — C2 Framework

> ⚠️ **AVERTISSEMENT** — Usage exclusivement éducatif et défensif.  
> Toute utilisation non autorisée est **ILLÉGALE** et engage votre responsabilité.

---

## 📖 Pourquoi Spider-C2 ?

**Spider-C2** est un framework C2 (Command & Control) pour le contrôle à distance d’agents Windows, Linux et macOS.

Il est conçu pour les **tests d’intrusion** et les **exercices Red Team**.

---

## 🧩 Modules (11)

| Catégorie | Modules |
|-----------|---------|
| **Agents** | Windows/Linux/macOS |
| **Communication** | HTTPS |
| **Commandes** | Shell, upload, download, screenshot |
| **Post‑exploit** | Persistance, exfiltration |

---

## 🔐 Sécurité

```bash
echo "SPIDER_C2_AUTHORIZED" > spiderc2.token
```

---

## ⚙️ Installation

```bash
git clone https://github.com/theanonspider/Spider-C2.git
cd Spider-C2
pip install -r requirements.txt
echo "SPIDER_C2_AUTHORIZED" > spiderc2.token
```

---

## 🚀 Exemples d’utilisation

```bash
# 1. Démarrer le serveur C2
python spiderc2.py server

# 2. Générer un agent Windows
python spiderc2.py generate -t windows -o agent.exe

# 3. Lister les agents connectés
python spiderc2.py list
```

---

## 📄 Sortie

Rapports dans `reports/` : **JSON + HTML**.

---

## ⚖️ Licence

Usage éducatif et défensif uniquement.

---

## 👤 Auteur

**@theanonspider** — Cybersécurité éthique. 🐺
