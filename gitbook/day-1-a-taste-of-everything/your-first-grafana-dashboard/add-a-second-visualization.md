# Add a second visualization

### State timeline

We will now add another type of visualization: State timeline. Start by entering Edit mode

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

Press <kbd>+ Add panel</kbd> below the current visualizations

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

Name the new panel <kbd>Channel history 2.4GHz</kbd> then click "Configure"

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

Click the field that defaults to "Time series" and search/select <kbd>State timeline</kbd>

<figure><img src="../../.gitbook/assets/image (4).png" alt="" width="461"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5).png" alt="" width="499"><figcaption></figcaption></figure>

Follow the same procedure as you did with the first panel, to recreate this query (remember the <kbd>$col</kbd> at the bottom):

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure></div>

It is not very useful or impressive yet :cry:

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

### Customizing the options

State timeline:

* Merge equal consecutive values: Enabled
* Align values: Center
* Row height: 0.8
* Fill opacity: 100
* Connect null values: Always

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

Standard options:

* Color scheme: Classic pallette

<figure><img src="../../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

Remember to save

<figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

### Duplicate the panel

Go back to the dashboard, and duplicate the new state timeline panel you created, if you have 6GHz radio on your AP, duplicate it twice. For each duplication, change

* Name: <kbd>Channel history 5GHz</kbd> (or 6GHz)
* Query -> <kbd>radio\_slot\_id::tag</kbd>:
  * 1 = 5GHz
  * 2= 5GHz dual radio or 6GHz (may not exist)
  * 3 = 6GHz (may not exist)

<figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>











