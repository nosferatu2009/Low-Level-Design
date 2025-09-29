
# Implement Simple Fixed window rate limiter i.e allow only n request in w window size
from .RateLimitingStrategy import RateLimitingStrategy
from threading import Lock
from collections import defaultdict
from RateLimitResponse import RateLimitResponse

class FixedWindowRateLimiter(RateLimitingStrategy) :

    def __init__(self, window_size, max_requests):
        super().__init__(window_size, max_requests)
        self.counters = defaultdict(lambda:1)
        self.lock = Lock
    
    def is_request_allowed(self, timestamp, user):

        with self.lock :

            current_counter = self.counters[user]

            if timestamp > (self.window_size * current_counter):
                self.counters[user] = timestamp//self.window_size + 1
                self.reset_bucket(user)  

            if len(self.user_buckets[user]) == self.max_requests :
                retry_after = (self.window_size*current_counter) - timestamp + 1
                return RateLimitResponse(allowed=False, remaining_requests = None, retry_after=retry_after)
            
            self.user_buckets[user].append(timestamp)
            
            return RateLimitResponse(allowed=True, remaining_requests = self.remaining_requests(user), retry_after=0)
    
    def reset_bucket(self, user):
        self.user_buckets[user].clear()
     