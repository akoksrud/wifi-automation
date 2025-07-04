# docker-compose.yml

Create a `docker-compose.yml` file in the tig-stack folder:

```bash
cd ~/tig-stack
touch ./docker-compose.yml
```

Add the following text to the <kbd>docker-compose.yml</kbd> file. You can either open it in VS Code or a terminal editor like nano.

```yaml
services:
  influxdb:
    container_name: influxdb
    image: influxdb:3-core
    expose:
      - 8181
    restart: always
    volumes:
      - influxdb-data:/var/lib/influxdb3
    ports:
      - 8181:8181
    command:
      - influxdb3
      - serve
      - --node-id=influxdb0
      - --object-store=file
      - --data-dir=/var/lib/influxdb3
    healthcheck:
      test: ["CMD-SHELL", "curl -f -H 'Authorization: Bearer ${INFLUXDB_TOKEN}' http://localhost:8181/health || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 3

  telegraf:
    container_name: telegraf
    image: telegraf:1.34.1
    depends_on:
      influxdb:
        condition: service_healthy
    restart: always
    ports:
      - 57000:57000
    environment:
      - INFLUXDB_TOKEN=${INFLUXDB_TOKEN}
      - INFLUXDB_ORG=${INFLUXDB_ORG}
      - INFLUXDB_DB=${INFLUXDB_DB}
    volumes:
      - ./telegraf/conf/telegraf.conf:/etc/telegraf/telegraf.conf:ro

  grafana:
    container_name: grafana
    image: grafana/grafana:12.0.1
    expose:
      - 3000
    restart: always
    ports:
      - 3000:3000
    environment:
      - GF_SECURITY_ADMIN_USER=${GF_SECURITY_ADMIN_USER}
      - GF_SECURITY_ADMIN_PASSWORD=${GF_SECURITY_ADMIN_PASSWORD}
      - GF_FEATURE_TOGGLES_ENABLE="dashboardNewLayouts,kubernetesDashboards,dashboardScene"
      - GF_INSTALL_PLUGINS=
    volumes:
      - grafana-data:/var/lib/grafana
      - ./grafana/grafana.ini:/etc/grafana/grafana.ini:ro
      - ./grafana/conf/provisioning/datasources:/etc/grafana/provisioning/datasources:ro
    depends_on:
      - influxdb
      - telegraf

volumes:
  grafana-data:
    external: true
  influxdb-data:
    external: true

```



