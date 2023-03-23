from Server.Models.base_model import Base, DateTimeModel
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Vtuber(Base):
    __tablename__ = 'vtuber'
    vtuber_id = Column(Integer, primary_key=True, index=True)
    vtuber_name = Column(String, primary_key=False, index=False)
    
    channel = relationship("VtuberPlatform", back_populates='owner')

class VtuberPlatform(DateTimeModel):
    __tablename__ = 'vtuber_platform'
    channel_id = Column(String, primary_key=True, index=True)
    vtuber_id = Column(Integer, ForeignKey("vtuber.vtuber_id"), primary_key=False, index=True)
    platform_id = Column(Integer, ForeignKey("stream_platform.platform_id"), primary_key=False, index=True)
    vtuber_name = Column(String, primary_key=False, index=False)
    channel_name = Column(String, primary_key=False, index=False)

    owner = relationship("Vtuber", back_populates='channel')
    platform = relationship('StreamPlatform', back_populates='channel')
    playlists = relationship('Playlist', back_populates='channel')