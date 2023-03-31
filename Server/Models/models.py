from Server.Models.base_model import Base, DateTimeModel
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime

class Vtuber(Base):
    __tablename__ = 'vtuber'
    vtuber_id = Column(Integer, primary_key=True, index=True)
    vtuber_name = Column(String, primary_key=False, index=False)
    
    channel = relationship(
        "VtuberPlatform", 
        back_populates='owner',
        primaryjoin=f'and_(Vtuber.vtuber_id==VtuberPlatform.vtuber_id, VtuberPlatform.end_date=="{datetime(year=9999, month=12, day=31)}")'
    )

    @classmethod
    def get_vtuber(cls, db, **kwargs):
        return db.query(Vtuber).filter_by(**kwargs).first()
    
    @classmethod
    def get_vtubers(cls, db, limit=None, offset=None, **kwargs):
        query = db.query(Vtuber).filter_by(**kwargs)

        if limit:
            query = query.limit()
        
        if offset:
            query = query.offset(offset)

        return query.all()

class VtuberPlatform(DateTimeModel):
    __tablename__ = 'vtuber_platform'
    channel_id = Column(String, primary_key=True, index=True)
    vtuber_id = Column(Integer, ForeignKey("vtuber.vtuber_id"), primary_key=False, index=True)
    platform_id = Column(Integer, ForeignKey("stream_platform.platform_id"), primary_key=False, index=True)
    channel_name = Column(String, primary_key=False, index=False)

    owner = relationship("Vtuber", back_populates='channel')
    platform = relationship('StreamPlatform', back_populates='channel')
    playlists = relationship('Playlist', back_populates='channel')

class StreamPlatform(Base):
    __tablename__ = 'stream_platform'
    platform_id = Column(Integer, primary_key=True, index=True)
    platform_name = Column(String, primary_key=False, index=False)

    channel = relationship('VtuberPlatform', back_populates='platform')

class Playlist(Base):
    __tablename__ = 'channel_playlist'
    playlist_id = Column(String, primary_key=True, index=True)
    channel_id = Column(String, ForeignKey("vtuber_platform.channel_id"), primary_key=False, index=True)
    playlist_type = Column(String, primary_key=False, index=False)

    channel = relationship('VtuberPlatform', back_populates="playlists")

    @classmethod
    def get_playlist(cls, db, **kwargs):
        return db.query(Playlist).filter_by(**kwargs).all()