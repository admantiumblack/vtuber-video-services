from Server.Schemas.base_schema import YoutubeSchema

class VideoSchema(YoutubeSchema):
    channel_id: str
    parts:str = 'liveStreamingDetails,statistics,topicDetails,snippet'
    playlist_type:str = 'uploads'