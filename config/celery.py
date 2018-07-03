from celery import Celery
from config.log import logger
import celery_pubsub
import celery as main_celery


celery = Celery(
    'smarti-consumer',
    backend='redis://172.17.0.1:6379/1',
    broker='redis://172.17.0.1:6379/1'
)


@main_celery.task
def add(*args, **kwargs):
    logger.info("[consumer] {}".format(args[0]))
    return args[0]


celery_pubsub.subscribe('some.topic', add)
