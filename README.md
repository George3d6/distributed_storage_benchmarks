# distributed storage benchmarks


## Memcached vs Consul vs Aerospike

### Setup

#### Install

Servers:

`sudo apt install consul`

`sudo apt install memcached`

```
wget -O aerospike.tgz 'https://www.aerospike.com/download/server/latest/artifact/ubuntu18' && \
tar -xvf aerospike.tgz && \
cd aerospike-server-community-*-ubuntu18* && \
sudo ./asinstall # will install the .deb packages && \
sudo systemctl start aerospike;
```

Clients:

`pip3 install python-consul`

`pip3 install aiomcache`

`sudo pip3 install aerospike`

 
