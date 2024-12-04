from fastapi import FastAPI, Request
from logger import logger
import time

async def log_middleware(request: Request,call_next):
    start = time.time()
    response = await call_next(request)
    process_time = time.time()-start
    client_ip = request.client.host
    log_dict = {
        "url": request.url.path,
        "method": request.method,
        "client_ip": client_ip,
        "process_time": process_time
    }
    logger.info(log_dict, extra=log_dict)
    

    
    return response