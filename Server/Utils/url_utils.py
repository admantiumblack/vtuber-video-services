def build_url(url, param:dict={}):
    param_parts = []
    for i in param:
        if isinstance(param[i], list):
            param_parts.append(f'{i}={",".join(param[i])}')
        else:
            param_parts.append(f'{i}={param[i]}')
    
    final_url = url + '?' + '&'.join(param_parts)
    return final_url

def create_metadata(url, params, next_token, prev_token):
    metadata = {
        'nextPageUrl': None,
        'prevPageUrl': None
    }
    if next_token:
        params['page_token'] = next_token
        metadata['nextPageUrl'] = build_url(url, params)
    if prev_token:
        params['page_token'] = prev_token
        metadata['nextPageUrl'] = build_url(url, params)
    
    return metadata