import redis
from rq import Worker, Queue

from .logging_config import configure_logging
from .settings import settings

logger = configure_logging("worker-service")


def start_worker() -> None:
    conn = redis.from_url(settings.redis_url)
    queue = Queue("default", connection=conn)
    logger.info(f"Worker version: {settings.worker_version}")
    logger.info(f"Connecting to Redis: {settings.redis_url}")
    worker = Worker([queue], connection=conn)
    worker.work()
