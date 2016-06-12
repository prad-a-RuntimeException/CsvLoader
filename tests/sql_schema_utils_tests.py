from unittest import TestCase
from sql_schema_utils import create_table
from tests.test_utils import get_sqllite_engine_for_testing as get_engine
from data_source import metadata


class TestSqlSchemaUtils(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.table = create_table("Test_Table", "resources/valid_data_schema.txt", get_engine())

    def test_should_create_table(self):
        # Questionable way of creating table (once per execution, breaking the idea of unit)
        # , the runtime gain seems to justify it.
        self.assertIsNotNone(TestSqlSchemaUtils.table)

    @classmethod
    def tearDownClass(cls):
        cls.table.drop(get_engine())
