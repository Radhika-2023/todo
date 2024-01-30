import os
import sys
import models
from database import engine
import uvicorn


from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from common.exceptions import JsonException
from routers.owner_portal import locations
from routers.owner_portal import vehicles

print(os.path.dirname(os.path.dirname(os.path.abspath("__file__"))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("__file__"))))

app = FastAPI()
app.include_router(locations.router)
app.include_router(vehicles.router)

models.Base.metadata.create_all(bind=engine)

#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8000)

# - need to move this to common.exceptions - R & D
@app.exception_handler(JsonException)
async def json_exception_handler(request: Request, exc: JsonException):
    return JSONResponse(
        content={
            "success": exc.state,
            "response": f"{exc.response}",
            "details": {
                "message": f"{exc.message}"
            }
        }, status_code=exc.status
    )
