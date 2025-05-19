import unittest
from mongoengine import connect, disconnect
from ganabosques_orm.collections.enterprise import Enterprise
import mongomock
from ganabosques_orm.enums.typeenterprise import TypeEnterprise
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
    
    # Test para validar nombre correcto (con type_enterprise válido)
    def test_name_validate(self):
        enterprise = Enterprise(name="Mi empresa", type_enterprise=TypeEnterprise.ENTERPRISE)
        self.assertTrue(enterprise.validate())

    # Test para nombre vacío (con type_enterprise válido)
    def test_name_empty(self):
        enterprise = Enterprise(name="", type_enterprise=TypeEnterprise.ENTERPRISE)
        with self.assertRaises(ExceptionData) as context:
            enterprise.validate()
        self.assertEqual(str(context.exception), "Name field is mandatory")

    # Test específico para type_enterprise válido (con nombre válido)
    def test_type_enterprise_validate(self):
        enterprise = Enterprise(name="Empresa válida", type_enterprise=TypeEnterprise.SLAUGHTERHOUSE)
        self.assertTrue(enterprise.validate())

    # Test específico para type_enterprise vacío (con nombre válido)
    def test_type_enterprise_empty(self):
        enterprise = Enterprise(name="Empresa válida", type_enterprise=None)
        with self.assertRaises(ExceptionData) as context:
            enterprise.validate()
        self.assertEqual(str(context.exception), "Type Enterprise field is mandatory")
