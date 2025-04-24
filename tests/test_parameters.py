import unittest
from ganabosques_orm.auxiliaries.parameters import Parameters

class TestParameters(unittest.TestCase):

    def test_create_parameters(self):
        instance = Parameters()
        self.assertIsInstance(instance, Parameters)