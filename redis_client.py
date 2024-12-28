import redis
import json

redis = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)


def insert_data_to_redis(air_pollution_data):
    key = air_pollution_data['timestamp']
    filtered_data = {
        "air_quality_index": air_pollution_data['air_quality_index'],
        "components": air_pollution_data['components'],
    }
    value = json.dumps(filtered_data)
    redis.set(key, value)
