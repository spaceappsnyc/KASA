from un_clusters import *
from population_density import optimalPopDensityScore
import json

"""
    Given a latitude and longitude we calculate the scores for each potential
    displacement camp location based on measures such as distance from UN clusters,
    distance from healthcare facilities, accessibility score and population density
"""
def score_calculation(userCoordinates):
    #Score Calculation - Based on Distance from IDP Camps
    unClusterDistances = getDistancesToIdpCamps(userCoordinates)

    #Get shortest distance IDP Camp value
    shortestDistance = unClusterDistances[0]["distance"]
    for unClusterDistancesJson in unClusterDistances:
        if (unClusterDistancesJson["distance"] < shortestDistance):
            shortestDistance = unClusterDistancesJson["distance"]

    overallScoreList = []

    #Score Calculation - Based on Population density scores
    populationDensityScores = optimalPopDensityScore()

    #Iterate through the list of IDP camps and combine scores from each measure
    for unClusterDistancesJson in unClusterDistances:
        city = unClusterDistancesJson["city"]
        latitude = float(unClusterDistancesJson["latitude"])
        longitude = float(unClusterDistancesJson["longitude"])
        existingDistance = unClusterDistancesJson["distance"]
        nearbyIdpCamp = unClusterDistancesJson["name"]

        #IDP Camp score
        percentageIDPCampDiff = (existingDistance - shortestDistance)/shortestDistance
        unScore = 100 - percentageIDPCampDiff

        #Population Density score
        popDensityScore = populationDensityScores[city]["score"]

        #Overall Score - taking weights into account
        score = (unScore * 0.6) + (popDensityScore * 0.4)
        coords = {"longitude": longitude, "latitude": latitude}
        scoreDict = {"city": city, "score": score, "nearbyIdpCamp": nearbyIdpCamp, "coords": coords }
        print(scoreDict)
        overallScoreList.append(scoreDict)

    print(overallScoreList)
    return json.dumps(overallScoreList)
