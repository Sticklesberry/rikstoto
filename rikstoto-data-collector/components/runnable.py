from typing import Callable

class Runnable:
    def __init__(self, function: Callable, *args, **kwargs):
        self.callback = function

    def run(self):
        self.callback()
