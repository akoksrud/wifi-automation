# Written by Andreas Koksrud, based on framework from Erik Rongved and Espen Frøstrup.
from ansible.module_utils.basic import AnsibleModule
from datetime import datetime

def run_module():
    # Define available arguments/parameters available to pass to the module from Ansible
    module_args = dict(
        interface_dict=dict(type='dict', required=True),
    )

    # Define the result object (which is passed back to Ansible)
    result = dict(
        changed=False
    )

    # Define the AnsibleModule object that will be instatiated when the module runs
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # From this point and down, is where the actual "doing" of the module takes place

    interface_dict = module.params['interface_dict']
    timestamp = datetime.now().strftime('%D %H:%M:%S')
    description = interface_dict['Cisco-IOS-XE-native:interface']['GigabitEthernet'][0]['description']

    # If the description field contains "Uplink" we will do nothing. If not, we will change the description including a timestamp just for fun
    if "Uplink" in description:
        result['Gi1_old_description'] = description
        result['Gi1_new_description'] = description
        result['new_interface_dict'] = interface_dict
        result['comments'] = f"Unchanged"
    else:
        result['Gi1_old_description'] = description
        result['Gi1_new_description'] = f"Uplink - modified {timestamp}"
        interface_dict['Cisco-IOS-XE-native:interface']['GigabitEthernet'][0]['description'] = f"Uplink - modified {timestamp}"
        result['new_interface_dict'] = interface_dict
        result['changed'] = True
        result['comments'] = f"Changed {timestamp}"

    # After doing the work, return the result back to Ansible as JSON
    module.exit_json(**result)


def main():
    run_module()

if __name__ == '__main__':
    main()
