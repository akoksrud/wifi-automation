import datetime
from netmiko import ConnectHandler
from dotenv import dotenv_values

# Import variables from the .env file
env = dotenv_values('.env')

# Use netmiko to connect to the WLC
cisco_wlc = {
    'device_type': 'cisco_ios',
    'ip': env['WLC_IP'],
    'username': env['USERNAME'],
    'password': env['PASSWORD']
}
net_connect = ConnectHandler(**cisco_wlc)

# Define functions
def show_ap_summary():
    print(net_connect.send_command("show ap summary"))

def show_client_summary():
    print(net_connect.send_command("show wireless client summary"))

def show_cdp_neighbors():
    print("WLC CDP neighbors:\n-------------------------------------")
    print(net_connect.send_command("show cdp neighbors"))
    print("AP CDP neighbors:\n-------------------------------------")
    print(net_connect.send_command("show ap cdp neighbors"))

def save_config_to_file():
    output=net_connect.send_command("show run")
    now = datetime.datetime.now()
    filename = f"{env['WLC_IP']}-run-conf ({now.strftime('%Y-%m-%d %H:%M:%S')}).txt"
    with open(filename, 'w') as f:
        f.write(output)
    print(f"Config saved to {filename}")
    

# Text menu with 4 options that run each of the functions, or quit
while True:
    print('\nYou are connected to WLC: ' + env['WLC_IP'])
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
        net_connect.disconnect()
        break
    else:
        print("Invalid choice. Please choose again.")
