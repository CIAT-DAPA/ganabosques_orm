import unittest
from ganabosques_orm.auxiliaries.criteria import Criteria

class TestCriteria(unittest.TestCase):

    def test_create_criteria(self):
        instance = Criteria()
        self.assertIsInstance(instance, Criteria)