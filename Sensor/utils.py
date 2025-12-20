import json

import numpy as np
import pandas as pd

from Sensor.config import client


def dump_csv_file_to_mongodb_collection(file_path:str,database_name:str,collection_name:str) -> None:
    try:
        df = pd.read_csv(file_path)
        df.reset_index(drop=True,inplace=True)

        # df.T — Transpose the DataFrame , df.T.to_json() — Convert the transposed DataFrame to JSON
        #json.loads(...) — Convert JSON string → Python dictionary
        #.values() — Take only the values
        #list(...) — Convert dict_values → list
        #json_records = [
        #{"A": 1, "B": 2},
        #{"A": 3, "B": 4}
        #]

        json_records=list(json.loads(df.T.to_json()).values())
        client[database_name][collection_name].insert_many(json_records)

    except Exception as e:
        print(e)
