import os
if os.environ.get("HBNB_TYPE_STORAGE") == HBNB_MYSQL_DB=hbnb_dev_db:
    import DBStorage
    storage = DBStorage()
    storage = storage.reload()
else:
    import FileStorage
    storage = FileStorage
    storage = storage.reload()
