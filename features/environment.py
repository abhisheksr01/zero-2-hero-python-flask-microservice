import subprocess
import time

import os

TEST_TYPE = os.getenv("TEST_TYPE", "bdd")


def before_scenario(context, scenario):
    if f"{TEST_TYPE}" == "bdd":
        proc = subprocess.Popen(["make", "start"])
        time.sleep(4)
        context.proc = proc
        context.root_url = "http://localhost:5000"
    else:
        context.root_url = os.getenv("ROOT_ENDPOINT")


def after_scenario(context, scenario):
    if f"{TEST_TYPE}" == "bdd":
        proc = context.proc
        proc.terminate()
