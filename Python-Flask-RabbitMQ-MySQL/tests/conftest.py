import pytest


@pytest.fixture
def app_config():
    return {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "RABBIT_MQ_HOST": "localhost",
        "RABBIT_MQ_PORT": 5672,
        "RABBIT_MQ_USER": "test",
        "RABBIT_MQ_PASSWORD": "test",
        "RABBIT_MQ_QUEUE": "operations-test",
    }
