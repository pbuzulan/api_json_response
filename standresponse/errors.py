from datetime import datetime


class Error(Exception):
    def __init__(self, state: int, message="", *args):
        super(Error, self).__init__(*args)
        self.state = state
        self.message = message
        self.time = datetime.utcnow()

    def __str__(self):
        return self.message

    def __repr__(self):
        return f" State: {self.state}, Message: {self.message}, Time: {self.time}"
