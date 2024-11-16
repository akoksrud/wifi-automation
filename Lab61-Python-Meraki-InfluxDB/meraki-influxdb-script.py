from influxdb import InfluxDBClient
from datetime import datetime, timezone
from dotenv import dotenv_values
import requests
import json

# Import variables from the .env file
env = dotenv_values('.env')
apiKey = env['apiKey']
organizationId=env['organizationId']
networkId=env['networkId']

def get_devices():
    url = f"https://api.meraki.com/api/v1/organizations/{organizationId}/devices"
    payload = {}
    headers = {
        'Accept': 'application/json',
        'X-Cisco-Meraki-API-Key': apiKey
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text

def get_channel_utilization():
    url = f"https://api.meraki.com/api/v1/organizations/{organizationId}/wireless/devices/channelUtilization/byDevice?timespan=300&interval=300"
    payload = {}
    headers = {
        'Accept': 'application/json',
        'X-Cisco-Meraki-API-Key': apiKey
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text

def update_influxDB():
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    json_body = [
        {
            "measurement": "ap_stats",
            "tags": {
                "host": "AP_name",
            },
            "time": timestamp,
            "fields": {
                "value": 0.66,
                "value2" : 1.33,
                "textfield": "text"
            }
        }
    ]

    client = InfluxDBClient('localhost', 8086, 'devnet-adm', 'ChangeMe2025!', 'syslog-db')
    client.write_points(json_body)
    result = client.query('select value from cpu_load_short;')
    print("Result: {0}".format(result))

# Iterate through all devices and do stuff
def iterate_access_points():
    devices = json.loads(get_devices())
    utilization = json.loads(get_channel_utilization())
    ap_serial_map = {}
    for device in devices:
        if device['productType'] == "wireless":
            ap_serial_map[device['serial']] = device['name']
    for util in utilization:
        serial = util['serial']
        for band in util['byBand']:
            wifi = band['wifi']['percentage']
            nonwifi = band['nonWifi']['percentage']
            total = band['total']['percentage']
        print(f'{ap_serial_map[serial]} (S/N: {serial}), WiFi: {wifi}%, Non-WiFi: {nonwifi}%, Total: {total}%')


iterate_access_points()
