import pandas as pd

def readDataForHealthcare(healthcareFileName):
    headers = ["city", "rating"]
    df = pd.read_csv(healthcareFileName, names=headers)
    print(df["rating"])
    #print(df['rating'])

readDataForHealthcare("./resources/test.csv")
