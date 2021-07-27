## File, Web, DNS and CA Server

This server acts as the File and Web server that hosts MUD Files, local DNS and local Certificate Authority.

#### Installation
1. Set up Web Hosting on Nginx
```
apt install -y nginx 

cp /safe-patching/file/default /etc/nginx/sites-enabled/default

```

2. Set up Local DNS using Bind
```
apt install -y bind9 bind9utils resolvconf 

# Create Forward and Reverse Zones for www (web), proxy, mud-manager

systemctl restart bind9
```

3. Create CA Key & Certificate, Web Key & Certificate, and MUD Signing Key & Certificate.


#### Usage
test.json, test.p7s and test.html serve as the valid MUD file, MUD signature and sample patch file.

testmal.json, testmal.p7s and testmal.exe serve as malicious MUD file, signature and patch.
