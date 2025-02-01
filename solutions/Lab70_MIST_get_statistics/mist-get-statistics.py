from dotenv import dotenv_values
import requests
from pprint import pprint
import os

# Import variables from the .env file
env = dotenv_values('.env')
apitoken = env['apitoken']
host=env['host']
org_id=env['org_id']
site_id=env['site_id']

# Define functions
def show_device_summary():
    print('Device summary:\n-------------------------------------')

    url = f"https://api.eu.mist.com/api/v1/sites/{site_id}/devices"

    payload = {}
    headers = {
    'Authorization': f'Token {apitoken}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    pprint(response.json())


def show_client_summary():
    print('Client summary:\n-------------------------------------')
    url = f"https://api.eu.mist.com/api/v1/sites/{site_id}/clients/search"

    payload = {}
    headers = {
    'Authorization': f'Token {apitoken}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    pprint(response.json())


def show_device_statistics():
    print(f"Full Statistics for all devices on site:\n-------------------------------------")
    url = f"https://api.eu.mist.com/api/v1/sites/{site_id}/stats/devices"

    payload = {}
    headers = {
    'Authorization': f'Token {apitoken}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    pprint(response.json())



# Text menu with 3 options that run each of the functions, or quit
while True:
    # Clear the screen
    print(f'\nYou are connected to organization {org_id} and site {site_id}')
    print("Menu:")
    print("1. Show device summary")
    print("2. Show client summary")
    print("3. Show device statistics")
    print("4. Quit")

    choice = input("Enter choice: ")
    os.system('cls' if os.name == 'nt' else 'clear')

    if choice == "1":
        show_device_summary()
    elif choice == "2":
        show_client_summary()
    elif choice == "3":
        show_device_statistics()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please choose again.")
