from Server.Config.base_config import ApiSettings
from functools import lru_cache

class YoutubeSettings(ApiSettings):
    
    class Config:
        env_prefix = 'youtube_'
    
@lru_cache
def get_youtube_settings():
    return YoutubeSettings()