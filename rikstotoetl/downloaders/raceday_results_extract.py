from rikstotoetl.api.rikstoto_api import RikstotoAPI
from datetime import date
from dateutil.relativedelta import relativedelta
from time import sleep
import json
from typing import List

class RacedayDownloader:
    """
    Class for downloading racedays and store them in a file.
    
    Example use:
    from rikstotoetl.downloaders.raceday_results_extract import RacedayDownloader

    start_date = date(year=2016, month=1, day=1)
    end_date = date(year=2016, month=1, day=17)
    interval = 7
    output_file = 'racedays.json'

    downloader = RacedayDownloader(start_date, end_date, output_file, interval)
    downloader.download_and_write_to_file()
    """
    def __init__(self, start: date, end: date, output_filename: str, interval: int=7, sleep_time: float=0.5):
        self.start: date = start
        self.end: date = end
        self.output_filename: str = output_filename
        self.interval: int = interval
        self.result_list: List = []
        self.sleep_time: float = sleep_time

    def download_and_write_to_file(self):
        """
        Downloads raceday JSONs and stores them in a file
        """
        self.download_from_source()

        self.write_result_to_file()


    def download_from_source(self):
        """
        Downloads raceday JSONs 
        """
        while self.start <= self.end:
            self.result_list += RikstotoAPI.get_racedays(
                start = self.start,
                end   = min(self.start + relativedelta(days=self.interval - 1), self.end)
            )

            self.pause()

            self.start += relativedelta(days=self.interval)

        return self.result_list

    def write_result_to_file(self):
        """
        Writes whatever is in the result_list to a file
        """
        with open(self.output_filename, 'w') as output_file:
            json.dump(self.result_list, output_file, ensure_ascii=False)

    def pause(self):
        sleep(self.sleep_time)


