import unittest
from ganabosques_orm.enums.deforestationtype import DeforestationType

class TestDeforestationType(unittest.TestCase):

    def test_enum_values(self):
        values = [e.value for e in DeforestationType]
        self.assertTrue(len(values) > 0)