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













### Linting errors - and fixing them













### Example run of the finished playbook
