---
description: Section created in cooperation with Kjetil Teigen Hansen (@mrTeigen)
---

# Install Grafana / TIG-stack

{% hint style="info" %}
This exercise is marked as optional. However, if you plan on doing more Grafana stuff on day to we highly recommend that you do this, even if it will take some extra time today, or continue on to day 2. If you plan doing primarily Python or Ansible stuff on day 2, you can skip this exercise (installing TIG stack) and skip to the next section ([your-first-grafana-dashboard](../your-first-grafana-dashboard/ "mention")). You can then use the installation on one of the pre-installed Ubuntu Servers.
{% endhint %}

In this lab exercise, we will install the "TIG stack" as a Docker container on the Ubuntu server. As part of the installation we will

* Create a .env file containing variables
* Ensure persistent storage
* Create a database to store our data

The next sections will give some basic overview of the TIG stack and how it all fits together

T = Telegraf

I = InfluxDB

G = Grafana

