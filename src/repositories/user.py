from typing import List
from src.schemas.user import User as UserSchema
from src.schemas.user import UserCreate as UserCreateSchema
from src.models.user import User as UserModel

class UserRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_user_by_id(self, id: int) -> UserSchema:
        element = self.db.query(UserModel).filter(UserModel.id == id).first()
        return element

    def get_user(self, email: str) -> UserSchema:
        element = self.db.query(UserModel).filter(UserModel.email ==email).first()
        return element

    def get_users(self) -> List[UserSchema]:
        elements = self.db.query(UserModel).all()
        return elements

    def create_user(self, user: UserCreateSchema) -> dict:
        new_user = UserModel(**user.model_dump())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def edit_user(self, id: str, user: UserSchema) -> dict:
        element = self.db.query(UserModel).filter(UserModel.id == id).first()
        if element:
            element.name = user.name
            element.last_name = user.last_name
            element.email = user.email
            element.password = user.password
            element.age = user.age
            self.db.commit()
            self.db.refresh(element)
        return element

    def delete_user(self, id: int) -> dict:
        element = self.db.query(UserModel).filter(UserModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element