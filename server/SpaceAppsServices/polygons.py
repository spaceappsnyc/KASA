import constants
import requests

def getCoordinates(city):
    cityName = city["City"]
    url = constants.POLYGON_COORDS_BASE + "q=" + cityName + "+Nigeria&polygon_geojson=1&format=json"
    response = requests.get(url)
    if (response.status_code == 200):
        data = response.json()
        if(data[1]['geojson']['coordinates']):
            return data[1]['geojson']['coordinates']
        else:
            print data
            print "JSON Response Missing Coordinates"
    else:
        raise Exception("GET request failed: " + url)

getCoordinates({"City" : "Lagos"})