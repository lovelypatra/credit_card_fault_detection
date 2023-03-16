import pymongo
import pandas as pd
import json
from credit.config import mongo_client


DATA_FILE_PATH = "/config/workspace/UCI_Credit_Card.csv"
DATABASE_NAME="bank"
COLLECTION_NAME="credit"


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns: {df.shape}")

    #convert dataframe to json format so that we can dump these record in mongo DB
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())#json.loads is used to convert any python object
    print(json_record[0])

    #insert converted json record to mongo DB
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)


