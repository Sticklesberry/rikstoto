from datetime import datetime
from api.utils import convert_timestamp_to_datetime
from typing import Any
from abc import ABC, abstractproperty
from datetime import date

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

    def is_same_date_as(self, date: date) -> bool:
        return self.start_time.date() == date

    def __str__(self):
        date, time = self.start_time.__str__().split(" ")
        return f"{date}T{time}"

    # why make it simple when you can make it hard? (same as self.rikstoto_time_string)
    def __repr__(self):
        date, time = self.start_time.__str__().split(" ")
        return f"{date}T{time}"

    @property
    def is_today(self) -> bool:
        return self.is_same_date_as(date.today())

    @property
    def toString(self) -> str:
        return self.rikstoto_time_string
