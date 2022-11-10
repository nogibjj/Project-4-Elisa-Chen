from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from get_requests import get_activity

app = FastAPI()


@app.get("/")
async def root():
    """Home Page with GET HTTP Method"""

    return {"message": "Hello! Generate a random activity to do using the path \"/get_activity\""}

@app.get("/activity")
async def get_activity():
    """Get an activity from Boredapi.com
    Parameters
    ----------

    returns : dict
    """
    return get_activity()

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")