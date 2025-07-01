# Postman

In this lab exercise we will\


* Create a Workspace
* Create an Environment
* Create a Collection
* Test some queries found from yangcatalog.org or YANG Suite (any of your choice)
* Output code to CURL or Python

### Overview

Postman is a "go-to" tool for RESTCONF APIs. Some examples for automation is testing and validating RESTCONF calls to IOS-XE devices before implementing in Python, Ansible, etc.

Here is an example view of Postman and how the YANG modules from previous exercises can look. We will test and explain this in more detail in this exercise

Refer to the figure:

1. RESTCONF path
2. YANG module
3. Xpath

<div data-full-width="true"><figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure></div>

### Launching Postman

Start by launching Postman. You should already be logged in from the pre-lab task. If not, log in now. It might look something like this

<div data-full-width="true"><figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure></div>

### Create Workspace

Navigate to <kbd>Workspaces > Create Workspace</kbd>

<figure><img src="../.gitbook/assets/image (9).png" alt="" width="399"><figcaption></figcaption></figure>

Select <kbd>Blank workspace</kbd> , then <kbd>Next</kbd>&#x20;

<p align="center"> <img src="../.gitbook/assets/image (10).png" alt=""></p>

Select <kbd>Only me</kbd>, then <kbd>Create</kbd>

<figure><img src="../.gitbook/assets/image (11).png" alt="" width="264"><figcaption></figcaption></figure>

&#x20;Create Environment

After creating the "Automation workspace", navigate to <kbd>Environments</kbd> , then click the <kbd>+</kbd> button to create a new environment in the workspace

<figure><img src="../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

Instead of "New Environment" create a descriptive name, like "Lab devices WLPC"

<figure><img src="../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

Activate the new environment by selecting it in the menu in the top right corner of the window. It should say "No environment" before you select your environment

<figure><img src="../.gitbook/assets/image (15).png" alt="" width="363"><figcaption></figcaption></figure>

Then, create some variables

* <kbd>Initial value</kbd> - Values in this column are synced to your Postman account
* <kbd>Current value</kbd> - Values in this column are only stored locally in Postman on your PC

<figure><img src="../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

Remember to save the variables by pressing the <kbd>Save</kbd> button in the top right corner

### A word about saving

Saving deserves its own chapter. It is very common to forget saving :relaxed:

This little orange dot means the file/tab/whatever is not saved. Later, you will also see a similar behavior in VS Code (only using a white dot instead).

<figure><img src="../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

Use Ctrl+S to save the current tab, or click this icon ![](<../.gitbook/assets/image (18).png>)

An example: When you run a RESTCONF call with variables from an environment, like <mark style="color:orange;">`{{host}}`</mark> or <mark style="color:orange;">`{{password}}`</mark> it will use the value from your SAVED file. So if you do changes in the environment, remember to save the tab

### Create Collection

We will now create a "Collection" which is a collection of RESTCONF calls. You can group it the way you like, in this exercise we will create a collection for a specific device (Cisco WLC 9800)

1. Select <kbd>Collections</kbd>  (see large screenshot below)
2. Click the <kbd>+</kbd> and create a Blank collection

<div align="left"><figure><img src="../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure></div>

3. Rename the collection

<div align="left"><figure><img src="../.gitbook/assets/image (21).png" alt="" width="155"><figcaption></figcaption></figure></div>

4. Click <kbd>Authorization</kbd> select <kbd>Basic Auth</kbd> Enter Username and Password like this\
   Creating the variables like this will make Postman get them from the current active environment (that we just created)

<div data-full-width="true"><figure><img src="../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure></div>

Again... remember to save :relaxed:

### Create your first Request







### Exercise: Get config







### Exercise: Get AP summary







### Exercise: Get client summary







### Output to Python







