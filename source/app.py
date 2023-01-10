from threading import Thread
from flask import Flask
from routes.usage import blueprint
from services import MonitoringService
import cash
app: Flask = Flask(__name__)
connection = aaa.acquire_connection()


def setup_routes():
    app.register_blueprint(blueprint)


def setup_services():
    monitoring = MonitoringService()
    Thread(target=monitoring.monitor, args=(connection, 5)).start()


if __name__ == '__main__':
    setup_routes()
    setup_services()
    app.run("127.0.0.1", 8000)
