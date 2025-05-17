# RedSMB

A Python-based penetration testing tool designed to automate SMB share enumeration, file inspection, and secrets discovery. Built using the powerful Impacket library, RedSMB streamlines your SMB penetration testing workflow.

---

## 🚀 Features

* ✅ Checks if SMB port 445 is open
* 🔐 Supports authenticated SMB login, including guest access
* 📁 Enumerates non-hidden SMB shares
* 📂 Scans files with suspicious extensions such as `.txt`, `.ps1`, and `.bat`
* 🕵️ Detects hardcoded secrets using customizable regex patterns
* 📄 Exports findings in a clean, easy-to-read JSON format

---

## 📦 Installation

```bash
# Clone the repository
$ git clone https://github.com/yourusername/RedSMB.git
$ cd RedSMB

# (Optional) Set up a virtual environment
$ python3 -m venv venv && source venv/bin/activate

# Install required dependencies
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

## 🔐 Legal Notice

This tool is intended for educational and authorized penetration testing purposes **only**. Unauthorized use is illegal and unethical.

---

## 📄 PoC Report

A sample red team PoC report is included as `PoC_Report.pdf`.


