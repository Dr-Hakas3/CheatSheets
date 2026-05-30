# Playbookの反映

```bash
vagrant@vagrant:~/GOAD$ cd ~/GOAD

ANSIBLE_ROLES_PATH=ad/OSCP+_AD_Set_v1/ansible/roles \
ansible-playbook \
-i ad/OSCP+_AD_Set_v1/data/inventory \
-i workspace/cae6ea-oscp+_ad_set_v1-virtualbox/inventory \
ad/OSCP+_AD_Set_v1/ansible/playbooks/site.yml
```