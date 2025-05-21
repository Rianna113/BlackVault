import datetime

class Logger:
    LEVELS = {
        'DEBUG': 10,
        'INFO': 20,
        'ERROR': 30
    }

    def __init__(self, level='INFO'):
        self.level = level
        self.level_value = self.LEVELS.get(level.upper(), 20)

    def _log(self, level_name, message):
        if self.LEVELS[level_name] >= self.level_value:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{timestamp}] [{level_name}] {message}")

    def debug(self, message):
        self._log('DEBUG', message)

    def info(self, message):
        self._log('INFO', message)

    def error(self, message):
        self._log('ERROR', message)
