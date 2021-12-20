from influxdb import InfluxDBClient
from datetime import datetime
from core.settings import INFLUX_PASSWORD, INFLUX_USER, INFLUX_HOST, INFLUX_DB, INFLUX_PORT


def write_to_influx_charge_records(device_name: str, rfid_tag: str, start: datetime, end: int, duration: int, wh: float, costs: float) -> bool:
    try:
        client = InfluxDBClient(host=INFLUX_HOST, port=INFLUX_PORT, username=INFLUX_USER, password=INFLUX_PASSWORD)
        client.switch_database(INFLUX_DB)
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
        client.write_points(data)
        client.close()
        print("Successful write data to influx")
        return True
    except Exception as e:
        print(e)
        print("Cannot write data to influx!")
        return False


def write_to_influx_charge_data(device_name: str, act_pwr: float, date_time) -> bool:
    try:
        client = InfluxDBClient(host=INFLUX_HOST, port=INFLUX_PORT, username=INFLUX_USER, password=INFLUX_PASSWORD)
        client.switch_database(INFLUX_DB)

        data = [
            {
                "measurement": "amtron_charge_data",
                "tags": {
                    "device_id": device_name
                },
                "time": date_time,
                "fields": {
                    "act_pwr": act_pwr
                }
            }
        ]
        print(data)
        client.write_points(data)
        client.close()
        print("Successful write data to influx")
        return True
    except Exception as e:
        print(e)
        print("Cannot write data to influx!")
        return False
