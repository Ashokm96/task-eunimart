import os


SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///messages.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
RABBIT_MQ_HOST = os.getenv("RABBIT_MQ_HOST", "rabbitmq")
RABBIT_MQ_PORT = int(os.getenv("RABBIT_MQ_PORT", "5672"))
RABBIT_MQ_USER = os.getenv("RABBIT_MQ_USER", "")
RABBIT_MQ_PASSWORD = os.getenv("RABBIT_MQ_PASSWORD", "")
RABBIT_MQ_QUEUE = os.getenv("RABBIT_MQ_QUEUE", "operations")
