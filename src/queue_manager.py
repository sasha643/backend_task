import redis

class QueueManager:
    def __init__(self, queue_name="linkedin_profiles"):
        self.redis = redis.Redis(host='localhost', port=6379, db=0)
        self.queue_name = queue_name

    def push_new_profiles(self, profile_urls):
        for url in profile_urls:
            self.redis.rpush(self.queue_name, url)

    def get_next_profile_url(self):
        url = self.redis.lpop(self.queue_name)
        return url.decode('utf-8') if url else None

    
    def remove_profile_url(self, url):
        self.redis.lrem(self.queue_name, 1, url)
