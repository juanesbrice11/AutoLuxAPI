from typing import List
from fastapi import HTTPException
from src.schemas.article import Article
from src.models.article import Article as ArticleModel

class ArticleRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_Articles(self) -> List[Article]:
        query = self.db.query(ArticleModel)
        return query.all()

    def get_Article(self, id: int ) -> Article:
        element = self.db.query(ArticleModel).filter(ArticleModel.id == id).first()
        return element
    
    def create_Article(self, Article: Article) -> dict:
        new_Article = ArticleModel(**Article.model_dump())
        self.db.add(new_Article)
        self.db.commit()
        self.db.refresh(new_Article)
        return new_Article
    
    def update_Article(self, id:str, article:Article)-> dict:
        UpdateArticle: Article= self.db.query(ArticleModel).filter(ArticleModel.id == id).first()  
        if UpdateArticle is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        UpdateArticle.title = article.title
        UpdateArticle.update_date = article.update_date
        UpdateArticle.content = article.content
        UpdateArticle.date = article.date
        UpdateArticle.vehicle_id = article.vehicle_id

        self.db.commit()
        self.db.refresh(UpdateArticle)
        return UpdateArticle
    
    def delete_Article(self, id: int) -> dict:
        element: Article = self.db.query(ArticleModel).filter(ArticleModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element  