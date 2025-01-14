# Magic Box

**This project is in a very early stages of development. Many features and documentation are missing, and it is not ready for production use.**

## Overview

Magic Box is designed as a second brain that you can put everything in, and get everything out. It aims to be a comprehensive tool for managing and retrieving information efficiently. Whether it's notes, documents, or any other type of data, Magic Box helps you organize and access it with ease.

## Features

- **Data Storage**: Store various types of data securely.
- **Search**: Powerful search capabilities to find information quickly.
- **API Integration**: Integrate with other services using APIs.
- **User-Friendly Interface**: Easy-to-use interface for managing your data.
- **Extensibility**: Extend functionality with plugins and extensions.

## Getting Started

To get started with Magic Box, follow the deployment instructions below and set up the browser plugin for an enhanced experience.

## Deployment

1. Download the [compose.yaml](./compose.yaml) file.  
2. Download the [.env.example](./.env.example) file, rename it to `.env`, and configure it with your OpenAI-compatible API key.  
3. Run `docker compose up -d`.  
4. Open your browser and go to [localhost:8000#/test](http://localhost:8000#/test).  

```shell
wget -O 'compose.yaml' 'https://raw.githubusercontent.com/import-ai/magic-box/refs/heads/main/compose.yaml'
wget -O '.env' 'https://raw.githubusercontent.com/import-ai/magic-box/refs/heads/main/.env.example'
docker compose up -d
```

## Browser Plugin

1. Clone [github.com/import-ai/magic-box-client-chrome](https://github.com/import-ai/magic-box-client-chrome.git).
2. Open Chrome, go to `chrome://extensions/`, enable "Developer mode" in the top right corner.
3. Click "Load unpacked" and select the cloned repository folder.
4. The extension should now be loaded and ready to use.
5. Right-click the extension icon in the toolbar, select "Options", and configure the settings as needed.

| Key | Value for demo |
| --- | --- |
| API Base URL | `http://localhost:8000` |
| API Key | `null` |
| Namespace | `test` |
| Space Type | `private` |

## Roadmap

- **Mobile Support**: Post from iOS and Android devices.
- **File Type Support**: Handle various file types including PDF, DOCX, PPT, XLSX, etc.
- **RSS Support**: Integrate and manage RSS feeds.
- **Feed Support**: Support for various types of feeds for content aggregation.
- **Collaboration Tools**: Enable real-time collaboration on documents and data.
- **Advanced Analytics**: Provide insights and analytics on stored data.
- **AI Integration**: Leverage AI for smarter data organization and retrieval.
- **Security Enhancements**: Implement advanced security features to protect user data.
- **Cross-Platform Sync**: Ensure seamless data synchronization across multiple devices and platforms.
- **Customizable Dashboards**: Allow users to create and customize their own dashboards for better data visualization.
- **Automated Backups**: Implement automated backup solutions to prevent data loss.
- **Localization**: Support multiple languages for a global user base.
- **User Permissions**: Fine-grained user permissions and access control.
- **Notification System**: Implement a notification system for updates and alerts.
