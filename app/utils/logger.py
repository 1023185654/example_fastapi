import logging
import os
import sys

from loguru import logger as loguru_logger


class Logging:
    """自定义日志"""

    def __init__(self):
        self.log_path = "logs"
        os.makedirs(self.log_path, exist_ok=True)
        self._init_logger()

    def _init_logger(self):
        loguru_logger.remove()
        LOG_FILE_FORMAT = "{time:YYYY-MM-DD HH:mm:ss.SSS}/{level}/{module}.{function}:{line} {message}"
        LOG_STDOUT_FORMAT_WITH_COLOR = (
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> "
            "<level>{level: <8}</level> <cyan>{module}</cyan>.<cyan>{function}</cyan>:<cyan>{line}</cyan> <level>{message}</level>"
        )

        loguru_logger.add(
            sys.stdout,
            filter=lambda record: record["level"].no >= logging.INFO,
            colorize=True,
            format=LOG_STDOUT_FORMAT_WITH_COLOR,
        )

        loguru_logger.add(
            os.path.join(self.log_path, "server.err.log.{time:YYYY-MM-DD}"),
            format=LOG_FILE_FORMAT,
            filter=lambda record: record["level"].no >= logging.WARNING,
            rotation="00:00",
            backtrace=True,
            diagnose=True,
            retention="1 week",
        )

        loguru_logger.add(
            os.path.join(self.log_path, "server.info.log.{time:YYYY-MM-DD}"),
            format=LOG_FILE_FORMAT,
            filter=lambda record: record["level"].no == logging.INFO,
            rotation="00:00",
            retention="1 week",
        )

        loguru_logger.add(
            os.path.join(self.log_path, "server.debug.log.{time:YYYY-MM-DD}"),
            format=LOG_FILE_FORMAT,
            filter=lambda record: record["level"].no == logging.DEBUG,
            rotation="00:00",
            retention="3 days",
        )
