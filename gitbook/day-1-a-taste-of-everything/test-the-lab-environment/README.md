# Test the lab environment

* [ ] Connect your laptop to the wired network
  * Ensure you get DHCP in the range 192.168.10.71-250
  * Ensure you get internet access through the wired connection
* [ ] Boot up your Ubuntu VM
  * Connect to the console of your Ubuntu VM
* [ ] Change from DHCP to static IP
  * If you are using Multipass: [Change to static IP ( Multipass)](change-to-static-ip-multipass.md)
  * If you are NOT using Multipass: [Change to static IP](change-to-static-ip.md)
* [ ] Access from your laptop to the shared devices
  * SSH from to one or more of the shared Ubuntu servers (192.168.10.11 - .18)
  * SSH and HTTPS to your designated WLC (192.168.10.51 / 53 / 55 / etc)

{% hint style="info" %}
You have admin access to all shared devices, please don't mess up for each other :sunglasses:
{% endhint %}

* [ ] Access from your Ubuntu Server to the devices
  * Ping from your Ubuntu VM to your designated WLC
  * Ping from your Ubuntu VM to the Internet
* [ ] Access from the WLC to your Ubuntu Server
  * Ping from your designated WLC to your Ubuntu VM

When done, go to the next chapter: [Explore VS Code](../explore-vs-code/)
