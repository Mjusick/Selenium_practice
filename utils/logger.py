import logging


def get_logger(module_name: str):
    logger = logging.getLogger(module_name)
    logging.basicConfig(filename='test_logs.log', filemode="w", level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
    return logger
