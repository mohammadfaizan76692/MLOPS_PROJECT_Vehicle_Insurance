import sys
import logging

def error_message_detail(error:Exception, error_detail: sys) -> str:
    """
    Extracts detailed error information include file name, line number and the error message
    
    :param error: The Exception that occured
    :type error: Exception

    :param error_detail: The sys module to access the traceback details
    :type error_detail: sys

    :return: A formatted error message.
    :rtype: str
    """

    #Extract traceback details (exception information)
    _, _, exc_tb = error_detail.exc_info()

    # get the file name where exception occured
    file_name = exc_tb.tb_frame.f_code.co_filename

    #Create a formatted error message string with file name, line number and the actual error
    line_number = exc_tb.tb_lineno
    error_message = f"Error occured in Python Script: [{file_name}] at line number [{line_number}]: {str(error)}"

    # logging
    logging.error(error_message)

    return error_message

class MyException(Exception):
    def __init__(self, error_message:Exception ,error_detail: sys ):
        super().__init__()
        """
        Initializes the Vichle Insurance Exception with a detailed error message.

        :param error_message: description of error
        :type error_message: 

        :param error_detail: The sys module to access the traceback details
        :type error_detail: sys

        """
        self.error_message = error_message_detail(error_message, error_detail)


    def __str__(self) -> str:
        """
        Returns the string representation of the error message.
        """
        return self.error_message

