import datetime
from dotenv import dotenv_values
from nornir import InitNornir  # Initialize Nornir
from nornir_utils.plugins.functions import print_result  # Print results
from nornir_netmiko.tasks import netmiko_send_command  # Send Netmiko command

# Import variables from the .env file
env = dotenv_values('.env')

# Initialize Nornir
nr = InitNornir()

# Set defaults for all devices
nr.inventory.defaults.username = env['USERNAME']  # Username from .env
nr.inventory.defaults.password = env['PASSWORD']  # Password from .env
nr.inventory.defaults.platform="ios"  # Platform set to Cisco IOS

# Define functions
def show_ap_summary():
    results = nr.run(
        task=netmiko_send_command,
        command_string="show ap summary"
    )
    print_result(results)

def show_client_summary():
    results = nr.run(
        task=netmiko_send_command,
        command_string="show wireless client summary"
    )
    print_result(results)

def show_cdp_neighbors():
    print("WLC CDP neighbors:\n-------------------------------------")
    results = nr.run(
        task=netmiko_send_command,
        command_string="show cdp neighbors"
    )
    print_result(results)
    print("AP CDP neighbors:\n-------------------------------------")
    results = nr.run(
        task=netmiko_send_command,
        command_string="show ap cdp neighbors"
    )
    print_result(results)

def save_config_to_file():
    print("Saving config to file...")
    results = nr.run(
        task=netmiko_send_command,
        command_string="show run"
    )
    for host in nr.inventory.hosts:
        if results[host][0].failed:
            print(f'Save run-config for {host} ({nr.inventory.hosts[host].hostname}) failed. See nornir.log for details.')
        else:
            now = datetime.datetime.now()
            filename = f"{nr.inventory.hosts[host].hostname}-run-conf ({now.strftime('%Y-%m-%d %H:%M:%S')}).txt"
            with open(filename, 'w') as f:
                f.write(str(results[host][0]))
            print(f"Config saved to {filename}")
    

# Text menu with 4 options that run each of the functions, or quit
while True:
    print('\nYou are connected to these devices: ')
    for host in nr.inventory.hosts:
        print(f'-> {host}: {nr.inventory.hosts[host].hostname}')
    print("Menu:")
    print("1. Show AP summary")
    print("2. Show client summary")
    print("3. Show CDP neighbors")
    print("4. Save run-config to file")
    print("5. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_ap_summary()
    elif choice == "2":
        show_client_summary()
    elif choice == "3":
        show_cdp_neighbors()
    elif choice == "4":
        save_config_to_file()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please choose again.")
