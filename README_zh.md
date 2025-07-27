# OmniBox - 小黑

[![omnibox-web](https://img.shields.io/github/v/release/import-ai/omnibox-web?color=brightgreen&label=Web&sort=semver)](https://github.com/import-ai/omnibox-web/releases)
[![omnibox-backend](https://img.shields.io/github/v/release/import-ai/omnibox-backend?color=blue&label=Backend&sort=semver)](https://github.com/import-ai/omnibox-backend/releases)
[![omnibox-wizard](https://img.shields.io/github/v/release/import-ai/omnibox-wizard?color=orange&label=Wizard&sort=semver)](https://github.com/import-ai/omnibox-wizard/releases)
[![omnibox-browser-extension](https://img.shields.io/github/v/release/import-ai/omnibox-browser-extension?color=yellow&label=Browser%20Extension&sort=semver)](https://github.com/import-ai/omnibox-browser-extension/releases)

## 简介

> “小黑”取自《爱情公寓》中的“楼下小黑”

OmniBox（小黑）是一个简单、跨平台 All in One 的 AI 知识中枢，你需要做的只有收集，然后提问。

### 核心特性

1. 通过浏览器插件将网页正文保存至小黑
2. PDF、Word、PPT、MP3 等格式的文件上传与端到端解析、索引
3. Markdown 编辑、渲染（公式、脑图、流程图、时序图、甘特图、五线谱等）
4. 基于互联网和本地的数据库进行问答、写作
5. 用户、团队系统、权限、分享管理、多租户、多语言、暗色模式、移动端自适应等

### 截图

<details>
<table>
<tr>
<th>功能</th>
<th>源</th>
<th>解析结果</th>
</tr>
<tr>
<td>收藏网页</td>
<td><img src="assets/screenshots/extension/SCR-20250727-uniy.png" alt="Source web"></td>
<td><img src="assets/screenshots/extension/SCR-20250727-srzd.png" alt="Extension parsing result"></td>
</tr>
<tr>
<td rowspan="2">文件解析</td>
<td><a href="assets/example.mp3">example.mp3</a></td>
<td><img src="assets/screenshots/uploads/SCR-20250727-uakj.png"></td>
</tr>
<tr>
<td><img src="assets/screenshots/uploads/SCR-20250727-ujjl.png"></td>
<td><img src="assets/screenshots/uploads/SCR-20250727-uanf.png">
<img src="assets/screenshots/uploads/SCR-20250727-uaoi.png"></td>
</tr>
</table>

<table>
<tr>
<th>功能</th>
<th>截图</th>
</tr>
<tr>
<td>问答</td>
<td><img src="assets/screenshots/chat/SCR-20250727-uder.png"></td>
</tr>
<tr>
<td>写作</td>
<td><img src="assets/screenshots/chat/SCR-20250727-udta.png">
<img src="assets/screenshots/chat/SCR-20250727-uegk.png"></td>
</tr>
<tr>
<td>Markdown</td>
<td><img src="assets/screenshots/markdown/SCR-20250727-ssnr.png">
<img src="assets/screenshots/markdown/SCR-20250727-ssou.png">
<img src="assets/screenshots/markdown/SCR-20250727-sspn.png">
<img src="assets/screenshots/markdown/SCR-20250727-ssqi.png"></td>
</tr>
</table>
</details>

## 快速开始

欢迎使用我们的在线服务：[omnibox.pro](https://www.omnibox.pro)，支持邮箱注册以及微信登录。

### 浏览器插件

[![Chrome Web Store Version](https://img.shields.io/chrome-web-store/v/gckiocdfdaofgabchobljcdimjieookl?label=Google%20Chrome&color=yellow)](https://chromewebstore.google.com/detail/save-to-omnibox/gckiocdfdaofgabchobljcdimjieookl)
[![Mozilla Add-on Version](https://img.shields.io/amo/v/save-to-omnibox?label=Mozilla%20Firefox&color=%23f72f54)
](https://addons.mozilla.org/en-US/firefox/addon/save-to-omnibox/)

### 部署

```shell
git clone https://github.com/import-ai/omnibox.git
cd omnibox
cp example.env .env
bash scripts/compose.yaml up -d
```

### 本地开发

```shell
git clone --recurse-submodules https://github.com/import-ai/omnibox.git
cd omnibox
cp example.env .env
bash scripts/dev.yaml up -d --build
```

## 迭代计划

1. RSS 订阅
2. Agent、文件夹、文档公开分享
3. 微信小程序
4. 提升写作的长度上限（目前最多能写 5000 字）
5. API
