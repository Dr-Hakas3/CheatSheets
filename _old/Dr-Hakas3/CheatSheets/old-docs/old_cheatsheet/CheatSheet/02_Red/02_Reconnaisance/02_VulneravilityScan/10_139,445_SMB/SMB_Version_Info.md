```bash
SMB1 => Win2000 / XP / 2003
SMB2.0 => Vista / 2008
SMB2.1 => Win7 / 2008R2
SMB3.0 => Win8 /  2012
SMB 3.02 => Win8.1 / 2012R2

# Configuration tips
# Can be usefull to configure /etc/samba/smb.conf with:
client min protocol = SMB2
client max protocol = SMB3

# Then
service smbd restart
```