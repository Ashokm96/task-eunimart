from flask import Blueprint

from ..controllers import main, rabbit_mq

api = Blueprint("api", __name__)


@api.get("/")
def home():
    return main.home()


@api.get("/health")
def health():
    return {"status": "healthy"}, 200


@api.post("/publish")
def publish():
    return rabbit_mq.send()


@api.get("/consume")
def consume():
    return rabbit_mq.receive()
