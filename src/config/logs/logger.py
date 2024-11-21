import logging

logging.basicConfig(
    level=logging.INFO, format="\033[32m%(levelname)s\033[0m:\t  %(message)s"
)

logger = logging.getLogger("chess-ml-api")
