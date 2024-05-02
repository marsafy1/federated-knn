import redis

subscriber = redis.Redis(
  host='redis-10323.c274.us-east-1-3.ec2.redns.redis-cloud.com',
  port=10323,
  password='hN34pvKTT8nrhOe3S9annZ6R6yNzY5Ia')

# Subscribe to the channel
pubsub = subscriber.pubsub()
pubsub.subscribe('messages')


# Listen for messages (this will block and wait for messages)
for message in pubsub.listen():
    if message['type'] == 'message':
        print('Received:', message['data'].decode())
        subscriber.publish('messages', 'Hello from the client!')