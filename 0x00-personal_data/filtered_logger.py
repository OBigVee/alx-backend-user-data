#!/usr/bin/env python3
"""obfuscated log message"""

import logging
import re
from typing import List


PII_FIELDS = ('email', 'phone', 'ssn', 'password','ip')



def filter_datum(
    fields: list, redaction: str, message: str, seperator: str
) -> List[str]:
    """returns the log message obfuscated"""
    for i in fields:
        # re.sub(pattern, replace, string(message) );
        message = re.sub(
            i + "=.*?" + seperator, i + "=" + redaction + seperator, message
        )
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: list):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        return filter_datum(
            self.fields,
            self.REDACTION,
            super(RedactingFormatter, self).format(record),
            self.SEPARATOR,
        )

def get_logger()->logging.Logger:
    """returns a reference to a logger instance."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    streamH = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    logger.setFormatter(formatter)
    logger.addHandler(streamH)
    return logger
    #return logger.info(logging.StreamHandler(RedactingFormatter))
