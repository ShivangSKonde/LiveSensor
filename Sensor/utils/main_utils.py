import yaml
import pandas as pd
import numpy as np
import os
import dill
import sys
from Sensor.exception import SensorException

""" this utils file we use for reading and writing the schema.yaml file """
def read_yaml_file(file_path: str) -> dict:
    try:

        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)


    except Exception as e:
        raise SensorException(e, sys)


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    # content → Python data (dict, list, etc.) to write into YAML
    # replace → whether to overwrite an existing file
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)       #Converts Python objects → YAML format
                                            # Writes it to the file




    except Exception as e:
        raise SensorException(e, sys)

