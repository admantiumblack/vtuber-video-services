from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime

Base = declarative_base()

class DateTimeModel(Base):
    __tablename__ = None
    begin_date = Column(DateTime, primary_key=False, index=False)
    end_date = Column(DateTime, primary_key=False, index=False)