from celery import Celery
from celery.result import AsyncResult
import asyncio
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())
host = os.environ.get('REDIS_HOST', 'localhost')
port = os.environ.get('REDIS_PORT', '6379')
polling_interval = int(os.environ.get('POLLING_INTERVAL', 1))

# Celery client
client = Celery(
    'client',
    broker=f'redis://{host}:{port}/0',
    backend=f'redis://{host}:{port}/0'
)

# Async wait for task result
async def wait_for_result(task_id):
    result = AsyncResult(task_id, app=client)
    while not result.ready():
        print(f"[Client] Waiting for result of task {task_id}...")
        await asyncio.sleep(polling_interval)
    print(f"[Client] Task {task_id} completed with result: {result.result}")

# Simple use of sending task and waiting for result asynchronously
async def run_task():
    # TODO: Modify the implementation based on requirements
    result = client.send_task('task', args=(), queue='task_queue')
    await wait_for_result(result.id)

# asyncio.run(run_task())