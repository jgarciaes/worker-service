from redis import Redis
from rq import Queue
from app.tasks import example_task
from app.settings import settings

if __name__ == "__main__":
    print(f"Enqueuer version: {settings.worker_version}")
    conn = Redis.from_url(settings.redis_url)
    q = Queue("default", connection=conn)
    job = q.enqueue(example_task, "Hello from RQ script!")
    print(f"Enqueued job: {job.id}")
