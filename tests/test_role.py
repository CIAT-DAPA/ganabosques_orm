import unittest

import mongomock
from mongoengine import connect, disconnect, ValidationError

from ganabosques_orm.collections.role import Role
from ganabosques_orm.enums.actions import Actions
from ganabosques_orm.enums.options import Options


class TestRole(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect(
            db='mongoenginetest',
            host='mongodb://localhost',
            mongo_client_class=mongomock.MongoClient
        )

    @classmethod
    def tearDownClass(cls):
        disconnect()

    def tearDown(self):
        Role.drop_collection()

    def _get_action(self):
        return list(Actions)[0]

    def _get_second_action(self):
        actions = list(Actions)
        return actions[1] if len(actions) > 1 else actions[0]

    def _get_option(self):
        return list(Options)[0]

    def _get_second_option(self):
        options = list(Options)
        return options[1] if len(options) > 1 else options[0]

    def test_create_instance(self):
        instance = Role()
        self.assertIsInstance(instance, Role)

    def test_collection_name_is_role(self):
        self.assertEqual(Role._get_collection_name(), 'role')

    def test_create_instance_with_valid_data(self):
        instance = Role(
            name='Administrador',
            actions=[self._get_action()],
            options=[self._get_option()]
        )

        self.assertEqual(instance.name, 'Administrador')
        self.assertEqual(instance.actions, [self._get_action()])
        self.assertEqual(instance.options, [self._get_option()])

    def test_save_instance_with_valid_data(self):
        instance = Role(
            name='Supervisor',
            actions=[self._get_action()],
            options=[self._get_option()]
        )
        instance.save()

        saved = Role.objects(id=instance.id).first()

        self.assertIsNotNone(saved)
        self.assertEqual(saved.name, 'Supervisor')
        self.assertEqual(saved.actions, [self._get_action()])
        self.assertEqual(saved.options, [self._get_option()])

    def test_save_instance_with_multiple_actions_and_options(self):
        instance = Role(
            name='Operador',
            actions=[self._get_action(), self._get_second_action()],
            options=[self._get_option(), self._get_second_option()]
        )
        instance.save()

        saved = Role.objects(id=instance.id).first()

        self.assertIsNotNone(saved)
        self.assertEqual(len(saved.actions), 2)
        self.assertEqual(len(saved.options), 2)
        self.assertEqual(saved.actions[0], self._get_action())
        self.assertEqual(saved.actions[1], self._get_second_action())
        self.assertEqual(saved.options[0], self._get_option())
        self.assertEqual(saved.options[1], self._get_second_option())

    def test_save_instance_with_empty_fields(self):
        instance = Role()
        instance.save()

        saved = Role.objects(id=instance.id).first()

        self.assertIsNotNone(saved)
        self.assertIsNone(saved.name)
        self.assertEqual(saved.actions, [])
        self.assertEqual(saved.options, [])

    def test_save_instance_with_empty_actions_and_options_lists(self):
        instance = Role(
            name='Consulta',
            actions=[],
            options=[]
        )
        instance.save()

        saved = Role.objects(id=instance.id).first()

        self.assertIsNotNone(saved)
        self.assertEqual(saved.name, 'Consulta')
        self.assertEqual(saved.actions, [])
        self.assertEqual(saved.options, [])

    def test_validate_invalid_action_value_raises_validation_error(self):
        instance = Role(actions=['invalid_action'])

        with self.assertRaises(ValidationError):
            instance.validate()

    def test_validate_invalid_option_value_raises_validation_error(self):
        instance = Role(options=['invalid_option'])

        with self.assertRaises(ValidationError):
            instance.validate()

    def test_update_persisted_instance(self):
        instance = Role(
            name='Rol Base',
            actions=[self._get_action()],
            options=[self._get_option()]
        )
        instance.save()

        instance.name = 'Rol Actualizado'
        instance.actions = [self._get_action(), self._get_second_action()]
        instance.options = [self._get_option(), self._get_second_option()]
        instance.save()

        updated = Role.objects(id=instance.id).first()

        self.assertIsNotNone(updated)
        self.assertEqual(updated.name, 'Rol Actualizado')
        self.assertEqual(len(updated.actions), 2)
        self.assertEqual(len(updated.options), 2)
        self.assertEqual(updated.actions[0], self._get_action())
        self.assertEqual(updated.actions[1], self._get_second_action())
        self.assertEqual(updated.options[0], self._get_option())
        self.assertEqual(updated.options[1], self._get_second_option())

    def test_delete_instance(self):
        instance = Role(
            name='Rol a Eliminar',
            actions=[self._get_action()],
            options=[self._get_option()]
        )
        instance.save()
        instance_id = instance.id

        instance.delete()

        deleted = Role.objects(id=instance_id).first()
        self.assertIsNone(deleted)


if __name__ == '__main__':
    unittest.main()