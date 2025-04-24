import unittest
from ganabosques_orm.enums.deforestationsource import DeforestationSource

class TestDeforestationSource(unittest.TestCase):

    def test_enum_values(self):
        values = [e.value for e in DeforestationSource]
        self.assertTrue(len(values) > 0)