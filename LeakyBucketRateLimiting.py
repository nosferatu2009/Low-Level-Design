
# Implement Simple Fixed window rate limiter i.e allow only n request in w window size
from .RateLimitingStrategy import RateLimitingStrategy
from threading import Lock
from collections import defaultdict, deque
from RateLimitResponse import RateLimitResponse
import time

class LeakyBucketRateLimiter(RateLimitingStrategy) :

    def __init__(self, capacity, leak_rate):
        self.buckets = defaultdict(deque)
        self.last_refill = defaultdict(lambda : 0)
        self.leak_rate = leak_rate
        self.capacity = capacity
        self.lock = Lock()
    
    def is_request_allowed(self, timestamp, user):

        with self.lock :

            elapsed_time = timestamp - self.last_refill[user]

            # leak requests we need to pop 
            leaked_requests = int(elapsed_time*self.leak_rate)

            while self.buckets[user] and leaked_requests :
                self.buckets[user].popleft()
                leaked_requests-=1

            # to avoid adding refill time in case requests at same time  
            if elapsed_time > 0 :
                self.last_refill[user] = timestamp

            if len(self.buckets[user]) >= self.capacity :

                # refill_rate n token per seconds we need to find token in 1 sec
                retry_after = 1/self.leak_rate

                return RateLimitResponse(allowed=False, remaining_requests = None, retry_after = retry_after)

            self.buckets[user].append(timestamp)
            
            return RateLimitResponse(allowed=True, remaining_requests = self.capacity - len(self.buckets[user]), retry_after=0)
     