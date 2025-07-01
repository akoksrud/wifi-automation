# YANG Suite

### About YANG Suite

YANG Suite is an installable tool that can be used to pull supported YANG models directly from the actual devices​. You can also use it to test communication to your device using RESTCONF and more.

<figure><img src="../../.gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
You will explore YANG Suite using one of the servers where it is pre-installed. The installation has some bindings to the IP of the server, so it should be installed when you have the permanent static IP of your server. If you want to install it on your own VM, the instructions are included in the optional Lab Exercise [install-yang-suite-optional.md](install-yang-suite-optional.md "mention"), beware that it will take a little while so you might want to do it later instead of during the deep dive&#x20;
{% endhint %}

In the pre-installed servers, YANG models will already be pulled from one of the pre-installed WLCs. To get an even distribution, you can spread so that if you have the following WLC, use the following Ubuntu Servers to explore YANG Suite

<figure><img src="../../.gitbook/assets/image (74).png" alt=""><figcaption></figcaption></figure>

### Starting YANG Suite

If YANG-Suite is not running on any of those machines, start it with the following commands

```bash
cd ~/yangsuite/docker
docker compose up -d
```

### Explore YANG modules











