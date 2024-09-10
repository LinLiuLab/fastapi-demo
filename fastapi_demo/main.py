"""
Main module for the FastAPI application.
"""
from fastapi_demo.database import engine
from fastapi_demo.routers.document.api import document_router
from fastapi_demo.routers.document.models import Base as document_base

import uvicorn
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost",     # 带端口的
    "http://localhost:3000",    # 不带端口的
    "http://localhost:3002", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(document_router)


if __name__ == "__main__":
    document_base.metadata.create_all(bind=engine)
    uvicorn.run(app, host="127.0.0.1", port=8000)
