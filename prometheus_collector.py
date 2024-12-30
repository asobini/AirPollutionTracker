from prometheus_client import start_http_server, REGISTRY
from prometheus_client.core import GaugeMetricFamily
from redis_client import get_redis_time_series_data
import time


class PrometheusCollector(object):
    def __init__(self):
        pass

    def collect(self):
        keys = ['air_quality_index', 'co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']
        try:
            for key in keys:
                data = get_redis_time_series_data(key)
                if data is not None:
                    gauge = GaugeMetricFamily(key, f'{key} levels')
                    gauge.add_metric(['value'], data[1])
                    yield gauge
        except Exception:
            return


if __name__ == "__main__":
    start_http_server(5000)
    REGISTRY.register(PrometheusCollector())
    while True:
        time.sleep(5)
