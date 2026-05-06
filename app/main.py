"""
朋友圈文案侠 - FastAPI应用入口
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.routers import moment, user

app = FastAPI(
    title="朋友圈文案侠 API",
    description="AI朋友圈文案生成器 - 拍照配文不求人",
    version="1.0.0"
)

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(moment.router)
app.include_router(user.router)


@app.get("/")
async def root():
    """健康检查"""
    return {
        "name": "朋友圈文案侠 API",
        "status": "running",
        "version": "1.0.0"
    }


@app.get("/health")
async def health():
    """健康检查"""
    return {"status": "ok"}
