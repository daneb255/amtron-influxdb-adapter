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

INFLUX_TOKEN = os.environ.get("INFLUX_TOKEN", "CHANGEME")
INFLUX_BUCKET = os.environ.get("INFLUX_BUCKET", "CHANGEME")
INFLUX_HOST = os.environ.get("INFLUX_HOST", "CHANGEME")
INFLUX_ORG = os.environ.get("INFLUX_ORG", "CHANGEME")
