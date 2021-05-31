from datetime import datetime
from constants.rikstoto_api_constants import timestamp_format
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
        self.start_time: datetime = datetime.strptime(start_time, timestamp_format)

    @property
    def is_today(self) -> bool:
        return self.start_time.date() == self.start_time.today().date()
