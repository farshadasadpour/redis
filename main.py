from redis_service import *
from conf import REDIS_SERVER_IP

redis = RedisService(host=REDIS_SERVER_IP)
counter = 1
while True:
    try:
        redis.set_key()
    except Exception as e:
        print(f"Error:{e}")
    else:
        print(f"key set successfully key:{counter}")
        counter += 1