# Explore VS Code

* TODO: Use uv for VENV, and create a .venv in the working folder of the wifi-automation project
* Should it be rebuilt, or just added to the current structure?
*

#### Install extensions

Following the pre-lab tasks you should have installed the Python extension in VS Code. Go to the Extensions tab on the left side of the VS Code window

<div align="left"><figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure></div>

In the "Local - installed" section, find the Python extension. If you have not installed it yet, install it now. Click the blue button/text saying "Install in SSH: 192.168.10.x" to install the extension into your Ubuntu Server:

<div align="left"><figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure></div>

#### Open the terminal in VS Code

VS Code has a great built-in terminal which we will use. Depending on if you customized your shell or not, it might look different from the screenshots. The content should be the same. Open the VS Code terminal by going to Terminal -> New Terminal (notice the hotkey to later, you will probably not have the insane Norwegian "ø" character as your hotkey)

<div align="left"><figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure></div>

#### Install UV

We will use "uv" for managing virtual environments and packages in Python. We start by installing uv from the newly opened terminal

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After installing, restart your shell (exit and re-open the terminal, or source \~/.bashrc)

#### Create a virtual environment

To use various packages in Python, we create a Python virtual environment (venv). We use uv do to this. Then we can add various packages which we can use ("import") in our Python scripts. Make sure you are in the \~/wifi-automation folder, then use uv to create a venv.

```
cd ~/wifi-automation
uv venv
```

You will notice a new folder has been created: `~/wifi-automation/.venv`. You could have whatever name you like, but by using the default name it will make things easier when working in VS Code, as it will automatically recognize and use the virtual environment when you open the \~/wifi-automation folder.

#### Open a Python file

Now you can go to the file explorer, find the "examples" folder and open the `python-hello-world.py` file:

<div align="left"><figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure></div>

Notice in the lower right corner of your screen, it will say "Select interpreter". Click that, and a pop-up will appear at the top of your screen asking you to select which Python interpreter to use. Since we have created a virtual environment called ".venv" in the working folder, it will be the recommended Python interpreter. Go ahead and use that.

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

The text in the lower right corner will change to indicate you are using the virtual environment

<div align="left"><figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure></div>

If you (re)open the built-in terminal, the virtual environment will be auto-activated as well

<div align="left"><figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure></div>





