from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

from .settings import settings


def configure_tracing(service_name: str) -> trace.Tracer:
    resource = Resource(
        attributes={"service.name": service_name, "service.version": settings.worker_version}
    )
    trace.set_tracer_provider(TracerProvider(resource=resource))

    otlp_exporter = OTLPSpanExporter(endpoint=settings.otel_exporter_otlp_endpoint)
    trace.get_tracer_provider().add_span_processor(SimpleSpanProcessor(otlp_exporter))

    console_exporter = ConsoleSpanExporter()
    trace.get_tracer_provider().add_span_processor(SimpleSpanProcessor(console_exporter))

    return trace.get_tracer(__name__)
