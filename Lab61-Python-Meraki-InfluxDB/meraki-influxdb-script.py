from influxdb import InfluxDBClient
from datetime import datetime, timezone
from dotenv import dotenv_values
import requests
import json
import time

# Import variables from the .env file
env = dotenv_values('.env')
apiKey = env['apiKey']
organizationId=env['orgId']

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

def update_influxDB(measurement_name, hostname, fields):
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    json_body = [
        {
            "measurement": measurement_name,
            "tags": {
                "host": hostname,
            },
            "time": timestamp,
            "fields": fields
        }
    ]
    client = InfluxDBClient('localhost', 8086, 'devnet-adm', 'ChangeMe2025!', 'cloud-ap-db')
    client.write_points(json_body)
    print(f"Updated InfluxDB with data from {hostname} at {timestamp}")

# Iterate through all devices and do stuff
def iterate_access_points():
    devices = json.loads(get_devices())
    utilization = json.loads(get_channel_utilization())
    ap_serial_map = {}
    interference = {}
    for device in devices:
        if device['productType'] == "wireless":
            ap_serial_map[device['serial']] = device['name']
    for util in utilization:
        serial = util['serial']
        interference[serial] = {}
        for band in util['byBand']:
            interference[serial][band['band']+"GHz Wi-Fi"] = band['wifi']['percentage']
            interference[serial][band['band']+"GHz non-Wi-Fi"] = band['nonWifi']['percentage']
            interference[serial][band['band']+"GHz Total"] = band['total']['percentage']
        update_influxDB('ch_utilization', ap_serial_map[serial], interference[serial])

while True:
    iterate_access_points()
    time.sleep(10)
