import logging

def new_logger():
    class CustomLogger(logging.Formatter):
        green = "\x1b[32;20m"
        yellow = "\x1b[33;20m"
        red = "\x1b[31;20m"
        bold_red = "\x1b[31;1m"
        reset = "\x1b[0m"
        fmt = "%(asctime)s {} %(levelname)s {} %(message)s"

        FORMATS = {
            logging.DEBUG: fmt.format(green, reset),
            logging.INFO: fmt.format(green, reset),
            logging.WARNING: fmt.format(yellow, reset),
            logging.ERROR: fmt.format(red, reset),
            logging.CRITICAL: fmt.format(bold_red, reset),
        }

        def format(self, record):
            log_fmt = self.FORMATS.get(record.levelno)
            formatter = logging.Formatter(log_fmt, datefmt="%y-%b-%d %H:%M:%S")
            return formatter.format(record)

    logger = logging.getLogger("PowerSwitch")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(CustomLogger())
    logger.addHandler(handler)
    return logger

GLOBAL_LOGGER = new_logger()

def info(msg: str, *arg) -> None:
    GLOBAL_LOGGER.info(msg, *arg)

def warn(msg: str, *arg) -> None:
    GLOBAL_LOGGER.warn(msg, *arg)

def error(msg: str, *arg) -> None:
    GLOBAL_LOGGER.error(msg, *arg)
