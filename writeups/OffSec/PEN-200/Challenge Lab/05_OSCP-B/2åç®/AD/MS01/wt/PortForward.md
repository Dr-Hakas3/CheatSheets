sudo ip tuntap add user kali mode tun ligolo

sudo ip link set ligolo up

![[PortForward image.png]]

~/Tools/PENTEST_and_Red/Port_Forwarding/ligolo-ng/release/ligolo-ng_proxy_0.8_linux_amd64/proxy -selfcert

![[PortForward image 1.png]]

.\agent.exe -connect 192.168.45.163:11601 -ignore-cert

![[PortForward image 2.png]]

![[PortForward image 3.png]]