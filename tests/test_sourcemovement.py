import unittest
from ganabosques_orm.auxiliaries.sourcemovement import SourceMovement

class TestSourceMovement(unittest.TestCase):

    def test_create_source_movement(self):
        instance = SourceMovement()
        self.assertIsInstance(instance, SourceMovement)