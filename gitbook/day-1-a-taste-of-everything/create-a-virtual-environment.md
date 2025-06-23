# Create a virtual environment

#### What is a virtual environment?

When working with Python it is best practice to use a "virtual environment" for each project. In a virtual environment you have full control of which packages are installed (and which Python version), so the application or script run in a deterministic environment. To keep the complexity as low as possible, for this deep dive we will consider the whole lab as a single project, with one common virtual environment.

A virtual environment are often called a "venv", and have a few common places to be defined. We will use a subfolder in the project direcory, called `.venv/`

Other project files are also common, but for this deep dive we will not  need them so we keep it out of scope. The last section on this page will give you some more pointers/links.

#### UV and its alternatives

In this deep dive we will use uv ([https://docs.astral.sh/uv](https://docs.astral.sh/uv/)) for managing virtual environments and packages i Python. Some other popular alternatives are pip for managing packages, and virtualenv for managing virtual environments. UV can also replace other tools that we do not touch in this deep dive, like poetry and twine.

#### Install UV

We start by installing uv from the newly opened terminal in VS Code, to our server.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After installing, restart your shell (exit and re-open the terminal, or source \~/.bashrc)

#### Create a virtual environment

To use various packages in Python, we create a Python virtual environment (venv). Then we can add various packages which we can use ("import") in our Python scripts. Make sure you are in the \~/wifi-automation folder, then use uv to create a venv. We will create a single virtual environment for all of our needs in this deep dive, in the "wifi-autmation" folder.

```
cd ~/wifi-automation
uv venv
```

You will notice a new folder has been created: `~/wifi-automation/.venv`. You could have whatever name you like, but by using the default name it will make things easier when working in VS Code, as it will automatically recognize and use the virtual environment when you open the `~/wifi-automation/` folder.

#### Open a Python file

Now you can go to the file explorer, find the "examples" folder and open the `python-hello-world.py` file that we briefly opened earlier. If you still have it open, great :)

<div align="left"><figure><img src="../.gitbook/assets/image (6) (1).png" alt=""><figcaption></figcaption></figure></div>

Notice in the lower right corner of your screen, it will say "Select interpreter". Click that, and a pop-up will appear at the top of your screen asking you to select which Python interpreter to use. Since we have created a virtual environment called ".venv" in the working folder, it will be the recommended Python interpreter. Go ahead and use that.

<figure><img src="../.gitbook/assets/image (7) (1).png" alt=""><figcaption></figcaption></figure>

The text in the lower right corner will change to indicate you are using the virtual environment

<div align="left"><figure><img src="../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure></div>

If you (re)open the built-in terminal, the virtual environment will be auto-activated as well. You will see the name of your venv in parentheses at the start of the terminal line.

<figure><img src="../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

If you use a customized shell it might show some other info, like which git branch you are working on ("main"), and the python version of your venv (v3.12.3).

<div align="left"><figure><img src="../.gitbook/assets/image (9) (1).png" alt=""><figcaption></figcaption></figure></div>

#### Other project files

To read more about initializing a project from scratch, check out the following links:

{% embed url="https://docs.astral.sh/uv/guides/projects/" %}

{% embed url="https://docs.astral.sh/uv/guides/scripts/" %}

