
class FileLogger:
    def log(self):
        print("Logging to file")

class DatabaseLogger:
    def log(self):
        print("Logging to database")

def log_message(logger):
    logger.log()

