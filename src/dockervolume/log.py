import os
import logging.config

DEFAULT_LOGGER_CONFIG = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'conf/log.ini')


def setup_logging(path=DEFAULT_LOGGER_CONFIG):
    logging.config.fileConfig(path)
