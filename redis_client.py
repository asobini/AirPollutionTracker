import redis

redis = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)
redis_time_series = redis.ts()


def insert_time_series_data_to_redis(air_pollution_data):
    # convert timestamp to milliseconds
    timestamp = air_pollution_data['timestamp'] * 1000
    air_quality_index = air_pollution_data['air_quality_index']
    co = air_pollution_data['components']['co']
    no = air_pollution_data['components']['no']
    no2 = air_pollution_data['components']['no2']
    o3 = air_pollution_data['components']['o3']
    so2 = air_pollution_data['components']['so2']
    pm2_5 = air_pollution_data['components']['pm2_5']
    pm10 = air_pollution_data['components']['pm10']
    nh3 = air_pollution_data['components']['nh3']

    data_points = [
        ("air_quality_index", timestamp, air_quality_index),
        ("co", timestamp, co),
        ("no", timestamp, no),
        ("no2", timestamp, no2),
        ("o3", timestamp, o3),
        ("so2", timestamp, so2),
        ("pm2_5", timestamp, pm2_5),
        ("pm10", timestamp, pm10),
        ("nh3", timestamp, nh3),
    ]

    redis_time_series.madd(data_points)


def create_redis_time_series():
    if not redis.exists("air_quality_index"):
        redis_time_series.create("air_quality_index")
    if not redis.exists("co"):
        redis_time_series.create("co")
    if not redis.exists("no"):
        redis_time_series.create("no")
    if not redis.exists("no2"):
        redis_time_series.create("no2")
    if not redis.exists("o3"):
        redis_time_series.create("o3")
    if not redis.exists("so2"):
        redis_time_series.create("so2")
    if not redis.exists("pm2_5"):
        redis_time_series.create("pm2_5")
    if not redis.exists("pm10"):
        redis_time_series.create("pm10")
    if not redis.exists("nh3"):
        redis_time_series.create("nh3")


def get_redis_time_series_data(key):
    return redis_time_series.get(key)
