from Server.Models.base_model import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class StreamPlatform(Base):
    __tablename__ = 'stream_platform'
    platform_id = Column(Integer, primary_key=True, index=True)
    platform_name = Column(String, primary_key=False, index=False)

    channel = relationship('VtuberPlatform', back_populates='platform')
