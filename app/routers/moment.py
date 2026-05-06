"""
朋友圈文案侠 - 文案生成路由
"""

from fastapi import APIRouter, HTTPException
from app.models.schemas import (
    GenerateRequest, 
    GenerateResponse, 
    MomentItem,
    MetaResponse,
    SceneItem,
    StyleItem
)
from app.services.generator import generator
from app.services.billing import billing

router = APIRouter(prefix="/api", tags=["朋友圈文案"])


@router.get("/meta", response_model=MetaResponse)
async def get_meta():
    """获取所有场景和风格元数据"""
    scenes = [
        SceneItem(id=s["id"], name=s["name"], keywords=s["keywords"])
        for s in generator.get_scenes()
    ]
    styles = [
        StyleItem(id=s["id"], name=s["name"])
        for s in generator.get_styles()
    ]
    return MetaResponse(success=True, scenes=scenes, styles=styles)


@router.post("/generate", response_model=GenerateResponse)
async def generate_moment(request: GenerateRequest):
    """生成朋友圈文案"""
    # 检查配额
    usage_check = billing.check_and_increment(
        user_id=request.user_id,
        is_pro=request.is_pro
    )
    
    if not usage_check["allowed"]:
        return GenerateResponse(
            success=False,
            message=usage_check["message"],
            results=[],
            usage=usage_check
        )
    
    # 生成文案
    try:
        results = generator.generate(
            scene=request.scene,
            style=request.style,
            custom_keyword=request.keyword,
            count=request.count
        )
        
        items = [
            MomentItem(
                content=r.content,
                emojis=r.emojis,
                self_deprecating_reply=r.self_deprecating_reply,
                location_text=r.location_text,
                tips=r.tips
            )
            for r in results
        ]
        
        return GenerateResponse(
            success=True,
            message=usage_check["message"],
            results=items,
            usage=usage_check
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"生成失败: {str(e)}")


@router.get("/usage")
async def get_usage(user_id: str = None, is_pro: bool = False):
    """获取使用量信息"""
    return billing.get_usage_info(user_id, is_pro)
