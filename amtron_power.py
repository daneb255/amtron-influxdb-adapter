import requests

from core.settings import AMTRON_URL, AMTRON_PIN1
from influx_handler import write_to_influx_charge_data
from amtron import get_device_data


def get_charge_data() -> str:
    try:
        url = f'{AMTRON_URL}/MHCP/1.0/ChargeData'
        headers = {
            'Accept': 'application/json'
        }
        params = {
            'DevKey': AMTRON_PIN1
        }
        r = requests.get(url, headers=headers, params=params)
        if r.status_code == 200:
            data = r.json()
            print('Successfully get charge data information!')
            return data['ActPwr']
        else:
            print(f'Cannot get device information from {AMTRON_URL} !')
            return ''

    except Exception as e:
        print(str(e))
        return ''


if __name__ == '__main__':

    device_name = get_device_data()
    act_pwr = get_charge_data()
    write_to_influx_charge_data(device_name, float(act_pwr))
