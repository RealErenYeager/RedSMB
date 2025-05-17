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
$ git clone https://github.com/yourusername/smb_tool.git
$ cd smb_tool

# Set up virtual environment (optional but recommended)
$ python3 -m venv venv && source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt
```

---

## 🛠 Usage

```bash
python smb_recon.py -t <TARGET_IP> [-u <USERNAME>] [-p <PASSWORD>] [-o <OUTPUT_FILE>]
```

### Examples:

```bash
python smb_recon.py -t 192.168.1.10 -u guest -p ""
python smb_recon.py -t 10.0.0.5 -u admin -p pass123 -o report.json
```

---

## 📁 Sample Output

```json
[
    {
        "share": "Public",
        "file": "creds.txt",
        "matches": ["password=SuperSecret123", "user=admin"]
    }
]
```

---

## 📚 Dependencies

* Python 3.6+
* impacket

Add to `requirements.txt`:

```txt
impacket
```

---

## 🧪 Screenshots / Demo

![smb\_scan](screenshots/smb_scan.png)
![found\_secrets](screenshots/secrets_found.png)

---

## 🔐 Legal Notice

This tool is intended for educational and authorized penetration testing purposes **only**. Unauthorized use is illegal and unethical.

---

## 📄 PoC Report

A sample red team PoC report is included as `PoC_Report.pdf`.

---

## 📬 Contact

For collaboration, reach out via GitHub or email: `yourname@protonmail.com`

---

## 📃 License

MIT License
