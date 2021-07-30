## Cisco MUD Manager

#### Introduction
The following is the setup procedure to install Cisco MUD-Manager.


#### Installation
1. Installing necessary packages

```

apt-get install make gcc
apt-get install -y openssl libcurl4-openssl-dev
```

2. Installing cJSON
```
cd /
git clone https://github.com/DaveGamble/cJSON 
cd /cJSON
make
make install
```

3. Installing MongoDB
```
apt-get install -y gnupg
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
add-apt-repository 'deb [arch=arm64,amd64] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse'

apt update
apt-get install -y mongodb-org
```

4. Installing MongoC-Driver
```
apt-get install -y libmongoc-1.0-0
```

5a. Installing Cisco MUD-Manager
```
apt-get install -y libcurl4-openssl-dev libmongoc-dev automake libtool libtool-bin
cd /
git clone --branch 3.0.1 https://github.com/CiscoDevNet/MUD-Manager
cd MUD-Manager
autoreconf -f -i
./configure
```
5b. Replace mud_manager.c from /MUD-Manager/src with the one in this repository, then make and make install.
```
cp safe-patching/Cisco-Mud-Manager/mud_manager.c /MUD-Manager/src/mud_manager.c

make
make install
```

6. Installing FreeRadius
```
cd /
apt-get install -y libtalloc-dev libjson-c-dev libcurl4-gnutls-dev libperl-dev libkqueue-dev libssl-dev 
wget https://freeradius.org/ftp/pub/radius/freeradius-server-3.0.19.tar.gz
tar -xf freeradius-server-3.0.19.tar.gz
cd freeradius-server-3.0.19
./configure --with-rest --with-json-c --with-perl --build=aarch64-unknown-linux-gnu
make
make install
cd /MUD-Manager/examples/AAA-LLDP-DHCP
./FR-setup.sh
```

7. Adding NAS. Open Freeradiusd clients.conf file (/usr/local/etc/raddb/clients.conf), and add the following to the end of the file. The value of the ipaddr is your NAS
```
client 192.168.1.1 {
  ipaddr	= 192.168.1.1
  secret	= cisco
}
```

8. Enable and start MongoD service
```
systemctl enable mongod
systemctl restart mongod
```

#### Execution
```
# Create downloads folder to save JSON MUD Files
mkdir /MUD-Manager/downloads

# File Sender Service to send JSON MUD Files to Proxy Server
cp /safe-patching/Cisco-Mud-Manager/filesender.py /MUD-Manager/downloads
cp /safe-patching/Cisco-Mud-Manager/sender.service /etc/systemd/system/sender.service

# Automated Startup Service for MUD-Manager & FreeRADIUS
cp /safe-patching/Cisco-Mud-Manager/servicemanager.py /MUD-Manager
cp /safe-patching/Cisco-Mud-Manager/mud.service /etc/systemd/system/mud.service

systemctl daemon-reload
systemctl enable sender.service
systemctl restart sender.service

systemctl enable mud.service
systemctl restart mud.service
```
