from fastapi import APIRouter,status,Query
from databases.models import Blog
from databases.sqllite import create_tables,add_blog,get_blog,del_blog

from schemas import blog_schema
router = APIRouter(
    prefix='/blog',
    tags=["blog"]
)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:blog_schema.Blog):
    create_tables()
    blog = Blog(title=f"{request.title}",body=f"{request.body}")
    add_blog(blog)
    response_data = {
        "query": "OK",
        **request.dict()  # 解构原始请求数据
    }
    return response_data

@router.get('/{id}',status_code=status.HTTP_200_OK)
def get_content(id:int):
    response = {
        "query": "OK",
        "content": get_blog(id)
    }
    return response

@router.delete('/')
def delete_content(id: int = Query(default=...,description="要删除的博客的id")):
    result = del_blog(id)  # 调用删除博客的函数
    if result == 'OK':
        return {
            "query": "OK",
            "content": "deleted the blog"
        }
    else:
        return {
            "query": "Failed",
            "content": "Failed to delete the blog"
        }
    