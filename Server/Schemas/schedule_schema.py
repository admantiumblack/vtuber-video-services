from pydantic import BaseModel, Field

class ScheduleSchema(BaseModel):
    vtuber_id: str = None
    parts: str = None
    limit: int = 5
    offset: int = 0
    status: str = 'upcoming'

class LiveSchema(BaseModel):
    vtuber_id: str = None
    limit: int = None
    offset: int = None