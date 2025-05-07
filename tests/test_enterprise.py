import unittest
from mongoengine import connect, disconnect
from ganabosques_orm.collections.enterprise import Enterprise
import mongomock
from ganabosques_orm.tools.exceptiondata import ExceptionData

class TestEnterprise(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #connect('mongoenginetest', host='mongomock://localhost')
        connect(db='mongoenginetest',host='mongodb://localhost',mongo_client_class=mongomock.MongoClient)

    @classmethod
    def tearDownClass(cls):
        disconnect()

    # Test that an instance of the model can be created and is of correct type
    def test_create_instance(self):
        instance = Enterprise()
        self.assertIsInstance(instance, Enterprise)
    
    def test_name_validate(self):
        enterprise = Enterprise(name="Mi empresa")
        self.assertTrue(enterprise.validate())

    def test_name_empty(self):
        enterprise = Enterprise(name="")
        with self.assertRaises(ExceptionData) as context:
            enterprise.validate()
        self.assertEqual(str(context.exception), "Name field is mandatory")