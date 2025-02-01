from dotenv import dotenv_values
import requests

# Import variables from the .env file
env = dotenv_values('.env')
apiKey = env['apiKey']
organizationId=env['orgId']
networkId=env['networkId']
serial=env['serial']

# Define functions
def show_device_summary():
    print('Device summary:\n-------------------------------------')
    url = f"https://api.meraki.com/api/v1/organizations/{organizationId}/devices"
    payload = {}
    headers = {
        'Accept': 'application/json',
        'X-Cisco-Meraki-API-Key': apiKey
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

def show_client_summary():
    print('Client summary:\n-------------------------------------')
    url = f"https://api.meraki.com/api/v1/networks/{networkId}/clients"
    payload = {}
    headers = {
        'Accept': 'application/json',
        'X-Cisco-Meraki-API-Key': apiKey
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

def show_cdp_neighbors():
    print(f"CDP neighbors for device {serial}:\n-------------------------------------")
    url = f"https://api.meraki.com/api/v1/devices/{serial}/lldpCdp"
    payload = {}
    headers = {
        'Accept': 'application/json',
        'X-Cisco-Meraki-API-Key': apiKey
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

def get_device_dhcp_subnets():
    print(f"DHCP subnets for device {serial}:\n-------------------------------------")
    url = f"https://api.meraki.com/api/v1/devices/{serial}/appliance/dhcp/subnets"
    payload = {}
    headers = {
        'Accept': 'application/json',
        'X-Cisco-Meraki-API-Key': apiKey
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    
# Text menu with 4 options that run each of the functions, or quit
while True:
    print(f'\nYou are connected to organization {organizationId} and network {networkId}')
    print("Menu:")
    print("1. Show Device summary")
    print("2. Show client summary")
    print("3. Show CDP neighbors")
    print("4. Show DHCP subnets")
    print("5. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_device_summary()
    elif choice == "2":
        show_client_summary()
    elif choice == "3":
        show_cdp_neighbors()
    elif choice == "4":
        get_device_dhcp_subnets()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please choose again.")
