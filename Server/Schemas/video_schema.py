from Server.Config.Schemas.base_schema import YoutubeSchema

class VideoSchema(YoutubeSchema):
    channel_id: str