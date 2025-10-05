import uuid
import requests
import random
import time

headers = {
    "idempotency-key" : str(uuid.uuid4())
}
data = {
    "amount" : 100,
    "CUR" : "INR"
}

url = "http://127.0.0.1:5000/process_payment"
MAX_RETRIES = 5
BASE_DELAY = 1

for attempt in range(1, MAX_RETRIES):

    try:
        response = requests.post(url=url, json=data, headers=headers, timeout=3, verify=False)

        if response.status_code in [200, 201] :
            print("Request Processed")
        else :
            # server error
            print("Server Error")
    # network error 
    except requests.exceptions.RequestException as ex:
        print("Network Error")
    
    backoff = BASE_DELAY* (2**(attempt-1))
    jitter = random.uniform(0, 0.3*backoff)

    time.sleep(backoff + jitter)

else :
    print("Payment failed after maximum retires")



