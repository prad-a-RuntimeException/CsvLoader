import os
from sqlalchemy import create_engine
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def get_path(file_name):
    return os.path.join(BASE_DIR, file_name)

def get_sqllite_engine_for_testing():
    return create_engine('sqlite+pysqlite:///test.db')


