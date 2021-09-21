# backend/Dockerfile

FROM python:3.8-slim

WORKDIR /app
RUN apt-get update
RUN apt-get install \
    'ffmpeg'\
    'libsm6'\
    'libxext6'\
        'gcc'  -y

# RUN pip install tensorflow
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]