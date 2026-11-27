import sys
import threading
import socket
import select
import getpass
import paramiko
import argparse

# デバッグ用のverbose関数
def verbose(message):
    print(f"[DEBUG] {message}")

# オプション解析関数の仮実装
def parse_options():
    parser = argparse.ArgumentParser(description="Reverse SSH Tunnel")
    parser.add_argument("server", help="SSH server in the format host:port")
    parser.add_argument("-p", "--port", type=int, required=True, help="Local port to forward")
    parser.add_argument("-r", "--remote", required=True, help="Remote host:port to forward to")
    parser.add_argument("--user", required=True, help="Username for SSH authentication")
    parser.add_argument("--keyfile", help="Path to private key file for authentication")
    parser.add_argument("--look-for-keys", action="store_true", help="Look for private keys in ~/.ssh/")
    parser.add_argument("--readpass", action="store_true", help="Prompt for SSH password")
    args = parser.parse_args()

    # サーバ情報を分割
    server = args.server.split(":")
    if len(server) != 2:
        print("Error: Server must be in the format host:port")
        sys.exit(1)

    # リモート情報を分割
    remote = args.remote.split(":")
    if len(remote) != 2:
        print("Error: Remote must be in the format host:port")
        sys.exit(1)

    return args, (server[0], int(server[1])), (remote[0], int(remote[1]))

def main():
    options, server, remote = parse_options()
    password = None
    if options.readpass:
        password = getpass.getpass('Enter SSH password: ')
    client = paramiko.SSHClient()
    client.load_system_host_keys()

    client.set_missing_host_key_policy(paramiko.WarningPolicy())

    verbose(f'Connecting to ssh host {server[0]}:{server[1]} ...')
    try:
        client.connect(server[0],
                       server[1],
                       username=options.user,
                       key_filename=options.keyfile,
                       look_for_keys=options.look_for_keys,
                       password=password
        )
    except Exception as e:
        print(f'*** Failed to connect to {server[0]}:{server[1]}: {e}')
        sys.exit(1)

    verbose(f'Now forwarding remote port {options.port} to {remote[0]}:{remote[1]} ...')

    try:
        reverse_forward_tunnel(
            options.port, remote[0], remote[1], client.get_transport())
    except KeyboardInterrupt:
        print('C-c: Port forwarding stopped.')
        sys.exit(0)

def reverse_forward_tunnel(server_port, remote_host, remote_port, transport):
    try:
        transport.request_port_forward('', server_port)
        verbose(f"Listening on port {server_port} for connections...")
        while True:
            chan = transport.accept(1000)
            if chan is None:
                continue
            verbose(f"Channel opened: {chan.origin_addr}")
            thr = threading.Thread(target=handler, args=(chan, remote_host, remote_port))
            thr.setDaemon(True)
            thr.start()
    except Exception as e:
        print(f"Error in reverse forwarding: {e}")

def handler(chan, host, port):
    sock = socket.socket()
    try:
        sock.connect((host, port))
    except Exception as e:
        verbose(f"Forwarding request to {host}:{port} failed: {e}")
        chan.close()
        return

    verbose(f"Connected! Tunnel open {chan.origin_addr} -> {host}:{port}")
    while True:
        try:
            r, w, x = select.select([sock, chan], [], [])
            if sock in r:
                data = sock.recv(1024)
                if len(data) == 0:
                    break
                chan.send(data)
            if chan in r:
                data = chan.recv(1024)
                if len(data) == 0:
                    break
                sock.send(data)
        except Exception as e:
            verbose(f"Error in tunnel: {e}")
            break
    chan.close()
    sock.close()
    verbose(f"Tunnel closed from {chan.origin_addr}")

if __name__ == "__main__":
    main()
