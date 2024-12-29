import os
from datetime import timedelta
from celery import Celery
from celery.signals import worker_ready
from celery import chain
from pollution_data import fetch_air_pollution_data
from alert import send_email
from redis_client import create_redis_time_series, insert_time_series_data_to_redis

# Get environment variables
latitude = float(os.getenv('LATITUDE', '40.7128'))
longitude = float(os.getenv('LONGITUDE', '-74.0060'))
interval_in_seconds = float(os.getenv('INTERVAL_IN_SECONDS', '10'))
api_key = os.getenv('API_KEY')
from_email = os.getenv('FROM_EMAIL')
from_password = os.getenv('FROM_PASSWORD')
to_email = os.getenv('TO_EMAIL')

app = Celery(
    'pollution_tracker',
    broker='redis://redis:6379/0',
    backend=None,
)


@worker_ready.connect
def at_worker_start(sender, **kwargs):
    set_up_redis_time_series.apply_async()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        timedelta(seconds=interval_in_seconds),
        trigger_chain.s()
    )


@app.task
def set_up_redis_time_series():
    create_redis_time_series()


@app.task
def trigger_chain():
    # Trigger the chain manually
    chain(fetch_data.s() | send_alert.s())()


@app.task
def fetch_data():
    air_pollution_data = fetch_air_pollution_data(latitude, longitude, api_key)
    insert_time_series_data_to_redis(air_pollution_data)
    return air_pollution_data


@app.task
def send_alert(air_pollution_data):
    # If air quality is poor (index 4 and 5), send an alert
    if air_pollution_data["air_quality_index"] >= 4:
        send_email(
            air_pollution_data["air_quality_index"],
            from_email,
            from_password,
            to_email
        )
