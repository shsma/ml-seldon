class CustomException(Exception):

    def __init__(self, message, application_error_code=-1, http_status_code=404):
        Exception.__init__(self)
        self.message = message
        self.status_code = http_status_code
        self.application_error_code = application_error_code

    def to_dict(self):
        rv = {"status": {"status": self.status_code, "message": self.message,
                         "app_code": self.application_error_code}}
        return rv


class InvalidInputException(CustomException):

    def __init__(self, message, application_error_code=-1, http_status_code=404):
        super().__init__(message, application_error_code, http_status_code)

class NoItemForRecommendations(CustomException):
    def __init__(self, message, application_error_code=-1, http_status_code=500):
        super().__init__(message, application_error_code, http_status_code)

class NoModelFoundException(CustomException):

    def __init__(self, message, application_error_code=-1, http_status_code=404):
        super().__init__(message, application_error_code, http_status_code)


class ZeroItemFilterException(CustomException):
    
    def __init__(self, message, application_error_code=-1, http_status_code=404):
        super().__init__(message, application_error_code, http_status_code)