from datetime import datetime


class Error(Exception):
    def __init__(self, internal_state: int, http_state: int, message="", *args):
        super(Error, self).__init__(*args)
        self.internal_state = internal_state
        self.http_state = http_state
        self.message = message
        self.time = datetime.utcnow()

    def __str__(self):
        return self.message

    def __repr__(self):
        return f"HTTP State: {self.http_state}, Internal State: {self.internal_state}, Message: {self.message}, Time: {self.time}"
