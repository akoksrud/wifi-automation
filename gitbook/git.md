# Git

#### Prerequisites

You must have Git installed for this part to work.

Windows

```powershell
winget install Git.Git
```

Mac

```powershell
brew install git
```

Ubuntu

```powershell
sudo apt install git
```

#### Git config

Start by setting your name and email (change to your Git username and email accordingly)

```bash
git config --global user.name "akoksrud"
git config --global user.email "andreas@koksrud.no"
```

If you have a SSH key, you can enable signed commits using that key

```bash
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global gpg.format ssh
git config --global commit.gpgsign true
```

#### Upload SSH key

See the following link for uploading the public SSH key to your GitHub account: [https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
