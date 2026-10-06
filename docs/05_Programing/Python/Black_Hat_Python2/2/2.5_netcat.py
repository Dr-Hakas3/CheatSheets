import argparse
import locale
import os
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return

    if os.name == "nt":
        shell = True
    else:
        shell = False

        output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT, shell=shell)

    if locale.getdefaultlocale() == ('ja_JP', 'cp932'):
        return output.decode('cp932')
    else:
        return output.decode()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='BHP Net Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
        ```実行例:
        netcat.py -t 192.168.1.108 -p 5555 -l -c

        netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.text

        netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\"

        echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135

        netcat.py -t 192.168.1.108 -p 5555
        ```))
    parser.add_argument('-c', '--command', action='store_true',
                            help='対話型シェルの初期化')
    parser.add_argument('-e', '--execute', action='store_true',
                            help='指定コマンドの実行')
    parser.add_argument('-l', '--listen', action='store_true',
                            help='通信待受モード')
    parser.add_argument('-p', '--port', type=int, default=5555,
                            help='ポート番号の指定')
    parser.add_argument('-t', '--target', default='192.168.1.203',
                            help='IPアドレスの指定')
    parser.add_argument('-u', '--upload',
                                help='ファイルのアップロード')

    args = parser.parse_args()
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()
    nc = NetCat(args, buffer.encode())
    nc.run() 

class NetCat:
    