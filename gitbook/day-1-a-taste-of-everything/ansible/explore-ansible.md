---
description: >-
  In this lab you will be given a basic task to get you started with Ansible.
  More advanced exercises is available in the "Day 2" content.
---

# Explore Ansible

### Gather facts

We start by creating a folder for this exercise, inside our working folder \~/wifi-automation/

```bash
cd ~/wifi-automation
mkdir ansible-gather-facts
```

The folder will show up automatically in VS Code

<div align="center"><figure><img src="../../.gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure></div>

You can create files and folders from VS Code as well. Do that now  by right-clicking the folder name, then <kbd>New File...</kbd>

<div align="center"><figure><img src="../../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure></div>

Name the file <kbd>gather-facts-playbook.yml</kbd>

<figure><img src="../../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

VS Code will automatically open the new file. Paste the following contents into the file, then save it

```yaml
---
- name: IOS Facts
  hosts: wlc
  connection: network_cli
  gather_facts: false
  tasks:
    - name: Gather all legacy facts
      cisco.ios.ios_facts:
        gather_subset: all
      register: facts1
    - name: Show facts
      ansible.builtin.debug:
        msg: "{{ facts1 }}"
```

Notice that when recognized as an Ansible file type (because we had "playbook" in the file name), VS Code will apply Ansible color styles to the file. It will help you spot errors when you are more familiar with Ansible.

<figure><img src="../../.gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>

### Ansible hosts file

The playbook we have created is an important part. Equally important is the inventory, which will tell Ansible which devices to run the playbook on. Create a file named <kbd>hosts.yml</kbd>

<figure><img src="../../.gitbook/assets/image (37).png" alt=""><figcaption></figcaption></figure>

In the terminal, enter the directory and verify that you can see the file that you created in VS Code in the folder structure.

```bash
cd ~/wifi-automation
cd ansible-gather-facts
ls -l
```

<figure><img src="../../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

The hosts.yml file should be open in the editor. Copy the following text to the file, and change the placeholder <kbd>{WLC-IP}</kbd>  to the IP address of the WLC you have been assigned

```yaml
wlc:
  hosts:
    192.168.10.{WLC-IP}:
  vars:
    ansible_connection: network_cli
    ansible_network_os: ios
    ansible_ssh_pass: ChangeMe2025!
    ansible_password: ChangeMe2025!
    ansible_user: devnet-adm
```

When you have unsaved changes in an open file, a white dot will show beside the file name:

<figure><img src="../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

Save the file (Ctrl+S). The white dot will disappear.

<figure><img src="../../.gitbook/assets/image (44).png" alt=""><figcaption></figcaption></figure>

### Fix dependencies

We will now try to run the playbook

* [ ] Go to the terminal in VS Code (or open it if it is closed)
* [ ] Verify that your venv is activated, it should show (wifi-automation) at the beginning of the line (or other place depending on your shell customization). If not, you can exit and re-open your terminal, or run

```bash
source ~/wifi-automation/.venv/bin/activate
```

* [ ] Enter the playbook folder

```bash
cd ~/wifi-automation
cd ansible-gather-facts
```

Run the playbook using the <kbd>ansible-playbook</kbd> command and specifying your inventory with the -i parameter

```bash
ansible-playbook -i hosts.yml gather-facts-playbook.yml
```

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure></div>

The warning outlined in blue shows us that we are missing a package called <kbd>ansible-pylibssh</kbd>  which we will use to connect to the WLC. Let's install the missing package

```bash
uv pip install ansible-pylibssh
```

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure></div>

### SSH host key checking

After installing the missing package, try running the ansible-playbook command again. Yet another error message is thrown, telling you that the authenticity of the host can't be established.

```bash
ansible-playbook -i hosts.yml gather-facts-playbook.yml
```

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure></div>

Depending on your environment and the type of playbook, host key checking could be a vital part of the security. For this deep dive we will not care much, and we will disable the host key checking in the inventory file. For some types of playbooks this might be the intended mode of operation.

Add the following line to the bottom of your <kbd>hosts.yml</kbd> file

```yaml
ansible_host_key_checking: false
```

The file will look like this (except your WLC IP will be different):

<figure><img src="../../.gitbook/assets/image (46).png" alt=""><figcaption></figcaption></figure>

### Gather facts - successful play

Run the playbook again:

```bash
ansible-playbook -i hosts.yml gather-facts-playbook.yml
```

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure></div>

### Use return values

If we take a look at the last part of our playbook, we can see the variable "facts1", which is populated with data in the line `register: facts1` and used in the line `msg: "{{ facts1 }}"` .

<figure><img src="../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

