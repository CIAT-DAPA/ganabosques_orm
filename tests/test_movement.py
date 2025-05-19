import unittest
from mongoengine import connect, disconnect
from ganabosques_orm.collections.movement import Movement
import mongomock
from datetime import datetime
from ganabosques_orm.enums.typemovement import TypeMovement
from ganabosques_orm.tools.exceptiondata import ExceptionData

class TestMovement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #connect('mongoenginetest', host='mongomock://localhost')
        connect(db='mongoenginetest',host='mongodb://localhost',mongo_client_class=mongomock.MongoClient)

    @classmethod
    def tearDownClass(cls):
        disconnect()

    # Test that an instance of the model can be created and is of correct type
    def test_create_instance(self):
        instance = Movement()
        self.assertIsInstance(instance, Movement)
    
    def test_valid_movement(self):
        # Verifica que una instancia válida pasa la validación
        movement = Movement(
            date=datetime.utcnow(),
            type_origin=TypeMovement.FARM,
            type_destination=TypeMovement.ENTERPRISE
        )
        self.assertTrue(movement.validate())

    def test_missing_date(self):
        # Verifica que se lanza excepción si falta la fecha
        movement = Movement(
            type_origin=TypeMovement.FARM,
            type_destination=TypeMovement.ENTERPRISE
        )
        with self.assertRaises(ExceptionData) as context:
            movement.validate()
        self.assertEqual(str(context.exception), "Date field is mandatory")

    def test_missing_type_origin(self):
        # Verifica que se lanza excepción si falta el origen
        movement = Movement(
            date=datetime.utcnow(),
            type_destination=TypeMovement.ENTERPRISE
        )
        with self.assertRaises(ExceptionData) as context:
            movement.validate()
        self.assertEqual(str(context.exception), "Type origin field is mandatory")

    def test_missing_type_destination(self):
        # Verifica que se lanza excepción si falta el destino
        movement = Movement(
            date=datetime.utcnow(),
            type_origin=TypeMovement.FARM
        )
        with self.assertRaises(ExceptionData) as context:
            movement.validate()
        self.assertEqual(str(context.exception), "Type destination field is mandatory")
