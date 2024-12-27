import os
from celery import Celery
from pollution_data import fetch_air_pollution_data
from datetime import timedelta

# Get environment variables
latitude = float(os.getenv('LATITUDE', '40.7128'))
longitude = float(os.getenv('LONGITUDE', '-74.0060'))
interval_in_seconds = float(os.getenv('INTERVAL_IN_SECONDS', '60'))
api_key = os.getenv('API_KEY')

app = Celery(
    'pollution_tracker',
    broker='redis://redis:6379/0',  # Redis as the message broker
    backend='redis://redis:6379/0'  # Redis as the result backend
)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(timedelta(seconds=5), fetch_data.s())


@app.task
def fetch_data():
    return fetch_air_pollution_data(latitude, longitude, api_key)
