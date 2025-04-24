import unittest
from mongoengine import connect, disconnect
from ganabosques_orm.collections.suppliers import Suppliers

class TestSuppliers(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls):
        disconnect()

    # Test that an instance of the model can be created and is of correct type
    def test_create_instance(self):
        instance = Suppliers()
        self.assertIsInstance(instance, Suppliers)