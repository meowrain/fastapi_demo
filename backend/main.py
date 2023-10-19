from fastapi import FastAPI
import uvicorn
from middleware.cors import setCors
from routers import random_acg,blog,user

# app 实例
app = FastAPI()

# 设置跨域请求
setCors(app)

# Routers
app.include_router(random_acg.router)
app.include_router(blog.router)
app.include_router(user.router)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)