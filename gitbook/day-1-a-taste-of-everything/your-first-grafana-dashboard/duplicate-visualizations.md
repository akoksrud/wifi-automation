# Duplicate visualizations

### Auto grid

Go back to the dashboard

In the Dashboard, click anywhere in the dashboard OUTSIDE your visualization. Then, in the Dashboard options to the right, select "Auto grid" and set the Max columns to 1.

<figure><img src="../../.gitbook/assets/image (146).png" alt=""><figcaption></figcaption></figure>

Then click  (Exit edit mode)

<figure><img src="../../.gitbook/assets/image (147).png" alt=""><figcaption></figcaption></figure>

No matter the width of your browser window, the visualization will fill the screen width

<figure><img src="../../.gitbook/assets/image (148).png" alt="" width="563"><figcaption></figcaption></figure>

### Duplicate visualization

We will now create a 5GHz and a 6GHz variant of our visualization panel. Don't worry, it will be much easier than creating the first one :relaxed:

Enter edit mode again, then by using the menu at the top right of your visualization, select <kbd>More...</kbd> and <kbd>Duplicate</kbd>&#x20;

<figure><img src="../../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

Edit the duplicated visualization

<figure><img src="../../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

Edit as follows:

* Panel options: Title = <kbd>AP RRM 5GHz $APName</kbd>
* Query (below the visualization): Select <kbd>radio\_slot\_id::tag</kbd> = <kbd>1</kbd>

Save, then go back to the dashboard

### Duplicate for 6GHz visualization

If your APs have a 6GHz radio, you can also do the same once more for the 6GHz radio:

* Panel options: Title = <kbd>AP RRM 6GHz $APName</kbd>
* Query (below the visualization): Select <kbd>radio\_slot\_id::tag</kbd> = <kbd>2</kbd>



My dashboard looks like this now (the test AP does not have 6GHz)

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure></div>





