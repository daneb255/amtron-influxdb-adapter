import influxdb_client

from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
from core.settings import INFLUX_TOKEN, INFLUX_BUCKET, INFLUX_HOST, INFLUX_ORG


def write_to_influx_charge_records(device_name: str, rfid_tag: str, start: datetime, end: int, duration: int, wh: float, costs: float) -> bool:
    try:
        client = influxdb_client.InfluxDBClient(
            url=INFLUX_HOST,
            token=INFLUX_TOKEN,
            org=INFLUX_ORG
        )

        data = [
            {
                "measurement": "amtron_charge_records",
                "tags": {
                    "device_id": device_name,
                    "rfid_tag": rfid_tag
                },
                "time": start,
                "fields": {
                    "end": end,
                    "duration": duration,
                    "wh": wh,
                    "costs": costs
                }
            }
        ]
        write_api = client.write_api(write_options=SYNCHRONOUS)
        write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=data)
        print("Successful write data to influx")
        return True
    except Exception as e:
        print(e)
        print("Cannot write data to influx!")
        return False


def write_to_influx_charge_data(device_name: str, act_pwr: float) -> bool:
    try:
        client = influxdb_client.InfluxDBClient(
            url=INFLUX_HOST,
            token=INFLUX_TOKEN,
            org=INFLUX_ORG
        )

        data = [
            {
                "measurement": "amtron_charge_data",
                "tags": {
                    "device_id": device_name
                },
                "time": datetime.now(),
                "fields": {
                    "act_pwr": act_pwr
                }
            }
        ]
        print(data)
        write_api = client.write_api(write_options=SYNCHRONOUS)
        write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=data)
        print("Successful write data to influx")
        return True
    except Exception as e:
        print(e)
        print("Cannot write data to influx!")
        return False
