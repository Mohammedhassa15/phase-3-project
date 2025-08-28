from lib.db.base import engine
from sqlalchemy import inspect

inspector = inspect(engine)
print(inspector.get_table_names())
