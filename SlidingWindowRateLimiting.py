
# Implement Sliding window rate limiter i.e allow only n request in w window size
from .RateLimitingStrategy import RateLimitingStrategy
from collections import deque
from threading import Lock
from RateLimitResponse import RateLimitResponse

class SlidingWindowRateLimiter(RateLimitingStrategy) :

    def __init__(self, window_size, max_requests):
        super().__init__(window_size, max_requests)
        self.lock = Lock()
    
    def is_request_allowed(self, timestamp, user):
        
        with self.lock :

            current_queue = self.user_buckets[user]

            while current_queue and current_queue[0] <= timestamp- self.window_size: 
                current_queue.popleft()

            if len(current_queue) == self.max_requests :
                retry_after = (current_queue[-1] + self.window_size) - timestamp
                return RateLimitResponse(allowed=False, remaining_requests = None, retry_after=retry_after)
            
            current_queue.append(timestamp)

            return RateLimitResponse(allowed=True, remaining_requests = self.remaining_requests(user), retry_after=0)
    