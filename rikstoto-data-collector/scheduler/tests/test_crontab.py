import unittest
from crontab import CronTab

class TestCrontab(unittest.TestCase):
    def test_instantiate_crontab(self):
        c = None

        try:
            c = CronTab()
        except:
            pass

        self.assertIsNotNone(c)
