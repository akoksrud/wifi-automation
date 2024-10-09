# Written by Andreas Koksrud, based on framework from Erik Rongved and Espen Frøstrup.
from ansible.module_utils.basic import AnsibleModule

def run_module():
    # Define available arguments/parameters available to pass to the module from Ansible
    module_args = dict(
        hostname=dict(type='str', required=True),
        show_run=dict(type='str', required=True),
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

    # We start populating the result object with the hostname of the WLC.
    result['hostname']=module.params['hostname']

    # Then we check if the text "restconf" is present in the run-config, and write some 
    # corresponding values to the result object to pass back to Ansible
    if "restconf" in module.params['show_run']:
        result['restconf_enabled']=True
        result['comments']="RESTCONF status: Enabled"
    else:
        result['restconf_enabled']=False
        result['comments']="RESTCONF status: Disabled"

    # After doing the work, return the result back to Ansible as JSON
    module.exit_json(**result)


def main():
    run_module()

if __name__ == '__main__':
    main()
