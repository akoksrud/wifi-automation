---
icon: linux
---

# Note: WSL (Windows)

You can use WSL (Windows Subsystem for Linux) instead of a Ubuntu VM running in a hypervisor, for Python and Ansible stuff

TIG stack and other docker stuff is not tested (yet)

No instructions for using WSL or adopting the lab guide to WSL is included at this moment

Install WSL (start Powershell as administrator)

```powershell
PS C:\> wsl --install
```

Check WSL version

```powershell
PS C:\> wsl --version
WSL version: 2.3.24.0
(... if this command is not showing version, you must upgrade)
```

Upgrade WSL

```powershell
PS C:\> wsl --update
```

Install Ubuntu (or other specific distro)

```powershell
PS C:\> wsl --install -d Ubuntu
```

List installed WSL VMs, run "wsl --list"

```powershell
PS C:\> wsl --list
```

Fix network connectivity (from Powershell. Restart WSL)

```powershell
PS C:\> echo '[wsl2]' > ~\.wslconfig
PS C:\> echo 'networkingMode=mirrored' >> ~\.wslconfig
```

You might have to create some FW-openings and/or do some port forwarding to get the external devices (like the 9800 WLC) to communicate into your WSL Telegraf etc. This is not tested yet, and not part of this deep dive material
