# Running the script from terminal

One way to run a Python script, is by using the terminal. When in the folder of the script, run using "python" and the filename.

```bash
source ~/wifi-automation/.venv/bin/activate
cd ~/wifi-automation/python-get-ap-table/
python get-ap-table.py
```

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (12) (1) (1).png" alt=""><figcaption></figcaption></figure></div>

If there are no APs on the WLC it will have status code 204 (No Content). So it will not print the table etc, if it tried it would produce an error on the "json()\[blablabla] part"

```bash
Status code: 204: No Content
```

Successful run will look something like this:

{% code fullWidth="true" %}
```bash
 	wtp-mac              name          wtp-ip  ... ap-state.ap-operation-state     ap-time-info.boot-time            ap-time-info.join-time
0  4c:a6:4d:65:f9:40        9120E-ekms  192.168.10.182  ...                  registered  2024-07-25T00:28:12+00:00  2024-07-25T00:30:04.335182+00:00
1  d4:2c:44:d9:24:40  APD42C-44D8-2F38  192.168.10.177  ...                  registered  2024-07-31T19:22:07+00:00  2024-07-31T19:23:42.643078+00:00

```
{% endcode %}

Wrong username/password will look something like this:

```bash
Status code: 401: Unauthorized
```

Since we are using uv we can also run the python script using <kbd>uv run</kbd>

```bash
uv run get-ap-table.py
```
