from typing import List
from fastapi import HTTPException
from src.schemas.role import Role
from src.models.role import Role as RoleModel

class RoleRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_roles(self) -> List[Role]:
        query = self.db.query(RoleModel)
        return query.all()

    def get_role(self, id: int ) -> Role:
        element = self.db.query(RoleModel).filter(RoleModel.id == id).first()
        return element
    
    def create_role(self, role: Role) -> dict:
        new_role = RoleModel(**role.model_dump())
        self.db.add(new_role)
        self.db.commit()
        self.db.refresh(new_role)
        return new_role
    
    def update_role(self, id: int, role: Role) -> dict:
        update_role: Role = self.db.query(RoleModel).filter(RoleModel.id == id).first()
        if update_role is None:
            raise HTTPException(status_code=404, detail="Role not found")
        
        update_role.name = role.name
        self.db.commit()
        self.db.refresh(update_role)
        return update_role
    
    def delete_role(self, id: int) -> dict:
        element: Role = self.db.query(RoleModel).filter(RoleModel.id == id).first()
        if element is None:
            raise HTTPException(status_code=404, detail="Role not found")
        
        self.db.delete(element)
        self.db.commit()
        return element
