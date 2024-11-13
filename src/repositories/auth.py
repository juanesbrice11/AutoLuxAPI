from fastapi import HTTPException, status
from src.repositories.user import UserRepository
from src.config.database import SessionLocal
from src.auth import auth_handler
from src.schemas.user import UserLogin as UserLoginSchema
from src.schemas.user import UserCreate as UserCreateSchema

class AuthRepository:
    def __init__(self) -> None:
        pass

    def register_user(self, user: UserCreateSchema) -> dict:
        db = SessionLocal()
        if UserRepository(db).get_user(email=user.email) != None:
            raise Exception("Account already exists")
        hashed_password = auth_handler.hash_password(password=user.password)
        new_user: UserCreateSchema = UserCreateSchema(
            id=user.id,
            name=user.name,
            last_name=user.last_name,
            email=user.email, 
            password=hashed_password,
            age=user.age,
            role_id=user.role_id
        )
        return UserRepository(db).create_user(new_user)

    def login_user(self, user: UserLoginSchema) -> dict:
        db = SessionLocal()
        check_user = UserRepository(db).get_user(email=user.email)
        if check_user is None:
            return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials (1)",
        )

        if not auth_handler.verify_password(user.password, check_user.password):
            return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials (2)",
        )

        access_token = auth_handler.encode_token(check_user)
        refresh_token = auth_handler.encode_refresh_token(check_user)
        return access_token, refresh_token