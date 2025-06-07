---
description: Instructions on some simple shell customizations
---

# Customize the shell

#### Modifying the "PS1" variable in \~/.bashrc

Edit your .bashrc file

```bash
nano ~/.bashrc
```

Locate the current "PS1=" section under "if \[ "$color\_prompt". This is where it should be:

<figure><img src=".gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

Replace itwith the following line. Then save the file and exit.

{% code fullWidth="true" %}
```bash
PS1='\[\e[93m\][\t]\[\e[0m\] \[\e[32m\]\u@\h\[\e[37m\] in \[\e[94m\]\w\[\e[0m\] \[\e[37m\]\$\[\e[0m\] '
```
{% endcode %}

Use ("source") the updated .bashrc file

```bash
source ~/.bashrc
```

Your new shell prompt will look like this:

<figure><img src=".gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

#### Starship

Starship is a more comprehensive shell extensions. Compared to the simple change we did by just editing the PS1 variable in the .bashrc file, Starship adds functionality, like \
\- Showing the time consumed by "slow" tasks\
\- Showing status (branch, unsynced changes etc) when you are in a git repository\
\- Showing info on the Python virtual environment\
Install Starship by issuing the following command, and answer "y" to the question:

```bash
curl -sS https://starship.rs/install.sh | sh
```

<figure><img src=".gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

As the instructions say, edit your \~/.bashrc file again,

```bash
nano ~/.bashrc
```

&#x20;and add the following line to the end of the file. Then save and exit

```
eval "$(starship init bash)"
```

Use ("source") the updated .bashrc file

```bash
source ~/.bashrc
```

It will look like this:

<figure><img src=".gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

You can also enable a theme



