import json
import requests

import constants

def getDistance(originCoordinates, destinationCoordinates):
    url = constants.GOOGLE_MAPS_DISTANCE_API + "?" + constants.GOOGLE_MAPS_KEY_URI + "&origins=" + originCoordinates + "&destinations=" + destinationCoordinates
    response = requests.get(url)
    if (response.status_code == 200):
        data = response.json()
        if (len(data["rows"]) > 0 and len(data["rows"][0]["elements"]) > 0):
            return data["rows"][0]["elements"][0]["distance"]
        else:
            raise Exception("GET request did not return distance: " + url)
    else:
        raise Exception("GET request failed: " + url)
