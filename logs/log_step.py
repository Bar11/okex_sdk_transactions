import logging
from config.config import LOGGING_FILE, LOGGING_LEVEL
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler


class LoggingHandler:
    _FORMAT = '%(asctime)s [%(levelname)s] %(name)s:%(lineno)d - %(message)s'

    def __init__(self):
        self.logger = logging.getLogger("okex-sdk-transactions")
        self.logger.setLevel(LOGGING_LEVEL)

    def Init_Logger(self):
        self.setup_time_rotation()
        return self.logger

    def setup_time_rotation(self):
        """时间轮转配置"""
        handler = TimedRotatingFileHandler(
            LOGGING_FILE,
            when='midnight',
            interval=1,
            backupCount=7,
            encoding='utf-8'
        )
        self._add_handler(handler)

    def setup_size_rotation(self):
        """容量轮转配置"""
        handler = RotatingFileHandler(
            LOGGING_FILE,
            maxBytes=10 * 1024 * 1024,  # 10MB
            backupCount=5,
            encoding='utf-8'
        )
        self._add_handler(handler)

    def _add_handler(self, handler):
        """统一处理器配置"""
        formatter = logging.Formatter(self._FORMAT)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def close(self):
        """资源释放方法"""
        for handler in self.logger.handlers:
            handler.close()
            self.logger.removeHandler(handler)