This variable is a dictionary, and you can pull any subset of information by using dot-notation or bracket-notation for accessing dictionaries. Let us try this in a couple of examples.&#x20;

* [ ] Find the values to use, by browsing the output from the previous play.&#x20;
  * The section marked "1." is the first level to use, and will return everything at that level (essentially, everything below).&#x20;
  * The two section marked "2." are at the second level in the dictionary (JSON represented here), and if we specify one of those they will return only the corresponding blue marked sections.
  * Let us try it out, so it will hopefully make some sense :)

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (49).png" alt=""><figcaption></figcaption></figure></div>

* [ ] Use dot-notation to return the value from "ansible\_net\_hostname".&#x20;

<figure><img src="../../.gitbook/assets/image (50).png" alt=""><figcaption></figcaption></figure>

Save the file, then run the playbook again.

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (51).png" alt=""><figcaption></figcaption></figure></div>

* [ ] Use bracket-notation to return the value from "ansible\_net\_interfaces". Notice that when you use double quotes on the outside of the statement, you MUST use single quotes inside. You can do the opposite also, but you can NOT use the same type of quotes when you have to use quotes inside a quoted statement. This is true for most programming languages.

<figure><img src="../../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

Again, save the file... then run the playbook again.

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure></div>

* [ ] Use the run-config which was returned as a part of the "facts1" dictionary in a new task that will save this to a file
  * First, remove the "Show facts" task
  * Create a new task instead, with name "Write run-config to file"
  * Use the "ansible.builtin.copy" module
    * Documentation on Ansible Community Documentation: [https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy\_module.html](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html)

{% code fullWidth="true" %}
```yaml
---
- name: IOS Facts
  hosts: wlc
  connection: network_cli
  gather_facts: no
  tasks:
    - name: Gather all legacy facts
      cisco.ios.ios_facts:
        gather_subset: all
      register: facts1
    - name: Write run-config to file
      ansible.builtin.copy:
        content: "{{ facts1.ansible_facts.ansible_net_config }}"
        dest: "{{ './' + facts1.ansible_facts.ansible_net_hostname + '-run-conf.txt' }}"

```
{% endcode %}

We are using both the "ansible\_net\_config" and the "ansible\_net\_hostname" in this example

<figure><img src="../../.gitbook/assets/image (55).png" alt=""><figcaption></figcaption></figure>

Save the file. Don't mind if you get a couple of linting errors, we will fix them shortly...  For now, run the playbook again.&#x20;

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure></div>

Notice a new file has been created, with the run-config.

<figure><img src="../../.gitbook/assets/image (57).png" alt=""><figcaption></figcaption></figure>

Now.... imagine doing this same task, just changing the inventory to contain all your switches and WLCs? If you want to try it out, just change the inventory to contain all WLCs in this deep dive lab

<figure><img src="../../.gitbook/assets/image (58).png" alt=""><figcaption></figcaption></figure>

### Linting errors - and fixing them

If you copied the contents of the playbook above, you should get two linting errors when you saved the file. The first one you might be able to work out yourself how to fix. And you can try the second one as well by following the link in the message, and maybe some help from the internet or an AI assistant. Or just read below and follow along for the solutions

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure></div>

The first linting error is because Ansible want boolean operators to be either <kbd>true</kbd> or <kbd>false</kbd> . That means that <kbd>yes</kbd>, <kbd>no</kbd>, <kbd>True</kbd>, <kbd>False</kbd>, <kbd>0</kbd> or <kbd>1</kbd> is not valid, even though some of them might work perfectly fine. We fix this error by replacing <kbd>no</kbd> with <kbd>false</kbd>.

```yaml
  gather_facts: false
```

The second linting error is because when writing files (by using copy or other file writing modules) you should always explicitly specify the file permissions. We fix this by adding the line <kbd>mode: "0600"</kbd>

```yaml
        mode: "0600"
```

The playbook should look like this:

<figure><img src="../../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

{% code fullWidth="true" %}
```yaml
---
- name: IOS Facts
  hosts: wlc
  connection: network_cli
  gather_facts: false
  tasks:
    - name: Gather all legacy facts
      cisco.ios.ios_facts:
        gather_subset: all
      register: facts1
    - name: Write run-config to file
      ansible.builtin.copy:
        content: "{{ facts1.ansible_facts.ansible_net_config }}"
        dest: "{{ './' + facts1.ansible_facts.ansible_net_hostname + '-run-conf.txt' }}"
        mode: "0600"

```
{% endcode %}

### Example run of the finished playbook

Running the finished playbook and listing the files in the folder should look like this. It will be some more devices and run-config files if you modified the inventory to run on more devices.

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure></div>
