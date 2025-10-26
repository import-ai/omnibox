# OmniBox - 小黑

[![omnibox-web](https://img.shields.io/github/v/release/import-ai/omnibox-web?color=brightgreen&label=Web&sort=semver)](https://github.com/import-ai/omnibox-web/releases)
[![omnibox-backend](https://img.shields.io/github/v/release/import-ai/omnibox-backend?color=blue&label=Backend&sort=semver)](https://github.com/import-ai/omnibox-backend/releases)
[![omnibox-wizard](https://img.shields.io/github/v/release/import-ai/omnibox-wizard?color=orange&label=Wizard&sort=semver)](https://github.com/import-ai/omnibox-wizard/releases)
[![omnibox-browser-extension](https://img.shields.io/github/v/release/import-ai/omnibox-browser-extension?color=yellow&label=Browser%20Extension&sort=semver)](https://github.com/import-ai/omnibox-browser-extension/releases)

English | [简体中文](./README_zh.md)

## Docs

[OmniBox Docs](https://www.omnibox.pro/docs/?utm_source=gh_readme_en)

## Introduction

OmniBox (小黑) is a simple, cross-platform, all-in-one AI knowledge hub. All you need to do is collect, then ask.

### Core Features

1. Save the main content of a webpage to OmniBox via the browser extension.
2. Upload and end-to-end parsing & indexing for files in formats like PDF, Word, PPT, MP3, etc.
3. Markdown editing and rendering (formulas, mind maps, flowcharts, sequence diagrams, Gantt charts, music notation, etc.)
4. Q&A and writing based on both Internet and local databases.
5. **Flash**: Quick capture of fleeting ideas on iOS with support for voice recordings and text notes.
6. **Share**: Seamless file sharing to OmniBox directly from iOS.
7. **WeChat Bot**: Save files, webpages, videos, voice messages, text, and chat records to OmniBox anytime, anywhere via WeChat.
8. User and team system, permissions, sharing management, multi-tenancy, multi-language, dark mode, mobile responsiveness, and more.

### Screenshots

<details>
<table>
<tr>
<th>Feature</th>
<th>Source</th>
<th>Parsing Result</th>
</tr>
<tr>
<td>Save Webpage to OmniBox</td>
<td><img src="assets/screenshots/extension/SCR-20250727-uniy.png" alt="Source web"></td>
<td><img src="assets/screenshots/extension/SCR-20250727-srzd.png" alt="Extension parsing result"></td>
</tr>
<tr>
<td rowspan="2">File Parsing</td>
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
<th>Feature</th>
<th>Screenshot</th>
</tr>
<tr>
<td>Q&A</td>
<td><img src="assets/screenshots/chat/SCR-20250727-uder.png"></td>
</tr>
<tr>
<td>Writing</td>
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

<table>
<tr>
<th>Feature</th>
<th>Demo Video</th>
</tr>
<tr>
<td>Flash - Voice Recording</td>
<td><video src="https://github.com/user-attachments/assets/7d7c1089-5f7d-4575-b3cc-a2ee5effb3db" width="300"></video></td>
</tr>
<tr>
<td>Flash - Text Note</td>
<td><video src="https://github.com/user-attachments/assets/b31c6bbd-78b3-4808-8370-a93e16ff6ddd" width="300"></video></td>
</tr>
<tr>
<td>Share Files to OmniBox</td>
<td><video src="https://github.com/user-attachments/assets/0000f920-4028-4d3d-8024-e4fbfb78a77f" width="300"></video></td>
</tr>
</table>
</details>

## Quick Start

Welcome to our online service: [omnibox.pro](https://www.omnibox.pro/?utm_source=gh_readme_en), supporting login via Email, Google and WeChat.

### Browser Extension

[Browser Extension Installation | OmniBox Docs](https://www.omnibox.pro/docs/collect/browser-extension)

### Deployment

```shell
GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/import-ai/omnibox.git
cd omnibox
cp example.env .env
bash scripts/compose.sh up -d
```

### Local Development

```shell
git clone --recurse-submodules https://github.com/import-ai/omnibox.git
cd omnibox
cp example.env .env
bash scripts/dev.sh up -d --build
```

## Roadmap

- [x] Agent, folder, and document public sharing
- [x] WeChat Bot
- [x] Open API
- [ ] WeChat Mini Program
- [ ] RSS Subscription
