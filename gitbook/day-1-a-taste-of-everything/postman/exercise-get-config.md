# Exercise: Get config

You will create a RESTCONF request using YANG models that get the config from your IOS-XE device. Notice that this is NOT the "show run-config" version, it is the general config of the device, in JSON format.

Create the Request based on the information explored from [https://yangcatalog.org](https://yangcatalog.org/)

At the [https://yangcatalog.org](../yang-models/https-yangcatalog.org.md) website, navigate to <kbd>YANG Module Detail Viewer</kbd> and type/select the module <kbd>Cisco-IOS-XE-native</kbd> . Press "Get Details" and then "Tree View"

<figure><img src="../../.gitbook/assets/image (78).png" alt="" width="480"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (80).png" alt="" width="116"><figcaption></figcaption></figure>

Expand the tree until you find what you want to get, in this case the container named <kbd>native</kbd>

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure></div>

The "Base RESTCONF path" on a Cisco IOS-XE device is

```html
https://{{host}}/restconf/data
```

Add the "Sensor Path" from the YANG model, and you will get the full RESTCONF path that we will use in Postman:

```
https://{{host}}/restconf/data/Cisco-IOS-XE-native:native
```

Enter that path in Postman in the Request you created

<figure><img src="../../.gitbook/assets/image (82).png" alt=""><figcaption></figcaption></figure>

Go to "Headers" and enter the following:

<figure><img src="../../.gitbook/assets/image (83).png" alt=""><figcaption></figcaption></figure>

Press "Send" and you should get a response similar to this:

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure></div>

### YANG Suite alternative

To create the same path using YANG Suite, you will use the same "Base RESTCONF path"

```html
https://{{host}}/restconf/data
```

To find the "Sensor path" you use the field "Module" and "Xpath" in YANG Suite, but you have to substitute the forward slash in Xpath with a colon

<figure><img src="../../.gitbook/assets/image (5) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

```html
https://{{host}}/restconf/data/Cisco-IOS-XE-native:native
```
