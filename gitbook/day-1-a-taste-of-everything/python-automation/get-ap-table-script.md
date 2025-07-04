# Get AP Table script

Copy the following code to your Python file <kbd>get-ap-table.py</kbd> in VS Code. We will explain the different parts below.

{% code overflow="wrap" fullWidth="false" %}
```python
import requests
import pandas as pd
import getpass

wlc = input("Enter WLC IP: ")
user = input("Enter user: ")
password = getpass.getpass("Enter password: ")
url = f"https://{wlc}/restconf/data/Cisco-IOS-XE-wireless-access-point-oper:access-point-oper-data/capwap-data?fields=wtp-mac;wtp-ip;name;ap-state;device-detail/static-info/board-data/wtp-serial-num;device-detail/static-info/board-data/wtp-enet-mac;device-detail/static-info/ap-models/model;tag-info/tag-source;tag-info/policy-tag-info;tag-info/site-tag;tag-info/rf-tag;tag-info/filter-info/filter-name;ap-time-info/boot-time;ap-time-info/join-time"

payload = {}
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
  }

response = requests.get(url, auth=(user, password), headers=headers, data=payload, verify=False)

if (response.status_code==200):
    ap_table = pd.json_normalize(response.json()['Cisco-IOS-XE-wireless-access-point-oper:capwap-data'])
    print(ap_table)
    ap_table.to_excel('ap_table.xlsx')
    ap_table.to_csv('ap_table.csv')
else:
    print(f"Status code: {response.status_code}: {response.reason}")

```
{% endcode %}

<figure><img src="../../.gitbook/assets/image (4) (1).png" alt=""><figcaption></figcaption></figure>

1. Import the modules we will use
2. WLC IP, username and password as input fields, it will be asked when running the script
3. Create the RESTCONF call using the IP of your WLC, and the path you tested with Postman
4. Make the call and save the response
5. Some very basic error checking
6. The response is given as JSON. We use a pandas function "json\_normalize" to flatten parts of the JSON object to present it in a table
7. Print the table in the terminal, then save the table to Excel and CSV
