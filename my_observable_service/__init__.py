from werkzeug.wsgi import DispatcherMiddleware
from prometheus_client import make_wsgi_app

from .hello_app import app as hello_app

# Add prometheus wsgi middleware to route /metrics requests
app = DispatcherMiddleware(hello_app, {
    '/metrics': make_wsgi_app()
})

