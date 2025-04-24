import unittest
from mongoengine import connect, disconnect
from ganabosques_orm.collections.adm3risk import Adm3Risk
import mongomock

class TestAdm3Risk(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #connect('mongoenginetest', host='mongomock://localhost')
        connect(db='mongoenginetest',host='mongodb://localhost',mongo_client_class=mongomock.MongoClient)

    @classmethod
    def tearDownClass(cls):
        disconnect()

    # Test that an instance of the model can be created and is of correct type
    def test_create_instance(self):
        instance = Adm3Risk()
        self.assertIsInstance(instance, Adm3Risk)