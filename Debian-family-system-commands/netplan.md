###

```yaml
# cat /etc/netplan/00-installer-config.yaml 
# This is the network config written by 'subiquity'
network:
  ethernets:
    ens33:
      dhcp4: false
      addresses:
        - 192.168.30.30/24
      routes:
        - to: default
          via: 192.168.30.1
      nameservers:
        addresses:
          - 192.168.30.1
          - 114.114.114.114
          - 8.8.8.8
  version: 2
```

netplan apply