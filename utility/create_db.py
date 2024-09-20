from module.db import *

# https://docs.sqlalchemy.org/en/13/core/metadata.html#creating-and-dropping-database-tables
# https://stackoverflow.com/questions/54118182/sqlalchemy-not-creating-tables

metadata = Base.metadata

metadata.create_all(engine)
