import unittest
from data.schedulable import Schedulable
from datetime import date

class TestSchedulable(unittest.TestCase):
    def setUp(self):
        self.start_time = "2021-05-30T13:00:00"
        self.schedulable = Schedulable(self.start_time)

    def test_is_today_when_false(self):
        self.assertFalse(self.schedulable.is_today)

    def test_is_today_when_true(self):
        today = date.today()
        today_start_time = f"{today.year}-{today.month}-{today.day}T12:00:00"
        today_schedulable = Schedulable(today_start_time)

        self.assertTrue(today_schedulable.is_today)