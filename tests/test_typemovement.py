import unittest
from ganabosques_orm.enums.typemovement import TypeMovement

class TestTypeMovement(unittest.TestCase):

    def test_enum_values(self):
        values = [e.value for e in TypeMovement]
        self.assertTrue(len(values) > 0)