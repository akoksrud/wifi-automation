---
description: Hyper-V is our recommendation if you will run the VMs on your Windows laptop
---

# (a) Hyper-V

## Installing Hyper-V

Full instructions on how to enable/install Hyper-V, or to troubleshoot this, is outside the scope of this lab guide. But in short, go to "Turn Windows Features on or off" and enable Hyper-V. See more at [https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v#enable-the-hyper-v-role-through-settings](https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v)

<div data-full-width="false"><figure><img src="../../.gitbook/assets/image.png" alt="" width="344"><figcaption></figcaption></figure></div>

<figure><img src="../../.gitbook/assets/image (2).png" alt="" width="437"><figcaption></figcaption></figure>

Start by opening Hyper-V manager from the Start Menu

<figure><img src="../../.gitbook/assets/image (3).png" alt="" width="416"><figcaption></figcaption></figure>

## Creating a virtual switch

To create virtual switches (Networks) to connect your Ubuntu and 9800-CL, select "Virtual Switch Manager…"

<figure><img src="../../.gitbook/assets/image (4).png" alt="" width="375"><figcaption></figcaption></figure>

You want to create an "External" switch. In some other Hypervisors this is called "Bridged Adapter". This will connect the adapter of your virtual machine on the same network as your Ethernet adapter, and it will get an IP address on the same network.

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

Create the virtual switch as shown in this screenshot

* Use a descriptive name, like External (LAN)
* Choose "External network"
* Select your Ethernet adapter
* Enable "Allow management operating system to share this network adapter"
* Click OK when you are done

<figure><img src="../../.gitbook/assets/image (6).png" alt="" width="563"><figcaption></figcaption></figure>

## Download Ubuntu Server

Go to [https://ubuntu.com/download/server](https://ubuntu.com/download/server)

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption><p>Click "Download 24.04 LTS"</p></figcaption></figure>

## Create the VM

Open Hyper-V manager and click Action -> New -> Virtual Machine...

<figure><img src="../../.gitbook/assets/image (9).png" alt="" width="563"><figcaption></figcaption></figure>

Click past the first page. On page 2, specify a name. Click Next

<figure><img src="../../.gitbook/assets/image (10).png" alt="" width="563"><figcaption></figcaption></figure>

Specify Generation: Generation 2

<figure><img src="../../.gitbook/assets/image (11).png" alt="" width="563"><figcaption></figcaption></figure>

Assign 4GB memory

<figure><img src="../../.gitbook/assets/image (12).png" alt="" width="554"><figcaption></figcaption></figure>

On Configure Networking, select the "External (LAN)" vSwitch you created earlier

<figure><img src="../../.gitbook/assets/image (13).png" alt="" width="563"><figcaption></figcaption></figure>

For Hard Disk, create a VHDX disk with 40GB

<figure><img src="../../.gitbook/assets/image (14).png" alt="" width="563"><figcaption></figcaption></figure>

Installation Options: Use the Ubuntu Server ISO image you downloaded. Then click "Finish"

<figure><img src="../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

Right click you new machine, and select "Settings…"

<figure><img src="../../.gitbook/assets/image (16).png" alt="" width="539"><figcaption></figcaption></figure>

Under "Security" select Template: Microsoft UEFI Certificate Authority

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

Start your machine

<figure><img src="../../.gitbook/assets/image (18).png" alt="" width="209"><figcaption></figcaption></figure>

Skip the chapters for the other hypervisors, continue from the "Ubuntu Server common steps" chapter&#x20;

{% content-ref url="ubuntu-server-common-steps.md" %}
[ubuntu-server-common-steps.md](ubuntu-server-common-steps.md)
{% endcontent-ref %}
