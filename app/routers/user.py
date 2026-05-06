"""
朋友圈文案侠 - 用户相关路由
"""

from fastapi import APIRouter
from app.models.schemas import UpgradeRequest, UpgradeResponse
from app.services.billing import billing

router = APIRouter(prefix="/api/user", tags=["用户"])


@router.post("/upgrade", response_model=UpgradeResponse)
async def upgrade_pro(request: UpgradeRequest):
    """升级Pro版"""
    result = billing.upgrade_to_pro(request.user_id)
    
    return UpgradeResponse(
        success=result["success"],
        message=result["message"],
        checkout_url=None  # 实际应返回支付链接
    )


@router.get("/quota")
async def check_quota(user_id: str = None, is_pro: bool = False):
    """检查用户配额"""
    info = billing.get_usage_info(user_id, is_pro)
    
    if info["is_pro"]:
        quota_info = "Pro用户，无限制"
    else:
        quota_info = f"免费版: {info['used']}/{info['limit']}，剩余 {info['remaining']} 次"
    
    return {
        "quota": quota_info,
        "detail": info
    }
