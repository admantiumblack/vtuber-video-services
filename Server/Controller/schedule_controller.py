from Server.Models.models import Vtuber
from Server.Schemas.video_schema import VideoSchema
from Server.Utils.web_access import get_api_response
from Server.Config import get_holodex_settings

def get_schedule_list(db, vtuber_id, limit=5, parts=None, offset=0, **params):
    vtuber = Vtuber.get_vtuber(db, vtuber_id=vtuber_id)
    if not vtuber:
        return []

    active_channel = vtuber.channel
    if not active_channel:
        return []
    params = {
        'channel_id': active_channel[0].channel_id,
        'limit': limit,
        'include': parts,
        'offset': offset,
        'status': 'upcoming'
    }

    return get_api_response(get_holodex_settings(), 'live', params)

def get_live_list(db, limit=None, offset=None, **params):
    vtubers = Vtuber.get_vtubers(db, limit=limit, offset=offset, **params)
    if not vtubers:
        return []

    channel_ids = []
    for i in vtubers:
        channel = i.channel
        if channel:
            channel_ids.append(channel[0].channel_id)

    params = {
        'channels': ','.join(channel_ids)
    }

    return get_api_response(get_holodex_settings(), 'users/live', params)