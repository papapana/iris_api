from fastapi import FastAPI

from iris_api.app.api import ranges_api, stats_api
from iris_api.app.db import client

app = FastAPI()


@app.on_event('shutdown')
async def shutdown():
    await client.close()

app.include_router(ranges_api.router)
app.include_router(stats_api.router)
