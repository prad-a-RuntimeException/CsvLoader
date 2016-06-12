from unittest import TestCase
from data_types import __get_column_type as getColumnType, __get_column as getColumn, get_columns_from_definition
from tests.test_utils import get_path


class TestDataLoader(TestCase):
    def test_get_column_from_type(self):
        str = "String(100)"
        column_type = getColumnType(str)
        self.assertEqual(column_type.length, 100)
        self.assertEqual(column_type.python_type.__name__, "str");
        print(column_type)

    def test_get_column_from_type_with_no_size(self):
        str = "String"
        column_type = getColumnType(str)
        self.assertEqual(column_type.__name__, "String")
        print(column_type)

    def test_get_column_from_type_for_number(self):
        str = "Decimal"
        column_type = getColumnType(str)
        self.assertEqual(column_type.__name__, "DECIMAL")
        print(column_type)

    def test_get_column_from_type_for_boolean(self):
        str = "Boolean"
        column_type = getColumnType(str)
        self.assertEqual(column_type.__name__, "CustomBoolean")
        print(column_type)

    def test_get_column_from_str(self):
        str = "Value,String(100)"
        column = getColumn(str)
        self.assertEqual(column.name, 'Value')
        self.assertEqual(column.type.python_type.__name__, 'str')

    def test_get_column_definitions(self):
        '''
            Putting it all together. The Function is a composition of the other two functions.
        :return: List of column definitions.
        '''
        definition = get_columns_from_definition("tests/resources/valid_data_schema.txt")
        self.assertTrue(len(definition), 11)

    def test_get_column_definitions_invalid_type(self):
        '''
            Tests if the exception thrown is useful
        '''
        self.assertRaisesRegex(ValueError, ".*is not a valid.*", get_columns_from_definition,
                               "tests/resources/invalid_data_schema.txt")
