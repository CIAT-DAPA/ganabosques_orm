import unittest
from ganabosques_orm.auxiliaries.classification import Classification

class TestClassification(unittest.TestCase):

    def test_create_classification(self):
        instance = Classification()
        self.assertIsInstance(instance, Classification)