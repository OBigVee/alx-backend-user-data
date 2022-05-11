#!/usr/bin/env python3
"""obfuscated log message"""
import logging
import re
from typing import List


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError



def filter_datum(fields:list, redaction:str, message:str, seperator:str) -> List[str]:
    """returns the log message obfuscated"""
    for i in fields:
        # re.sub(pattern, replace, string(message) );
        message = re.sub(
            i + "=.*?" + seperator, i + "=" + redaction + seperator, message
        )
    return message
