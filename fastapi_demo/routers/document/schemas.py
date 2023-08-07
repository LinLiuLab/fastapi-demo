"""
Document schemas. The difference between schemas and models is that schemas are used for request and response bodies, while models are used for database models.
"""
from pydantic import BaseModel
from typing import Optional


class DocumentBase(BaseModel):
    title: str
    content: str
    published: Optional[bool] = False
