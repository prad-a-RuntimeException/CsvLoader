"""
 Entry point of method, that takes both the data definition, actual data to insert, type of
 data connection(sql dialect) and actual connection.
"""

import logging
from data_source import default_engine
from sql_schema_utils import create_table
from csv_reader import read_file

stopwords = set([',', "-", "_"])


def get_table_from_file(filename):
    def remove_stop_words(filename):
        return ''.join([c for c in filename.lower() if c not in stopwords])

    def remove_extension(processed_file_name):
        return processed_file_name[:processed_file_name.find('.')]

    return remove_extension(remove_stop_words(filename))


def import_table(data_definition_file, data_file, engine=default_engine, table_name=None):
    '''
    Uses data_definition to create table and then import the data from data_file in to table.
    Expects data_file and data_definitions to be csv files, with valid data and no missing

    Raises a RuntimeError if conditions are not met. (Although effort has been made to provide meaningful
    exceptions)
    columns
    :param data_definition_file:  See sample data_definition_files under tests/resources/<valid_data_schema.txt>
    :param data_file: CSV file with data columns matching the data_definition_file and in order
    :param engine: SqlEngine to be used to import the data. eg:  MySql, SqlLite
    :param table_name: Table name to be created and imported. If None, will try to inference from the file name
    :return: Will throw Error otherwise (not false, since it's not expected to be a
     recoverable condition)
    '''
    logging.info("Import using engine %s", engine)
    logging.info("Importing table %s  with data_definition_file %s and data_file %s", table_name, data_definition_file,
                 data_file)
    table_name = table_name if table_name is not None else get_table_from_file(table_name)
    table = create_table(table_name, data_definition_file, engine=engine)
    column_names = [column.name for column in table.columns]
    conn = engine.connect()
    trans = conn.begin()
    try:
        for content in read_file(data_file, "^"):
            param = {key: value.strip().replace("~", "") for (key, value) in zip(column_names, content)}
            try:
                conn.execute(table.insert(), param)
            except Exception as e:
                logging.exception(e)
    except Exception as e:
        logging.exception("Failed importing table", e)
    finally:
        trans.commit()
        trans.close()


if __name__ == '__main__':
    table_name = get_table_from_file("product_File-Simelsd.txt")
    print(table_name)
