import unittest
from mongoengine import connect, disconnect
from ganabosques_orm.collections.adm1 import Adm1

class TestAdm1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls):
        disconnect()

    # Test that an instance of the model can be created and is of correct type
    def test_create_instance(self):
        instance = Adm1()
        self.assertIsInstance(instance, Adm1)