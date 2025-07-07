# WLC telemetry subscriptions

For this dashboard we will let the device (WLC) send telemetry data to Telegraf on periodic intervals. The intervals can vary depending on the metrics and how often we need it. Telegraf will then insert the metrics into InfluxDB, and Grafanas dashboards will read the data from InfluxDB.

* [ ] Log in to your WLC using your favorite SSH client

First, check if the subscriptions exist already. Since you are sharing WLCs you will have to create your own subscriptions pointing to your Ubuntu server.

```
show run | sec telemetry ietf
```

* [ ] Change subscription IDs below
  * Exchange&#x20;
    * {SUB\_ID\_A} with 105
    * {SUB\_ID\_B} with 106
    * {SUB\_ID\_C} with 107
    * etc
  * IF subscriptions with number 105, 106, 107 etc exists, you can use 205, 206, 207 etc
* [ ] Change receiver IP below
  * Exchange {Ubuntu\_IP} to your Ubuntu server IP, the same in each of the three subscriptions

```yang
conf t
telemetry ietf subscription {SUB_ID_A}
 encoding encode-kvgpb
 filter xpath /wireless-access-point-oper:access-point-oper-data/wireless-access-point-oper:ap-name-mac-map 
 stream yang-push
 update-policy periodic 30000
 receiver ip address {Ubuntu_IP} 57000 protocol grpc-tcp
 do show telemetry ietf subscription 105
telemetry ietf subscription {SUB_ID_B}
 encoding encode-kvgpb
 filter xpath /wireless-rrm-oper:rrm-oper-data/wireless-rrm-oper:rrm-measurement/wireless-rrm-oper:load 
 stream yang-push
 update-policy periodic 5000
 receiver ip address {Ubuntu_IP} 57000 protocol grpc-tcp
 do show telemetry ietf subscription 106
telemetry ietf subscription {SUB_ID_C}
 encoding encode-kvgpb
 filter xpath /wireless-access-point-oper:access-point-oper-data/wireless-access-point-oper:radio-oper-data/wireless-access-point-oper:phy-ht-cfg
 stream yang-push
 update-policy periodic 5000
 receiver ip address {Ubuntu_IP} 57000 protocol grpc-tcp
 do show telemetry ietf subscription 107
```











