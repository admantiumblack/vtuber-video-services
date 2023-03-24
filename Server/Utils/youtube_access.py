from requests import get
from Server.Config.youtube_config import get_youtube_settings


def get_youtube(path, params:dict={}, **kwargs):
    youtube_config = get_youtube_settings()
    params['key'] = youtube_config.youtube_secret_key

    url = youtube_config.build_url(path, params)
    print(url)
    response = get(url)
    
    return response.json()