from Server.Models.base_model import Base, DateTimeModel
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Playlist(Base):
    __tablename__ = 'channel_playlist'
    playlist_id = Column(String, primary_key=True, index=True)
    channel_id = Column(String, ForeignKey("vtuber_platform.channel_id"), primary_key=False, index=True)
    playlist_type = Column(String, primary_key=False, index=False)

    channel = relationship('VtuberPlatform', back_populates="playlists")