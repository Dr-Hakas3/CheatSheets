---
title: Vagrant
parent: Green Team
---

# SCP

```powershell
PS G:\Virtual_Machines\GOAD-main\workspace\cae6ea-oscp+_ad_set_v1-virtualbox\provider> scp -r `
>> -i "G:\Virtual_Machines\GOAD-main\workspace\cae6ea-oscp+_ad_set_v1-virtualbox\provider\.vagrant\machines\PROVISIONING\virtualbox\private_key" `
>> "G:\Virtual_Machines\GOAD-main\ad\OSCP+_AD_Set_v1" `
>> vagrant@192.168.56.3:/home/vagrant/GOAD/ad/
all.yml                                                                               100%  183    89.4KB/s   00:00
hosts.ini                                                                             100%  335   327.1KB/s   00:00
site.yml                                                                              100%  117   114.3KB/s   00:00
main.yml                                                                              100%  119    58.1KB/s   00:00
main.yml                                                                              100%  262   255.9KB/s   00:00
automation.xml                                                                        100%  525     0.5KB/s   00:00
task.bat                                                                              100%  343   111.7KB/s   00:00
main.yml                                                                              100% 1048   511.8KB/s   00:00
config.json                                                                           100%   21KB   6.7MB/s   00:00
inventory                                                                             100% 2269     1.1MB/s   00:00
inventory_disable_vagrant                                                             100% 1026   501.0KB/s   00:00
ATTACK_CHAIN.md                                                                       100%   22    10.7KB/s   00:00
global.sol                                                                            100%  192   187.5KB/s   00:00
loader.rb                                                                             100%  423   206.6KB/s   00:00
inventory                                                                             100%  539   526.3KB/s   00:00
Vagrantfile                                                                           100%  779     0.8KB/s   00:00
Vagrantfile                                                                           100%  289   141.1KB/s   00:00
README.md                                                                             100%  579   188.5KB/s   00:00
```