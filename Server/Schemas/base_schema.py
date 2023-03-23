from pydantic import BaseModel, validator
from datetime import datetime
from fastapi import HTTPException

class BaseDateSchema(BaseModel):
    begin_date:datetime = None
    end_date:datetime = None
    begin_date_symbol:str = None
    end_date_symbol:str = None
    
    @validator('begin_date_symbol', 'end_date_symbol')
    def validate_symbol(self, symbol):
        valid_symbols = {
            '>',
            '>=',
            '!=',
            '<',
            '<='
        }
        if symbol is None or symbol in valid_symbols:
            return symbol
        
        raise HTTPException(status_code=400, detail='invalid symbol for date')

class YoutubeSchema(BaseDateSchema):
    page_token:str = None
    limit:int = 5