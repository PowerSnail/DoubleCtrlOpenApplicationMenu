import atexit
import enum
import pathlib
import subprocess
import sys
import threading
import time

import keyboard

DEFAULT_LAUNCHER_COMMAND = "ulauncher-toggle"
LISTENER_PATH = "sudo ./.venv/bin/double-ctrl-listener"


def main():
    p1 = subprocess.Popen(
        [LISTENER_PATH], stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True
    )

    def exit_handler():
        print("My application is ending!")
        p1.kill()

    atexit.register(exit_handler)

    while True:
        line = p1.stdout.readline()
        subprocess.run(DEFAULT_LAUNCHER_COMMAND, shell=True)
        time.sleep(1)
