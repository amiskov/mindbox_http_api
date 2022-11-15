import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from api.v1 import api

from core.config import config
from core.logger import LOGGING
from repo import get_db

app = FastAPI(
    title=config.PROJECT_NAME,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse
)


@app.on_event("startup")
async def startup_event():
    get_db()


@app.on_event("shutdown")
async def shutdown_event():
    db = get_db()
    if db:
        db.disconnect()


app.include_router(
    api.router,
    prefix='/api/v1',
)


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        log_config=LOGGING,
        log_level=logging.DEBUG,
        reload=True,
    )
