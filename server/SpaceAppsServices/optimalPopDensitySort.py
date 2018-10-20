import constants

#sort cities by population density relative to optimal density
def optimalPopDensitySort(cityList):
    
    cityToDensity = {}

    for city in cityList:
        diff = abs(city['populationDensity'] - constants.OPTIMAL_DENSITY)
        cityToDensity[city['city']] = diff
    
    sortedCities = sorted(cityToDensity, key=cityToDensity.get)