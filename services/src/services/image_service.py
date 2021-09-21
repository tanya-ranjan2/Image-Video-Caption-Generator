from fastapi import APIRouter, Request, File, UploadFile
import uuid
import time

from src.core.caption import image_caption

image_api_router = APIRouter(tags=["Image Captioning Servies"])
base_path = "data/uploaded_files"

@image_api_router.post("/upload")
def upload_image(file: UploadFile = File(...)): 
    """
    # Upload file 
    """
    # get file and write it to folder with a unique name
    # create file path 
    # send the path to the model
    contents = file.file.read()
    file_ext = file.filename.split(".")[-1]
    file_path = f"{base_path}/{file.filename}"
    epoch_path = f"{base_path}/{time.time()}.{file_ext}"
    print(epoch_path)
    with open(epoch_path, "w+b") as f:
        f.write(contents)
        


    val = image_caption(epoch_path)
    return {"caption": val}