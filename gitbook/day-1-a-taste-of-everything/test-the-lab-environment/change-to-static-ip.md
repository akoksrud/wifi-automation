---
description: >-
  Descriptions to change to static IP if you are using Hyper-V, VirtualBox or
  Proxmox
---

# Change to static IP

You should have 1 network adapter on your Ubuntu Server. Most probably they will have the following names depending on your hypervisor:

* Proxmox: `ens18`
* Hyper-V: `eth0`
* VirtualBox: `enp0s3`

Check your network adapters name

```bash
netplan status | grep network
```

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Copy the netplan config file to a new file and backup the old one

```bash
sudo cp /etc/netplan/50-cloud-init.yaml /etc/netplan/99_config.yaml
sudo chmod 600 /etc/netplan/99_config.yaml
sudo mv /etc/netplan/50-cloud-init.yaml /etc/netplan/50-cloud-init.yaml.bak
```

Edit the new 99\_config.yaml file

```bash
sudo nano /etc/netplan/99_config.yaml
```

It looks like this (ish):

```yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: true
```

Change the file to disable dhcp4 and insert the static IP\
Insert your pod IP instead of the {YOUR\_POD\_IP} placeholder...\
(if the version: 2 is placed lower, it will not matter)

```yaml
network:
  version: 2
      dhcp4: false
      dhcp6: false
      addresses:
      - 192.168.10.{YOUR_POD_IP}/24
      routes:
      - to: default
        via: 192.168.10.1
      nameservers:
        addresses: 
        - 1.1.1.1
```

Then apply the new netplan config

```bash
sudo netplan apply
sudo netplan status
```

Reboot the server again, and you're good to go :relaxed:

```bash
sudo reboot now
```
