# USAGE — openbb-astock-clone

> 本文档为占位骨架版。功能完成(T5)后将补充: 部署、回滚、扩缩容、常见问题(含 "OpenBB 挂了怎么办")、5 张功能截图链接。

## 快速开始

### 前置条件

- Docker ≥ 24.0
- Docker Compose v2
- 本地可达的 OpenBB Platform API(默认 `http://192.168.1.12:6900`)

### 部署

```bash
# 1. 克隆仓库
git clone https://github.com/bs5189-web/openbb-astock-clone.git
cd openbb-astock-clone

# 2. 配置环境变量
cp .env.example .env
# 按需修改 OPENBB_API_URL

# 3. 启动
docker compose up -d

# 4. 访问
open http://localhost:8501
```

### 端口

默认监听 `8501`(Streamlit 默认端口)。可通过 `STREAMLIT_PORT` 环境变量修改。

## 环境变量

| 变量 | 必填 | 默认 | 说明 |
|---|---|---|---|
| `OPENBB_API_URL` | 是 | `http://192.168.1.12:6900` | OpenBB Platform API 地址 |
| `STREAMLIT_PORT` | 否 | `8501` | Streamlit 监听端口 |

## 后续补充

- [ ] 回滚流程
- [ ] 扩缩容建议
- [ ] 常见问题(FAQ)
- [ ] "OpenBB 挂了怎么办" 应急流程
- [ ] 5 张功能截图(首页/看板/回测/组合/股票查询)
