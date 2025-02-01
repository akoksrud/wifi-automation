import requests
import getpass
import pandas as pd

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
    ap_table = pd.json_normalize(response.json()['Cisco-IOS-XE-wireless-client-oper:common-oper-data'])
    print(ap_table)
    ap_table.to_excel('ap_table.xlsx')
else:
    print(f"Status code: {response.status_code}: {response.reason}")
