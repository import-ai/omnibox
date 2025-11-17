# OmniBox - 小黑

[![omnibox-web](https://img.shields.io/github/v/release/import-ai/omnibox-web?color=brightgreen&label=Web&sort=semver)](https://github.com/import-ai/omnibox-web/releases)
[![omnibox-backend](https://img.shields.io/github/v/release/import-ai/omnibox-backend?color=blue&label=Backend&sort=semver)](https://github.com/import-ai/omnibox-backend/releases)
[![omnibox-wizard](https://img.shields.io/github/v/release/import-ai/omnibox-wizard?color=orange&label=Wizard&sort=semver)](https://github.com/import-ai/omnibox-wizard/releases)
[![omnibox-browser-extension](https://img.shields.io/github/v/release/import-ai/omnibox-browser-extension?color=yellow&label=Browser%20Extension&sort=semver)](https://github.com/import-ai/omnibox-browser-extension/releases)

English | [简体中文](./README_zh.md)

<img width="923" height="620" alt="Image" src="https://github.com/user-attachments/assets/35dad1b4-5652-4f2f-8eac-38c49da0545f" />

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

## Quick Start

Welcome to our online service: [omnibox.pro](https://www.omnibox.pro/?utm_source=gh_readme_en), supporting login via Email, Google and WeChat.

### Browser Extension

[Browser Extension Installation | OmniBox Docs](https://www.omnibox.pro/docs/browser-extension?utm_source=gh_readme_en)

### Deployment

[Local Deployment](https://www.omnibox.pro/docs/deploy?utm_source=gh_readme_en)

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

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=import-ai/omnibox&type=date&legend=top-left)](https://www.star-history.com/#import-ai/omnibox&type=date&legend=top-left)
