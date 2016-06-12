from unittest import TestCase

from sqlalchemy import Table
from sqlalchemy.exc import NoSuchTableError

from data_source import default_engine, metadata
from import_data import import_table


class TestImportTable(TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            food_description_tb = Table('Food_Description', metadata, autoload=True, autoload_with=default_engine,
                                        extend_existing=True)
            metadata.bind = default_engine
            food_description_tb.drop(metadata.bind)
        except NoSuchTableError as e:
            pass

    def test_import_table(self):
        import_table('./resources/test_schema_to_import.txt',
                     './resources/test_data_to_import.txt',
                     default_engine,
                     table_name='Food_Description')

        food_description_tb = Table('food_description', metadata, autoload=True, autoload_with=default_engine)
        select = food_description_tb.select().where(food_description_tb.c.NDB_No == '01001')
        test_record = default_engine.connect().execute(select).fetchone()
        self.assertEqual(test_record.FdGrp_Cd, '0100')
        self.assertEqual(test_record.Long_Desc, 'Butter, salted')
        self.assertEqual(test_record.Survey, 1)
