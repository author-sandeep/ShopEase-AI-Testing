import logging
logging.basicConfig(
    filename="failures.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)