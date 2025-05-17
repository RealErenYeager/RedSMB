from impacket.smbconnection import SMBConnection
import re
import io


def connect_smb(ip, username="guest", password=""):
    try:
        conn = SMBConnection(ip, ip)
        conn.login(username, password)
        print("[+] SMB login successful")
        return conn
    except Exception as e:
        print(f"[!] SMB login failed: {e}")
        return None


def list_shares(conn):
    shares = []
    try:
        for share in conn.listShares():
            shares.append({"name": share['shi1_netname'][:-1], "type": share['shi1_type']})
    except Exception as e:
        print(f"[!] Error listing shares: {e}")
    return shares


def list_files(conn, share):
    file_list = []
    try:
        files = conn.listPath(share, '*')
        for file in files:
            if not file.is_directory():
                file_list.append(file.get_longname())
    except Exception as e:
        print(f"[!] Error listing files in share {share}: {e}")
    return file_list


def read_file(conn, share, filename):
    try:
        file_obj = io.BytesIO()
        conn.getFile(share, f"\\{filename}", file_obj.write)
        return file_obj.getvalue().decode(errors="ignore")
    except Exception as e:
        print(f"[!] Error reading file {filename} from {share}: {e}")
        return ""


def find_secrets(content):
    patterns = [
        r'password\s*[=:]\s*[^\s\'";]+',
        r'user(?:name)?\s*[=:]\s*[^\s\'";]+',
        r'pass\s*[=:]\s*[^\s\'";]+',
        r'token\s*[=:]\s*[^\s\'";]+',
        r'credentials\s*[=:]\s*[^\s\'";]+',
    ]
    findings = []
    for pattern in patterns:
        matches = re.findall(pattern, content, flags=re.IGNORECASE)
        findings.extend(matches)
    return findings