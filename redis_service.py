from ast import Return
import redis
import random
import string
import conf

class RedisService:
    def __init__(self,host:str,port=conf.REDIS_PORT) -> None:
        self.host = host
        self.port = port
        self.redis_obj = redis.Redis(host=self.host,port=self.port)


    def set_key(self):
        try:
            self.redis_obj.set(self.__key_generator(),self.__value_generator())
        except Exception as e:
            print(f"E:{e}")
        
    
    def get_value(self,key):
        try:
            value = self.redis_obj.get(key)
        except Exception as e:
            print(f"E:{e}")
        
        return f"key is :{key} and value is: {value}"
    
    @staticmethod
    def __key_generator():
        """this method generate key for redis

        Returns:
            _type_: string
        """
        letters  = string.ascii_lowercase
        return ( ''.join(random.choice(letters) for i in range(conf.KEY_LEN)) )
    
    
    @staticmethod
    def __value_generator():
        """this method generate value for redis key

        Returns:
            _type_: integer
        """
        letters = string.digits
        return ( ''.join(random.choice(letters) for i in range(conf.VALUE_LEN)) )