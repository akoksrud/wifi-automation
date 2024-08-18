import requests
import pandas as pd
import json
import openpyxl
import getpass

url = "https://192.168.10.10/restconf/data/Cisco-IOS-XE-wireless-access-point-oper:access-point-oper-data/capwap-data?fields=wtp-mac;wtp-ip;name;ap-state;device-detail/static-info/board-data/wtp-serial-num;device-detail/static-info/board-data/wtp-enet-mac;device-detail/static-info/ap-models/model;tag-info/tag-source;tag-info/policy-tag-info;tag-info/site-tag;tag-info/rf-tag;tag-info/filter-info/filter-name;ap-time-info/boot-time;ap-time-info/join-time"
user = input("Enter user: ")
password = getpass.getpass("Enter password: ")

payload = {}
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
  }

response = requests.get(url, auth=(user, password), headers=headers, data=payload, verify=False)

ap_table = pd.json_normalize(response.json()['Cisco-IOS-XE-wireless-access-point-oper:capwap-data'])
print(ap_table)
ap_table.to_excel('ap_table.xlsx')
