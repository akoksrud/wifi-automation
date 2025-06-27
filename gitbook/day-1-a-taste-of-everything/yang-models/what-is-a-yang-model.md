# What is a YANG model?

YANG models are structured representation of configurational and operational data. It is used primarily with NETCONF and RESTCONF. \
Below is an example of a part of the module <kbd>Cisco-IOS-XE-wireless-client-oper</kbd>

<figure><img src="../../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

Reference/download: [https://github.com/YangModels/yang/tree/main/vendor/cisco/xe/17151](https://github.com/YangModels/yang/tree/main/vendor/cisco/xe/17151) (for Cisco IOS-XE 17.15.1)

In this deep dive we will use YANG models for

* Specifying which data to send from the WLC with streaming telemetry (to visualize in Grafana)
* Read and write operations using Python
* Read and write operations using Ansible

One benefit of a read operation using the YANG model and RESTCONF (or NETCONF) is that reading a huge dictionary (like the table of all current clients on a high load WLC) is WAY faster and less resource demanding than alternatives like SNMP GET or parsing CLI output. An added bonus is that you will get it directly into your tool as a dictionary without further parsing.
