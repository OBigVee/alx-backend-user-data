#!/usr/bin/env python3
"""obfuscated log message"""
import re
import logging
from typing import List
import mysql.connector
from os import getenv



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

def get_db()->mysql.connector.connection.MySQLConnection:
    """returns a connector to the DB"""
    db_connection = mysql.connector.connection.MySQLConnection(
        user=getenv("PERSONAL_DATA_DB_USERNAME","root"),
        password=getenv("PERSONAL_DATA_DB_PASSWORD",""),
        host=getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=getenv("PERSONAL_DATA_DB_NAME")
    )
    return db_connection

def main()->None:
    """DB View unction and return None:
    The function will obtain a database connection using 'get_db'
    and retrieve all rows in the 'users' table and display each row
    under a filtered format like this:"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = [field[0] for field in cursor.description]

    logger = get_logger()

    for row in cursor:
        _row = "".join(f"{f} = {str(r_entry)}; " for r_entry, field in zip(row,fields))
        logger.info(_row.strip())

    cursor.close()
    db.close()

