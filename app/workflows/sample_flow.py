from prefect import flow, task
import time
import logging

@task
def step_one():
    logging.info("Step one started")
    time.sleep(2)
    return 1

@task
def step_two(x):
    logging.info("Step two started")
    time.sleep(2)
    return x + 1

@flow(name="sample-flow")
def sample_flow():
    x = step_one()
    y = step_two(x)
    logging.info(f"Flow result: {y}")
