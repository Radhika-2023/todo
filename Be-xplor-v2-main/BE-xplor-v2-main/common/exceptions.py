from fastapi import status

class JsonException(Exception):
    def __init__(self, state: bool, response: str, message: str, status: status):
        self.message = message
        self.response = response
        self.status = status
        self.state = state
