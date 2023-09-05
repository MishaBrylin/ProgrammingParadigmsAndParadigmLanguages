class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    def __init__(self):
        self.log_data = []

    def log(self, message):
        self.log_data.append(message)

    def print_logs(self):
        for log in self.log_data:
            print(log)


logger1 = Logger()
logger1.log("Hello")

logger2 = Logger()
logger2.log("Bye")

logger1.print_logs()  
logger2.print_logs()  