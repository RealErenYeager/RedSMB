# RedSMB

A Python-based penetration testing tool to automate SMB share enumeration, file inspection, and secrets discovery. Built using the Impacket library.

---

## 🚀 Features

* ✅ SMB port check (port 445)
* 🔐 Authenticated SMB login (supports guest access)
* 📁 Lists non-hidden SMB shares
* 📂 Scans files for suspicious extensions (.txt, .ps1, .bat)
* 🕵️ Extracts hardcoded secrets using regex patterns
* 📄 Exports results in JSON format

---

## 📦 Installation

```bash
# Clone the repo
$ git clone https://github.com/yourusername/RedSMB.git
$ cd RedSMB

# Set up virtual environment (optional but recommended)
$ python3 -m venv venv && source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

---
## 🛠 Usage
