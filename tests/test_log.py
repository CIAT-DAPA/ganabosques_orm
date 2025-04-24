import unittest
from ganabosques_orm.auxiliaries.log import Log

class TestLog(unittest.TestCase):

    def test_create_log(self):
        instance = Log()
        self.assertIsInstance(instance, Log)