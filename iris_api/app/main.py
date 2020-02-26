"""
Main fastapi file that sets the available routers
"""
import uvicorn
from fastapi import FastAPI

from iris_api.app.api import ranges_api, stats_api
from iris_api.app.db import client

app = FastAPI()


@app.on_event('shutdown')
async def shutdown():
    """
    Close the mongodb connection in the end
    """
    await client.close()

app.include_router(ranges_api.router)
app.include_router(stats_api.router)


# For debugging purposes
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=800)
