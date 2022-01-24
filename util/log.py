"""Development and Deployment Logging.

Logging to pipeline stdout.

    Logging layout:

    - squared
        │
        ├─
        └─

    - round
        │
        ├─
        ╰─

src: https://en.wikipedia.org/wiki/Box-drawing_character
"""
import logging
from util.log_colour import LogColour

format = "[%(levelname)s][%(filename)s:%(lineno)d] %(message)s"
logging.basicConfig(format=format,level=logging.INFO)
logger = logging.getLogger("root")



def log(data='', mode='none'):  
    if mode == 'none':
        print(data)
    elif mode == 'warning':
        logger.warning(data)
    elif mode == 'info':
        logger.info(data)
