import logging

def setup_logging(logger_name, log_file):

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(stream_handler)

    return logger