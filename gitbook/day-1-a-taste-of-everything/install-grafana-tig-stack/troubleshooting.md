# Troubleshooting

Here are some commands to use for basic troubleshooting

### Logging and troubleshooting

To view the current running containers:

```bash
docker ps
```

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (94).png" alt=""><figcaption></figcaption></figure></div>

To view logs of the individual containers, use <kbd>docker logs \<container name></kbd> . You can also use container id instead of name.

```bash
docker logs telegraf
```

You can also "follow" the log by using the <kbd>-f</kbd> flag

```bash
docker logs grafana -f
```

### Restarting

Restart one container

```bash
cd ~/tig-stack
docker restart telegraf
```

Restart the whole TIG stack

```bash
cd ~/tig-stack
docker compose down
docker compose up -d
```

### Deleting and starting fresh

* delete databases

```bash
cd ~/tig-stack
docker compose down
docker volume rm grafana-data
docker volume rm influxdb-data
docker volume create grafana-data
docker volume create influxdb-data
docker compose up -d
```

* delete stored data in influxdb



### Inspect Docker image

If you want to inspect a Docker image without downloading it, you can use Skopeo. You can check available versions if you want to lock in to a specific version etc.

```bash
sudo apt install skopeo
skopeo inspect docker://influxdb:3-core
```

