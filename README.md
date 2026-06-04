# openbb-astock-clone

> A 股智能投研平台复刻 — Streamlit 多页应用,数据源为本地 OpenBB Platform API。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 项目简介

复刻目标站点: <https://openbb.astock.com.cn/>。

技术栈:

- **前端**: Streamlit 多页应用
- **数据源**: 本地部署的 OpenBB Platform API (`http://192.168.1.12:6900`)
- **部署**: Docker 单容器

## 页面

1. 首页
2. 行情看板
3. 动量回测
4. 投资组合
5. 股票查询

## 快速开始

参见 [USAGE.md](./USAGE.md)。

```bash
git clone https://github.com/bs5189-web/openbb-astock-clone.git
cd openbb-astock-clone
cp .env.example .env
docker compose up -d
```

打开浏览器访问 <http://localhost:8501>。

## 文档

- [USAGE.md](./USAGE.md) — 部署/运维/常见问题
- 详细方案见父任务 [V-81 复刻 astock 网站方案计划](https://github.com/bs5189-web)

## 协议

MIT License。详见 [LICENSE](./LICENSE)。
