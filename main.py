from Sensor.constants.training_pipeline import SAVED_MODEL_DIR
from Sensor.exception import SensorException
import sys
import os
from Sensor.logger import logging
#from Sensor.utils import dump_csv_file_to_mongodb_collection
from Sensor.pipeline.training_pipeline import TrainPipeline

from Sensor.constants.application import APP_HOST, APP_PORT
from starlette.responses import RedirectResponse
from uvicorn import run as app_run
from fastapi.responses import Response
from Sensor.ml.model.estimator import ModelResolver,TargetValueMapping
from Sensor.utils.main_utils import load_object
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi import FastAPI, File, UploadFile, Response
import pandas as pd

# def test_exception():
#     try:
#         logging.info("Testing exception")
#         a=1/0
#     except Exception as e:
#         raise SensorException(e,sys)

app = FastAPI()

origins = ["*"]
# Cross-Origin Resource Sharing (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def train():
    try:

        training_pipeline = TrainPipeline()

        if training_pipeline.is_pipeline_running:
            return Response("Training pipeline is already running.")

        training_pipeline.run_pipeline()
        return Response("Training successfully completed!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.get("/predict")
async def predict():
    try:

        # get data and from the csv file
        # covert it into dataframe

        df = None

        Model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
        if not Model_resolver.is_model_exists():
            return Response("Model is not available")

        best_model_path = Model_resolver.get_best_model_path()
        model = load_object(file_path=best_model_path)
        y_pred = model.predict(df)
        df['predicted_column'] = y_pred
        df['predicted_column'].replace(TargetValueMapping().reverse_mapping, inplace=True)

        # get the prediction output as you wnat


    except  Exception as e:
        raise SensorException(e, sys)


def main():
    try:

        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)


""" Even though the mentioned is http://0.0.0.0:8080 but use http://127.0.0.1:8080/ to see the output"""
if __name__ == '__main__':
    # file_path= r"C:\Users\shiva\OneDrive\Desktop\LiveSensor\aps_failure_training_set1.csv"
    # database_name="Sensor_data"
    # collection_name="Sensor"
    #
    # dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)

    # training_pipeline = TrainPipeline()
    # training_pipeline.run_pipeline()

    app_run(app ,host=APP_HOST,port=APP_PORT)




    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)    # e is the exception object also having the error code