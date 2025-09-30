
# Implement Simple Fixed window rate limiter i.e allow only n request in w window size
from .RateLimitingStrategy import RateLimitingStrategy
from threading import Lock
from collections import defaultdict
from RateLimitResponse import RateLimitResponse
import time

class TokenBucketRateLimiter(RateLimitingStrategy) :

    def __init__(self, max_tokens, refill_rate):
        self.buckets = defaultdict(lambda : max_tokens)
        self.last_refill = defaultdict(lambda : 0)
        self.refill_rate = refill_rate
        self.max_tokens = max_tokens
        self.lock = Lock()
    
    def is_request_allowed(self, timestamp, user):

        with self.lock :

            elapsed_time = timestamp - self.last_refill[user]

            self.buckets[user] = min(self.max_tokens, self.buckets[user]+(elapsed_time*self.refill_rate))
            self.last_refill[user] = timestamp

            if self.buckets[user] <= 0 :

                # refill_rate n token per seconds we need to find token in 1 sec
                retry_after = 1/self.refill_rate

                return RateLimitResponse(allowed=False, remaining_requests = None, retry_after = retry_after)
            
            self.buckets[user] -=1
            
            return RateLimitResponse(allowed=True, remaining_requests = int(self.buckets[user]), retry_after=0)
    
     