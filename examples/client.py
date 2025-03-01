from celery import Celery
from celery.result import AsyncResult
import asyncio
from dotenv import load_dotenv, find_dotenv
from os import environ


load_dotenv(find_dotenv())
host = environ.get('REDIS_HOST', 'localhost')
port = environ.get('REDIS_PORT', '6379')

client = Celery(
    'client',
    broker=f'redis://{host}:{port}/0',
    backend=f'redis://{host}:{port}/0'
)

async def wait_for_result(task_id):
    result = AsyncResult(task_id, app=client)
    while not result.ready():
        print(f"[Client] Waiting for result of task {task_id}...")
        await asyncio.sleep(1)
    print(f"[Client] Task {task_id} completed with result: {result.result}")

async def run_tasks():
    task_names = ['add', 'subtract']
    inputs = [(1, 2), (3, 5)]
    tasks = []
    for input in inputs:
        for task_name in task_names:
            result = client.send_task(task_name, args=input, queue=f'{task_name}_queue')
            tasks.append(wait_for_result(result.id))
    await asyncio.gather(*tasks)

asyncio.run(run_tasks())