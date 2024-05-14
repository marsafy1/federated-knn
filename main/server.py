from collections import Counter
from MyRedis import MyRedis

CLIENTS_NUM = 3
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
    global responses_ack
    responses_ack = default_responses_ack.copy()

from collections import Counter


def handle_aggregation(key='most_common'):
    print("Handling aggregation...")
    print(client_responses)
    classification_result = None
    if key == 'most_common':
        classification_result = most_common_aggregation()
    elif key == 'weighted':
        classification_result = weighted_voting_aggregation()
    elif key == 'average_probabilities':
        classification_result = average_probabilities_aggregation()
    elif key == 'bayesian':
        classification_result = bayesian_aggregation()
    print(f"Key: {key} , Aggregation result: {classification_result}")
    # redisObject.publish_message('user_response', 'server', classification_result)
    return classification_result

def most_common_aggregation():
    responses = [client_responses[client].split(",")[0] for client in client_responses]
    count = Counter(responses)
    most_common_result, most_common_count = count.most_common(1)[0]
    return most_common_result

def weighted_voting_aggregation(weights={'client1': 3, 'client2': 1, 'client3': 1}):
    vote_counts = {}
    for client, data in client_responses.items():
        predicted_class = data.split(',')[0]
        vote_counts[predicted_class] = vote_counts.get(predicted_class, 0) + weights.get(client, 1)
    return max(vote_counts, key=vote_counts.get)

def average_probabilities_aggregation():
    total_prob_0, total_prob_1 = 0, 0
    num_clients = len(client_responses)
    for data in client_responses.values():
        _, prob_0, prob_1 = data.split(',')
        total_prob_0 += float(prob_0)
        total_prob_1 += float(prob_1)
    average_0 = total_prob_0 / num_clients
    average_1 = total_prob_1 / num_clients
    return '0' if average_0 > average_1 else '1'

def bayesian_aggregation(prior_prob_0=0.5, prior_prob_1=0.5):
    post_prob_0, post_prob_1 = prior_prob_0, prior_prob_1
    for data in client_responses.values():
        _, prob_0, prob_1 = data.split(',')
        post_prob_0 *= float(prob_0)
        post_prob_1 *= float(prob_1)
    normalization_factor = post_prob_0 + post_prob_1 if post_prob_0 + post_prob_1 != 0 else 1
    post_prob_0 /= normalization_factor
    post_prob_1 /= normalization_factor
    return '0' if post_prob_0 > post_prob_1 else '1'


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
                    can_accept_inputs = False
                    print('All Received -> Start aggregation')
                    reset_acks()
                    classification_result = handle_aggregation(key = 'most_common')
                    redisObject.publish_message('user_response', 'server', classification_result)
                    handle_aggregation(key = 'weighted')
                    handle_aggregation(key = 'average_probabilities')
                    handle_aggregation(key = 'bayesian')
                    can_accept_inputs = True


            
            if(message_type == "TERMINATE"):
                break
    print(f"Server shutting down...")
                    
                    
    



    