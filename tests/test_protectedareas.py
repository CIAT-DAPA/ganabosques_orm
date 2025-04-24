import unittest
from mongoengine import connect, disconnect
from ganabosques_orm.collections.protectedareas import ProtectedAreas
import mongomock

class TestProtectedAreas(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #connect('mongoenginetest', host='mongomock://localhost')
        connect(db='mongoenginetest',host='mongodb://localhost',mongo_client_class=mongomock.MongoClient)

    @classmethod
    def tearDownClass(cls):
        disconnect()

    # Test that an instance of the model can be created and is of correct type
    def test_create_instance(self):
        instance = ProtectedAreas()
        self.assertIsInstance(instance, ProtectedAreas)