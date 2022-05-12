#!/usr/bin/env python3
"""User passwords should NEVER be stored in plain text in a database."""

import bcrypt


def hash_password(password: str) -> bytes:
    """Encrypting passwords"""
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password:bytes, password: str) -> bool:
    """Check valid password"""
    return True if bcrypt.checkpw(password.encode(), hashed_password) else False
