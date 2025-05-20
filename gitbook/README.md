# Install Ubuntu Server

The lab itself will use 9800 WLCs that already run on our servers, which have Proxmox Virtual Environment installed. That is a Level 1 hypervisor (run directly on the hardware)

This chapter will have separate instructions for using Hyper-V, VirtualBox, Multipass/qemu and Proxmox and performing a fresh intsall of Ubuntu Server.  Some common steps are collected in the next chapter. &#x20;

Hyper-V (on Windows), VirtualBox and VMWare Workstation and Fusion are examples of level 2 hypervisors. That mean that they are running on top of another OS. They will be slower than level 1 hypervisors like Proxmox, Nutanix, VMWare ESXi, Hyper-V server etc. There are some differences between how long the "path to the hardware" is, which might explain some differences in speed using the alternatives.

{% hint style="info" %}
**Note**

You should turn OFF power save stuff on your laptop, as you might run into unexpected problems if your laptop enters power saving mode

You should always do a shutdown of your VMs before shutting down or putting your laptop in sleep or hibernation mode. Especially the 9800-CL do NOT like if the host OS sleeps, and might be corrupt so you have to reinstall the WLC
{% endhint %}

My experience is that on Windows, virtual machines in Hyper-V are faster than in VirtualBox. This might be due to suboptimal config, differences in hardware, or that Hyper-V have a shorter "path to the hardware"

If you have no preference, this is my recommendation for this deep dive:

* If you use Windows: Install Ubuntu Server in Hyper-V
* If you use Mac: Install Ubuntu Server using Multipass (w/qemu)
* WLC 9800-CL: Use our shared pre-built & tested servers referring to your Pod# in the Lab Topology map

For the rest of this chapter, and for chapter 2, follow the instructions for your chosen hypervisor

{% hint style="info" %}
**Note**

Many of these instructions require admin privileges. You should be in control of what you do so you don't break anything. We can give no guarantees. The instructions and screenshots are from the working solution on our own laptops, but we have no way to tell if it works on all setups and which conflicting software you might heave. If you do not want to do this on your laptop, you can use our pre-built and tested Ubuntu Servers and WLCs
{% endhint %}
