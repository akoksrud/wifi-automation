# Preparations: Persistent storage

Create a "volume" for each of InfluxDB and Grafana for persistent storage. Everything that is not persistent, will be reset after each restart of the containers.

```bash
docker volume create grafana-data
docker volume create influxdb-data
```
