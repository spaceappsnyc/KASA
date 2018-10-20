import pandas as pd
import json

import constants

def readDataForPopulationDensity(populationFileName):
    """
    Should only need to be run once to generate
    json file with calculated population densities
    """
    headers = ["city", "area", "populationCount"]
    popFile = pd.read_csv(populationFileName, names=headers)
    popJsonStr = popFile.to_json(orient="records")
    populations = json.loads(popJsonStr)
    for p in populations:
        popCount = float(p["populationCount"])
        area = float(p["area"])
        popDensity = popCount / (area * 1000)
        p["populationDensity"] = popDensity
    with open('./resources/populationWithDensities.json', 'w') as fp:
        json.dump(populations, fp)

def optimalPopDensitySort():
    """
    sort cities by population density relative to optimal density
    """
    with open("./resources/populationWithDensities.json") as f:
        cityList = json.load(f)

    cityToDensity = {}

    for city in cityList:
        diff = abs(city['populationDensity'] - constants.OPTIMAL_DENSITY)
        cityToDensity[city['city']] = diff
    
    return sorted(cityToDensity, key=cityToDensity.get)
