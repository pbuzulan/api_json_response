from datetime import datetime


class ErrorValidator:
    def __init__(self, message: str, http_state: int = None, internal_state: int = None):
        self.__http_state = http_state
        self.__message = message
        self.__internal_state = internal_state
        self.__time = datetime.utcnow()

    @property
    def http_state(self):
        return self.__http_state

    @http_state.setter
    def http_state(self, http_state):
        self.__http_state = http_state

    @property
    def internal_state(self):
        return self.__internal_state

    @internal_state.setter
    def internal_state(self, internal_state):
        self.__internal_state = internal_state

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message):
        self.__message = message

    @property
    def time(self):
        return str(self.__time)

    @time.setter
    def time(self, time):
        self.__time = time

    def __repr__(self):
        return f"HTTP State: {self.http_state}, Internal State: {self.internal_state}, Message: {self.message}, Time: {self.time}"

    def __str__(self):
        return str(self.__repr__())

    def asdict(self):
        return {"internal_state": self.internal_state, "message": self.message, "time": self.time}
