import unittest
from ganabosques_orm.enums.farmsource import FarmSource

class TestFarmSource(unittest.TestCase):

    def test_enum_values(self):
        values = [e.value for e in FarmSource]
        self.assertTrue(len(values) > 0)