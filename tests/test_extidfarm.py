import unittest
from ganabosques_orm.auxiliaries.extidfarm import ExtIdFarm

class TestExtIdFarm(unittest.TestCase):

    def test_create_ext_id_farm(self):
        instance = ExtIdFarm()
        self.assertIsInstance(instance, ExtIdFarm)