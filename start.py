import os
import uvicorn

if __name__ == "__main__":
    uvicorn.run("Server.startup:program", host="localhost", port=8000, reload=True)