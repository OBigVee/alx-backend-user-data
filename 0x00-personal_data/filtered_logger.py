#!/usr/bin/env python3
"""obfuscated log message"""
import logging
import re


def filter_datum(fields, redaction, message, seperator):
    """returns the log message obfuscated"""
    for i in fields:
        # re.sub(pattern, replace, string(message) );
        message = re.sub(
            i + "=.*?" + seperator, i + "=" + redaction + seperator, message
        )
    return message
