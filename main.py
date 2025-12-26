from Sensor.exception import SensorException
import sys
import os
from Sensor.logger import logging
#from Sensor.utils import dump_csv_file_to_mongodb_collection
from Sensor.pipeline.training_pipeline import TrainPipeline


# def test_exception():
#     try:
#         logging.info("Testing exception")
#         a=1/0
#     except Exception as e:
#         raise SensorException(e,sys)



if __name__ == '__main__':
    # file_path= r"C:\Users\shiva\OneDrive\Desktop\LiveSensor\aps_failure_training_set1.csv"
    # database_name="Sensor_data"
    # collection_name="Sensor"
    #
    # dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)

    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()



    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)    # e is the exception object also having the error code