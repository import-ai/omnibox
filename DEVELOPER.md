# DEVELOPER.md

This file provides guidance to developer when working with code in this repository.

## Project Overview

OmniBox is an AI-powered knowledge management platform. This is the monorepo containing four git submodules:

- **backend/** - NestJS REST API (TypeScript, PostgreSQL, TypeORM)
- **web/** - React 18 frontend (TypeScript, Vite, Tailwind CSS)
- **wizard/** - Python AI/ML service (FastAPI, LangChain, Meilisearch)
- **client/browser-extension/** - Browser extension for web clipping

## Development Commands

### Full Stack (Docker Compose)

```bash
# Start all services with dependencies (PostgreSQL, MinIO, Meilisearch, Kafka, etc.)
cp example.env .env
bash scripts/dev.sh up -d --build

# View logs
bash scripts/dev.sh logs -f

# Stop all services
bash scripts/dev.sh down
```

### Backend (NestJS)

```bash
cd backend
pnpm install
pnpm run dev              # Watch mode
pnpm run test:e2e         # E2E tests (uses testcontainers)
pnpm run lint:fix         # Lint and format
```

### Web (React/Vite)

```bash
cd web
pnpm install
pnpm dev                  # Dev server
pnpm build                # Production build
pnpm lint:fix             # Lint and format
```

### Wizard (Python/FastAPI)

```bash
cd wizard
poetry install
poetry run uvicorn main:app --reload --port 8001    # Dev server
poetry run pytest                                    # Tests
poetry run ruff check --fix .                        # Lint
```

## Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│    Web      │────▶│   Backend   │────▶│   Wizard    │
│  (React)    │     │  (NestJS)   │     │  (FastAPI)  │
└─────────────┘     └──────┬──────┘     └──────┬──────┘
                           │                   │
                    ┌──────┴──────┐     ┌──────┴──────┐
                    │ PostgreSQL  │     │ Meilisearch │
                    │ MinIO (S3)  │     │   (Vector)  │
                    │    Redis    │     └─────────────┘
                    │    Kafka    │
                    └─────────────┘
```

- **Web** proxies API requests to **Backend** via Nginx (`/api/v1`)
- **Backend** orchestrates business logic, auth, file storage (MinIO), and calls **Wizard** for AI tasks
- **Wizard** handles document processing, embeddings, LLM interactions, and vector search (Meilisearch)
- **Kafka** provides event streaming between Backend and Wizard worker

## Key Ports (Local Development)

| Service      | Port  |
|--------------|-------|
| Web          | 8080  |
| Backend API  | 8000  |
| Wizard API   | 8001  |
| PostgreSQL   | 5432  |
| MinIO        | 9000  |
| Meilisearch  | 7700  |
| Kafka        | 9092  |
| MailHog UI   | 8025  |

## Environment Variables

Key prefixes:
- `OBB_` - Backend config (PostgreSQL, JWT, S3, etc.)
- `OBW_` - Wizard config (AI models, embedding, Kafka, etc.)
- `GLOBAL_` - Shared across services (e.g., Meilisearch key)

See `example.env` for all available options. Copy to `.env` before running.

## Submodule-Specific Documentation

Each submodule has its own DEVELOPER.md with detailed architecture and patterns:
- `backend/DEVELOPER.md` - NestJS modules, auth system, migrations, testing patterns
- `web/DEVELOPER.md` - React component patterns, event-driven state, API layer

## Git Commit Guidelines

**Format**: `type(scope): Description`

**Types**: feat, fix, docs, style, refactor, perf, test, chore, revert, build

**Rules**:
- Scope is required (e.g., `auth`, `sidebar`, `wizard`)
- Sentence case with capital first letter
- Present tense action verbs (Add, Fix, Support, Update)
- No period at end

**Examples**:
```
feat(auth): Support Apple signin
fix(resources): Fix tree ordering on drag-drop
chore(compose): Update service dependencies
```

**Do NOT include**:
- "Generated with Claude Code" or similar attribution
- "Co-Authored-By: Claude" or any Claude co-author tags
