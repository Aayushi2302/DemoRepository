import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)


import logging
import hello.demo
from logs.log_config import LogConfig

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    level = logging.DEBUG,
    filename = "logs/logs.txt"
)
logger = logging.getLogger('main')


if __name__ == "__main__":
    print("hello")
    LogConfig.hello()