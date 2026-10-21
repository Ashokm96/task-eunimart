import json

import pika
from flask import current_app, jsonify, request

from .operations import Operations


def _connection():
    credentials = pika.PlainCredentials(
        current_app.config["RABBIT_MQ_USER"], current_app.config["RABBIT_MQ_PASSWORD"]
    )
    parameters = pika.ConnectionParameters(
        host=current_app.config["RABBIT_MQ_HOST"],
        port=current_app.config["RABBIT_MQ_PORT"],
        credentials=credentials,
    )
    return pika.BlockingConnection(parameters)


def send():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict) or "method" not in payload or "list" not in payload:
        return jsonify({"message": "JSON body must include method and list"}), 400

    connection = _connection()
    try:
        channel = connection.channel()
        queue = current_app.config["RABBIT_MQ_QUEUE"]
        channel.queue_declare(queue=queue, durable=True)
        channel.basic_publish(
            exchange="",
            routing_key=queue,
            body=json.dumps(payload),
            properties=pika.BasicProperties(delivery_mode=2),
        )
        return jsonify({"message": "Data sent to consumer"}), 200
    finally:
        connection.close()


def receive():
    connection = _connection()
    channel = connection.channel()
    queue = current_app.config["RABBIT_MQ_QUEUE"]
    channel.queue_declare(queue=queue, durable=True)

    def callback(ch, method, properties, body):
        operation = Operations(json.loads(body))
        operation.calculate()
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=False)
    try:
        channel.start_consuming()
    finally:
        connection.close()
    return jsonify({"message": "Consumer stopped"}), 200
