---
description: >-
  In this section we will open the Remote-SSH plugin and connect VS Code to the
  Ubuntu Server
---

# Remote SSH

*   [ ] Open the "Command palette" by one of the following methods:

    * Press F1 on your keyboard
    * In search bar at the top of your screen, type ">" to start command palette

    <div align="center"><figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure></div>

    * Navigate to Command Palette using the menu View > Command Palette... You can also use the hotkey shown in that menu to open the command palette

    <div align="center"><figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure></div>

    It will look something like this, and show some of your recently used items, which will differ from the screenshot

    <div align="center"><figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure></div>
*   [ ] Add a new SSH Host

    * Type "remote-ssh" to narrow down the choices. Select "Remote-SSH: Add New SSH Host..."

    <figure><img src="../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1).png" alt="" width="345"><figcaption></figcaption></figure>

    * Type in "devnet-adm@192.168.10.7" (replace the IP address with your server IP). Pess Enter.

    <figure><img src="../../.gitbook/assets/image (7) (1) (1) (1).png" alt="" width="491"><figcaption></figcaption></figure>

    * You will get a new prompt on the same place, asking which ssh file to update. Use the default choice presented

    <figure><img src="../../.gitbook/assets/image (8) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

    * Connect to the new host by clicking on the "Remote SSH" button in the lower left corner of your VS Code window

    <figure><img src="../../.gitbook/assets/image (9) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

    * Then a menu will open at the center top of screen. Select "Connect Current Window to Host..."

    <figure><img src="../../.gitbook/assets/image (10) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

    * Select the server you added

    <figure><img src="../../.gitbook/assets/image (11) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

    * When asked about password, enter the password
    * When asked about platform type, select Linux

    <figure><img src="../../.gitbook/assets/image (12) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

