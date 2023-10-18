from sqlmodel import Field, SQLModel
from typing import Optional
class Blog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True,index=True)
    title: str
    body: Optional[str] = None
    