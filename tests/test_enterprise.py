import unittest
from mongoengine import connect, disconnect
from ganabosques_orm.collections.enterprise import Enterprise

class TestEnterprise(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls):
        disconnect()

    # Test that an instance of the model can be created and is of correct type
    def test_create_instance(self):
        instance = Enterprise()
        self.assertIsInstance(instance, Enterprise)