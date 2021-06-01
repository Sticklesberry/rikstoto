from datetime import datetime
from api.utils import convert_timestamp_to_datetime
from typing import Any
from abc import ABC, abstractproperty

class SchedulableInterface(ABC):
    """
    Something that can be scheduled with crontab
    """
    @abstractproperty
    def is_today(self) -> bool:
        raise NotImplementedError

class Schedulable(SchedulableInterface):
    def __init__(self, start_time: str, *args: Any, **kwargs: Any):
        self.start_time: datetime = convert_timestamp_to_datetime(start_time)
        self.rikstoto_time_string: str = start_time

    @property
    def is_today(self) -> bool:
        return self.start_time.date() == self.start_time.today().date()

    @property
    def toString(self) -> str:
        return self.rikstoto_time_string
