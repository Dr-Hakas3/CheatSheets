OSCP Penetration Test Report

v.2.0

student@youremailaddress.com

OSID: XXXXX

![[GreenHorn image.png]]

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

**Exam Network:**

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
- **4.1 Target #1 –  10.10.11.25**
- **4.1.1 Initial Access –**

**Severity:**

- **4.1.1 Service Enumeration**

└─$ rustscan -r 1-65535 -a 10.10.11.25 -- -sV -Pn -A

.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.

\| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  \`| |

\| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |

\`-' \`-'\`-----'\`----'  \`-'  \`----'  \`---' \`-'  \`-'\`-' \`-'

The Modern Day Port Scanner.

________________________________________

: http://discord.skerritt.blog         :

: https://github.com/RustScan/RustScan :

\--------------------------------------

Scanning ports: The virtual equivalent of knocking on doors.

\[~\] The config file is expected to be at "/home/gkali/.rustscan.toml"

\[!\] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers

\[!\] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'.

Open 10.10.11.25:22

Open 10.10.11.25:80

\[~\] Starting Script(s)

\[>\] Running script "nmap -vvv -p {{port}} {{ip}} -sV -Pn -A" on ip 10.10.11.25

Depending on the complexity of the script, results may take some time to appear.

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.

\[~\] Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-29 22:12 JST

NSE: Loaded 156 scripts for scanning.

NSE: Script Pre-scanning.

NSE: Starting runlevel 1 (of 3) scan.

Initiating NSE at 22:12

Completed NSE at 22:12, 0.00s elapsed

NSE: Starting runlevel 2 (of 3) scan.

Initiating NSE at 22:12

Completed NSE at 22:12, 0.00s elapsed

NSE: Starting runlevel 3 (of 3) scan.

Initiating NSE at 22:12

Completed NSE at 22:12, 0.00s elapsed

Initiating Parallel DNS resolution of 1 host. at 22:12

Completed Parallel DNS resolution of 1 host. at 22:12, 0.05s elapsed

DNS resolution of 1 IPs took 0.05s. Mode: Async \[#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0\]

Initiating Connect Scan at 22:12

Scanning 10.10.11.25 \[2 ports\]

Completed Connect Scan at 22:12, 3.00s elapsed (2 total ports)

Initiating Service scan at 22:12

NSE: Script scanning 10.10.11.25.

NSE: Starting runlevel 1 (of 3) scan.

Initiating NSE at 22:12

Completed NSE at 22:12, 5.00s elapsed

NSE: Starting runlevel 2 (of 3) scan.

Initiating NSE at 22:12

Completed NSE at 22:12, 0.00s elapse

d

NSE: Starting runlevel 3 (of 3) scan.

Initiating NSE at 22:12

Completed NSE at 22:12, 0.00s elapsed

Nmap scan report for 10.10.11.25

Host is up, received user-set.

Scanned at 2024-08-29 22:12:25 JST for 9s

PORT   STATE    SERVICE REASON      VERSION

22/tcp filtered ssh     no-response

80/tcp filtered http    no-response

NSE: Script Post-scanning.

NSE: Starting runlevel 1 (of 3) scan.

Initiating NSE at 22:12

Completed NSE at 22:12, 0.00s elapsed

NSE: Starting runlevel 2 (of 3) scan.

Initiating NSE at 22:12

Completed NSE at 22:12, 0.00s elapsed

NSE: Starting runlevel 3 (of 3) scan.

Initiating NSE at 22:12

Completed NSE at 22:12, 0.00s elapsed

Read data files from: /usr/bin/../share/nmap

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 8.60 seconds

![[GreenHorn image 1.png]]

![[GreenHorn image 2.png]]

└─$ nmap -Pn greenhorn.htb

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-30 00:05 JST

Nmap scan report for greenhorn.htb (10.10.11.25)

Host is up (0.52s latency).

Not shown: 997 closed tcp ports (conn-refused)

PORT     STATE SERVICE

22/tcp   open  ssh

80/tcp   open  http

3000/tcp open  ppp

Nmap done: 1 IP address (1 host up) scanned in 46.02 seconds

![[GreenHorn image 3.png]]

└─$ whatweb 10.10.11.25

http://10.10.11.25 \[302 Found\] Country\[RESERVED\]\[ZZ\], HTTPServer\[Ubuntu Linux\]\[nginx/1.18.0 (Ubuntu)\], IP\[10.10.11.25\], RedirectLocation\[http://greenhorn.htb/\], Title\[302 Found\], nginx\[1.18.0\]

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
| 10.10.11.25 | **TCP**:22,80,3000 |

We run nmap to scan the target and found a few ports open.

**4.1.2** **Initial Access –**

**Directory Enumeration**

└─$ ffuf -c -w /usr/share/seclists/Discovery/Web-Content/common.txt -u http://greenhorn.htb/FUZZ -fc 404

![[GreenHorn image 4.png]]

**Browser Access**

![[GreenHorn image 5.png]]

![[GreenHorn image 6.png]]

Pluck-v4.7.18

https://github.com/Rai2en/CVE-2023-50564_Pluck-v4.7.18_PoC/tree/main

![[GreenHorn image 7.png]]

**I found the pass.php**

![[GreenHorn image 8.png]]

d5443aef1b64544f3685bf112f6c405218c573c7279a831b1fe9612e3a4d770486743c5580556c0d838b51749de15530f87fb793afdcc689b6b39024d7790163

![[GreenHorn image 9.png]]

**iloveyou1**

![[GreenHorn image 10.png]]

![[GreenHorn image 11.png]]

![[GreenHorn image 12.png]]

![[GreenHorn image 13.png]]

![[GreenHorn image 14.png]]

**Local.txt value:**0a6761002e20a24129eb12ff18952904

**4.1.3** **Privilege Escalation -**

junior@greenhorn:~$ cp 'Using OpenVAS.pdf' a.pdf

cp 'Using OpenVAS.pdf' a.pdf

![[GreenHorn image 15.png]]

junior@greenhorn:~$ python3 -m http.server

python3 -m http.server

Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

10.10.16.60 - - \[29/Aug/2024 23:27:36\] "GET /a.pdf HTTP/1.1" 200 -

![[GreenHorn image 16.png]]

**Open a.PDF**

![[GreenHorn image 17.png]]

**Extract Image from PDF.**

Need pdfimages.

![[GreenHorn image 18.png]]

└─$ pdfimages -png a.pdf b.png

![[GreenHorn image 19.png]]

└─$ git clone https://github.com/spipm/Depix.git

![[GreenHorn image 20.png]]

└─$ cd Depix/

└─$ python3 depix.py -p ../b.png-000.png -s images/searchimages/debruinseq_notepad_Windows10_closeAndSpaced.png -o ./output.png

![[GreenHorn image 21.png]]

open output.png

![[GreenHorn image 22.png]]

sidefromsidetheothersidesidefromsidetheotherside

![[GreenHorn image 23.png]]

**Proof.txt value:**bafadd49b010b25222cc9fbfe0b58b09