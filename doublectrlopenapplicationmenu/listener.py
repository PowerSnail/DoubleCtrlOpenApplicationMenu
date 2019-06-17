import enum
import subprocess
import sys
import threading
import time

import keyboard


class DoubleCtrlCallback:
    def __init__(self, interval=0.3):
        self.last_pressed_time = None
        self.interval = interval
        self.lock = threading.Lock()

    def __call__(self, event: keyboard.KeyboardEvent):
        self.lock.acquire()
        if (
            self.last_pressed_time is None
            or event.time - self.last_pressed_time > self.interval
        ):
            self.last_pressed_time = event.time
            self.lock.release()
        else:
            self.last_pressed_time = None
            print("ok", flush=True)
            print("ok", flush=True, file=sys.stderr)
            self.lock.release()


def main():
    callback = DoubleCtrlCallback()
    keyboard.on_release_key("ctrl", callback)
    keyboard.wait()
