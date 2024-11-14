from typing import List
from fastapi import HTTPException
from src.schemas.comment import Comment
from src.models.comment import Comment as CommentModel

class CommentRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_Comments(self) -> List[Comment]:
        query = self.db.query(CommentModel)
        return query.all()

    def get_Comment(self, id: int ) -> Comment:
        element = self.db.query(CommentModel).filter(CommentModel.id == id).first()
        return element
    
    def create_Comment(self, Comment: Comment) -> dict:
        new_Comment = CommentModel(**Comment.model_dump())
        self.db.add(new_Comment)
        self.db.commit()
        self.db.refresh(new_Comment)
        return new_Comment
    
    def update_Comment(self, id:str, comment:Comment)-> dict:
        UpdateComment: Comment= self.db.query(CommentModel).filter(CommentModel.id == id).first()  
        if UpdateComment is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        UpdateComment.date = comment.date
        UpdateComment.content = comment.content
        UpdateComment.vehicle_id = comment.vehicle_id
        UpdateComment.user_id = comment.user_id
        UpdateComment.likes = comment.likes
        UpdateComment.dislikes = comment.dislikes

        self.db.commit()
        self.db.refresh(UpdateComment)
        return UpdateComment
    
    def delete_Comment(self, id: int) -> dict:
        element: Comment = self.db.query(CommentModel).filter(CommentModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element  







