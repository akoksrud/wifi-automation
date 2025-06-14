---
description: Descriptions to change to static IP if you are using Multipass
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
---

# Change to static IP (Multipass)

If you are using Multipass, it creates two network adapters. Please follow these instructions if you are using Multipass. If you are NOT using multipass, follow the next section which cover the other options.

Check that the bridged network is correct. Choose your USB dongle or ethernet port etc

<figure><img src="../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

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
    default:
      match:
        macaddress: "52:54:00:cb:dc:82"
      dhcp-identifier: "mac"
      dhcp4: true
    extra0:
      match:
        macaddress: "52:54:00:8f:54:67"
      optional: true
      dhcp-identifier: "mac"
      dhcp4: true
      dhcp4-overrides:
        route-metric: 200
```

Change the "extra0" part to disable dhcp4 and insert the static IP\
Insert your pod IP instead of the {YOUR\_POD\_IP} placeholder...

```yaml
# Do not change this first part (including you don't have to write this comment...)
network:
  version: 2
  ethernets:
    default:
      match:
        macaddress: "52:54:00:cb:dc:82"
      dhcp-identifier: "mac"
      dhcp4: true
    extra0:
      match:
        macaddress: "52:54:00:8f:54:67"
# Changed from here and down
      dhcp4: false
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
