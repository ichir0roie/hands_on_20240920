import fastapi

from module.api.endpoint import app
import uvicorn

# https://fastapi.tiangolo.com/tutorial/debugging/

host = "localhost"
port = 9999
if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port)

print(f"ここ開いて！ {host}:{port}/docs")
#
