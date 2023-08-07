"""
Document management service.
"""

from fastapi_demo.routers.document import schemas
from fastapi_demo.routers.document import models
from fastapi_demo.database import engine, SessionLocal


db = SessionLocal()


def create_document(document: schemas.DocumentBase):
    """Create a new document."""
    try:
        db.add(models.Document(**dict(document)))
        db.commit()
        return {"message": "Document created successfully."}
    except Exception as e:
        return {"message": f"Error: {e}"}


def get_document(document_id: int):
    """Get a document by its id."""
    try:
        db_document = db.query(models.Document).filter_by(id=document_id).first()
        if not db_document:
            return {"message": "Document not found."}
        return {"message": "Document retrieved successfully.", "data": db_document}
    except Exception as e:
        return {"message": f"Error: {e}"}


def get_all_documents():
    """Get all documents."""
    try:
        db_documents = db.query(models.Document).all()
        return {"message": "Documents retrieved successfully.", "data": db_documents}
    except Exception as e:
        return {"message": f"Error: {e}"}


def update_document(document_id: int, document: schemas.DocumentBase):
    """Update a document by its id."""
    try:
        db_document = db.query(models.Document).filter_by(id=document_id).first()
        if not db_document:
            return {"message": "Document not found."}

        # update the document only if it exists
        db.query(models.Document).filter_by(id=document_id).update(dict(document))
        return {"message": "Document updated successfully."}
    except Exception as e:
        return {"message": f"Error: {e}"}


def delete_document(document_id: int):
    """Delete a document by its id."""
    try:
        db_document = db.query(models.Document).filter_by(id=document_id).first()
        if not db_document:
            return {"message": "Document not found."}

        # delete the document only if it exists
        db.delete(db_document)
        db.commit()
        return {"message": "Document deleted successfully."}
    except Exception as e:
        return {"message": f"Error: {e}"}
