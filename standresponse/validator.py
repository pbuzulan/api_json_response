from datetime import datetime


class ErrorValidator:
    def __init__(self, state: int, message: str):
        self.__state = state
        self.__message = message
        self.__time = datetime.utcnow()

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state

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
        return f"State: {self.state}, Message: {self.message}, Time: {self.time}"

    def __str__(self):
        return str(self.__repr__())

    def asdict(self):
        return {"state": self.state, "message": self.message, "time": self.time}
