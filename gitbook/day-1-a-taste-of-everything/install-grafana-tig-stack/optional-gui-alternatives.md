# Optional: GUI alternatives

### InfluxDB GUI (create token and database)

You have created an admin token and a database by using the CLI commands of InfluxDB. InfluxDB3 doesn't come with a GUI as standard, and I have not created material for GUI alternatives of doing those operations. You can check out InfluxDB 3 Explorer (instructions might be included in a future update of this deep dive material, based on demand/feedback from previous students and test users).

{% embed url="https://docs.influxdata.com/influxdb3/explorer/install/" %}

### Grafana GUI (create datasource)

When installing Grafana (using Docker Compose) we automatically created a datasource in Grafana, pointing to our InfluxDB database as the default datasource. If you want to do this by GUI or need to add another datasource later (and want do do it by GUI and not adding to the <kbd>datasources.yml</kbd>), here are some instructions.&#x20;

Log in to Grafana (http://{server-ip}:3000)

In the menu on the left side, navigate to <kbd>Connections > Data sources</kbd>

<figure><img src="../../.gitbook/assets/image (95).png" alt=""><figcaption></figcaption></figure>

Click <kbd>+ Add new data source</kbd>  (you can also click the existing one if you just want to inspect it)

<figure><img src="../../.gitbook/assets/image (96).png" alt=""><figcaption></figcaption></figure>

Select InfluxDB (you can narrow the search by typing in the search field)

<figure><img src="../../.gitbook/assets/image (97).png" alt="" width="513"><figcaption></figcaption></figure>

In the Name field, give the data source a name. The pre-configured is called "influxdb" so if you are adding another influxdb, call it influxdb-2 or some more descriptive name like "influxdb-something\_descriptive" :relaxed:Only one of your data sources can be the "Default", which will be selected as the default when you create dashboards.

<figure><img src="../../.gitbook/assets/image (98).png" alt=""><figcaption></figcaption></figure>

Set the Query language to <kbd>InfluxQL</kbd> . InfluxDB3 also support SQL, but in Grafana this is currently in Alpha, so we will not use it for our dashboards (maybe in the future).

<figure><img src="../../.gitbook/assets/image (99).png" alt=""><figcaption></figcaption></figure>

In the HTTP section, type the URL of the InfluxDB server. Since InfluxDB and Grafana run on the same "stack" (we run it from the same docker-compose.yml file, there are some details but it is far outside the scope of this deep dive) we can use the name "influxdb" to reach our InfluxDB server. We use port 8181.

<figure><img src="../../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

In the Auth section, we keep everything off except that we create some Custom HTTP Headers where we enter the token we created earlier. We saved this token in the <kbd>.env</kbd> file in the <kbd>\~/tig-stack</kbd> folder. The "Header" should be <kbd>Authorization</kbd>  and the "Value" should be the text "Bearer " and your token, for example&#x20;

{% code fullWidth="true" %}
```
Bearer apiv3_X1P_39ANAaLl_e232AntsenEucAA1gia4idRZBIIynDy0W3W7CSW9V90zYjmCypQs9qB-PCy1yiWl2NPoFcDOw
```
{% endcode %}

<figure><img src="../../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

In the InfluxDB Details section you only need the Database name, which should be "c9800-db"

<figure><img src="../../.gitbook/assets/image (102).png" alt=""><figcaption></figcaption></figure>

Click the "Save & test" button. You should have some measurements found (probably 3 or 5 depending on how much you have done in this deep dive, and maybe you reuse a shared server etc)

<figure><img src="../../.gitbook/assets/image (103).png" alt=""><figcaption></figcaption></figure>



