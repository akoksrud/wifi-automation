# Exercise: Get client summary

You will create a RESTCONF request using YANG models that get the client summary from your IOS-XE device.&#x20;

Create the Request based on the information explored from [https://yangcatalog.org](https://yangcatalog.org/)

At the [https://yangcatalog.org](../yang-models/https-yangcatalog.org.md) website, navigate to <kbd>YANG Module Detail Viewer</kbd> and type/select the module <kbd>Cisco-IOS-XE-wireless-client-oper</kbd> . Press "Get Details" and then "Tree View"

<figure><img src="../../.gitbook/assets/image (7).png" alt="" width="423"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (80).png" alt="" width="116"><figcaption></figcaption></figure>

Expand the tree until you find what you want to get, the container named <kbd>common-oper-data</kbd> . You may have to use the scroll bar down at the bottom to scroll over to "Sensor Path". The scroll bar might be a bit difficult to find.

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure></div>

The "Base RESTCONF path" on a Cisco IOS-XE device is

```html
https://{{host}}/restconf/data
```

Add the "Sensor Path" from the YANG model, and you will get the full RESTCONF path that we will use in Postman. You can use the "Copy" icon to copy the sensor path.

{% code fullWidth="true" %}
```
https://{{host}}/restconf/data/Cisco-IOS-XE-wireless-client-oper:client-oper-data/common-oper-data
```
{% endcode %}

Duplicate the previous request as in the previous exercises.

Enter the new path in Postman in the Request you created

<figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

Press "Send" and you should get a response similar to this. In this example, no users were connected, so it will return "No Content" (status code 204). With connected users you will get some JSON content.

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure></div>

### YANG Suite alternative

To create the same path using YANG Suite, you will use the same "Base RESTCONF path"

```html
https://{{host}}/restconf/data
```

To find the "Sensor path" you use the field "Module" and "Xpath" in YANG Suite, but you have to substitute the forward slash in Xpath with a colon

<figure><img src="../../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

{% code fullWidth="true" %}
```html
https://{{host}}/restconf/data/Cisco-IOS-XE-wireless-client-oper:client-oper-data/common-oper-data
```
{% endcode %}

