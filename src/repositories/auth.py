from fastapi import HTTPException, status
from src.repositories.user import UserRepository
from src.config.database import SessionLocal
from src.auth import auth_handler
from src.schemas.user import UserLogin as UserLoginSchema
from src.schemas.user import UserCreate as UserCreateSchema