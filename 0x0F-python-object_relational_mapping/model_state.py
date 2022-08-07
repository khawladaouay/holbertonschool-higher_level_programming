#!/usr/bin/python3
"""Defined State which inherits from Base class"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State (Base):
	"""State table in MySQL database"""

	__tablename__ = "states"
	id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
	name = Column(String(128), nullable=False)
