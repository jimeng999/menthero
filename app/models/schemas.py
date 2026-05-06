"""
朋友圈文案侠 - 数据模型
"""

from pydantic import BaseModel, Field
from typing import List, Optional


class GenerateRequest(BaseModel):
    """生成文案请求"""
    scene: str = Field(..., description="场景类型: food/travel/fitness/pet/work/party/daily/love")
    style: str = Field(..., description="风格类型: literary/humor/cold/warm/vaush/poet")
    keyword: str = Field(default="", description="自定义关键词")
    count: int = Field(default=3, ge=1, le=5, description="生成数量1-5")
    user_id: Optional[str] = Field(default=None, description="用户ID")
    is_pro: bool = Field(default=False, description="是否为Pro用户")


class MomentItem(BaseModel):
    """单条文案"""
    content: str = Field(..., description="主文案")
    emojis: List[str] = Field(..., description="推荐emoji组合")
    self_deprecating_reply: str = Field(..., description="自嘲回复")
    location_text: str = Field(..., description="定位文案")
    tips: str = Field(..., description="配图建议")


class GenerateResponse(BaseModel):
    """生成文案响应"""
    success: bool
    message: str
    results: List[MomentItem]
    usage: dict


class SceneItem(BaseModel):
    """场景项"""
    id: str
    name: str
    keywords: List[str]


class StyleItem(BaseModel):
    """风格项"""
    id: str
    name: str


class MetaResponse(BaseModel):
    """元数据响应"""
    success: bool
    scenes: List[SceneItem]
    styles: List[StyleItem]


class UpgradeRequest(BaseModel):
    """升级请求"""
    user_id: str
    plan: str = Field(default="pro", description="升级方案")


class UpgradeResponse(BaseModel):
    """升级响应"""
    success: bool
    message: str
    checkout_url: Optional[str] = None
