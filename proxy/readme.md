## Proxy Analyser

The Proxy serves to download patch files after its is obtained by the MUD Manager. 
It will upload the patch file to VirusTotal for checks and keep the patch file if it is neither malicious nor suspicious.

#### Installation
1. Move files to appropriate directories. Root (/) folder with root permissions is assumed.
```
cd /safe-patching/proxy
mv proxy.py /; mv fsm.py /; mv proxy.service /etc/systemd/system/
```

2. Enable and start proxy.service
```
systemctl daemon-reload 
systemctl enable proxy.service
systemctl restart proxy.service
```
