from datetime import date
from typing import List, Dict, Any
from api.raceday.collect_races import (
    find_todays_races,
    find_races_of_date,
)

std_schedule_filename = "race_schedule.txt"

def log_races_of_date_to_schedule(tracks: List[Dict[str, Any]], date: date, filename=std_schedule_filename):
    for race in find_races_of_date(tracks, date):
        race.log_race_to_schedule(filename)


def log_todays_races_to_schedule(tracks: List[Dict[str, Any]], filename=std_schedule_filename):
    log_races_of_date_to_schedule(tracks, date.today())


#from components.runnable import Runnable
#from components.schedulable import Schedulable
#from crontab import CronTab
#from datetime import datetime
#cron = CronTab()
#job = cron.new('echo "kjeldsbekk2!" > kjeldsbekk.txt')
#
#job.setall(datetime(2021, 6, 3, 20, 2, 0))
#job.run()
#
#class Scheduler:
#    """
#    Dette objektet instansieres hver x minutt av crontab og så
#    åpner det en fil med dagens løp, scheduler de som går de neste
#    x+5 min og fjerner dem fra fila
#    """
#    pass