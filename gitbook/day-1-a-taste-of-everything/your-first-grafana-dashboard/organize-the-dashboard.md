# Organize the dashboard

Now, we only need to organize our dashboard a bit. We can do this manually, or using the auto grid feature. Start by clicking outside any of the panels. You will get the dashboard layout options to the right.&#x20;

### Custom layout

Select:

* Panel layout: Custom

You can drag the panels around as you like, but they will snap up and to the left to avoid a messy layout. Each panel can be resized by pulling the lower right corner:

<figure><img src="../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

For now, you can try reproducing the following layout:

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

### Auto grid layout

The auto grid layout was introduced in Grafana 12. It enables a more dynamic layout, including the use of tabs within the dashboard. We will try this now, with a tab for each frequency band.

Select

* Panel layout: Auto grid
* Max columns: 2

<figure><img src="../../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

Then, drag the panels around so you get the Channel history of each band to the left of the RRM graph for that band. It will look like this.&#x20;

<figure><img src="../../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

Within each panel group the panels will be distributed to equal sizes. Depending on your preferences and the various visualizations/panel types you might want to use one or the other. For now, let's go back to the custom layout.

### Organizing panels in tabs

Select <kbd>Group Panels</kbd> below the panens, and the <kbd>Group into tab</kbd> option

<figure><img src="../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

Name the first tab <kbd>2.4GHz</kbd>

<figure><img src="../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

Create new tabs and name them <kbd>5GHz</kbd> and <kbd>6GHz</kbd>&#x20;

<figure><img src="../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

Drag and drop the 5GHz and 6GHz panels into their respective tabs

<figure><img src="../../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

Save and exit Edit mode. Your dashboard will now look like this:

<figure><img src="../../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

Clicking the other tabs will show their content

<figure><img src="../../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>





