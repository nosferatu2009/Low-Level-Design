from RateLimiter import RateLimiter
from RateLimitStrategies.FixedWindowRateLimiting import FixedWindowRateLimiter
from RateLimitStrategies.SlidingWindowRateLimiting import SlidingWindowRateLimiter
from RateLimitStrategies.TokenBucketRateLimiting import TokenBucketRateLimiter
from RateLimitStrategies.LeakyBucketRateLimiting import LeakyBucketRateLimiter

def main() :

    # windowSize = int(input("Enter Window Size "))
    # requestsAllowed = int(input("Enter No of Request Allowed "))
     
    # rate_limiting_strategy = FixedWindowRateLimiter(windowSize, requestsAllowed)
    # rate_limiting_strategy = SlidingWindowRateLimiter(windowSize, requestsAllowed)

    # max_tokens = int(input("Enter Max Tokens "))
    # refill_rate = int(input("Enter Refill rate "))

    # rate_limiting_strategy = TokenBucketRateLimiter(max_tokens = max_tokens, refill_rate = refill_rate)

    capacity = int(input("Enter Capacity "))
    leak_rate = int(input("Enter Leak rate "))

    rate_limiting_strategy = LeakyBucketRateLimiter(capacity=capacity, leak_rate = leak_rate)

    rateLimiter = RateLimiter(rate_limiting_strategy)
    
    while True :

        try :
            
            raw = input("Enter Timestamp and User i.e. <timestamp>,<user>")
            if raw.lower() == 'q' :
                print("Finish")
                return
            
            timestamp, user = [x.strip() for x in raw.split(',')]
            
            response = rateLimiter.is_request_allowed(int(timestamp), user)
            print(f"Rate Limiter response - {response}")

        except ValueError :
            print("Invalid Input format - Please use format <timestamp>,<user> ")

if __name__ == "__main__" :
    main()