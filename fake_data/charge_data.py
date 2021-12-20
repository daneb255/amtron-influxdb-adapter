from influx_handler import write_to_influx_charge_data
import random
from datetime import datetime


for mo in range(10, 12):
    for d in range(1, 30):
        for h in range(1, 23):
            for mi in range(1, 59):

                start_datetime = datetime.now().replace(day=d, month=mo, hour=h, minute=mi)

                act_pwr = round(float(random.uniform(1.0, 22.0)))

                write_to_influx_charge_data('AMTRON', act_pwr, start_datetime)
