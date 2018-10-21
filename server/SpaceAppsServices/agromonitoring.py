import json
import requests

import constants

def createPolygon(city, coordinates):
    with open("./resources/polygon_payload_base.json") as f:
        payload = json.load(f)
    polygonIds = {}
    url = constants.AGROMONITORING_POLYGON_API + "?appid=" + constants.AGROMONITORING_API_KEY
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if (response.status_code == 201):
        data = response.json()
        polygonIds[city] = data["id"]
    else:
        raise Exception("POST request failed: " + url)
    with open('./resources/polygon_ids.json', 'w') as fp:
        json.dump(polygonIds, fp)

createPolygon(
    "lagos",
    [
        [-121.1958,37.6683],
        [-121.1779,37.6687],
        [-121.1773,37.6792],
        [-121.1958,37.6792],
        [-121.1958,37.6683]
    ]
)