import unittest
from mongoengine import connect, disconnect
from ganabosques_orm.collections.analysis import Analysis
import mongomock

class TestAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #connect('mongoenginetest', host='mongomock://localhost')
        connect(db='mongoenginetest',host='mongodb://localhost',mongo_client_class=mongomock.MongoClient)

    @classmethod
    def tearDownClass(cls):
        disconnect()

    # Test that an instance of the model can be created and is of correct type
    def test_create_instance(self):
        instance = Analysis()
        self.assertIsInstance(instance, Analysis)