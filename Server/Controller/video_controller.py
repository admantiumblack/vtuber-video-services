from Server.Models.models import Vtuber, Playlist
from Server.Schemas.video_schema import VideoSchema
from Server.Utils.web_access import get_api_response
from Server.Config import get_youtube_settings

def get_youtube_playlist_items(playlist_id, limit=5, parts='',page_token=None):
    params = {
        'maxResults': limit,
        'playlistId': playlist_id
    }
    if page_token is not None:
        params['pageToken'] = page_token
    if parts:
        params['part'] = parts
    youtube_config = get_youtube_settings()
    return get_api_response(youtube_config, 'playlistItems', params)

def get_youtube_videos(video_id, limit=None, parts=None, page_token=None):
    params = {
        'id': video_id
    }
    if limit:
        params['maxResults'] = limit
    
    if parts:
        params['part'] = parts

    if page_token:
        params['pageToken'] = page_token
    youtube_config = get_youtube_settings()
    return get_api_response(youtube_config, 'videos', params)

def get_video_list(db, vtuber_id, playlist_type, limit=5, parts=None, page_token=None):
    vtuber = Vtuber.get_vtuber(db, vtuber_id=vtuber_id)
    if not vtuber:
        return [], None, None

    active_channel = vtuber.channel
    if not active_channel:
        return [], None, None

    channel_id = active_channel[0].channel_id
    channel_id = channel_id[:1] + 'U' + channel_id[1+1:]

    playlist_items = get_youtube_playlist_items(channel_id, parts='contentDetails', page_token=page_token)
    video_ids = [i['contentDetails']['videoId'] for i in playlist_items['items']]
    videos = get_youtube_videos(','.join(video_ids), parts=parts)

    res = []
    for i in videos['items']:
        topic_detail = i.get('topicDetails')
        topics = []
        if topic_detail:
            topics = topic_detail.get('topicCategories')
        video_attr = {
            'id':i['id'],
            'snippet':i['snippet'],
            'statistics':i['statistics'],
            'topics':topics,
            'liveStreamingDetails': i.get('liveStreamingDetails')
        }
        res.append(video_attr)
    print(playlist_items)
    next_page = playlist_items.get('nextPageToken')
    prev_page = playlist_items.get('prevPageToken')
    return res, next_page, prev_page