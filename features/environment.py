import subprocess
import time


def before_scenario(context, scenario):
    proc = subprocess.Popen(["make", "start"])
    time.sleep(4)
    context.proc = proc


def after_scenario(context, scenario):
    proc = context.proc
    proc.terminate()
