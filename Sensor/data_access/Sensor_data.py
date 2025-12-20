import sys
from typing import Optional

import numpy as np
import pandas as pd
import json
from Sensor.configuration.mongo_db_connection import MongoDBClient
from Sensor.constants.database import DATABASE_NAME
from Sensor.exception import SensorException


class SensorData:
    """
    This class help to export entire mongo db record as pandas dataframe
    """

    def __init__(self):

        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)

        except Exception as e:
            raise SensorException(e, sys)

    def save_csv_file(self, file_path, collection_name: str, database_name: Optional[str] = None):
        try:
            """Everything that is stored in mongodb is stored in json format"""
            data_frame = pd.read_csv(file_path)
            data_frame.reset_index(drop=True, inplace=True)
            records = list(json.loads(data_frame.T.to_json()).values())
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            collection.insert_many(records)
            return len(records)
        except Exception as e:
            raise SensorException(e, sys)

    def export_collection_as_dataframe(
            self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            """
            export entire collectin as dataframe:
            return pd.DataFrame of collection
            """
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))

            """ we get the id when we retrive the data form mongodb.
                and we want data which is collected form the mongodb in dataframe format ,therefore we convert it in df
            """
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)

            df.replace({"na": np.nan}, inplace=True)

            """ now this data ready for the data ingestion"""
            return df

        except Exception as e:
            raise SensorException(e, sys)
