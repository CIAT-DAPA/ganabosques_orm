import unittest
from ganabosques_orm.auxiliaries.attributes import Attributes

class TestAttributes(unittest.TestCase):

    def test_create_attributes(self):
        instance = Attributes()
        self.assertIsInstance(instance, Attributes)