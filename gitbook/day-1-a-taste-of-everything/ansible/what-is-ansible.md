# What is Ansible

* Automation using "playbooks" written in YAML format
* Agent-less architecture
  * No installation on the managed nodes
* Idempotency
  * Does not change/write if target is already in state described by playbook
* Control node
  * System where Ansible is installed and runs the playbooks
* Inventory
  * List of managed nodes where the playbook will affect
* Managed nodes
  * Remote systems that are the targets of your playbooks

<figure><img src="../../.gitbook/assets/image (22).png" alt="" width="462"><figcaption></figcaption></figure>

### Plugins

* Extends the core functionality of Ansible
* Examples
  * cisco.ios.ios cliconf - To run CLI commands on Cisco IOS device
  * Become plugins, how to get write access on various systems ("sudo", "enable" etc)
  * Connection plugins, like SSH

### Modules

* Built-in or custom code snippets to perform various tasks
* A special type of plugin
*   Examples

    * cisco.ios.ios\_config

    <div align="left"><figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1).png" alt="" width="345"><figcaption></figcaption></figure></div>

    * cisco.ise.endpoint

    <div align="left"><figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1) (1).png" alt="" width="261"><figcaption></figcaption></figure></div>







