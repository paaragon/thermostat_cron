import os
import requests
import json


def set_temp(temp, mode):
    data = {
        "temp": temp,
        "mode": mode
    }

    headers = {
        "Authorization": os.environ["SET_TEMP_AUTHORIZATION"],
        "Content-type": "application/json"
    }
    r = requests.post(os.environ["SET_TEMP_URL"], data=json.dumps(data), headers=headers)

    return r
