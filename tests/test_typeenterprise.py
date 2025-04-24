import unittest
from ganabosques_orm.enums.typeenterprise import TypeEnterprise

class TestTypeEnterprise(unittest.TestCase):

    def test_enum_values(self):
        values = [e.value for e in TypeEnterprise]
        self.assertTrue(len(values) > 0)