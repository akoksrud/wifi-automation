import time
import requests
import getpass
import urllib3
import matplotlib.pyplot as plt

urllib3.disable_warnings()
wlc = input("Enter WLC IP: ")
user = input("Enter user: ")
password = getpass.getpass("Enter password: ")
url = f"https://{wlc}/restconf/data/Cisco-IOS-XE-process-cpu-oper:cpu-usage/cpu-utilization/five-seconds"
payload = {}
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
  }

cpu_values = [0]
plt.ion()
while True:
    response = requests.get(url, auth=(user, password), headers=headers, data=payload, verify=False)
    if (response.status_code==200):
        cpu_values.append(response.json()['Cisco-IOS-XE-process-cpu-oper:five-seconds'])
        plt.plot(cpu_values)
        plt.draw()
        plt.pause(1)
    else:
        print(f"Status code: {response.status_code}: {response.reason}")
    time.sleep(1)
