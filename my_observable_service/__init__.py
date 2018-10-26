from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import subprocess

app = Flask(__name__)
metrics = PrometheusMetrics(app)

my_version = subprocess.check_output(["git", "describe", "--always"]).strip()
metrics.info('app_info', 'My observable service', version=my_version)

@app.route("/")
def hello():
    return "Hello World!"
