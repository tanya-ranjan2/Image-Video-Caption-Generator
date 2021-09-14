from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.services.image_service import image_api_router

app = FastAPI(
    title="Image Captioning",
    version="v0.1",
    description="Image Captioning module",
    root_path=""
)

app.include_router(image_api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PUT"],
    allow_headers=["*"],
)
