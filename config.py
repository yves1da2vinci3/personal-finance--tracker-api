# config.py
import os

class Config:
    """Configuration settings for the API."""

    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")

