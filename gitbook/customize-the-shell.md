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

Replace it with the following line. Then save the file and exit.

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
\- Showing info on the Python virtual environment

First, make sure you have a Nerd Font installed and enabled in your terminal. I use [Cascadia Code NF](https://github.com/microsoft/cascadia-code/releases), there are many available at [https://www.nerdfonts.com/font-downloads](https://www.nerdfonts.com/font-downloads). Download one and use it in your terminal before continuing.

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

You can also enable a preset ("theme") for Starship

{% code fullWidth="true" %}
```bash
mkdir ~/.config
curl https://starship.rs/presets/toml/gruvbox-rainbow.toml -o ~/.config/gruvbox-rainbow.toml
starship preset gruvbox-rainbow -o ~/.config/starship.toml
```
{% endcode %}

<figure><img src=".gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

For further info, check [https://starship.rs/](https://starship.rs/)

#### Oh-my-bash

Another popular prompt is [oh-my-bash](https://github.com/ohmybash/oh-my-bash). You can install it with the following command

{% code fullWidth="true" %}
```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"
```
{% endcode %}

For more info on use, configuration, [themes](https://github.com/ohmybash/oh-my-bash/wiki/Themes), etc you should check [https://github.com/ohmybash/oh-my-bash](https://github.com/ohmybash/oh-my-bash)
