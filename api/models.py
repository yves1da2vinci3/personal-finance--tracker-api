# models.py

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    """Model for a user."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True)
    password = Column(String(255))

class Expense(Base):
    """Model for an expense."""

    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    amount = Column(Integer)
    date = Column(Date)

class Income(Base):
    """Model for an income."""

    __tablename__ = "incomes"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    amount = Column(Integer)
    date = Column(Date)
