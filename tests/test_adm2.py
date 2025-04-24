import unittest
from mongoengine import connect, disconnect
from ganabosques_orm.collections.adm2 import Adm2

class TestAdm2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls):
        disconnect()

    # Test that an instance of the model can be created and is of correct type
    def test_create_instance(self):
        instance = Adm2()
        self.assertIsInstance(instance, Adm2)