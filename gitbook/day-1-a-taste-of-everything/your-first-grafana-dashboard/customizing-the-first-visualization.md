# Customizing the first visualization

### Common options (for all fields in this visualization)

In the field to the right you have lots of configuration options. The sections can be expanded or collapsed by using the small arrows to the right. Start by collapsing all of them to look like this screenshot. We will use the sections marked 1-4 which will be explained below.

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

1. Panel options: Set the panel title as follows. Notice how we use the variable we created. The actual title of the panel will follow the AP Name that we select in the variable selection box above the visualization

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt="" width="284"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

2. Graph styles: Set the <kbd>Line interpolation</kbd> and <kbd>Connected null values</kbd> as follows. You can try the other settings if you want and see the result on the graph.

<figure><img src="../../.gitbook/assets/image (5) (1).png" alt=""><figcaption></figcaption></figure>

3. Standard options: Set the Unit to Percent (0-100). As in the other boxes, it is possible to search

<figure><img src="../../.gitbook/assets/image (6) (1).png" alt=""><figcaption></figcaption></figure>

Also, set the <kbd>Min</kbd> to 0 and <kbd>Max</kbd> to 100. Set the <kbd>Decimals</kbd> to 0. Keep the other settings at their default values. The section should look like this

<figure><img src="../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

### Overrides (for specific fields)

Most of the fields in this visualization are correct to show as percent. But the number of connected clients should not be shown as percent, it should be shown as actual number of clients. To make this change for only the stations field we create a field override. This is located below the other sections in the options area to the right.

4. Add field override: Select <kbd>Fields with name matching regex</kbd>

<figure><img src="../../.gitbook/assets/image (9) (1).png" alt=""><figcaption></figcaption></figure>

Type in <kbd>/.\*Clients/</kbd> (it will also work with only <kbd>.\*Clients.\*</kbd> or create your own regex)

<figure><img src="../../.gitbook/assets/image (11) (1).png" alt=""><figcaption></figcaption></figure>

Then click <kbd>+ Add override property</kbd> . Start typing "un" to show the <kbd>Unit</kbd> choice.

<figure><img src="../../.gitbook/assets/image (12) (1).png" alt=""><figcaption></figcaption></figure>

When you select the Standard options > Unit choice, you get another box that will let you choose the unit to use. Click the <kbd>Choose</kbd> field and start typing (or select) the unit <kbd>short</kbd>&#x20;

<figure><img src="../../.gitbook/assets/image (13) (1).png" alt=""><figcaption></figcaption></figure>

You can also choose other units, the unit <kbd>Number</kbd> would be an appropriate unit for the number of connected clients, so let us change to that. It is the first choice in the list.

<figure><img src="../../.gitbook/assets/image (14) (1).png" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">!!! For the next instruction, DO NOT press the Esc key. Use the "Back to dashboard" button !!!</mark>

<figure><img src="../../.gitbook/assets/image (16) (1).png" alt=""><figcaption></figcaption></figure>

Go back to the dashboard, it will look similar to this screenshot. I have resized the browser window to make it fit nicely in the screenshot, your dashboard will be a little more spread.

<figure><img src="../../.gitbook/assets/image (15) (1).png" alt=""><figcaption></figcaption></figure>

In the next section we will make some more customizations. They are optional so if you want to skip a chapter that will be perfectly fine :relaxed:
