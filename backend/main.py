from fastapi import FastAPI,status
from databases.sqllite import create_tables,add_blog,get_blog
from databases.models import Blog
from schemas import blog_schema
import uvicorn

app = FastAPI()

@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create(request:blog_schema.Blog):
    create_tables()
    blog = Blog(title=f"{request.title}",body=f"{request.body}")
    add_blog(blog)
    response_data = {
        "query": "OK",
        **request.dict()  # 解构原始请求数据
    }
    return response_data

@app.get('/blog',status_code=status.HTTP_200_OK)
def get_content(id:int):
    response = {
        "query": "OK",
        "content": get_blog(id)
    }
    return response
    
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)