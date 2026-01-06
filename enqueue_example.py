from redis import Redis
from rq import Queue
from worker import example_task

if __name__ == "__main__":
    conn = Redis.from_url("redis://localhost:6379/0")
    q = Queue('default', connection=conn)
    job = q.enqueue(example_task, "Hello from RQ script!")
    print(f"Enqueued job: {job.id}")
