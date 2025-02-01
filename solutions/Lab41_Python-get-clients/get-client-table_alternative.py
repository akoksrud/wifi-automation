import requests
import getpass
import json

wlc = input("Enter WLC IP: ")
user = input("Enter user: ")
password = getpass.getpass("Enter password: ")
url = f"https://{wlc}/restconf/data/Cisco-IOS-XE-wireless-client-oper:client-oper-data/common-oper-data"
payload = {}
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
  }

response = requests.get(url, auth=(user, password), headers=headers, data=payload, verify=False)
if (response.status_code==200):
    print(json.dumps(response.json(), indent=4))
else:
    print(f"Status code: {response.status_code}: {response.reason}")
