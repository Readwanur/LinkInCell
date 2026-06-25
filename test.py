from LinkInCell.logger import logger
from LinkInCell.custom_exception import InvalidURLException

try:
    raise InvalidURLException()   
except Exception as e:
    logger.error(f"An error occured: {e}")