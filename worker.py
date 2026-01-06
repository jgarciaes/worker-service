import time
from rq import Worker, Queue
import redis

def example_task(data):
    print(f"Processing: {data}")
    time.sleep(5)
    print(f"Done: {data}")

if __name__ == "__main__":
    redis_url = "redis://localhost:6379/0"
    conn = redis.from_url(redis_url)
    queue = Queue('default', connection=conn)
    worker = Worker([queue], connection=conn)
    worker.work()
