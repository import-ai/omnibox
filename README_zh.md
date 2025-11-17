# 小黑 - OmniBox

[![omnibox-web](https://img.shields.io/github/v/release/import-ai/omnibox-web?color=brightgreen&label=Web&sort=semver)](https://github.com/import-ai/omnibox-web/releases)
[![omnibox-backend](https://img.shields.io/github/v/release/import-ai/omnibox-backend?color=blue&label=Backend&sort=semver)](https://github.com/import-ai/omnibox-backend/releases)
[![omnibox-wizard](https://img.shields.io/github/v/release/import-ai/omnibox-wizard?color=orange&label=Wizard&sort=semver)](https://github.com/import-ai/omnibox-wizard/releases)
[![omnibox-browser-extension](https://img.shields.io/github/v/release/import-ai/omnibox-browser-extension?color=yellow&label=Browser%20Extension&sort=semver)](https://github.com/import-ai/omnibox-browser-extension/releases)

[English](./README.md) | 简体中文

<img width="923" height="620" alt="Image" src="https://github.com/user-attachments/assets/35dad1b4-5652-4f2f-8eac-38c49da0545f" />

## 文档

[小黑帮助文档](https://www.omnibox.pro/docs/zh-cn/?utm_source=gh_readme_zh)

## 简介

> “小黑”取自《爱情公寓》中的“楼下小黑”

小黑（OmniBox）是一个简单、跨平台 All in One 的 AI 知识中枢，收集、整理、应用、分享，一应俱全。

### 核心特性

1. 通过浏览器插件将网页正文保存至小黑
2. PDF、Word、PPT、MP3 等格式的文件上传与端到端解析、索引
3. Markdown 编辑、渲染（公式、脑图、流程图、时序图、甘特图、五线谱等）
4. 基于互联网和本地的数据库进行问答、写作
5. **闪记**：iOS 端快速记录灵感，支持语音录制和文字笔记
6. **分享**：iOS 端无缝分享文件至小黑
7. **微信助手**：在微信中随时随地将文件、网页、视频、语音、文字、聊天记录保存至小黑
8. 用户、团队系统、权限、分享管理、多租户、多语言、暗色模式、移动端自适应等

## 快速开始

欢迎使用我们的在线服务：[omnibox.pro](https://www.omnibox.pro/?utm_source=gh_readme_zh)，支持邮箱注册以及谷歌、微信登录。

### 浏览器插件

[浏览器插件安装 | 小黑帮助文档](https://www.omnibox.pro/docs/zh-cn/browser-extension?utm_source=gh_readme_zh)

### 部署

[本地部署](https://www.omnibox.pro/docs/zh-cn/deploy?utm_source=gh_readme_zh)

### 本地开发

```shell
git clone --recurse-submodules https://github.com/import-ai/omnibox.git
cd omnibox
cp example.env .env
bash scripts/dev.sh up -d --build
```

## 迭代计划

- [x] Agent、文件夹、文档公开分享
- [x] 微信助手
- [x] Open API
- [ ] 微信小程序
- [ ] 订阅

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=import-ai/omnibox&type=date&legend=top-left)](https://www.star-history.com/#import-ai/omnibox&type=date&legend=top-left)
