from requests import get

def get_api_response(api_config, path, params:dict={}, **kwargs):
    url = api_config.build_url(path, params)
    response = get(url)
    
    return response.json()