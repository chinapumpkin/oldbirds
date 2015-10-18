import Queue
import socket
from flask_login import LoginManager
from flask_restful import Api
from flask import Flask
import yaml
from app.make_celery import make_celery
from app.database import db_session
from app.model import User

app = Flask(__name__)
app.secret_key = 'super secret key'
api = Api(app)
lm = LoginManager()
lm.init_app(app)
'''
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(app)
socket_queue = Queue.Queue()

'''

from app import view, model
