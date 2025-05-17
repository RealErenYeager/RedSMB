import argparse
import socket
import json
import os
from utils import smb_utils


def check_port_open(ip, port=445):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3)
            result = s.connect_ex((ip, port))
            return result == 0
    except Exception as e:
        print(f"[!] Error checking port: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="SMB Recon and Secrets Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP address")
    parser.add_argument("-u", "--username", default="guest", help="Username for SMB login")
    parser.add_argument("-p", "--password", default="", help="Password for SMB login")
    parser.add_argument("-o", "--output", default="findings.json", help="Output file for findings")
    
    args = parser.parse_args()

    print(f"[*] Starting SMB Recon on {args.target}")

    if not check_port_open(args.target):
        print("[!] Port 445 (SMB) is not open on the target.")
        return

    conn = smb_utils.connect_smb(args.target, args.username, args.password)
    if not conn:
        print("[!] SMB login failed.")
        return

    shares = smb_utils.list_shares(conn)
    findings = []

    for share in shares:
        if share['type'] != 'DISK' or share['name'].endswith('$'):
            continue

        print(f"[*] Scanning share: {share['name']}")
        files = smb_utils.list_files(conn, share['name'])

        for file in files:
            if any(file.lower().endswith(ext) for ext in ['.txt', '.ps1', '.bat']):
                content = smb_utils.read_file(conn, share['name'], file)
                secrets = smb_utils.find_secrets(content)
                if secrets:
                    findings.append({
                        "share": share['name'],
                        "file": file,
                        "matches": secrets
                    })

    print(f"[*] Found {len(findings)} suspicious file(s) with potential secrets.")

    with open(args.output, 'w') as out:
        json.dump(findings, out, indent=4)
        print(f"[*] Results saved to {args.output}")

    conn.close()


if __name__ == "__main__":
    main()
