import unittest
from ganabosques_orm.auxiliaries.extidenterprise import ExtIdEnterprise

class TestExtIdEnterprise(unittest.TestCase):

    def test_create_ext_id_enterprise(self):
        instance = ExtIdEnterprise()
        self.assertIsInstance(instance, ExtIdEnterprise)