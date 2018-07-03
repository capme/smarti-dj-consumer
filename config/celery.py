from celery import Celery
from config.log import logger
import celery_pubsub
import celery as app


celery = Celery(
    'smarti-consumer',
    backend='redis://172.17.0.1:6379/1',
    broker='redis://172.17.0.1:6379/1'
)


@app.task(
    name="pub_sub_add"
)
def add(*args, **kwargs):
    logger.info("[consumer 2] {}".format(args[0]))
    return args[0]


@app.task(
    name="pub_sub_main"
)
def main_publisher_distributed():
    for x in range(0, 100000):
        # res = celery_pubsub.publish('some.topic', x)
        res = add.delay(x)
        logger.info("[publisher 2] {}".format(x))
        # not working
        # res = celery_pubsub.publish('some.topic', x)
        # logger.info("[publisher] {}".format(res))

# celery_pubsub.subscribe('some.topic', add)
