import requests
import getpass
import pandas as pd
import ipaddress

# Ask user for WLC IP and credentials
while True:
    wlc = input("Enter WLC IP: ")
    try:
        ipaddress.ip_address(wlc)
        break
    except ValueError:
        print("Invalid IP address. Please enter a valid IP address.")
user = input("Enter user: ")
password = getpass.getpass("Enter password: ")

# Construct API URL
url = f"https://{wlc}/restconf/data/Cisco-IOS-XE-wireless-client-oper:client-oper-data"

# Set up API headers
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
  }

# Send GET request to API
response = requests.get(url, auth=(user, password), headers=headers, verify=False)

# Check if API request was successful
if (response.status_code==200):
    # Extract JSON data from API response
    clients = pd.json_normalize(response.json()['Cisco-IOS-XE-wireless-client-oper:client-oper-data'])
    # Save data to Excel file
    clients.to_excel('clients.xlsx', index=False)
else:
    # Print error message if API request failed
    print(f"Status code: {response.status_code}: {response.reason}")
