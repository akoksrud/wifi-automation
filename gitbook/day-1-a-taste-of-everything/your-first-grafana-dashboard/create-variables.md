# Create variables

### Selectable variable

We will create a couple of variables that we can use in our dashboards. In this dashboard, we will have drop-down menus at the top of our dashboard to select which AP we want to see statistics for. Similar variables can be created for WLCs, clients, switches, frequency bands, SD-WAN Managers, FTDs, etc.

Our variable will get all AP names and put them in a selectable list.

Go to Dashboard settings -> Variables

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure></div>

For copy-paste, here is the text in the Query box:

```
SHOW TAG VALUES WITH KEY = "wtp_name"
```



### Helper variable

We will also create a helper variable. That is a variable that will be used in the dashboards, but it will not be shown as a selection box. This is controlled through the "Show on dashboard" setting.

<figure><img src="../../.gitbook/assets/image (1).png" alt="" width="514"><figcaption></figcaption></figure>

1. Do not show the variable selection box on the dashboard
2. Enter the following text in the Query box:

{% code overflow="wrap" %}
```sql
SELECT distinct("wtp_mac") FROM "Cisco-IOS-XE-wireless-access-point-oper:access-point-oper-data/ap-name-mac-map" WHERE ("wtp_name" =~ /^$APName$/)
```
{% endcode %}

Check if it is working with Run query:

<figure><img src="../../.gitbook/assets/image (2).png" alt="" width="341"><figcaption></figcaption></figure>

Press Apply, then Save dashboard on top of screen

<figure><img src="../../.gitbook/assets/image (104).png" alt="" width="375"><figcaption></figcaption></figure>





