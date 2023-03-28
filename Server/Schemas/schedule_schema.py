from pydantic import BaseModel, Field

class ScheduleSchema(BaseModel):
    vtuber_id: str = None
    parts: str = None
    limit: int = 5
    offset: int = 0
    status: str = 'upcoming'
