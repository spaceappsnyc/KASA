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
    supportScore = 0
    for unClusterDistancesJson in unClusterDistances:
        latitude = float(unClusterDistancesJson["latitude"])
        longitude = float(unClusterDistancesJson["longitude"])
        existingDistance = unClusterDistancesJson["distance"]
        nearbyIdpCamp = unClusterDistancesJson["siteName"]

        #IDP Camp score
        if existingDistance != "":
            percentageIDPCampDiff = (existingDistance - shortestDistance)/shortestDistance
        else:
            percentageIDPCampDiff = 100
        unScore = 100 - percentageIDPCampDiff

        #Support score
        if unClusterDistancesJson["washSupport"] == "Yes":
            supportScore += 1
        if unClusterDistancesJson["cccmSupport"] == "Yes":
            supportScore += 1
        if unClusterDistancesJson["healthSupport"] == "Yes":
            supportScore += 1
        if unClusterDistancesJson["shelterNfiSupport"] == "Yes":
            supportScore += 1
        if unClusterDistancesJson["foodSupport"] == "Yes":
            supportScore += 1
        if unClusterDistancesJson["protectionSupport"] == "Yes":
            supportScore += 1
        if unClusterDistancesJson["educationSupport"] == "Yes":
            supportScore += 1
        if unClusterDistancesJson["livelihoodSupport"] == "Yes":
            supportScore += 1

        overallSupportScore = (supportScore/8)*100
        print(overallSupportScore)

        #Population Density score
        #popDensityScore = populationDensityScores[city]["score"]

        #Overall Score - taking weights into account
        #score = (unScore * 0.6) + (popDensityScore * 0.4)

        coords = {"longitude": longitude, "latitude": latitude}
        score = unScore*.5 + overallSupportScore*.5
        scoreDict = {"idpCamp": nearbyIdpCamp, "score": score,  "coords": coords }
        print(scoreDict)
        supportScore = 0
        overallScoreList.append(scoreDict)

    print(overallScoreList)
    return json.dumps(overallScoreList)

score_calculation("7.247324,6.010124")
