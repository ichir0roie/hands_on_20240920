from module.db import *

# https://docs.sqlalchemy.org/en/13/core/metadata.html#creating-and-dropping-database-tables


metadata.create_all(engine)
