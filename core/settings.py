import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

AMTRON_URL = os.environ.get("AMTRON_URL", 'CHANGEME')
AMTRON_PIN1 = os.environ.get("AMTRON_PIN1", 'CHANGEME')

INFLUX_USER = os.environ.get("INFLUX_USER", "CHANGEME")
INFLUX_PASSWORD = os.environ.get("INFLUX_PASSWORD", "CHANGEME")
INFLUX_HOST = os.environ.get("INFLUX_HOST", "CHANGEME")
INFLUX_PORT = os.environ.get("INFLUX_PORT", 8086)
INFLUX_DB = os.environ.get("INFLUX_DB", "sensorlog")
