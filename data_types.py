"""
    Functions to convert text based schema metadata to RDBMS column information.
    The main methods are  is getColumnsFromDefinition, please look at sample
    definition files and the unit tests for valid and invalid formats.
"""
from sqlalchemy import Column, String
from mysql_custom_datatypes.custom_datatypes import CustomBoolean, CustomDecimal

column_dict = {'String': String, 'Float': CustomDecimal, 'Boolean': CustomBoolean}


def get_columns_from_definition(data_definition_file):
    with open(data_definition_file) as def_file:
        return [__get_column(line) for line in def_file]


def __get_column(column_str):
    name_with_type = column_str.split(",")
    return Column(name_with_type[0], __get_column_type(name_with_type[1]))


def __get_column_type(column_type_str):
    def __check_type(t):
        if t not in column_dict:
            raise ValueError("{} is not a valid value ctype".format(t))
        return True

    type_with_size = column_type_str.split("(")
    ctype = type_with_size[0].strip()
    __check_type(ctype)
    column = column_dict.get(ctype)(int(type_with_size[1].strip()[:-1])) \
        if len(type_with_size) > 1 else column_dict.get(ctype)
    return column
