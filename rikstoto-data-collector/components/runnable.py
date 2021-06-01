from typing import Callable
from abc import ABC, abstractmethod

class RunnableInterface(ABC):
    @abstractmethod
    def run(self):
        raise NotImplementedError

class Runnable(RunnableInterface):
    def __init__(self, function: Callable, *args, **kwargs):
        self.callback = function

    def run(self):
        self.callback()
