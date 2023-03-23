from pydantic import BaseSettings
from functools import lru_cache

class YoutubeSettings(BaseSettings):
    youtube_host: str = 'youtube.com'
    youtube_secret_key: str = ''
    
@lru_cache
def get_youtube_settings():
    return YoutubeSettings()