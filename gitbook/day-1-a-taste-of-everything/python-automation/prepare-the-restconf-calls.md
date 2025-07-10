# Prepare the RESTCONF calls

Using Postman, test the RESTCONF calls to get the AP table from your WLC. You can open the RESTCONF call that you created in [exercise-get-ap-summary.md](../postman/exercise-get-ap-summary.md "mention") which is the one we will continue to use in this exercise.

The URL of the RESTCONF call we will use is

{% code fullWidth="true" %}
```url
https://{{host}}/restconf/data/Cisco-IOS-XE-wireless-access-point-oper:access-point-oper-data/capwap-data
```
{% endcode %}

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure></div>

The result should look similar to this:

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

This will return a lot of data. It might not matter for small deployments or one-off scripts, but if you will run recurring calls on large datasets it might be good to know how to reduce the dataset returned from the device. We do this by using an option in the URL called "fields", and can be done like this (for quite a number of fields, but WAY less than the default number that will be returned)

{% code overflow="wrap" %}
```
https://{{host}}/restconf/data/Cisco-IOS-XE-wireless-access-point-oper:access-point-oper-data/capwap-data?fields=wtp-mac;wtp-ip;name;ap-state;device-detail/static-info/board-data/wtp-serial-num;device-detail/static-info/board-data/wtp-enet-mac;device-detail/static-info/ap-models/model;tag-info/tag-source;tag-info/policy-tag-info;tag-info/site-tag;tag-info/rf-tag;tag-info/filter-info/filter-name;ap-time-info/boot-time;ap-time-info/join-time
```
{% endcode %}
