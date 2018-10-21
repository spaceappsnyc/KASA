import pandas as pd
import json
from pprint import pprint

from google_maps import getDistance

def readDataForIdpCamps(idpCampFileName):
    with open(idpCampFileName) as f:
        data = json.load(f)
    return data

def getDistancesToIdpCamps(userCoordinates):
    '''
    KEEP THIS IN CASE WE NEED IT FOR LATER
    idpCamps = readDataForIdpCamps("./resources/idp_camps.json")
    for idpCamp in idpCamps:
        idpCampCoordinates = idpCamp["coordinates"]
        distance = ""
        try:
            distance = getDistance(userCoordinates, idpCampCoordinates)["value"]
        except Exception as err:
            print("Error getting distance: " + repr(err))
        idpCamp["distance"] = distance
    with open('./resources/idpCampWithDistance.json', 'w') as fp:
        json.dump(idpCamps, fp)
    return idpCamps
    '''
    with open("./resources/idp_camps_with_distance.json") as f:
        data = json.load(f)
    return data

