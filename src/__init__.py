import time

from .config import settings


def main():
    print(settings.RETRY)
    print(settings.RABBITMQ_USERNAME)
    print(settings.RABBITMQ_PASSWORD)
    print(settings.RABBITMQ_HOST)
    print(settings.RABBITMQ_QUEUE)
    print(settings.RABBITMQ_ROUTING_KEY)
    print(settings.RABBITMQ_EXCHANGE)
    print(settings.RABBITMQ_DEFAULT_USER)
    print(settings.RABBITMQ_DEFAULT_PASS)

    while 1:
        time.sleep(1)
