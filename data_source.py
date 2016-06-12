from sqlalchemy import MetaData
from sqlalchemy import create_engine

default_engine = create_engine('mysql://root@localhost/usda')

metadata = MetaData()

def get_default_engine():
    return default_engine

def get_metadata():
    return metadata
