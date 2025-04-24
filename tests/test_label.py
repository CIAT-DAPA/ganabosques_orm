import unittest
from ganabosques_orm.enums.label import Label

class TestLabel(unittest.TestCase):

    def test_enum_values(self):
        values = [e.value for e in Label]
        self.assertTrue(len(values) > 0)