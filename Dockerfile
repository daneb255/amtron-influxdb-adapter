FROM python:3.9-slim-bullseye

WORKDIR /app

COPY ./core/settings.py /app/core/settings.py
COPY Pipfile* amtron.py amtron_power.py influx_handler.py /app/

RUN pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy --clear

CMD [ "python", "amtron.py" ]