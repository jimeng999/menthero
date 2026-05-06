"""
朋友圈文案侠 - 计费服务
免费5次/月，Pro版¥19/月
"""

from datetime import datetime, timedelta
from typing import Optional
import hashlib


class BillingService:
    """计费服务 - 简化版BYOK模式"""
    
    # 免费配额
    FREE_LIMIT = 5
    
    def __init__(self):
        # 简化存储 - 实际生产环境应使用数据库
        self.usage_cache = {}  # {user_id: {"count": int, "reset_date": str}}
    
    def _get_user_key(self, user_id: Optional[str]) -> str:
        """生成用户唯一标识"""
        if not user_id:
            return "anonymous"
        return hashlib.md5(user_id.encode()).hexdigest()[:16]
    
    def _should_reset(self, user_key: str) -> bool:
        """检查是否需要重置配额（每月重置）"""
        if user_key not in self.usage_cache:
            return True
        
        last_reset = self.usage_cache[user_key].get("reset_date", "")
        now = datetime.now()
        
        # 检查是否是同一个月
        if last_reset:
            try:
                reset_date = datetime.strptime(last_reset, "%Y-%m")
                if reset_date.year == now.year and reset_date.month == now.month:
                    return False
            except:
                pass
        return True
    
    def _reset_usage(self, user_key: str):
        """重置使用量"""
        now = datetime.now()
        self.usage_cache[user_key] = {
            "count": 0,
            "reset_date": now.strftime("%Y-%m")
        }
    
    def check_and_increment(self, user_id: Optional[str], is_pro: bool = False) -> dict:
        """
        检查配额并增加使用次数
        
        Returns:
            {
                "allowed": bool,
                "remaining": int,
                "is_pro": bool,
                "message": str
            }
        """
        user_key = self._get_user_key(user_id)
        
        # Pro用户不受限制
        if is_pro:
            return {
                "allowed": True,
                "remaining": -1,  # -1表示无限制
                "is_pro": True,
                "message": "Pro用户畅享无限创意"
            }
        
        # 检查是否需要重置
        if self._should_reset(user_key):
            self._reset_usage(user_key)
        
        # 获取当前使用量
        current = self.usage_cache.get(user_key, {"count": 0})["count"]
        
        # 检查配额
        if current >= self.FREE_LIMIT:
            return {
                "allowed": False,
                "remaining": 0,
                "is_pro": False,
                "message": f"本月免费次数已用完({self.FREE_LIMIT}/{self.FREE_LIMIT})，升级Pro解锁无限创意"
            }
        
        # 增加使用次数
        self.usage_cache[user_key]["count"] = current + 1
        remaining = self.FREE_LIMIT - self.usage_cache[user_key]["count"]
        
        return {
            "allowed": True,
            "remaining": remaining,
            "is_pro": False,
            "message": f"已使用{self.usage_cache[user_key]['count']}次，剩余{remaining}次免费额度"
        }
    
    def get_usage_info(self, user_id: Optional[str], is_pro: bool = False) -> dict:
        """获取使用信息"""
        user_key = self._get_user_key(user_id)
        
        if is_pro:
            return {
                "used": 0,
                "limit": -1,
                "remaining": -1,
                "is_pro": True
            }
        
        if self._should_reset(user_key):
            self._reset_usage(user_key)
        
        current = self.usage_cache.get(user_key, {"count": 0})["count"]
        
        return {
            "used": current,
            "limit": self.FREE_LIMIT,
            "remaining": self.FREE_LIMIT - current,
            "is_pro": False
        }
    
    def upgrade_to_pro(self, user_id: str) -> dict:
        """升级到Pro版"""
        user_key = self._get_user_key(user_id)
        # 实际生产环境应调用支付接口
        return {
            "success": True,
            "message": "Pro升级功能开发中，敬请期待！"
        }


# 全局实例
billing = BillingService()
