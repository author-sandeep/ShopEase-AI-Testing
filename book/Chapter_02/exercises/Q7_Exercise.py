from logging.handlers import RotatingFileHandler
def setup_log():
    log = logging.getLogger("Test")
    # Enforces a 5MB limit with 2 backups
    handler = RotatingFileHandler("test.log", maxBytes=5*1024*1024, backupCount=2)
    log.addHandler(handler)