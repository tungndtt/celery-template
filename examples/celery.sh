#!/usr/bin/env bash

mkdir -p /var/run/celery /var/log/celery
chown -R nobody:nogroup /var/run/celery /var/log/celery

exec celery -A worker worker -P gevent --loglevel=info --uid=nobody --gid=nogroup