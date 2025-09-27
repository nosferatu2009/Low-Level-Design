from RateLimiter import RateLimiter

def main() :

    windowSize = int(input("Enter Window Size "))
    requestsAllowed = int(input("Enter No of Request Allowed "))

    rateLimiter = RateLimiter(windowSize, requestsAllowed)
    
    while True :

        try :

            timestamp, user = [x.strip() for x in input("Enter Timestamp and User ").split(',')]
            if timestamp.lower() == 'q' :
                print("Finish")
                break
            check = rateLimiter.is_request_allowed(int(timestamp), user)
            print(f"Is Request Allowed - {check}")
            print(f"\nRemaining requests - {rateLimiter.remaining_requests()}")


        except ValueError :
            print("Invalid Input format - Please use format <timestamp>,<user> ")

if __name__ == "__main__" :
    main()