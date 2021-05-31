import unittest
from racedays.schedulable import Schedulable

class TestSchedulable(unittest.TestCase):
    def setUp(self):
        self.start_time = "2021-05-30T13:00:00"
        self.schedulable = Schedulable(self.start_time)

    def test_is_today(self):
        self.assertFalse(self.schedulable.is_today)