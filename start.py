import os
import uvicorn
from Server.Config.server_config import get_server_setting

if __name__ == "__main__":
    run_setting = get_server_setting()
    uvicorn.run(
        "Server.startup:program", 
        host=run_setting.host, 
        port=run_setting.port, 
        eload=run_setting.reload
    )