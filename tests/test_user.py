import unittest
from mongoengine import connect, disconnect
from ganabosques_orm.collections.user import User

class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls):
        disconnect()

    # Test that an instance of the model can be created and is of correct type
    def test_create_instance(self):
        instance = User()
        self.assertIsInstance(instance, User)