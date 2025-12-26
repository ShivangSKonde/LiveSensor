from Sensor.exception import SensorException
from Sensor.logger import logging
import os
import sys
from pandas import DataFrame
from Sensor.entity.config_entity import DataIngestionConfig
from Sensor.entity.artifact_entity import DataIngestionArtifact
from Sensor.data_access.Sensor_data import SensorData
from sklearn.model_selection import train_test_split

from Sensor.utils.main_utils import read_yaml_file
from Sensor.constants.training_pipeline import SCHEMA_FILE_PATH

""" 
for this file we needed the dataframe from Sensor_data
and confi_entity and artifact_entity     
"""
class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        # takes 2 values as input ingestion config and schema config
        try:
            self.data_ingestion_config = data_ingestion_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)

        except Exception as e:
            raise SensorException(e, sys)

    def export_data_into_feature_store(self) -> DataFrame:
        """
        Export mongo db collection record as data frame into feature.
        we have written this code to generate file sensor.csv in feature store folder
        """
        try:
            logging.info("Exporting data from mongodb to feature store")

            sensor_data = SensorData()

            dataframe = sensor_data.export_collection_as_dataframe(
                collection_name=self.data_ingestion_config.collection_name)

            feature_store_file_path = self.data_ingestion_config.feature_store_file_path

            # creating folder

            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)

            # Writes dataframe into CSV file
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe

        except  Exception as e:
            raise SensorException(e, sys)

    def split_data_as_train_test(self, dataframe: DataFrame) -> None:
        try:
            train_set, test_set = train_test_split(
                dataframe, test_size=self.data_ingestion_config.train_test_split_ratio
            )

            logging.info("Performed train test split on the dataframe")

            logging.info(
                "Exited split_data_as_train_test method of Data_Ingestion class"
            )

            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)

            os.makedirs(dir_path, exist_ok=True)

            logging.info(f"Exporting train and test file path.")

            # Load the train set to CSV file at the particular location
            train_set.to_csv(
                self.data_ingestion_config.training_file_path, index=False, header=True
            )

            test_set.to_csv(
                self.data_ingestion_config.testing_file_path, index=False, header=True
            )

            logging.info(f"Exported train and test file path.")
        except Exception as e:
            raise SensorException(e, sys)


    def initiate_data_ingestion(self) -> DataIngestionArtifact:
            try:
                # data frame taken from the 'feature store' function which is the first function
                dataframe = self.export_data_into_feature_store()

                # dropping the columns which are redundant such that it will match with the validation columns
                dataframe = dataframe.drop(self._schema_config["drop_columns"], axis=1)

                # folder and file creation for train and test actually happens in this line
                self.split_data_as_train_test(dataframe=dataframe)

                # This line is just storing the paths for train and test files such that it can be used in further steps
                data_ingestion_artifact = DataIngestionArtifact(
                    trained_file_path=self.data_ingestion_config.training_file_path,
                    test_file_path=self.data_ingestion_config.testing_file_path)

                return data_ingestion_artifact

            except Exception as e:
                raise SensorException(e, sys)





