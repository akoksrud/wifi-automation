# Telegraf preparations

Create a `telegraf.conf` file in the telegraf/conf/ subfolder

```bash
cd ~/tig-stack
mkdir -p telegraf/conf
touch telegraf/conf/telegraf.conf
```

Add the following text to the telegraf.conf file. You can either open it in VS Code or a terminal editor like nano.

```ini
[global_tags]
  host = "telegraf"
[agent]
  interval = "10s"
  round_interval = true
  metric_batch_size = 1000
  metric_buffer_limit = 10000
  collection_jitter = "0s"
  flush_interval = "10s"
  flush_jitter = "0s"
  precision = ""
  debug = false
  quiet = false
  logfile = ""
  hostname = "telegraf"
  omit_hostname = false


###############################################################################
#                            OUTPUT PLUGINS                                   #
###############################################################################

# Configuration for influxdb server to send metrics to


[[outputs.influxdb_v2]]
urls = [ "http://influxdb:8086" ]
  token = "${INFLUXDB_ADMIN_TOKEN}"
  organization = "${INFLUXDB_ORG}"
  bucket = "${INFLUXDB_BUCKET}"
# tagexclude = ["influxdb_database"] ### Optional: Exclude specific tags if needed
 [outputs.influxdb_v2.tagpass]
  influxdb_database = ["${INFLUXDB_BUCKET}"]


###############################################################################
#                            INPUT PLUGINS                                    #
###############################################################################

[[inputs.cisco_telemetry_mdt]]
  transport = "grpc"
  service_address = ":57000"
 [inputs.cisco_telemetry_mdt.tags]
  influxdb_database =  "${INFLUXDB_BUCKET}"

```











