import logging
class AlertFormatter(logging.Formatter):
    def format(self, record):
        return f"[AI_ALERT] {record.levelname}: {record.getMessage()}"