# Preparations: Create .env file

Create a .env file to store variables

```bash
cd ~/tig-stack
touch .env
```

Add the following text to the .env file. You can either open it in VS Code or a terminal editor like nano.

```
INFLUXDB_ADMIN_USER=devnet-adm
INFLUXDB_ADMIN_PASSWORD=ChangeMe2025!
INFLUXDB_ORG=devnet
INFLUXDB_DB=c9800-db
INFLUXDB_ADMIN_TOKEN=ChangeMe2025!
GF_SECURITY_ADMIN_USER=devnet-adm
GF_SECURITY_ADMIN_PASSWORD=ChangeMe2025!
```

Later we will add a token to this file as well. It will be created after we have fired up the InfluxDB container.





















