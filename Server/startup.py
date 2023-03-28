import os
from fastapi import FastAPI
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
### AppCode Import ###
from Server.Routes.videos import video_routes
from Server.Routes.schedule import schedule_routes

###############################################################################
program = FastAPI()
security = HTTPBearer()
###############################################################################

program.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

###############################################################################

program.include_router(video_routes)
program.include_router(schedule_routes)