import sys


class MyException(Exception):

    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()
        self.line_number = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"{self.error_message} at {self.filename} line {self.line_number}"


if __name__ == "__main__":
    try:
        a = 1/0

    except Exception as e:
        raise MyException(e, sys)
