import redis

class MyRedis:
    def __init__(self):
        self.redisObject = redis.Redis(
        host='redis-10323.c274.us-east-1-3.ec2.redns.redis-cloud.com',
        port=10323,
        password='hN34pvKTT8nrhOe3S9annZ6R6yNzY5Ia')
        self.pubsub = self.redisObject.pubsub()
        self.pubsub.subscribe('messages')

    def get_pubsub(self):
        return self.pubsub
    
    def publish_message(self, message_type, sender, message):
        self.redisObject.publish('messages', f'{message_type}#{sender}#{message}')

if __name__ == '__main__':
    redisObject = MyRedis()


