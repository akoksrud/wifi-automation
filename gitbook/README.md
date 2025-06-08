---
description: >-
  SSH keys are used to prove who you are, like login to a server or sign a Git
  commit.
---

# Create SSH keypair

#### References

[https://www.brandonchecketts.com/archives/ssh-ed25519-key-best-practices-for-2025](https://www.brandonchecketts.com/archives/ssh-ed25519-key-best-practices-for-2025)

#### Prerequisites

You need some SSH libraries like OpenSSH installed to run these commands. They should be the same on Windows, Mac or Linux

#### Create a SSH keypair for your user

(change the comment and filename to something of your choice)

```bash
PS C:\> ssh-keygen -t ed25519 -C "akoksrud_2025" -f "akoksrud_2025"
```

You should use a password for the private key for security reasons.

If you do not specify a filename (the -f option) the default name will be "id\_ed25519". It will be used in the examples below.

Your key pair will be stored in the ".ssh" folder in your home directory, and will be named&#x20;

* id\_ed25519 (this is your private key, do not share it)
* id\_ed25519.pub (this is your public key, to be shared with others, uploaded to github, etc)

```powershell
PS C:\Users\akoksrud> ls ~/.ssh
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---          03.10.2024    19:42            419 id_ed25519
-a---          03.10.2024    19:42            110 id_ed25519.pub
(...)
```

#### Copying the public key to a Linux server

To copy your public key to a Linux server, enter the following command. It should work on both Windows (using Powershell), MacOS and Linux.&#x20;

{% code fullWidth="true" %}
```bash
cat ~/.ssh/id_ed25519.pub | ssh devnet-adm@{SERVER_IP} "cat >> .ssh/authorized_keys"

# Change {SERVER_IP} to your server's IP, it will be like this:
cat ~/.ssh/id_ed25519.pub | ssh devnet-adm@192.168.10.7 "cat >> .ssh/authorized_keys"
```
{% endcode %}

