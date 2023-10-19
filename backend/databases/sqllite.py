from sqlmodel import create_engine,SQLModel,Session,select
from . import models
Blog = models.Blog
Users = models.Users
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
def del_blog(id:int):
    with Session(engine) as session:
        statement = select(Blog).where(Blog.id == id)
        blog = session.exec(statement).first()
        if blog is not None:
            session.delete(blog)
            session.commit()
            statement = select(Blog).where(Blog.id == id)
            check_blog = session.exec(statement).first()
            if check_blog is None:
                return 'OK'
            else:
                return 'Failed'
        else:
            return 'Failed'
def create_user(user):
    with Session(engine) as session:
        session.add(user)
        session.commit() 
def get_user(user):
    with Session(engine) as session:
        statement = select(Users).where(Users.username == user.username)
        user = session.exec(statement).first()
        if user is not None:
            return 'OK'