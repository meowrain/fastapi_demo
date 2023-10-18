import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
import random

app = FastAPI()

# 获取images文件夹中的所有图像文件的文件名
image_folder = "images"
image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

@app.get("/random_image/")
async def get_random_image():
    if not image_files:
        return "No images found in the folder."

    # 随机选择一个图像文件
    random_image_file = random.choice(image_files)
    
    # 构建图像文件的完整路径
    image_path = os.path.join(image_folder, random_image_file)
    
    # 返回所选图像文件
    return FileResponse(image_path, media_type="image/jpeg")  # 请根据实际文件格式更改"image/jpeg"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
