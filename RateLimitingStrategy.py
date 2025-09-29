from abc import ABC, abstractmethod
from collections import defaultdict, deque
from RateLimitResponse import RateLimitResponse

# per-user rate limiting
class RateLimitingStrategy(ABC) :
     
    def __init__(self, window_size, max_requests):
        self.window_size = window_size
        self.max_requests = max_requests
        self.user_buckets = defaultdict(deque)

    @abstractmethod    
    def is_request_allowed(self, timestamp, user) -> RateLimitResponse:
        pass
    
    def remaining_requests(self, user):
        return self.max_requests - len(self.user_buckets[user])    