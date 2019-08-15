import os
if os.environ.get('HBNB_TYPE_STORAGE') == os.environ.get('HBNB_MYSQL_DB=hbnb_dev_db'):
    from models.engine.db_storage import DBstorage
    storage = DBStorage()
    storage = storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage = storage.reload()
