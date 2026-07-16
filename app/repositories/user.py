from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models.user import User
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository):

    def __init__(self, db:Session,):
        super().__init__(db,User)
    
    def get_by_email(self,email:str):
        statement = select(User).where(
            User.email == email
        )

        return self.db.scalar(statement=statement)
    
    def get_by_username(self, username:str):
        statement = select(User).where(
            User.username == username
        )

        return self.db.scalar(statement=statement)
    
    def get_by_email_or_username(
            self,
            email:str,
            username: str,
    ):
        statment = select(User).where(
            (User.email == email)
             | (User.username == username)
        )
        return self.db.scalar(statement=statment)
