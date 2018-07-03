from celery import Celery


celery = Celery(
    'smarti-consumer',
    backend='redis://redis:6379/1',
    broker='redis://redis:6379/1'
)


@celery.task
def add(x, y):
    return x + y
