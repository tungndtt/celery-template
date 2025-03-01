# Celery Template

### Overview

Celery is a Python library which offloads time-consuming and CPU-intensive tasks from your Python application so it can stay fast and responsive. The related documentation can be found [here](https://docs.celeryq.dev/en/latest/userguide/workers.html).

### Setup

The steup can be decoupled into 2 main components:

-   **worker**: Leverage multiple processors to handle the distributed task from queues
-   **client**: Your Python application which offloads heavy tasks and asynchronously waits for results

Here is the template for [worker](./worker/) and [client](./client/).

**Note**: We uses [Redis](https://redis.io/) for message broker and result backend.

### Example

There is already an example to illustrate how-to-apply-template, which can be in [example](./examples/)

#### Local Run (Worker)

-   To run the worker locally, make sure Redis instance up-to-run on your machine. The current template works on **Redis 20+**
-   Install related dependencies `pip install -r requirements.txt`
-   Start the worker `celery -A worker worker --loglevel=info -P gevent`

#### Docker (Worker)

Instead of manual setup, you can use [docker]() to start the worker

-   Build the worker image `docker compose up --build`
-   Start the worker container `docker compose up`

#### Run (Client)

Run the client `python client.py`
