import unittest
from mongoengine import connect, disconnect
from ganabosques_orm.collections.farm import Farm
import mongomock
from ganabosques_orm.enums.farmsource import FarmSource
from ganabosques_orm.auxiliaries.extidfarm import ExtIdFarm
from ganabosques_orm.enums.source import Source
from ganabosques_orm.collections.adm3 import Adm3
from ganabosques_orm.tools.exceptiondata import ExceptionData

class TestFarm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #connect('mongoenginetest', host='mongomock://localhost')
        connect(db='mongoenginetest',host='mongodb://localhost',mongo_client_class=mongomock.MongoClient)

    @classmethod
    def tearDownClass(cls):
        disconnect()

    # Test that an instance of the model can be created and is of correct type
    def test_create_instance(self):
        instance = Farm()
        self.assertIsInstance(instance, Farm)

    def test_valid_farm(self):
        # Ensure that a fully valid Farm instance passes validation
        adm3 = Adm3(id="ADM3-001")  # simulate a referenced Adm3 document
        ext_id = ExtIdFarm(source=Source.GEOFARMER_ID, ext_code="123")

        farm = Farm(
            adm3_id=adm3,
            farm_source=FarmSource.GEOFARMER,
            ext_id=[ext_id]
        )
        self.assertTrue(farm.validate())

    def test_missing_adm3_id(self):
        # Check that missing adm3_id raises an exception
        ext_id = ExtIdFarm(source=Source.SIT_CODE, ext_code="123")
        farm = Farm(
            farm_source=FarmSource.SAGARI,
            ext_id=[ext_id]
        )
        with self.assertRaises(ExceptionData) as context:
            farm.validate()
        self.assertEqual(str(context.exception), "adm3_id is required")

    def test_missing_farm_source(self):
        # Check that missing farm_source raises an exception
        adm3 = Adm3(id="ADM3-002")
        ext_id = ExtIdFarm(source=Source.PRODUCER_ID, ext_code="456")

        farm = Farm(
            adm3_id=adm3,
            ext_id=[ext_id]
        )
        with self.assertRaises(ExceptionData) as context:
            farm.validate()
        self.assertEqual(str(context.exception), "farm_source is required")

    def test_empty_ext_id(self):
        # Check that an empty ext_id list raises an exception
        adm3 = Adm3(id="ADM3-003")

        farm = Farm(
            adm3_id=adm3,
            farm_source=FarmSource.SINIGAN,
            ext_id=[]
        )
        with self.assertRaises(ExceptionData) as context:
            farm.validate()
        self.assertEqual(str(context.exception), "ext_id must contain at least one entry")
