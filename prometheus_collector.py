from prometheus_client import Counter, Gauge, start_http_server, REGISTRY
from redis_client import get_redis_time_series_data
import time


class PrometheusCollector(object):
    def __init__(self):
        pass

    def collect(self):
        keys = ['air_quality_index', 'co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']
        for key in keys:
            data = get_redis_time_series_data(key)
            gauge = Gauge(key, f'{key} levels')
            for point in data:
                # TODO: set timestamp of point or always fetch the last of redis time series
                gauge.set(point[1])
            yield gauge


if __name__ == "__main__":
    start_http_server(5000)
    counter = Counter('request_count', 'A simple counter for counting requests')
    REGISTRY.register(PrometheusCollector())
    while True:
        counter.inc()
        time.sleep(5)
