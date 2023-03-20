import os
from fastapi import FastAPI
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
### AppCode Import ###

###############################################################################

os.system("pyclean . -q")
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


os.system("pyclean . -q")