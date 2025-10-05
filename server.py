from flask import Flask, jsonify, request
import uuid
import time

app = Flask(__name__)

processed_requests = {}

@app.route("/health", methods=['GET'])
def hello():
    return jsonify({"msg" :  "Hello"}), 200

@app.route('/process_payment', methods=['POST'])
def process_payment():
    
    data = request.get_json()
    print(f'{data}')

    idempotency_key = request.headers.get('idempotency-key')

    if not idempotency_key :
        return jsonify({"error" : "missing idempotency key in the header"}), 400
    
    if idempotency_key in processed_requests.keys():
        print("Request Already Processed")
        return jsonify(processed_requests[idempotency_key]), 200
    
    # here we will new request that we need to process
    # like do some database operations etc for transaction

    print("Processing new request")

    time.sleep(2)

    response = {    
                "status" : "success",
                "transaction_id" : uuid.uuid4()
                }
    
    processed_requests[idempotency_key] = response
    print("Processed new request")

    return jsonify(response), 200


if __name__ == "__main__" :
    app.run(host='localhost', debug=True)
    

