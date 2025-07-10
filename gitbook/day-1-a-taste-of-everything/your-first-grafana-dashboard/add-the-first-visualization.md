# Add the first visualization

Go back to the dashboard main page

<figure><img src="../../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

Press <kbd>+ Add visualization</kbd>

<figure><img src="../../.gitbook/assets/image (109).png" alt="" width="251"><figcaption></figcaption></figure>

Press the influxdb database in the data source list

<figure><img src="../../.gitbook/assets/image (108).png" alt=""><figcaption></figcaption></figure>

<kbd>Time Series</kbd> is automatically selected. This is the type of visualization that we will use now, so no need to change

<figure><img src="../../.gitbook/assets/image (110).png" alt=""><figcaption></figcaption></figure>

In the lower part of the screen we will create the database query that is going to tell Grafana what to show in the visualization. We start by clicking <kbd>select measurement</kbd>&#x20;

<figure><img src="../../.gitbook/assets/image (111).png" alt=""><figcaption></figcaption></figure>

You will get a menu of all measurements plus the variables we created. The measurements will be named by the full Xpath in the YANG model that we used to send them from the WLC. Select the\
<kbd>Cisco-IOS-XE-wireless-rrm-oper:rrm-oper-data/rrm-measurement/load</kbd>

<figure><img src="../../.gitbook/assets/image (112).png" alt=""><figcaption></figcaption></figure>

(Optional) You can enter [https://yangcatalog.org](../yang-models/https-yangcatalog.org.md), find the Cisco-IOS-XE-wireless-rrm-oper module and explore which values you could get from this YANG model

Click the <kbd>+</kbd> to the right of WHERE, and select <kbd>wtp\_mac::tag</kbd>&#x20;

Then, click <kbd>select tag value</kbd> and select <kbd>/^$APMac$/</kbd>

<figure><img src="../../.gitbook/assets/image (113).png" alt=""><figcaption></figcaption></figure>

Click the + to the right of that again, and select <kbd>radio\_slot\_id::tag</kbd>

<figure><img src="../../.gitbook/assets/image (114).png" alt=""><figcaption></figcaption></figure>

Click <kbd>select tag value</kbd> and select <kbd>0</kbd> . The first line should now look like this:

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (116).png" alt=""><figcaption></figcaption></figure></div>

Now we will start on the second line. Click <kbd>field (value)</kbd> and select <kbd>cca\_util\_percentage</kbd>&#x20;

<figure><img src="../../.gitbook/assets/image (117).png" alt=""><figcaption></figcaption></figure>

Click the <kbd>+</kbd> to the right, and select <kbd>last()</kbd> . You can search when you have clicked the +.&#x20;

Click the <kbd>+</kbd> again and select <kbd>alias()</kbd>. The line should now look like this:

<figure><img src="../../.gitbook/assets/image (118).png" alt=""><figcaption></figcaption></figure>

Click the text (alias) inside the parentheses and you will get a typing box like this:

<figure><img src="../../.gitbook/assets/image (119).png" alt=""><figcaption></figcaption></figure>

Write the text <kbd>CCA Util%</kbd>  <mark style="color:red;">!!!! and press ENTER !!!!</mark> (not Esc or Tab or anything else). Now, this line should look like this:

<figure><img src="../../.gitbook/assets/image (120).png" alt=""><figcaption></figcaption></figure>

Now we will add some more rows. Click the <kbd>+</kbd> to the rlight of our alias box and add another field (you can search in the box)

<figure><img src="../../.gitbook/assets/image (122).png" alt=""><figcaption></figcaption></figure>

It will copy the previous line:

<figure><img src="../../.gitbook/assets/image (123).png" alt=""><figcaption></figcaption></figure>

Now, edit the rest of the query to look like this:

<figure><img src="../../.gitbook/assets/image (124).png" alt=""><figcaption></figcaption></figure>

In the bottom of the query, in the ALIAS field, write <kbd>$col</kbd>

<figure><img src="../../.gitbook/assets/image (125).png" alt=""><figcaption></figcaption></figure>

You will see the descriptions below the graph updated to show the aliases of the fields instead of the full Xpath:

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

We now have a graph that looks something like this. In the next section we will customize how it looks.

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure></div>
