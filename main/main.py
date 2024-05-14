import subprocess
import time
import os
from MyRedis import MyRedis

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

        while(True):
            if user_can_input:
                user_input = input("Enter a string to classify (type 'e' to exit): ")
                if len(user_input) > 0:
                    user_can_input = False
                    if user_input == "e":
                        # Publish terminate message to all clients and server
                        redisObject.publish_message('TERMINATE','user','EMPTY')
                        break
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
                        # time.sleep(3)
                        user_can_input = True
                        break
    finally:
        redisObject.publish_message('TERMINATE','user','EMPTY')
        print("All processes have been terminated.")
