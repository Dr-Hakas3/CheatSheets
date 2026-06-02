### Services and Resources Scanning


# Base
```zsh
nmap -v --script=xxxx -p T:139,445 <IP>
```

# Hard
```zsh
nmap -n -sV --version-intensity=5 -sU -sS -Pn -p T:139,445,U:137 --script=xxx <IP>
```

# SMB Relate NSE Scripts
# Try to retrieve NetBIOS and MAC
- nbstat

# Enum
- smb-enum-domains
- smb-enum-groups
- smb-enum-processes
- smb-enum-sessions
- smb-os-discovery
- smb-server-stats
- smb-system-info

# Attempts to retrieve useful information about files shared on SMB volumes
- smb-ls

# Queries information managed by the Windows Master Browser
- smb-mbenum

# Try to print something
- smb-print-text

# Get security level information about SMB
- smb-security-mode

# Vulns
- smb-vuln-conficker (dangerous, can crash target)
- smb-vuln-ms06-025 (Buffer overflow in RRAS)
- smb-vuln-ms07-029 (Buffer overflow which can crash the RPC intrface in the DNS Server)
- smb-vuln-ms08-067 (Buffer overflow/RCE. Dangerous, can crash the target)
- smb-vuln-ms10-054 (Remote Memory Corruption. Result is BSOD -> DANGEROUS)
- smb-vuln-ms10-061 (Print vulnerability. Safe and can\'t crash the target)
- smb-vuln-ms17-010 (RCE, just checking if vulnerable)
