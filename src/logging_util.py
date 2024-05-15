import logging, pathlib, datetime, traceback

class Logger:
    verbose: bool
    internal_logger: logging.Logger

    def __init__(self) -> None:
        self.verbose = False
        self.internal_logger = logging.getLogger(__name__)

    def init_logger(self, verbose):
        self.verbose = verbose
        t = datetime.datetime.now()
        # Create log folder if it doesn't exist
        path = pathlib.Path(f"logs/{str(t).replace(' ', '.').replace(':', '-')}.log")
        path.parent.mkdir(exist_ok=True, parents=True)
        # Init logger
        logging.basicConfig(filename=path, filemode="w", level=logging.DEBUG, format="%(asctime)s %(levelname)s: %(message)s")

    def debug(self, msg):
        self.internal_logger.debug(msg)
        if self.verbose:
            print(f"DEBUG: {msg}")

    def info(self, msg: str):
        self.internal_logger.info(msg)
        print(f"INFO: {msg}")

    def warning(self, msg):
        self.internal_logger.warning(msg)
        print(f"WARN: {msg}")

    def __log_error(self, msg, level: str, has_exception = False):
        print(f"ERROR: {msg}")
        if has_exception:
            exception = traceback.format_exc()
            self.internal_logger.error(f"{msg}\n{exception}")
            if self.verbose:
                print(f"{level.upper()}: {exception}")
        else:
            self.internal_logger.error(msg)

    def error(self, msg, has_exception = False):
        """Log an error, output a traceback if `has_exception` == True"""
        self.__log_error(msg, "error", has_exception)

    def critical(self, msg, has_exception = False):
        """Log a critical error, output a traceback if `has_exception` == True"""
        self.__log_error(msg, "critical", has_exception)

    def flush(self):
        for handler in self.internal_logger.handlers:
            handler.flush()

__logger = Logger()

def getLogger() -> Logger:
    return __logger
