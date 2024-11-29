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
from src.routers.brand import Brand_router
from src.routers.role import role_router
from src.routers.vehicle import vehicle_router
from src.routers.article import Article_router
from src.routers.auth import auth_router
from src.routers.user import user_router
from src.routers.comment import Comment_router

from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

tags_metadata = [
    {
        "name": "country",
        "description": "country handling endpoints",
    },
    {
        "name": "Brand",
        "description": "brand handling endpoints",
    },
    {
        "name": "Article",
        "description": "article handling endpoints",
    },
    {
        "name": "Role",
        "description": "role handling endpoints",
    },
    {
        "name": "Auth",
        "description": "auth user handling endpoints",
    },
    {
        "name": "User",
        "description": "user handling endpoints",
    },
    {
        "name": "Comment",
        "description": "comment handling endpoints",
    }
]
app = FastAPI(openapi_tags=tags_metadata, root_path=f"/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://autolux.lat"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prefix="/brand", router=Brand_router)
app.include_router(prefix="/country", router=country_router)
app.include_router(prefix="/role", router=role_router)
app.include_router(prefix="/vehicle", router=vehicle_router)
app.include_router(prefix="/article", router=Article_router)
app.include_router(prefix="/auth", router=auth_router)
app.include_router(prefix="/user", router=user_router)
app.include_router(prefix="/comment", router=Comment_router)

app.title = "AUTOLUX"
app.summary = "API with FastAPI and Python"
app.description = "This is a demostration of API REST using Python"
app.version = "0.0.1"


@app.get('/hello',
    tags=["web"],
    description="Shows an HTML hello world")
def greet():
    return HTMLResponse("<h1>Hello World</h1>")
