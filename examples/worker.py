from celery import Celery
from kombu import Queue
from time import sleep
from dotenv import load_dotenv, find_dotenv
from os import environ


load_dotenv(find_dotenv())
host = environ.get('REDIS_HOST', 'localhost')
port = environ.get('REDIS_PORT', '6379')

worker = Celery(
    'worker',
    broker=f'redis://{host}:{port}/0',
    backend=f'redis://{host}:{port}/0'
)

worker.conf.update(
    broker_connection_retry_on_startup=True,
    task_queues=[Queue('add_queue'), Queue('subtract_queue')]
)

@worker.task(name='add', queue='add_queue', acks_late=True)
def add(x, y):
    result = x + y
    sleep(2)
    return result

@worker.task(name='subtract', queue='subtract_queue')
def subtract(x, y):
    result = x - y
    sleep(2)
    return result
