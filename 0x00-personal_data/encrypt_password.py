#!/usr/bin/env python3
"""User passwords should NEVER be stored in plain text in a database."""
import bcrypt

def hash_password(password: str)-> bytes:
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed


