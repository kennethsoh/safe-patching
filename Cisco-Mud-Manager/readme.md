##Cisco MUD Manager

####Introduction
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

5. Installing Cisco MUD-Manager
```
apt-get install -y libcurl4-openssl-dev libmongoc-dev automake libtool libtool-bin
cd /
git clone --branch 3.0.1 https://github.com/CiscoDevNet/MUD-Manager
cd MUD-Manager
autoreconf -f -i
./configure

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
