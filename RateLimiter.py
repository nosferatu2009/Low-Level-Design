
from RateLimitStrategies.RateLimitingStrategy import RateLimitingStrategy

class RateLimiter() :
     
    def __init__(self, rate_limiting_strategy):
        self.rate_limiting_strategy = rate_limiting_strategy
    
    def is_request_allowed(self, timestamp, user):
        return self.rate_limiting_strategy.is_request_allowed(timestamp, user)
    
    def remaining_requests(self, user):
        return self.rate_limiting_strategy.remaining_requests(user)