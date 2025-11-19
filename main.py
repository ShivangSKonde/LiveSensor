from Sensor.exception import SensorException
import sys
import os
from Sensor.logger import logging


def test_exception():
    try:
        logging.info("Testing exception")
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)



if __name__ == '__main__':
    try:
        test_exception()
    except Exception as e:
        print(e)    # e is the exception object also having the error code