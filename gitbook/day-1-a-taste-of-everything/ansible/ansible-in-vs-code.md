# Ansible in VS Code

### Selecting the virtual environment

After installing Ansible in your virtual environment you can try opening the example file again. It may have selected the virtual environment already. If not, click "Select Interpreter" or "Python 3.12.3" in the line at the bottom, and select the python3 in your .venv folder which should be the recommended selection.

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (25) (1).png" alt=""><figcaption></figcaption></figure></div>

When the python interpreter in the .venv folder is selected, it should look  similar to this:

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (26) (1).png" alt=""><figcaption></figcaption></figure></div>

You will notice a red curly line under the last line of the example file. We will look into this in the next section.

### File recognition

If not auto detected, file type can be changed for open files:

<figure><img src="../../.gitbook/assets/image (27) (1).png" alt=""><figcaption></figcaption></figure>

There are several methods to "help" VS Code recognize your files as ansible playbooks. This will give relevant coloring rules for Ansible. If not it will be recognized as standard YAML which is OK, but the Ansible coloring rules are more specialized to help with Ansible playbooks.

<figure><img src="../../.gitbook/assets/image (28) (1).png" alt="" width="563"><figcaption></figcaption></figure>

All Ansible playbooks in this deep dive will have names ending with "-playbook.yml"
