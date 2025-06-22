# Create a virtual environment

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

<div align="left"><figure><img src="../.gitbook/assets/image (6) (1).png" alt=""><figcaption></figcaption></figure></div>

Notice in the lower right corner of your screen, it will say "Select interpreter". Click that, and a pop-up will appear at the top of your screen asking you to select which Python interpreter to use. Since we have created a virtual environment called ".venv" in the working folder, it will be the recommended Python interpreter. Go ahead and use that.

<figure><img src="../.gitbook/assets/image (7) (1).png" alt=""><figcaption></figcaption></figure>

The text in the lower right corner will change to indicate you are using the virtual environment

<div align="left"><figure><img src="../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure></div>

If you (re)open the built-in terminal, the virtual environment will be auto-activated as well

<div align="left"><figure><img src="../.gitbook/assets/image (9) (1).png" alt=""><figcaption></figcaption></figure></div>
