import uvicorn
ENV = "dev"
WORKERS = 5
PORT = 5000
HOST = '0.0.0.0'

if  __name__ == '__main__':
    debug = False
    if ENV == "dev":
        debug = True
    
    uvicorn.run('main:app', host=HOST, port=PORT, workers=WORKERS, debug=debug)