# Exercise: Get AP summary

You will create a RESTCONF request using YANG models that get the AP summary from your IOS-XE device.&#x20;

Create the Request based on the information explored from [https://yangcatalog.org](https://yangcatalog.org/)

At the [https://yangcatalog.org](../yang-models/https-yangcatalog.org.md) website, navigate to <kbd>YANG Module Detail Viewer</kbd> and type/select the module <kbd>Cisco-IOS-XE-wireless-access-point-oper</kbd> . Press "Get Details" and then "Tree View"

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png" alt="" width="480"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (80).png" alt="" width="116"><figcaption></figcaption></figure>

Expand the tree until you find what you want to get, in this case the container named <kbd>capwap-data</kbd> . Also note that the middle of the screenshot is cut away (dotted black line) since it was way to wide to show properly. Use the scroll bar down at the bottom to scroll over to "Sensor Path". The scroll bar might be a bit difficult to find.

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

The "Base RESTCONF path" on a Cisco IOS-XE device is

```html
https://{{host}}/restconf/data
```

Add the "Sensor Path" from the YANG model, and you will get the full RESTCONF path that we will use in Postman. You can use the "Copy" icon to copy the sensor path.

{% code fullWidth="true" %}
```
https://{{host}}/restconf/data/Cisco-IOS-XE-wireless-access-point-oper:access-point-oper-data/capwap-data
```
{% endcode %}

Duplicate the previous request, then you don't have to enter the Headers again

<figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Enter the new path in Postman in the Request you created

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (4) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure></div>

Press "Send" and you should get a response similar to this:

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (5) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure></div>

### YANG Suite alternative

To create the same path using YANG Suite, you will use the same "Base RESTCONF path"

```html
https://{{host}}/restconf/data
```

To find the "Sensor path" you use the field "Module" and "Xpath" in YANG Suite, but you have to substitute the forward slash in Xpath with a colon

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

{% code fullWidth="true" %}
```html
https://{{host}}/restconf/data/Cisco-IOS-XE-wireless-access-point-oper:access-point-oper-data/capwap-data
```
{% endcode %}
