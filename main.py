from fastapi import FastAPI
import uvicorn
from get_requests import get_activity
from enum import Enum

class ActivityType(str, Enum):
    educational = "education"
    recreational = "recreational"
    social = "social"
    diy = "diy"
    charity = "charity"
    cooking = "cooking"
    relaxation = "relaxation"
    music = "music"
    busywork = "busywork"

app = FastAPI()


@app.get("/")
async def root():
    """Home Page with GET HTTP Method"""

    return {"message": "Hello! Generate a random activity to do using the path /activity. Type in /activity/{activity_type} from the list of parameters if an activity type needs to be specified."}

@app.get("/activity")
async def activity():
    """Get an activity from Boredapi.com
    Parameters
    ----------

    returns : dict
    """
    data = get_activity()

    return data

@app.get("/activity/{ActivityType}")
async def get_activity_type(activity_type: ActivityType):
    """Get an activity according to the user's activity type"""

    activity_t = activity_type.value
    data = get_activity(activity_type = activity_t)

    return data

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
