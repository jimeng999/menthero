# 朋友圈文案侠 ✨ (MomentHero)

> 拍照配文不求人，AI帮你写出让人点赞的朋友圈

## 🎯 产品定位

- **一句话**: 拍照配文不求人，AI帮你写出让人点赞的朋友圈
- **目标用户**: 所有用微信的人（10亿+用户池）
- **商业模式**: 免费5次/月 → Pro ¥19/月

## ✨ 功能特性

### 8种场景类型
- 🍜 美食打卡（餐厅/自己做的/路边摊）
- ✈️ 旅行出游（风景/城市/海边/爬山）
- 💪 健身运动（跑步/瑜伽/撸铁）
- 🐱 萌宠日常（猫/狗/其他）
- 💼 职场日常（加班/升职/摸鱼/吐槽）
- 🎉 聚会社交（生日/团建/老友）
- ☕ 日常心情（文艺/搞笑/丧/鸡汤）
- 💕 恋爱甜蜜（秀恩爱/纪念日）

### 6种风格选择
- 文艺清新（诗意的句子+留白）
- 搞笑幽默（段子手/自嘲）
- 高冷简约（一句话+emoji）
- 温暖治愈（鸡汤+正能量）
- 凡尔赛（低调炫耀）
- 朋友圈诗人（押韵/排比/对仗）

### 核心功能
- ✅ 48套专业文案模板（8场景×6风格）
- ✅ 智能emoji推荐组合
- ✅ 评论区自嘲回复（降低炫耀感）
- ✅ 定位文案建议
- ✅ 朋友圈预览效果
- ✅ 一键复制

## 🛠️ 技术栈

- **后端**: Python FastAPI
- **前端**: 单页HTML + CSS + JavaScript
- **部署**: Vercel Serverless

## 📁 项目结构

```
AI-MomentHero/
├── api/
│   ├── __init__.py
│   └── index.py          # Vercel Serverless入口
├── app/
│   ├── main.py           # FastAPI应用入口
│   ├── models/
│   │   └── schemas.py    # 数据模型
│   ├── routers/
│   │   ├── moment.py     # 文案生成路由
│   │   └── user.py       # 用户路由
│   └── services/
│       ├── generator.py  # 文案生成核心
│       └── billing.py    # 计费服务
├── static/
│   └── index.html        # 前端页面
├── vercel.json           # Vercel配置
├── requirements.txt      # Python依赖
└── README.md
```

## 🚀 快速开始

### 本地开发

```bash
# 克隆项目
git clone <repo-url>
cd AI-MomentHero

# 安装依赖
pip install -r requirements.txt

# 启动服务
uvicorn app.main:app --reload --port 3000

# 访问
open http://localhost:3000
```

### Vercel部署

```bash
# 安装Vercel CLI
npm i -g vercel

# 登录
vercel login

# 部署
vercel --prod
```

## 📡 API接口

### 获取元数据
```
GET /api/meta
```

### 生成文案
```
POST /api/generate
{
  "scene": "food",
  "style": "literary",
  "keyword": "",
  "count": 3,
  "user_id": "optional",
  "is_pro": false
}
```

### 获取使用量
```
GET /api/usage?user_id=xxx&is_pro=false
```

### 升级Pro
```
POST /api/user/upgrade
{
  "user_id": "xxx",
  "plan": "pro"
}
```

## 🎨 设计规范

### 配色方案
- 深色底: `#0a0a0b`
- 卡片背景: `#1a1a1c`
- 渐变起始: `#8b5cf6` (紫)
- 渐变中点: `#ec4899` (粉)
- 渐变终点: `#f59e0b` (金)

### 移动端适配
- 响应式布局（移动端优先）
- 触摸友好
- 适配刘海屏

## 📝 商业化

| 版本 | 价格 | 功能 |
|------|------|------|
| 免费版 | ¥0 | 5次/月 |
| Pro版 | ¥19/月 | 无限次 + 专属功能 |

## 🔮 未来规划

- [ ] DeepSeek API集成（BYOK模式）
- [ ] 配图建议功能
- [ ] 九宫格文案生成
- [ ] 节日专属模板
- [ ] 微信支付集成
- [ ] 用户历史记录

## 📄 License

MIT License
