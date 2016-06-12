from sqlalchemy import Table
from data_source import metadata
from data_types import get_columns_from_definition

"""
 Bunch of function used to create tables, manage relationships and handle data insert
"""


def create_table(table_name, data_definition_file, engine):
    table = Table(table_name, metadata, *get_columns_from_definition(data_definition_file),
                  extend_existing=True)
    table.create(engine, checkfirst=True)
    return table
