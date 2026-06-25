import urllib.request
from IPython import display
from LinkInCell.custom_exception import InvalidURLException
from LinkInCell.logger import logger

from urllib import response
def is_valid(URL: str)-> bool:
  try:
    response_status = urllib.request.urlopen(URL).getcode()
    assert response_status == 200
    logger.debug(f"response_status: {response_status}")
    return True

  except Exception as e:
    logger.exception(e)
    return False

def render_web(url: str, width: str="100%", height: str="600")-> str:
  try:
    if is_valid(url):
      response = display.IFrame(src=url, width=width, height=height)
      display.display(response)
      return "Success."
    else:
      raise InvalidURLException
  except Exception as e:
    raise e
  
