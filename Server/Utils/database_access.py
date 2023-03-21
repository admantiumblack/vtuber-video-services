from Server.Config import get_db_settings
from sqlalchemy import create_engine, MetaData

class DBConfig():
    
    def __init__(self, url):
        self.metadata = MetaData()
        self.engine = create_engine(url)
        self.connection = self.engine.connect()
    
    def get_connection(self):
        return self.connection

@lru_cache
def get_db_connection(db_url:str=None):
    if db_url is None:
        settings = get_db_settings()
        db_url = settings.db_url
        
    return DBConfig(db_url)