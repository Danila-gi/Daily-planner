import uvicorn
from main import app
from settings.config import settings

if __name__ == "__main__":
    host, port = settings.get_server_connect()

    uvicorn.run(app, host=host, port=port)