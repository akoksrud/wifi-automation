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

# Run command on all devices
results = nr.run(
    task=netmiko_send_command,  # Use the task "netmiko_send_command"
    command_string="show ap summary"  # Command to run
)

# Print results
print_result(results)
