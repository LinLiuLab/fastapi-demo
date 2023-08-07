"""
This file contains the database connection and session objects.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# define the database connection string
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root1234@localhost/fastapi_demo"

# create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# create a SessionLocal class which will be used to create a session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# create a Base class which will be used to create database models
Base = declarative_base()
