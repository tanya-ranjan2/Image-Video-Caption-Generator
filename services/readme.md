## run the code using fastAPI 
> run app.py # Uvicorn runs on http://0.0.0.0:'port' 


## ngrok to generate URL to localhost 

### ngrok setup
> download ngrok
> unzip the file in specided 'folder'
> cd 'folder'
> ./ngrok authtoken ..............

### generate URL to localhost 
> ./ngrok http 'port'


### Dockerise container
> make dockerfile
 -  cmd 
 > cd services/
 > docker build -t backend .
 > docker run -p 5000:5000 backend   # run the docker services