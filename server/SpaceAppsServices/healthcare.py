import pandas as pd

def readDataForHealthcare(healthcareFileName):
    headers = ["city", "rating"]
    df = pd.read_csv(healthcareFileName, names=headers)
    return df.to_json(orient='records')
    #print(df['rating'])

readDataForHealthcare("./resources/test.csv")
