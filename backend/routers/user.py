from fastapi import APIRouter,status
from databases.sqllite import create_tables,create_user

from databases.models import Users
from schemas import login_signin_schema

router = APIRouter()

@router.post('/login',status_code=status.HTTP_200_OK,tags=["users"])
def login(request: login_signin_schema.Login):
    username = request.username
    password = request.password
    pass

@router.post('/signin',status_code=status.HTTP_201_CREATED,tags=["users"])
def signin(request: login_signin_schema.Signin):
    create_tables()
    user = Users(username=f"{request.username}",password=f"{request.password}")
    create_user(user)
    response_data = {
        "query": "OK",
        **request.dict()
    }
    return response_data

