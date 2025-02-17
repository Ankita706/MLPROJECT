import sys 

def error_message_detail(error, error_detail: sys):
    """
    Returns a detailed error message with file name and line number.
    """
    _, _, exc_tb = error_detail.exc_info()  # Gives details about the error
    file_name = exc_tb.tb_frame.f_code.co_filename  # Extract filename

    error_message = "Error occurred in python script: [{0}] at line [{1}] with message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message  # Return the formatted error message


class CustomException(Exception):
    """
    Custom Exception class that extends the built-in Exception class.
    """
    def __init__(self, error_message, error_detail: sys):
        """
        Constructor that initializes the custom error message.
        """
        super().__init__(error_message)  # Corrected the super() call
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message  # Return the custom error message
