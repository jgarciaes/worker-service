import os
from dataclasses import dataclass


@dataclass
class Settings:
    worker_version: str = os.getenv("WORKER_VERSION", "dev")
    redis_url: str = os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0")
    otel_exporter_otlp_endpoint: str = os.getenv(
        "OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4318/v1/traces"
    )


settings = Settings()
