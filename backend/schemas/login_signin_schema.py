from pydantic import BaseModel

class Login(BaseModel):
    username: str
    password: str

class Signin(BaseModel):
    username: str
    password: str