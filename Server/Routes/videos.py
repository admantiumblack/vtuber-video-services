from fastapi import APIRouter, Depends, Request
from Server.Controller.video_controller import get_video_list
from Server.Schemas.video_schema import VideoSchema
from Server.Utils.database_access import create_session
from Server.Utils.url_utils import create_metadata

video_routes = APIRouter(
    prefix='/video'
)

@video_routes.get('/list', status_code=201)
def get_video_list_route(request:Request, video_query=Depends(VideoSchema), db=Depends(create_session)):
    params = video_query.dict(exclude_none=True)
    page_token = None
    res, next_page, prev_page = get_video_list(
        db, 
        params.get('channel_id'), 
        params.get('playlist_type'), 
        params.get('limit'), 
        params.get('parts'),
        params.get('page_token')
    )
    metadata = create_metadata(
        str(request.url), 
        video_query.dict(exclude_unset=True), 
        next_page, 
        prev_page
    )
    response = {
        'items': res,
        'meta': metadata
    }
    return response