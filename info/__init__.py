import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from info.moduel.index import index_blue
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_wtf.csrf import CSRFProtect
import redis

def set_up_log():
    logging.basicConfig(level=logging.DEBUG)
    file_log_handler = RotatingFileHandler('logs/log',maxBytes=104857600,backupCount=10)
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    file_log_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_log_handler)

db = SQLAlchemy()
def create_app():
    set_up_log()
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
    CSRFProtect(app)
    Session(app)
    app.register_blueprint(index_blue)
    return app,redis_store




