from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Any, Optional, List

from src.models.role import Role
from src.models.country import Country
from src.models.user import User
from src.models.brand import Brand
from src.models.vehicle import Vehicle
from src.models.article import Article
from src.models.comment import Comment
from src.config.database import Base, engine


from src.routers.country import country_router

Base.metadata.create_all(bind=engine)

tags_metadata = [
    {
        "name": "country",
        "description": "country handling endpoints",
    },
]
app = FastAPI(openapi_tags=tags_metadata)

app.include_router(prefix="/api/v1/country", router=country_router)

app.title = "AUTOLUX"
app.summary = "API with FastAPI and Python"
app.description = "This is a demostration of API REST using Python"
app.version = "0.0.1"


@app.get('/hello',
    tags=["web"],
    description="Shows an HTML hello world")
def greet():
    return HTMLResponse("<h1>Hello World</h1>")