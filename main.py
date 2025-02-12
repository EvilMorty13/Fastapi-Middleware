from fastapi import FastAPI
from logger import logger
from middleware import log_middleware
from starlette.middleware.base import BaseHTTPMiddleware
import asyncio

app = FastAPI()


app.add_middleware(BaseHTTPMiddleware,dispatch=log_middleware)
logger.info('Starting api')


    
@app.get('/')
async def index() -> dict:
    return{'message':'hello'}

@app.get('/upload-videos')
async def upload_videos() -> dict:
    await asyncio.sleep(1.5)
    return{'message':'Video uploaded'}


