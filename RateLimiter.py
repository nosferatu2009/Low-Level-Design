
# Implement Simple Fixed window rate limiter i.e allow only n request in w window size

class RateLimiter :

    def __init__(self, window_size, max_requests):
        self.window_size = window_size
        self.max_requests = max_requests
        self.request_in_bucket = []
        self.counter = 1
    
    def is_request_allowed(self, timestamp, user) :

        if timestamp > (self.window_size * self.counter):
            self.counter = timestamp//self.window_size + 1
            self.reset_bucket()  

        if len(self.request_in_bucket) == self.max_requests :
            print(f"Please Try After - {(self.window_size*self.counter) - timestamp + 1}s")
            return False
        
        self.request_in_bucket.append(timestamp)
        
        return True
    
    def reset_bucket(self):
        print(f"\nBucket Reset, counter {self.counter}")
        self.request_in_bucket = []
    
    def remaining_requests(self):
        return self.max_requests - len(self.request_in_bucket)    