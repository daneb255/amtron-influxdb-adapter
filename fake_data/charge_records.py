from influx_handler import write_to_influx_charge_records
import random
from datetime import datetime, timedelta
import time


for i in range(1, 30):
    start_datetime = datetime.now().replace(day=i, month=int(random.uniform(1, 12)), hour=int(random.uniform(1, 23)), minute=int(random.uniform(1, 23)),
                                            second=int(random.uniform(1, 59)))
    end_datetime = start_datetime + timedelta(hours=int(random.uniform(1, 3)))

    amt_wh = round(float(random.uniform(1.0, 48.0)))
    charging_costs = random.uniform(1000, 5999) / 1000

    unixtime_start = int(time.mktime(start_datetime.timetuple()))
    unixtime_end = int(time.mktime(end_datetime.timetuple()))

    duration = datetime.fromtimestamp(unixtime_end) - datetime.fromtimestamp(unixtime_start)
    write_to_influx_charge_records('AMTRON', '123456789', start_datetime,
                                   unixtime_end, duration.seconds, amt_wh, charging_costs)
