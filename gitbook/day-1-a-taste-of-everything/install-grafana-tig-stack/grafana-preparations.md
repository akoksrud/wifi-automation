# Grafana preparations

Create a `grafana.ini` file in the grafana subfolder, and a <kbd>datasources.yaml</kbd> in the grafana/conf/provisioning/datasources subfolder:

```bash
cd ~/tig-stack
mkdir -p ~/tig-stack/grafana/conf/provisioning/datasources
touch ~/tig-stack/grafana/grafana.ini
touch ~/tig-stack/grafana/conf/provisioning/datasources/datasources.yaml
```

Add the following text to the <kbd>grafana.ini</kbd> file. You can either open it in VS Code or a terminal editor like nano.

```ini
[security]
disable_initial_admin_creation = true
[feature_toggles]
dashboardNewLayouts = true
kubernetesDashboards = true
dashboardScene = true
[paths]
provisioning = /etc/grafana/provisioning
```

Add the following text to the <kbd>datasources.yaml</kbd> file. You can either open it in VS Code or a terminal editor like nano.

```yaml
# Configuration file version
apiVersion: 1

# List of data sources to delete from the database.
deleteDatasources:
  - name: influxdb
    orgId: 1

# Mark provisioned data sources for deletion if they are no longer in a provisioning file.
# It takes no effect if data sources are already listed in the deleteDatasources section.
prune: true

# List of data sources to insert/update depending on what's
# available in the database.
datasources:
  - name: influxdb
    type: influxdb
    access: proxy
    orgId: 1
    uid: influxdb
    url: http://influxdb:8181
    user: ${INFLUXDB_ADMIN_USER}
    database: ${INFLUXDB_DB}
    isDefault: true
    secureJsonData:
      password: ${INFLUXDB_ADMIN_PASSWORD}
    version: 1
    editable: true
```

