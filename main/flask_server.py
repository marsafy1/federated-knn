import subprocess
import time
import os
from MyRedis import MyRedis

from flask import Flask, request, jsonify

app = Flask(__name__)





def start_process(script, args=[], identifier=""):
    """ Helper function to start a process with redirected output to a specific file in the script_dump folder. """
    # Ensure the script_dump directory exists
    output_dir = "script_dump"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Define the output file path, incorporating the identifier if provided
    output_file = os.path.join(output_dir, f"{script.split('.')[0]}{identifier}_output.txt")
    with open(output_file, 'w') as f:
        return subprocess.Popen(['python', script] + args, stdout=f, stderr=subprocess.STDOUT)





@app.route('/api/v1/classify', methods=['GET'])
def handle_classification():
    # extract the data from the request
    text = request.args.get('text', None)

    # prepare the response
    response = {
        'data': '',
        'status': 'success'
    }
    status = 200
    # handle if text is None
    if(text is None):
        response['status'] = 'Text is missing'
        status = 400 # bad request code
    else:
        # classify
        response['data'] = get_class_for_input(text)
        print("----will send----")
        print(response)

        redisObject.publish_message('input', 'user', text)

    return jsonify(response), status


def get_class_for_input(user_input):
    while(True):
        if user_input == "e":
            # Publish terminate message to all clients and server
            redisObject.publish_message('TERMINATE','user','EMPTY')
            return "Terminated"
        else:
            # Classify the input using Redis
            redisObject.publish_message('input', 'user', user_input)
        # Listening for incoming messages from Redis and handling user input
        for message in redisObject.get_pubsub().listen():
            print("Listening for messages...")

            if message['type'] == 'message':
                decoded_message = message['data'].decode()
                message_type, sender, message_content = decoded_message.split("#")

                if message_type == "user_response":
                    print(f"Classification for the input was {message_content}")
                    return message_content
    return None

if __name__ == '__main__':
    # Start the server and client scripts
    server_process = start_process('server.py')
    client1_process = start_process('client.py', ['0'], "_1")
    client2_process = start_process('client.py', ['1'], "_2")
    client3_process = start_process('client.py', ['2', 'true'], "_3")

    try:
        # Setup Redis object for publishing and subscribing
        redisObject = MyRedis()
        user_can_input = True

        app.run(debug=True)

    finally:
        redisObject.publish_message('TERMINATE','user','EMPTY')
        print("All processes have been terminated.")

    