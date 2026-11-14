---
title: PING
parent: Ansible
---

# PING

```zsh
┌──(kali㉿kali)-[~/Lab/OSCP/AD_Set_v1/ansible]
└─$ ansible ad_labs -i hosts.ini -m win_ping
192.168.56.202 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
192.168.56.200 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
192.168.56.206 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```
# Playbookの反映

```bash
vagrant@vagrant:~/GOAD$ cd ~/GOAD

ANSIBLE_ROLES_PATH=ad/OSCP+_AD_Set_v1/ansible/roles \
ansible-playbook \
-i ad/OSCP+_AD_Set_v1/data/inventory \
-i workspace/cae6ea-oscp+_ad_set_v1-virtualbox/inventory \
ad/OSCP+_AD_Set_v1/ansible/playbooks/site.yml
```

# Error
## Windows11 Time out

```powershell
PS G:\Virtual_Machines\GOAD-main> py goad.py -t install -l OSCP+_AD_Set_v1 -p virtualbox -m vm
```

![](../../assets/images/Pasted%20image%2020260530195055.png)

```powershell
PS G:\Virtual_Machines\GOAD-main> cd G:\Virtual_Machines\GOAD-main\workspace\4776fe-oscp+_ad_set_v1-virtualbox\provider
```

```powershell
PS G:\Virtual_Machines\GOAD-main\workspace\4776fe-oscp+_ad_set_v1-virtualbox\provider> vagrant reload WS26
```