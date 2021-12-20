import requests
import time

from datetime import datetime, timedelta

from core.settings import AMTRON_URL, AMTRON_PIN1
from influx_handler import write_to_influx_charge_records


def get_device_data() -> str:
    try:
        url = f'{AMTRON_URL}/MHCP/1.0/DevInfo'
        headers = {
            'Accept': 'application/json'
        }
        params = {
            'DevKey': AMTRON_PIN1
        }
        r = requests.get(url, headers=headers, params=params)
        if r.status_code == 200:
            data = r.json()
            print('Successfully get device information!')
            return data['DevName']
        else:
            print(f'Cannot get device information from {AMTRON_URL} !')
            return ''

    except Exception as e:
        print(str(e))
        return ''


def get_charging_data(d_name: str, start: int, end: int) -> tuple:
    try:
        amt_wh = 0.0
        charging_costs = 0.0

        url = f'{AMTRON_URL}/MHCP/1.0/ChargeRecords'
        headers = {
            'Accept': 'application/json'
        }
        params = {
            'DevKey': AMTRON_PIN1,
            'Start': start,
            'End': end,
            'State': 'Open',
        }
        requests.get(url, headers=headers, params=params)
        params.update({'State': 'Read'})
        r = requests.get(url, headers=headers, params=params)
        if r.status_code == 200:
            data = r.json()
            if data['Transactions']:
                for transaction in data['Transactions']:
                    if transaction['Stop']:
                        amt_wh = round(float(transaction['ChgNrg']) / 1000, 1)
                        charging_costs = transaction['ChgCosts'] / 1000
                        duration = datetime.fromtimestamp(transaction['Stop']) - datetime.fromtimestamp(transaction['Start'])
                        write_to_influx_charge_records(d_name, transaction['Uid'], datetime.fromtimestamp(transaction['Start']),
                                                       transaction['Stop'], duration.seconds, amt_wh, charging_costs)
        else:
            print(f'Cannot get charging data from {AMTRON_URL} !')

        params.update({'State': 'Close'})
        requests.get(url, headers=headers, params=params)
        return amt_wh, charging_costs

    except Exception as e:
        print(str(e))
        return 0.0, 0.0


if __name__ == '__main__':
    end_datetime = datetime.now()
    start_datetime = end_datetime - timedelta(hours=6)

    unixtime_start = int(time.mktime(start_datetime.timetuple()))
    unixtime_end = int(time.mktime(end_datetime.timetuple()))

    device_name = get_device_data()
    get_charging_data(device_name, unixtime_start, unixtime_end)
