import sys
import datetime

class Logger:
    LEVELS = {
        'DEBUG': 10,
        'INFO': 20,
        'WARNING': 30,
        'ERROR': 40,
    }

    def __init__(self, level='DEBUG'):
        self.level = self.LEVELS.get(level.upper(), 10)

    def _log(self, level_name, message):
        if self.LEVELS[level_name] >= self.level:
            timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            print(f"{timestamp} [{level_name}] {message}", file=sys.stderr)

    def debug(self, message):
        self._log('DEBUG', message)

    def info(self, message):
        self._log('INFO', message)

    def warning(self, message):
        self._log('WARNING', message)

    def error(self, message):
        self._log('ERROR', message)
