from sqlmodel import create_engine,SQLModel,Session,select
from . import models
Blog = models.Blog
DB_FILE = 'demo.db'
sql_url = f"sqlite:///{DB_FILE}"
engine = create_engine(sql_url)
def create_tables():
    SQLModel.metadata.create_all(engine)
def add_blog(blog):
    with Session(engine) as session:
        session.add(blog)
        session.commit()
def get_blog(id:int):
    with Session(engine) as session:
        statement = select(Blog).where(Blog.id == id)
        blog = session.exec(statement).first()
        return blog
    
def create_user(user):
    with Session(engine) as session:
        session.add(user)
        session.commit() 