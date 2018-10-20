from un_clusters import *
import json

"""
    Given a latitude and longitude we calculate the scores for each potential
    displacement camp location based on measures such as distance from UN clusters,
    distance from healthcare facilities
"""
def score_calculation(userCoordinates):
    unClusterScore = getDistancesToIdpCamps(userCoordinates)
    print(str(type(unClusterScore)))
    shortestDistance = unClusterScore[0]["distance"]
    for unClusterScoreJson in unClusterScore:
        if (unClusterScoreJson["distance"] < shortestDistance):
            shortestDistance = unClusterScoreJson["distance"]
    print("shortest distance is " + str(shortestDistance))
    print(unClusterScore)

    unClusterScoreList = []
    for unClusterScoreJson in unClusterScore:
        city = unClusterScoreJson["city"]
        latitude = unClusterScoreJson["latitude"]
        longitude = unClusterScoreJson["longitude"]
        existingDistance = unClusterScoreJson["distance"]
        nearbyIdpCamp = unClusterScoreJson["name"]
        percentageDiff = (existingDistance - shortestDistance)/shortestDistance
        score = 100 - percentageDiff
        scoreDict = {"city": city, "nearbyIdpCamp": nearbyIdpCamp, "latitude": latitude, "longitude": longitude, "score": score}
        unClusterScoreList.append(scoreDict)
    print(unClusterScoreList)
    return json.dumps(unClusterScoreList)

score_calculation("6.5244,3.3792")
