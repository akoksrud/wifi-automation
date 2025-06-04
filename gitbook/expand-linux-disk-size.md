---
description: >-
  If you have extended your disk size, or forgot to use all available disk size
  at install
---

# Expand Linux disk size

Find the path for the "Logical Volume" (LV)

```bash
devnet-adm@ubuntu-devnet:~$ sudo lvdisplay | grep "LV Path"
 LV Path                /dev/ubuntu-vg/ubuntu-lv
```

Then extend this logical volume to use 100% of the free space on the disk after the volume. The path in the first line should be the path you found in the previous section

```bash
devnet-adm@ubuntu-devnet:~$ sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
devnet-adm@ubuntu-devnet:~$ df -h | grep "lv"
/dev/mapper/ubuntu--vg-ubuntu--lv   37G   14G   22G  39% /
```

Lastly, resize the file system to use the available space. The path here should be the path that you found in the previous session after resizing the LV

```bash
devnet-adm@ubuntu-devnet:~$ sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
```
