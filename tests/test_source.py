import unittest
from ganabosques_orm.enums.source import Source

class TestSource(unittest.TestCase):

    def test_enum_values(self):
        values = [e.value for e in Source]
        self.assertTrue(len(values) > 0)