from redis_service import *
from conf import REDIS_SERVER_IP

redis = RedisService(host=REDIS_SERVER_IP)
while True:
    try:
        redis.set_key()
    except Exception as e:
        print(f"Error:{e}")
    else:
        print("key set successfully")