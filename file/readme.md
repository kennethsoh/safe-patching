## File, Web, DNS and CA Server

This server acts as the File and Web server that hosts MUD Files, local DNS and local Certificate Authority.

#### Installation
1. Set up Web Hosting on Nginx
```
apt install -y nginx 

cp /safe-patching/file/default /etc/nginx/sites-enabled/default

rm -rf /var/www/html
cp -r /safe/patching/file/html /var/www/ 
```

2. Set up Local DNS using Bind
```
apt install -y bind9 bind9utils resolvconf 

cp /safe-patching/file/named.conf.local /etc/bind/named.conf.local
cp /safe-patching/file/forward.com /etc/bind/forward.com
cp /safe-patching/file/reverse.com /etc/bind/reverse.com

systemctl restart bind9
```

3. Create CA Key & Certificate, Web Key & Certificate, and MUD Signing Key & Certificate.
