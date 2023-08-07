"""
This file contains the model for the document table.
"""
from sqlalchemy import Column, Integer, String, Boolean
from fastapi_demo.database import Base


class Document(Base):
    __tablename__ = "document"

    id = Column(Integer, primary_key=True, index=True)  # primary key of the table
    title = Column(String(256), nullable=False)  # title of the document
    content = Column(String(256), nullable=False)  # content of the document
    published = Column(
        Boolean, default=False
    )  # whether the document is published or not
