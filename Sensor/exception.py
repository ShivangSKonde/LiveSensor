import sys
import os


class SensorException(Exception):

    def error_message_details(self,error, error_details:sys):
        _,_,exc_tb=error_details.exc_info()
        filename = exc_tb.tb_frame.f_code.co_filename
        lineno = exc_tb.tb_lineno

        message = "error occured and the file name is [{0}] and line number is [{1}] and error is [{2}]".format(filename, lineno, str(error))
        return message


    def __init__(self, error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message = self.error_message_details(error_message, error_details)

    def __str__(self):     #string returned by this function gets printed when we do "print(e)"
        return self.error_message