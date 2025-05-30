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

(change the comment to something of your choice)

```bash
PS C:\> ssh-keygen -t ed25519 -C "akoksrud_2025"
```

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

#### About private and public key

You can password protect your private key with the following command. It will be much safer if your machine is  lost or compromised, at the cost of having to type your password when using the key

```bash
ssh-keygen -p -f ~/.ssh/id_ed25519
```
