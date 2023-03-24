from Server.Utils.url_utils import build_url
from pydantic import BaseSettings
from functools import lru_cache

class YoutubeSettings(BaseSettings):
    youtube_host: str = 'youtube.com'
    youtube_secret_key: str = ''

    def build_url(self, path, param:dict={}):
        param_with_key = {
            'key': self.youtube_secret_key,
            **param
        }
        return build_url(self.youtube_host+'/'+path, param_with_key)
    
@lru_cache
def get_youtube_settings():
    return YoutubeSettings()