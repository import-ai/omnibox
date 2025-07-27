# OmniBox - 小黑

[![omnibox-web](https://img.shields.io/github/v/release/import-ai/omnibox-web?color=brightgreen&label=Web&sort=semver)](https://github.com/import-ai/omnibox-web/releases)
[![omnibox-backend](https://img.shields.io/github/v/release/import-ai/omnibox-backend?color=blue&label=Backend&sort=semver)](https://github.com/import-ai/omnibox-backend/releases)
[![omnibox-wizard](https://img.shields.io/github/v/release/import-ai/omnibox-wizard?color=orange&label=Wizard&sort=semver)](https://github.com/import-ai/omnibox-wizard/releases)
[![omnibox-browser-extension](https://img.shields.io/github/v/release/import-ai/omnibox-browser-extension?color=yellow&label=Browser%20Extension&sort=semver)](https://github.com/import-ai/omnibox-browser-extension/releases)

## Introduction

OmniBox (小黑) is a simple, cross-platform, all-in-one AI knowledge hub. All you need to do is collect, then ask.

### Core Features

1. Save the main content of a webpage to OmniBox via the browser extension.
2. Upload and end-to-end parsing & indexing for files in formats like PDF, Word, PPT, MP3, etc.
3. Markdown editing and rendering (formulas, mind maps, flowcharts, sequence diagrams, Gantt charts, music notation, etc.)
4. Q&A and writing based on both Internet and local databases.
5. User and team system, permissions, sharing management, multi-tenancy, multi-language, dark mode, mobile responsiveness, and more.

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
</details>

## Quick Start

Welcome to our online service: [omnibox.pro](https://www.omnibox.pro), supporting email registration and WeChat login.

### Browser Extension

[![Chrome Web Store Version](https://img.shields.io/chrome-web-store/v/gckiocdfdaofgabchobljcdimjieookl?label=Google%20Chrome&color=yellow)](https://chromewebstore.google.com/detail/save-to-omnibox/gckiocdfdaofgabchobljcdimjieookl)
[![Mozilla Add-on Version](https://img.shields.io/amo/v/save-to-omnibox?label=Mozilla%20Firefox&color=%23f72f54)
](https://addons.mozilla.org/en-US/firefox/addon/save-to-omnibox/)

### Deployment

```shell
git clone https://github.com/import-ai/omnibox.git
cd omnibox
cp example.env .env
bash scripts/compose.yaml up -d
```

### Local Development

```shell
git clone --recurse-submodules https://github.com/import-ai/omnibox.git
cd omnibox
cp example.env .env
bash scripts/dev.yaml up -d --build
```

## TODO

1. RSS subscription
2. Agent, folder, and document public sharing
3. WeChat Mini Program
4. Increase writing length limit (currently can write up to 5000 words)
5. API
