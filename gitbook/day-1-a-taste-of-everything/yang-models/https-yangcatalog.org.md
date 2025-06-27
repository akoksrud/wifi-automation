# https://yangcatalog.org

### Opening yangcatalog.org

Open the following website: [https://yangcatalog.org](https-yangcatalog.org.md) and select <kbd>Module Detail Viewer</kbd>

<figure><img src="../../.gitbook/assets/image (64).png" alt=""><figcaption></figcaption></figure>

Here you can start typing parts of available YANG models. Try it out by typing <kbd>IOS-XE-wireless</kbd> (it is not case sensitive, I just don't the look of stuff with wrong case, it might be a medical condition on my side :smile:)

Select the <kbd>Cisco-IOS-XE-wireless-access-point-oper</kbd> model and click "Get details"

<figure><img src="../../.gitbook/assets/image (65).png" alt=""><figcaption></figcaption></figure>

Then click "Tree View"

<figure><img src="../../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

### Navigating the Tree View

1. Expand/collapse all nodes
2. Expand/collapse this branch
3. This is a container / list which contains other nodes
4. Hover the mouse ofer an element name to get the description popup
5. This is a leaf node which contain a single value of the datatype specified to the right
6. There is a lot of info to the right, use the (sometimes very elusive) scrollbar at the bottom!

<figure><img src="../../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

### Using values from yangcatalog

When navigating the tree view, here is where you find the values you will typically use, with examples

* <kbd>Path</kbd> - Used when configuring 9800 to send values as streaming telemetry. We will use this in the Grafana lab exercises to configure WLC to send specific data to be visualized in Grafana
* <kbd>Sensor Path</kbd> - Used when you need a RESTCONF path. We will use this in the Postman and Python lab exercises shortly, and in many of the Day 2 labs (both Python and Ansible labs)

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure></div>

### Viewing the YANG tree in text format

You can get the tree view of a YANG module in text format like this

<figure><img src="../../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

Go to the YANG Module Detail Viewer again (see top of this page). Search and find a module of your choice (be creative and use what you know... maybe "client-oper", "wlan-cfg" or "rrm". Click "Get details". A way down in the details table you will find <kbd>yang-tree</kbd> , click the link to the right there

<figure><img src="../../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

The tree will open in a separate page/tab, as shown in the screenshot above.
