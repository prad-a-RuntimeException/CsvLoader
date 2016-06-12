from import_data import import_table
import os


class SchemaDef:
    def __init__(self, schema_file, table_name):
        self.schema_file = schema_file
        self.table_name = table_name
        super().__init__()


schema_data_map = {"FD_GROUP.txt": SchemaDef("food_group_description_schema.txt", "Food_Group_Description"),
                   "FOOD_DES.txt": SchemaDef("food_description_schema.txt", "Food_Description"),
                   "LANGDESC.txt": SchemaDef("langual_description_schema.txt", "Langual"),
                   "LANGUAL.txt": SchemaDef("langual_schema.txt", "Langual_Mapping")}

data_file_root = 'usda/data-files/'
schema_file_root = 'usda/database-schema/'


def run():
    data_files = os.listdir("usda/data-files")
    valid_files = [f for f in data_files if f in schema_data_map]
    for file in valid_files:
        schema_def = schema_data_map.get(file)
        import_table(schema_file_root + schema_def.schema_file, data_file_root + file, table_name=schema_def.table_name)


if __name__ == '__main__':
    run()
