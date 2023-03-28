from fastapi import APIRouter, Depends, Request
from Server.Controller.schedule_controller import get_schedule_list 
from Server.Schemas.schedule_schema import ScheduleSchema 
from Server.Utils.database_access import create_session
from Server.Utils.url_utils import create_metadata, create_metadata_lim

schedule_routes = APIRouter(
    prefix='/schedule'
)

@schedule_routes.get('/list', status_code=201)
def get_schedule_list_route(request:Request, db=Depends(create_session), schedule_scheema=Depends(ScheduleSchema)):
    params = schedule_scheema.dict(exclude_none=True)
    res = get_schedule_list(
        db, 
        **params
    )
    metadata = create_metadata_lim(str(request.url).split('?')[0], **params)
    return {'data': res, 'meta': metadata}