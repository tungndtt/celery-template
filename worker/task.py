from celery import Celery
from kombu import Queue
from dotenv import load_dotenv, find_dotenv
from os import environ


load_dotenv(find_dotenv())
host = environ.get('REDIS_HOST', 'localhost')
port = environ.get('REDIS_PORT', '6379')

# Celery worker
worker = Celery(
    'worker',
    broker=f'redis://{host}:{port}/0',
    backend=f'redis://{host}:{port}/0'
)

# Specify the worker config
worker.conf.update(
    broker_connection_retry_on_startup=True,
    task_queues=[Queue('task_queue')], # TODO: Modify the `task_queue` w.r.t the client
    # Further configuration can be found in https://docs.celeryq.dev/en/latest/userguide/workers.html
)

# Specify the task's business logic
@worker.task(name='task', queue='task_queue', acks_late=True)
def task():
    # TODO: Implement the task logic
    pass

