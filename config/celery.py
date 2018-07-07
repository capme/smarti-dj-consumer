from celery import Celery
from config.log import logger
import celery as app
from celery.result import allow_join_result
import random

celery = Celery(
    'smarti-consumer',
    backend='redis://172.17.0.1:6379/1',
    broker='redis://172.17.0.1:6379/1'
)


@app.task(
    name="pub_sub_add_main",
    trail=True
)
def add(*args, **kwargs):
    n_data = []
    for n in range(10):
        n_data.append(random.randint(1, 101))

    logger.info("Loop ke : {}. {}".format(args[0], n_data))
    return n_data


@app.task(
    name="pub_sub_main",
    trail=True
)
def main_publisher_distributed():
    n_data = []
    for x in range(0, 100000):
        res = add.delay(x)
        with allow_join_result():
            n_data.append(res.get())

    logger.info("Result data : {} ".format(n_data))
