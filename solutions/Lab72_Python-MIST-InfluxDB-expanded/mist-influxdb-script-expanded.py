from influxdb import InfluxDBClient
from datetime import datetime, timezone
from dotenv import dotenv_values
import requests
import time

# Import variables from the .env file
env = dotenv_values('.env')
host = env['host']
apitoken = env['apitoken']
org_id=env['org_id']
site_id=env['site_id']

def get_device_statistics():
    url = f"https://{host}/api/v1/sites/{site_id}/stats/devices"

    payload = {}
    headers = {
    'Authorization': f'Token {apitoken}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()

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
    devices = get_device_statistics()
    for device in devices:
        if device['type'] == "ap":
            interference = {}
            for band in device['radio_stat']:
                if band=="band_24": bandname = "2.4"
                if band=="band_5": bandname = "5"
                if band=="band_6": bandname = "6"
                interference[bandname+"GHz Wi-Fi"] = device['radio_stat'][band]['util_rx_in_bss'] + device['radio_stat'][band]['util_rx_other_bss'] + device['radio_stat'][band]['util_unknown_wifi'] + device['radio_stat'][band]['util_undecodable_wifi']
                interference[bandname+"GHz non-Wi-Fi"] = device['radio_stat'][band]['util_non_wifi']
                interference[bandname+"GHz Total"] = device['radio_stat'][band]['util_all']
            update_influxDB('ch_utilization', device['name'], interference)
            
            channel_history = {}
            for band in device['radio_stat']:
                if band=="band_24": bandname = "2.4"
                if band=="band_5": bandname = "5"
                if band=="band_6": bandname = "6"
                channel_history[bandname+"GHz #Clients"] = device['radio_stat'][band]['num_clients']
                channel_history[bandname+"GHz Channel"] = device['radio_stat'][band]['channel']
                channel_history[bandname+"GHz Bandwidth"] = device['radio_stat'][band]['bandwidth']
                channel_history[bandname+"GHz TxPower"] = device['radio_stat'][band]['power']
            update_influxDB('channel_history', device['name'], channel_history)

            device_info = {}
            device_info['model'] = device['model']
            device_info['ip'] = device['ip']
            device_info['ext_ip'] = device['ext_ip']
            device_info['mount'] = device['mount']
            device_info['power_src'] = device['power_src']
            device_info['mac'] = device['mac']
            device_info['radio_mac'] = device['radio_stat']['band_5']['mac']
            update_influxDB('device_info', device['name'], device_info)


while True:
    iterate_access_points()
    time.sleep(10)
