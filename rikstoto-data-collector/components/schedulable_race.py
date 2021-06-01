from typing import Dict, Any, List
from components.race import Race
from components.schedulable import Schedulable

class SchedulableRace(Race, Schedulable):
    """
    A race schedule representation is a triple that contains the following data:
    race start time, unique race key and race number.
    
    The unique race key and race number in combination are unique and represents
    one exact race. The race start time is included so one can schedule when to
    fetch info about the race.

    A RaceSchedule object has quite a few implicit information, such as url to
    win odds endpoint.
    """
    def __init__(self, start_time: str, raceday_key: str, race_number: int, *args: List[Any], **kwargs: Dict[Any, Any]):
        Race.__init__(self, raceday_key, race_number, *args, **kwargs)
        Schedulable.__init__(self, start_time, *args, **kwargs)

    def __str__(self) -> str:
        return f"({self.raceday_key}, {self.race_number}, {self.start_time})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_json(self) -> Dict[str, Any]:
        return {
            "start_time":  self.start_time,
            "raceday_key": self.raceday_key,
            "race_number": self.race_number,
        }

