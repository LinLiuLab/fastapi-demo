"""
This module contains the API for the document router.
"""
from fastapi_demo.routers.document.service import crud
from fastapi_demo.routers.document.schemas import DocumentBase

from fastapi import APIRouter


# create a router object
document_router = APIRouter(prefix="/document", tags=["document"])


@document_router.post("")
def create_document(document: DocumentBase):
    """Create a new document."""
    return crud.create_document(document)


@document_router.get("/{document_id}")
def get_document(document_id: int):
    """Get a document by its id."""
    return crud.get_document(document_id)


@document_router.get("")
def get_all_documents():
    """Get all documents."""
    return crud.get_all_documents()


@document_router.put("/{document_id}")
def update_document(document_id: int, document: DocumentBase):
    """Update a document by its id."""
    return crud.update_document(document_id, document)


@document_router.delete("/{document_id}")
def delete_document(document_id: int):
    """Delete a document by its id."""
    return crud.delete_document(document_id)
