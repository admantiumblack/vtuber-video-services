from Server.Models.models import Vtuber
from Server.Schemas.video_schema import VideoSchema
from Server.Utils.web_access import get_api_response
from Server.Config import get_holodex_settings

def get_schedule_list(db, vtuber_id, limit=5, parts=None, offset=0, **params):
    vtuber = Vtuber.get_vtuber(db, vtuber_id=vtuber_id)
    if not vtuber:
        return [], None, None

    active_channel = vtuber.channel
    if not active_channel:
        return [], None, None
    params = {
        'channel_id': active_channel[0].channel_id,
        'limit': limit,
        'include': parts,
        'offset': offset,
        'status': 'upcoming'
    }

    return get_api_response(get_holodex_settings(), 'live', params)