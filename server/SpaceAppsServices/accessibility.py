import pandas as pd
import json
from pprint import pprint

from google_maps import getDistance

def readDataForTopCities(topCitiesFileName):
    with open(topCitiesFileName) as f:
        data = json.load(f)
    return data

def getDistanceFromTopCities(userCoordinates):
    topCities = readDataForTopCities("./resources/top100CitiesNigeria.json")
    for topCity in topCities:
        lat = str(topCity["latitude"])
        lon = str(topCity["longitude"])
        topCityCoordinates = lat + ',' + lon
        distance = ""
        try:
            distance = getDistance(userCoordinates, topCityCoordinates)["value"]
        except Exception as err:
            print("Error getting distance: " + repr(err))
        topCity["distanceFromUser"] = distance
        
    with open('./resources/top_100_cities_with_distance.json', 'w') as fp:
        json.dump(topCities, fp)
