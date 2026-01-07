import time

from .logging_config import configure_logging
from .tracing import configure_tracing

logger = configure_logging("worker-service")
tracer = configure_tracing("worker-service")


def example_task(data):
    with tracer.start_as_current_span("example_task"):
        logger.info(f"Processing: {data}")
        time.sleep(5)
        logger.info(f"Done: {data}")
