import uvicorn
import os
ENV = os.environ.get("ENV","dev")
WORKERS = os.environ.get("WORKERS",5)
PORT = os.environ.get("PORT",5000)
HOST = os.environ.get("HOST",'0.0.0.0')
print(ENV)

if __name__ == '__main__':
    debug = ENV == "dev"
    uvicorn.run('main:app', host=HOST, port=PORT, workers=WORKERS, debug=debug)