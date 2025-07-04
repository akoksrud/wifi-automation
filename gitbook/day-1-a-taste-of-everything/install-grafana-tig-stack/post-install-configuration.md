# Post install configuration

### Create InfluxDB token

<pre class="language-bash" data-overflow="wrap" data-full-width="true"><code class="lang-bash"><strong>grep -v "INFLUXDB_TOKEN" .env > temp &#x26;&#x26; mv temp .env
</strong>echo "INFLUXDB_TOKEN=$(docker exec influxdb influxdb3 create token --admin | grep Token: | awk '{print $2}')" >> .env
source .env
</code></pre>

### Create InfluxDB database

{% code overflow="wrap" fullWidth="true" %}
```bash
docker exec influxdb influxdb3 create database --token "${INFLUXDB_TOKEN}" "${INFLUXDB_DB}"
```
{% endcode %}

### Restart the containers

After creating the token and the database, we need to restart everything to make sure we use our new token and database.

```bash
docker compose down
docker compose up -d
```







