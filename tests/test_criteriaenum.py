import unittest
from ganabosques_orm.enums.criteriaenum import CriteriaEnum

class TestCriteriaEnum(unittest.TestCase):

    def test_enum_values(self):
        values = [e.value for e in CriteriaEnum]
        self.assertTrue(len(values) > 0)