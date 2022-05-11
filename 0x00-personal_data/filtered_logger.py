#!/usr/bin/env python3
"""obfuscated log message"""
import logging
import re


def filter_datum(fields, redaction, message, seperator):
    """returns the log message obfuscated"""
    for i in fields:
        # re.sub(pattern, repl, string, count=0, flags=0);
        message = re.sub(
            i + "=.*?" + seperator, i + "=" + redaction + seperator, message
        )
    return message
