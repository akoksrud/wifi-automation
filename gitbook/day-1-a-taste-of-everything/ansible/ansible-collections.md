# Ansible Collections

A collection is a premade collection of playbooks, roles, modules and plugins, usually for a specific purpose or type of devices

[https://docs.ansible.com/ansible/latest/collections/index.html#list-of-collections](https://docs.ansible.com/ansible/latest/collections/index.html#list-of-collections)

### Your installed collections

This is how to look up which collections you have installed in your environment

```bash
ansible-galaxy collection list

# /home/devnet-adm/wifi-automation/.venv/lib/python3.12/site-packages/ansible_collections
Collection                               Version
---------------------------------------- -------
amazon.aws                               9.5.0  
ansible.netcommon                        7.2.0  
ansible.posix                            1.6.2  
ansible.utils                            5.1.2  
ansible.windows                          2.8.0  
arista.eos                               10.1.1 
awx.awx                                  24.6.1 
azure.azcollection                       3.4.0  
check_point.mgmt                         6.4.1  
chocolatey.chocolatey                    1.5.3  
cisco.aci                                2.11.0 
cisco.asa                                6.1.0  
cisco.dnac                               6.31.3 
cisco.intersight                         2.1.0  
cisco.ios                                9.2.0  
cisco.iosxr                              10.3.1 
(...)
```

To check all installed collections with "cisco" in the name you can run the following:

```bash
ansible-galaxy collection list | grep cisco
cisco.aci                                2.11.0 
cisco.asa                                6.1.0  
cisco.dnac                               6.31.3 
cisco.intersight                         2.1.0  
cisco.ios                                9.2.0  
cisco.iosxr                              10.3.1 
cisco.ise                                2.10.0 
cisco.meraki                             2.21.3 
cisco.mso                                2.10.0 
cisco.nxos                               9.4.0  
cisco.ucs                                1.16.0 
community.ciscosmb                       1.0.10 
```

### Navigating the collections documentation

[https://docs.ansible.com/ansible/latest/collections/index.html#list-of-collections](https://docs.ansible.com/ansible/latest/collections/index.html#list-of-collections)

Go to the "Collections Index" and click the "cisco.ios" collection

<div align="left"><figure><img src="../../.gitbook/assets/image (21).png" alt="" width="202"><figcaption></figcaption></figure></div>

Click the "ios\_facts" module

![](<../../.gitbook/assets/image (19).png>)

Here you will find documentation and examples

<figure><img src="../../.gitbook/assets/image (22).png" alt="" width="419"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

