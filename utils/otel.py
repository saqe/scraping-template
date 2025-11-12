from opentelemetry.instrumentation.botocore import BotocoreInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.instrumentation.redis import RedisInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.sqlite3 import SQLite3Instrumentor

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider

trace.set_tracer_provider(TracerProvider())

# Python Internal Logging.
LoggingInstrumentor().instrument(set_logging_format=True)

# Redis
RedisInstrumentor().instrument(tracer_provider=trace.get_tracer_provider())

# Requests
RequestsInstrumentor().instrument()

#
SQLite3Instrumentor().instrument()

# Instrument Botocore
BotocoreInstrumentor().instrument(
    tracer_provider=trace.get_tracer_provider()
)
