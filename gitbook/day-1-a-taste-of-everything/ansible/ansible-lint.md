# Ansible-lint

Linting is a common term in programming/coding for checking the code both for bugs/errors, but also for style issues and formatting. The "linter" can highlight sections/lines that doesn't comply with the rules for your language. It it also common to have the linter (or a separate formatting plugin) fix the formatting when you save the file. Examples of formatting can be placement of brackets or breaking too long lines to multiple lines.

Open the "ansible-first-playbook.yml" again. It should have an error that shows on the last line. Hover your mouse over the line, and a box should pop up with a description. This specific error message say that there is no "new line character" at the end of file, and specifies which rule it violates.

<figure><img src="../../.gitbook/assets/image (29).png" alt=""><figcaption></figcaption></figure>

Enter a new line at the end of the example file and try saving it again. You will probably get a new error now, because the new line is not empty.

<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

Remove the spaces on the line so it is empty, and save again. Now the linter will finally be happy :relaxed:

<figure><img src="../../.gitbook/assets/image (32).png" alt=""><figcaption></figcaption></figure>



You can also specify ansible-lint to exclude certain errors, we will use the "line too long" error as an example here.

Open Settings (<kbd>Ctrl-,</kbd>) (that is... Ctrl and comma) and search for "ansible-lint".\
Enter the value <kbd>-x yaml\[line-length]</kbd>  in the "Lint: Arguments" box.

<figure><img src="../../.gitbook/assets/image (30).png" alt=""><figcaption></figcaption></figure>
