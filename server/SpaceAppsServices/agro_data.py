import constants
import requests
import time
import datetime

def agroData(polyId):
    now = datetime.datetime.now()
    lastMonth = now - datetime.timedelta(days=30)
    nowUnix = int(time.mktime(now.timetuple()))
    lastMonthUnix = int(time.mktime(lastMonth.timetuple()))
     
    #url = constants.AGROMONITORING_NDVI_API + "polyid=" + polyId + "&start=" + str(lastMonthUnix) + "&end=" + str(nowUnix) + "&appid=" + constants.AGROMONITORING_API_KEY
    
    response = requests.get("http://api.agromonitoring.com/agro/1.0/ndvi/history?polyid=" + polyId + "&start=946684800&end=1540103851&appid=b5663a79a19a902ad50c8a81eb765fbe")
    if (response.status_code == 200):
        data = response.json()
        
        return(data[0]['data']['mean'])

    else:
        #print(url)
        print(response)
        raise Exception("GET request failed")

agroData("5bcbfe1d5a8a6000081fa0f7")