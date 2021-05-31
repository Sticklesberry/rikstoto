from typing import Dict, Any, List

from racedays.race import Race
from racedays.schedulable import Schedulable

class SchedulableRace(Schedulable, Race):
    """
    A race schedule representation is a triple that contains the following data:
    race start time, unique race key and race number.
    
    The unique race key and race number in combination are unique and represents
    one exact race. The race start time is included so one can schedule when to
    fetch info about the race.

    A RaceSchedule object has quite a few implicit information, such as url to
    win odds endpoint.
    """
    def __init__(self, raceday_key: str, race_number: int, start_time: str, *args: List[Any], **kwargs: Dict[Any, Any]):
        #self.start_time = convert_timestamp_to_datetime(start_time)
        #self.raceday_key: str = raceday_key
        #self.race_number = race_number
        super().__init__(
            start_time=start_time,
            raceday_key=raceday_key,
            race_number=race_number,
            *args,
            **kwargs,
        )


    def to_json(self) -> Dict[str, Any]:
        return {
            "start_time":  super().start_time,
            "raceday_key": super().raceday_key,
            "race_number": super().race_number,
        }

