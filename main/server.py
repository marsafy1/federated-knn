from collections import Counter
from MyRedis import MyRedis

CLIENTS_NUM = 2
default_responses_ack = {}
responses_ack = {}
client_responses = {}
redisObject = MyRedis()

def initialize_response_objects():
    for i in range(0, CLIENTS_NUM):
        default_responses_ack[f"client_{i}"] = False
        responses_ack[f"client_{i}"] = False
        client_responses[f"client_{i}"] = ''
    print(responses_ack)

def all_ack():
    for sender in responses_ack:
        if(not responses_ack[sender]):
            return False
    return True

def reset_acks():
    responses_ack = default_responses_ack.copy()

def handle_aggregation():
    print("Handling aggss")
    print(client_responses)
    responses = []
    for client in client_responses:
        responses.append(client_responses[client])

    count = Counter(responses)
    most_common_num, most_common_count = count.most_common(1)[0]

    classification_result = most_common_num
    redisObject.publish_message('user_response', 'server', classification_result)
    return classification_result

if __name__ == '__main__':
    print(f"Server up and running...")
    initialize_response_objects()
    can_accept_inputs = True
    # Listen for messages (this will block and wait for messages)
    for message in redisObject.get_pubsub().listen():
        message_type = message['type']
        if message['type'] == 'message':
            message = message['data'].decode()
    
            message_type = message.split("#")[0]
            sender = message.split("#")[1]
            message_content = message.split("#")[2]
    
            print(f'{message_type}@{sender}:', message_content)
    
            if(message_type == "input" and can_accept_inputs):
                redisObject.publish_message('client_task', 'server', message_content)

            if(message_type == "classification"):
                if sender in responses_ack.keys():
                    responses_ack[sender] = True
                    client_responses[sender] = message_content
                
                if all_ack():
                    print('All Received -> Start aggregation')
                    reset_acks()
                    handle_aggregation()
            
            if(message_type == "TERMINATE"):
                break
                    
                    
    



    