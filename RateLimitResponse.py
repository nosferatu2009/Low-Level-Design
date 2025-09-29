
class RateLimitResponse :

    def __init__(self, allowed, retry_after = None, remaining_requests = None) :
        self.allowed = allowed
        self.retry_after = retry_after
        self.remaining_requests = remaining_requests

    def __repr__(self):
        return f"<RateLimitResponse allowed={self.allowed}, remaining={self.remaining_requests}, retry_after={self.retry_after}s>"