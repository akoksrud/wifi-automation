# YANG Suite

### About YANG Suite

YANG Suite is an installable tool that can be used to pull supported YANG models directly from the actual devices​. You can also use it to test communication to your device using RESTCONF and more.

<figure><img src="../../.gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
You will explore YANG Suite using one of the servers where it is pre-installed. The installation has some bindings to the IP of the server, so it should be installed when you have the permanent static IP of your server. If you want to install it on your own VM, the instructions are included in the optional Lab Exercise [install-yang-suite-optional-todo.md](install-yang-suite-optional-todo.md "mention"), beware that it will take a little while so you might want to do it later instead of during the deep dive&#x20;
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

* [ ] Log in to YANG Suite
* [ ] Go to Explore -> YANG -> Select a YANG. Select a YANG model and click the "Load module(s)" button <img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="line">

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (11) (1).png" alt=""><figcaption></figcaption></figure></div>

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure></div>

This is the info you typically use to craft NETCONF and RESTCONF calls (Postman, Python, Ansible, etc) or create streaming telemetry subscriptions (from WLC)

### Explore more YANG modules

We will now check out a couple of more YAG modules. Just get somewhat familiar, you will use these in the next lab exercises (Postman, Python, Ansible, Grafana).&#x20;

{% hint style="info" %}
Browsing the YANG modules wil give you the model, not pull the actual data from the device. To pull data we will use the models in Postman and Grafana later.
{% endhint %}

* [ ] Get AP summary

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (5) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure></div>

* [ ] Get client summary

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (6) (1) (1) (1).png" alt=""><figcaption></figcaption></figure></div>

### (Optional - RESTCONF/NETCONF from YANG Suite)

You can also perform the actual RESTCONF call (or similar for NETCONF) to the device and pull actual data. In YANG Suite, navigate to:

* Protocols > RESTCONF > Find your module > Generate API(s) > Authorize > Try it out > Execute

<figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>



