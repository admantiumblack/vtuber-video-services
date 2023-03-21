from pydantic import BaseSettings
from functools import lru_cache

class DBSettings(BaseSettings):
    db_host: str = '127.0.0.1'
    db_port: int = 3306
    db_provider: str = 'mysql+mysqldb'
    db_name: str = ''
    db_user: str = None
    db_pass: str = None
    db_url: str = f'{db_provider}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

@lru_cache
def get_db_settings():
    return DBSettings()