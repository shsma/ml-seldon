import deploy.exceptions


def validate_request(request, expected_keys):
    if not isinstance(request, dict):
        raise deploy.exceptions.InvalidInputException("The request should be a dictionary")

    if not all(key in request for key in expected_keys):
        missing_keys = set(request.keys()) - set(expected_keys)
        raise deploy.exceptions.InvalidInputException(f"The request is missing some parameters: {missing_keys}")
