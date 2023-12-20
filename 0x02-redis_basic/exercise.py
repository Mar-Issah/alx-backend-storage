#!/usr/bin/env python3

from typing import Callable, Optional, Union
from uuid import uuid4
import redis
from functools import wraps

class Cache:
    """Cache class"""

    def __init__(self):
        """Constructor for the class."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    # @count_calls
    # @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store input data in Redis.
        """
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key

    # def get(self, key: str,
    #         fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
    #     '''
    #         Get data from the cache.
    #     '''
    #     value = self._redis.get(key)
    #     if fn:
    #         value = fn(value)
    #     return value

    # def get_str(self, key: str) -> str:
    #     '''
    #         Get a string from the cache.
    #     '''
    #     value = self._redis.get(key)
    #     return value.decode('utf-8')

    # def get_int(self, key: str) -> int:
    #     '''
    #         Get an int from the cache.
    #     '''
    #     value = self._redis.get(key)
    #     try:
    #         value = int(value.decode('utf-8'))
    #     except Exception:
    #         value = 0
    #     return value
