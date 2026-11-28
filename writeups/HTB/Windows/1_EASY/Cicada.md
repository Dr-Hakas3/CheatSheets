- **Independent Challenges**
- **1 Target #1 – 10.10.11.35**
- **1.1 Initial Access –**

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:**

**Steps to reproduce the attack:**

- **1.1 Service Enumeration**
- └─# nmap -p- cicada.htb --min-rate 20000

![[Cicada image.png]]

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
|  | **TCP**: 53,88,135,139,389,445,464,593,636,3268,3269,5985,57994 |

53 nothing

88

![[Cicada image 1.png]]

135,139,445

![[Cicada image 2.png]]

![[Cicada image 3.png]]

![[Cicada image 4.png]]

![[Cicada image 5.png]]

![[Cicada image 6.png]]

![[Cicada image 7.png]]

Cicada$M6Corpb*@Lp#nZp!8

![[Cicada image 8.png]]

![[Cicada image 9.png]]

**次に見つかったユーザ名とパスワードを利用して再度****nxc****を実行します。**

![[Cicada image 10.png]]

**david.orelious****/**aRt$Lp#7t*VQ!3

![[Cicada image 11.png]]

![[Cicada image 12.png]]

![[Cicada image 13.png]]

![[Cicada image 14.png]]

**1.2** **Initial Access –**

![[Cicada image 15.png]]

**Local.txt value:**c80ccfee37477293cf3bcbb5f3ba3ae7

**1.3** **Privilege Escalation  -SeBackupPrivilege**

**ユーザにファイルの読み取り権限が設定されていたことによる権限昇格**

![[Cicada image 16.png]]

![[Cicada image 17.png]]

**Administrator****のハッシュ値の取得**

![[Cicada image 18.png]]

**1.4** **Post Exploitation**

**Proof.txt value:**c80db9699e930b0a83c033d91cf19176

- **Active Directory Set**

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
|  | **TCP:** |
|  | **TCP:** |
|  | **TCP:** |

- **1  –**
- **1.1 Initial Access –**

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:** **Critical**

**Steps to reproduce the attack:**

- **1.2 Privilege Escalation –**

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:** **Critical**

**Steps to reproduce the attack:**

- **1.3 Post-Exploitation**

**System Proof screenshot:**

- **2  –**
- **2.1 Initial Access –**

**Steps to reproduce the attack:**

- **2.2 Post-Exploitation**

**Local Proof Screenshot:**

- **3 DC –**
- **5.3.1 Initial Access –**

**Steps to reproduce the attack:**

- **3.2 Post-Exploitation**

**System Proof Screenshot:**