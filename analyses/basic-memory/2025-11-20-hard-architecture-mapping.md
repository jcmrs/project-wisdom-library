# Hard Architecture Mapping: Basic Memory

**Investigation Date:** 2025-11-20  
**Subject:** https://github.com/basicmachines-co/basic-memory  
**Level:** 1 (Data & Reality)  
**Methodology:** Hard Architecture Mapping

---

## Executive Summary

Basic Memory is a **local-first knowledge management system** that implements a bidirectional bridge between **Markdown files** (human-editable) and a **knowledge graph** (AI-traversable) via the **Model Context Protocol (MCP)**. It represents a fundamental architectural pattern: **Files-as-Database, MCP-as-Interface, Bidirectional-Sync-as-Reconciliation**.

**Key Metrics:**
- **Codebase Size:** ~24,823 LOC (Python)
- **Commits:** 957 commits across ~21 contributors
- **Architecture:** 5-layer clean architecture
- **MCP Tools:** 17 tools across 4 clusters
- **Specifications:** 20 SPECs (specification-driven development)
- **Database:** Dual-backend (SQLite primary, PostgreSQL experimental)
- **Cloud Mode:** Optional bidirectional sync with subscription-based cloud storage

---

## 1. System Architecture Overview

### 1.1 Five-Layer Clean Architecture

```
┌──────────────────────────────────────────────────────────────┐
│  LAYER 1: INTERFACE LAYER                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ MCP Server   │  │ FastAPI      │  │ Typer CLI    │      │
│  │ (Tools +     │  │ (REST API)   │  │ (Commands)   │      │
│  │  Prompts +   │  │              │  │              │      │
│  │  Resources)  │  │              │  │              │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
│         │                  │                  │              │
└─────────┼──────────────────┼──────────────────┼──────────────┘
          │                  │                  │
┌─────────┼──────────────────┼──────────────────┼──────────────┐
│  LAYER 2: SERVICE LAYER (Business Logic)                      │
│  ┌──────▼───────┐  ┌──────▼───────┐  ┌──────▼───────┐      │
│  │ Knowledge    │  │ Sync Service │  │ Auth Service │      │
│  │ Service      │  │ (File↔DB)    │  │ (Cloud JWT)  │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
│         │                  │                  │              │
└─────────┼──────────────────┼──────────────────┼──────────────┘
          │                  │                  │
┌─────────┼──────────────────┼──────────────────┼──────────────┐
│  LAYER 3: REPOSITORY LAYER (Data Access)                      │
│  ┌──────▼───────────────────────────────────┐                │
│  │ Repository Pattern (SQLAlchemy 2.0)     │                │
│  │ - EntityRepository                       │                │
│  │ - ObservationRepository                  │                │
│  │ - RelationRepository                     │                │
│  │ - ProjectRepository                      │                │
│  └──────┬───────────────────────────────────┘                │
│         │                                                     │
└─────────┼─────────────────────────────────────────────────────┘
          │
┌─────────┼─────────────────────────────────────────────────────┐
│  LAYER 4: DATA LAYER                                          │
│  ┌──────▼───────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ SQLite       │  │ PostgreSQL   │  │ Markdown     │      │
│  │ (Primary)    │  │ (Experimental)│  │ Files        │      │
│  │              │  │              │  │ (Source of   │      │
│  │ - Entities   │  │ - Dual       │  │  Truth)      │      │
│  │ - Relations  │  │   Backend    │  │              │      │
│  │ - FTS5       │  │   Support    │  │ - Frontmatter│      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
│         │                  │                  │              │
└─────────┼──────────────────┼──────────────────┼──────────────┘
          │                  │                  │
┌─────────┼──────────────────┼──────────────────┼──────────────┐
│  LAYER 5: INFRASTRUCTURE LAYER                                │
│  ┌──────▼───────┐  ┌──────▼───────┐  ┌──────▼───────┐      │
│  │ File System  │  │ rclone       │  │ Cloud Storage│      │
│  │ (Local)      │  │ (Bisync)     │  │ (S3/Tigris)  │      │
│  │              │  │              │  │              │      │
│  │ - Watchfiles │  │ - Project-   │  │ - WebDAV     │      │
│  │ - Obsidian   │  │   Scoped     │  │ - Mount      │      │
│  │   Compat     │  │   Sync       │  │ - Backup     │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└──────────────────────────────────────────────────────────────┘
```

### 1.2 Core Architectural Patterns

1. **Files-as-Database**
   - Markdown files are the **Source of Truth**
   - SQLite is an **index/cache** for fast queries and full-text search
   - Database can be regenerated from files (`basic-memory sync --force-full`)

2. **Bidirectional Synchronization**
   - **File → Database:** Watched file changes trigger DB updates
   - **Database → File:** MCP tool operations write both DB and files
   - **Conflict Resolution:** Filesystem timestamps are authoritative

3. **Knowledge Graph in Markdown**
   - **Entities:** Each Markdown file = Node
   - **Observations:** List items with `[category]` prefix = Facts
   - **Relations:** WikiLinks `[[Target]]` with relation types = Edges

4. **MCP-as-Universal-Interface**
   - MCP server exposes tools to any MCP-compatible AI
   - Tools use ASGI HTTP client (in-process) to FastAPI backend
   - Context manager pattern for proper resource management

5. **Dual-Mode Architecture**
   - **Local Mode:** Standalone filesystem + SQLite
   - **Cloud Mode:** + JWT auth + rclone sync + cloud storage

---

## 2. Technology Stack Deep Dive

### 2.1 Core Dependencies

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| **Runtime** | Python | 3.12+ | Type parameters, type aliases (3.12 syntax) |
| **Database** | SQLite | 3.x | Primary storage (FTS5 for search) |
| **Database** | PostgreSQL | 13+ | Experimental dual-backend support |
| **ORM** | SQLAlchemy | 2.0+ | Async ORM with repository pattern |
| **MCP** | FastMCP | 2.10.2+ | Model Context Protocol implementation |
| **MCP** | MCP SDK | 1.2.0+ | Core MCP protocol types |
| **API** | FastAPI | 0.115.8+ | REST API for tools + cloud |
| **CLI** | Typer | 0.9.0+ | Command-line interface |
| **Parsing** | python-frontmatter | 1.1.0+ | YAML frontmatter extraction |
| **Parsing** | markdown-it-py | 3.0.0+ | Markdown parsing |
| **Validation** | Pydantic | 2.10.3+ | Schema validation (v2 syntax) |
| **Sync** | watchfiles | 1.0.4+ | Filesystem watching (Rust-based) |
| **Sync** | rclone | External | Bidirectional cloud sync (bisync) |
| **Auth** | PyJWT | 2.10.1+ | JWT token validation (cloud mode) |
| **Observability** | logfire | 0.73.0+ | Optional OpenTelemetry (disabled by default) |

### 2.2 Architectural Innovations

1. **Specification-Driven Development (20 SPECs)**
   - Every major feature has a SPEC document
   - SPECs define problem, solution, implementation phases
   - Examples: SPEC-1 (Process), SPEC-16 (MCP Consolidation), SPEC-19 (Streaming), SPEC-20 (Rclone)

2. **Async-First Architecture**
   - SQLAlchemy 2.0 async engine
   - FastAPI async endpoints
   - aiofiles for async file I/O
   - pytest-asyncio for testing (strict mode)

3. **Context Manager Pattern (SPEC-16)**
   - All HTTP clients use `async with get_client() as client`
   - Replaced module-level singleton client
   - Enables dependency injection for cloud consolidation
   - Three modes: Local (ASGI), CLI Cloud (HTTP + JWT), Cloud App (factory injection)

4. **Circuit Breaker Pattern**
   - Sync failures trigger circuit breaker
   - Prevents cascading failures during file operations
   - Configurable thresholds and recovery

---

## 3. MCP Tool Architecture

### 3.1 Tool Clusters (17 Tools)

#### **Content Management (7 tools)**
1. `write_note(title, content, folder, tags, note_type)` - Create/update notes with knowledge graph
2. `read_note(identifier, page, page_size)` - Read notes by title/permalink/memory:// URL
3. `read_content(path)` - Raw file content (bypasses knowledge graph)
4. `view_note(identifier)` - Formatted artifact display
5. `edit_note(identifier, operation, content)` - Incremental edits (append, find/replace, etc.)
6. `move_note(identifier, destination_path)` - Move with database consistency
7. `delete_note(identifier)` - Delete from knowledge base

#### **Knowledge Graph Navigation (3 tools)**
8. `build_context(url, depth, timeframe)` - Traverse graph via memory:// URLs
9. `recent_activity(type, depth, timeframe)` - Time-based filtering (e.g., "1d", "1 week")
10. `list_directory(dir_name, depth, file_name_glob)` - Browse with filtering

#### **Search & Discovery (1 tool)**
11. `search_notes(query, page, page_size, search_type, types, entity_types, after_date)` - FTS5 full-text search

#### **Project Management (4 tools)**
12. `list_memory_projects()` - List all projects
13. `create_memory_project(project_name, project_path, set_default)` - Create new projects
14. `delete_project(project_name)` - Remove project
15. `get_current_project()` - Current project stats
16. `sync_status()` - File sync status

#### **Visualization (1 tool)**
17. `canvas(nodes, edges, title, folder)` - Generate Obsidian JSON Canvas

### 3.2 MCP Prompts (5 prompts)
- `ai_assistant_guide()` - Onboarding guidance for AI assistants
- `continue_conversation(topic, timeframe)` - Resume conversations with context
- `search(query, after_date)` - Formatted search results
- `recent_activity(timeframe)` - Formatted recent changes
- `json_canvas_spec()` - Full Obsidian canvas specification

### 3.3 MCP Resources (1 resource)
- `project://current` - Current project metadata and stats

---

## 4. Knowledge Graph Schema

### 4.1 Core Data Model

```python
Entity (Markdown File)
├── id: UUID
├── title: str
├── permalink: str (normalized slug)
├── entity_type: str (e.g., "note", "person", "concept")
├── content: str (raw markdown)
├── folder: str (relative path)
├── created_at: datetime
├── updated_at: datetime
├── Observations: List[Observation]
└── Relations: List[Relation]

Observation (Fact about Entity)
├── id: UUID
├── entity_id: UUID (foreign key)
├── content: str
├── category: str (extracted from [category])
├── tags: List[str] (extracted from #tag)
├── context: str (optional parenthetical)
└── created_at: datetime

Relation (Link between Entities)
├── id: UUID
├── source_entity_id: UUID
├── target_entity_id: UUID
├── relation_type: str (e.g., "relates_to", "inspired_by")
├── context: str (optional)
└── created_at: datetime
```

### 4.2 Markdown → Knowledge Graph Mapping

**Input Markdown:**
```markdown
---
title: Coffee Brewing Methods
permalink: coffee-brewing-methods
type: note
tags:
  - coffee
  - brewing
---

# Coffee Brewing Methods

## Observations
- [method] Pour over extracts floral notes #brewing
- [tip] Water temp ~205°F optimal (for light roasts)

## Relations
- pairs_well_with [[Chocolate Desserts]]
- requires [[Burr Grinder]]
```

**Output Knowledge Graph:**
```
Entity(
    title="Coffee Brewing Methods",
    permalink="coffee-brewing-methods",
    entity_type="note",
    observations=[
        Observation(category="method", content="Pour over extracts floral notes", tags=["brewing"]),
        Observation(category="tip", content="Water temp ~205°F optimal", context="for light roasts")
    ],
    relations=[
        Relation(type="pairs_well_with", target="Chocolate Desserts"),
        Relation(type="requires", target="Burr Grinder")
    ]
)
```

---

## 5. Sync Architecture (Files ↔ Database)

### 5.1 Local Sync Flow

```
File Change (watchfiles) → Sync Service → Parse Markdown → Upsert Entity → Update Relations
     ↓                                                                              ↓
Database Query (read_note) → Repository → Entity + Observations + Relations → JSON Response
```

### 5.2 Cloud Sync Flow (SPEC-20: Project-Scoped Rclone)

```
Local Files → rclone bisync → Cloud Storage (S3/Tigris) → Tenant Isolation
     ↑                                    ↓
     └─────────── rclone bisync ──────────┘
                (bidirectional)
```

**Key Properties:**
- **Project-Scoped:** Each project has its own rclone config
- **Bidirectional:** Changes flow both ways (via rclone bisync)
- **Conflict Detection:** rclone bisync flags conflicts
- **Filesystem Timestamp Authority:** File mtime is source of truth (SPEC-19 #369)
- **Post-Sync Force-Full:** Database reindexed after sync for consistency

### 5.3 Sync Optimizations (SPEC-19)

- **Streaming Foundation:** Async I/O throughout sync pipeline
- **Circuit Breaker:** Prevents cascading failures
- **Memory Optimization:** Reduced OOM on large projects (10k+ files)
- **43% Performance Gain:** Optimized queries and file processing (#352)
- **Directory Operations:** 10-100× faster traversal (#350)

---

## 6. Authentication & Multi-Tenancy (Cloud Mode)

### 6.1 JWT Authentication Flow

```
CLI: basic-memory cloud login
  → Supabase OAuth (Google/GitHub)
  → JWT Token (signed)
  → Stored in ~/.basic-memory/auth.json
  → Subscription Validation (Cloud API)
  → Project-Scoped Access
```

### 6.2 Tenant Isolation

- **Signed Headers:** JWT + Tenant ID in every request
- **S3 Prefixes:** `s3://bucket/tenant-{id}/project-{name}/`
- **Database Isolation:** Tenant-scoped queries (future: multi-tenant DB)
- **Configuration Persistence:** Tigris S3 for tenant configs (SPEC-15)

---

## 7. CLI Architecture

### 7.1 Command Structure (Typer)

```
basic-memory
├── mcp              # Start MCP server
├── sync             # Local file→DB sync (--watch for realtime)
├── status           # Sync status
├── import           # Import from Claude/ChatGPT/Memory JSON
│   ├── claude
│   ├── chatgpt
│   └── memory-json
├── project          # Project management
│   ├── list
│   ├── create
│   ├── switch
│   └── delete
├── tools            # CLI access to MCP tools
│   ├── basic-memory-guide
│   └── continue-conversation
└── cloud            # Cloud operations (requires auth)
    ├── login
    ├── logout
    ├── sync         # Bidirectional rclone sync
    ├── upload       # WebDAV upload
    ├── check        # Integrity check
    ├── mount        # Mount cloud storage
    └── unmount
```

### 7.2 Alias Support

- `bm` = `basic-memory` (shorter alias)

---

## 8. Data Persistence Patterns

### 8.1 Dual-Backend Architecture (SPEC: PostgreSQL Support)

```python
# Abstract database interface
class DatabaseInterface(Protocol):
    async def execute(self, query: str) -> Result
    async def fetch_all(self, query: str) -> List[Row]
    # ...

# Implementations
class SQLiteBackend(DatabaseInterface):
    # Uses aiosqlite + FTS5
    
class PostgresBackend(DatabaseInterface):
    # Uses asyncpg + pg_trgm
```

**Status:** PostgreSQL support is **experimental** (feature branch)

### 8.2 Migration Strategy

- **Alembic:** Database migrations (20+ migrations)
- **Version Tracking:** Automatic schema versioning
- **Backward Compatibility:** Graceful handling of old schemas

---

## 9. Configuration Management

### 9.1 Configuration Files

```
~/.basic-memory/
├── config.json           # Project list, default project
├── auth.json             # JWT token, refresh token (cloud mode)
└── projects/
    └── {project-name}/
        ├── basic-memory.db    # SQLite database
        └── {markdown-files}   # Source of truth
```

### 9.2 Environment Variables

| Variable | Purpose | Default |
|----------|---------|---------|
| `BASIC_MEMORY_HOME` | Config directory | `~/.basic-memory` |
| `BASIC_MEMORY_PROJECT_ROOT` | Constrain project paths (security) | None |
| `BASIC_MEMORY_CLOUD_MODE` | Enable cloud features | `false` |
| `LOGFIRE_TOKEN` | OpenTelemetry observability | Disabled |

---

## 10. Testing Architecture

### 10.1 Test Structure

```
tests/              # Unit tests (mocked, fast)
├── unit/
│   ├── test_markdown.py
│   ├── test_repository.py
│   └── ...
└── integration/
    └── ...

test-int/           # Integration tests (real implementations)
├── test_project_commands_integration.py
├── test_sync_performance_benchmark.py   # Marked with @pytest.mark.benchmark
└── ...
```

### 10.2 Test Infrastructure

- **In-Memory SQLite:** Each test gets isolated DB
- **Temporary Directories:** `tmp_path` fixture for filesystem tests
- **Async Testing:** pytest-asyncio strict mode
- **Coverage:** Unified coverage across unit + integration tests
- **Benchmarks:** Performance regression detection

---

## 11. Deployment & Distribution

### 11.1 Installation Methods

```bash
# UVX (recommended)
uvx basic-memory

# UV tool install
uv tool install basic-memory

# Docker
docker run ghcr.io/basicmachines-co/basic-memory:v0.16.2

# Development
just install  # or pip install -e ".[dev]"
```

### 11.2 Release Process

- **Versioning:** UV Dynamic Versioning (PEP 440 + Git tags)
- **Changelog:** Comprehensive CHANGELOG.md (82KB, 950+ commits documented)
- **GitHub Actions:** CI/CD with matrix testing (SQLite + PostgreSQL, multi-platform)
- **Docker Images:** Multi-arch builds (amd64, arm64)

---

## 12. Platform Support

### 12.1 Operating Systems

- **Linux:** ✅ Primary development platform
- **macOS:** ✅ Full support (Apple Silicon + Intel)
- **Windows:** ✅ Full support (WSL + native)
  - Special handling: Line endings (#422), Unicode (#411, #414), Path separators (#429)

### 12.2 AI Platform Integrations

- **Claude Desktop:** ✅ Primary integration via MCP config
- **VS Code:** ✅ Workspace MCP config (`.vscode/mcp.json`)
- **Zed Editor:** ✅ MCP support
- **Obsidian:** ✅ Realtime file editing (Markdown compatibility)
- **Any MCP Client:** ✅ Protocol-based, platform-agnostic

---

## 13. Key Architectural Decisions

### 13.1 Files-as-Source-of-Truth

**Decision:** Markdown files are the authoritative data source, not the database.

**Rationale:**
- Human-readable and editable in any text editor
- Version control via Git
- Platform-independent (no vendor lock-in)
- Obsidian and other tools can edit directly
- Database can be regenerated (`sync --force-full`)

### 13.2 MCP-as-Universal-Interface

**Decision:** Use MCP protocol instead of custom API for AI integration.

**Rationale:**
- Works with any MCP-compatible AI (Claude, future LLMs)
- Standardized protocol (schema validation, type safety)
- Tooling support (MCP Inspector for debugging)
- Future-proof (protocol evolves independently)

### 13.3 Dual-Mode Architecture (Local + Cloud)

**Decision:** Support both local-only and cloud-synced modes.

**Rationale:**
- **Privacy:** Local mode keeps all data on user's machine
- **Collaboration:** Cloud mode enables multi-device sync
- **Business Model:** Subscription revenue from cloud features
- **Flexibility:** Users choose their data sovereignty level

### 13.4 Bidirectional Sync (Not One-Way)

**Decision:** rclone bisync for two-way synchronization.

**Rationale:**
- Users can edit files locally OR in cloud
- Supports multiple devices
- Conflict detection (rclone handles)
- Mirrors user expectations (Dropbox-like behavior)

### 13.5 Specification-Driven Development

**Decision:** Every major feature starts with a SPEC document.

**Rationale:**
- Forces design before implementation
- Documents "Why" not just "What"
- Enables asynchronous decision-making
- Creates institutional memory

---

## 14. Performance Characteristics

### 14.1 Benchmarks (from SPEC-19 and test-int/)

| Operation | Performance | Notes |
|-----------|-------------|-------|
| **Sync (43% faster)** | ~10k files/minute | After #352 optimization |
| **Directory List (10-100×)** | <100ms for 1k files | After #350 optimization |
| **Search (FTS5)** | <50ms for 10k notes | SQLite full-text search |
| **Memory (optimized)** | <500MB for 10k files | After #380 OOM fix |
| **Startup** | <1s | MCP server initialization |

### 14.2 Scalability Limits

- **Files:** Tested up to 10,000+ markdown files
- **Knowledge Graph:** Millions of observations/relations (SQLite scales)
- **Concurrent Users:** Single-user by design (local-first)
- **Cloud Projects:** Multi-tenant, tenant-scoped (no cross-tenant data)

---

## 15. Security Architecture

### 15.1 Local Mode Security

- **No Network:** Fully offline operation
- **No Auth:** Direct filesystem access
- **Path Constraints:** `BASIC_MEMORY_PROJECT_ROOT` limits project creation

### 15.2 Cloud Mode Security

- **JWT Auth:** Signed tokens with expiration
- **Subscription Validation:** API checks active subscription
- **Tenant Isolation:** S3 prefixes, scoped queries
- **TLS:** HTTPS for all cloud communication
- **No Shared Secrets:** OAuth flow (Supabase)

---

## 16. Observability & Debugging

### 16.1 Logging

- **loguru:** Structured logging throughout
- **Log Levels:** DEBUG, INFO, WARNING, ERROR
- **Async-Safe:** Works with asyncio

### 16.2 Observability (Optional)

- **logfire:** OpenTelemetry integration (SPEC-12)
- **Disabled by Default:** Opt-in via `LOGFIRE_TOKEN`
- **Traces:** Request/response tracking
- **Metrics:** Performance monitoring

### 16.3 Development Tools

- **MCP Inspector:** Debug MCP server (`just run-inspector`)
- **Type Checking:** pyright with strict mode
- **Linting:** ruff with 100-char line limit
- **Formatting:** ruff format

---

## 17. Architectural Strengths

1. **Local-First Philosophy:** Privacy, ownership, offline capability
2. **Standards-Based:** MCP protocol, Markdown, YAML, SQLite
3. **Bidirectional Sync:** Humans and AIs collaborate on same files
4. **Clean Architecture:** Testable, maintainable, extensible
5. **Specification-Driven:** Design documents for every major feature
6. **Async-First:** Modern Python patterns (async/await)
7. **Dual-Backend:** SQLite primary, PostgreSQL experimental
8. **Multi-Platform:** Linux, macOS, Windows support
9. **Obsidian Compatible:** Works with existing Obsidian vaults
10. **Open Source:** AGPL-3.0 license

---

## 18. Architectural Constraints

1. **Single-User by Design:** Not built for real-time collaboration
2. **SQLite Limitations:** Write concurrency (mitigated by async)
3. **rclone Dependency:** Cloud sync requires external tool
4. **Python 3.12+:** Modern syntax limits backward compatibility
5. **MCP Maturity:** Protocol still evolving (v1.2.0)
6. **Markdown Parsing:** Strict format requirements for knowledge graph
7. **Memory Usage:** Large projects (10k+ files) need optimization
8. **PostgreSQL Experimental:** Not production-ready yet

---

## 19. Capability Matrix

### 19.1 Knowledge Management Capabilities

| Capability | Implementation | Status |
|------------|----------------|--------|
| Create Notes | `write_note` tool | ✅ Stable |
| Read Notes | `read_note`, `view_note` tools | ✅ Stable |
| Edit Notes | `edit_note` tool (5 operations) | ✅ Stable |
| Delete Notes | `delete_note` tool | ✅ Stable |
| Move Notes | `move_note` tool | ✅ Stable |
| Search Notes | `search_notes` tool (FTS5) | ✅ Stable |
| Knowledge Graph | Observations + Relations | ✅ Stable |
| Visualizations | `canvas` tool (Obsidian) | ✅ Stable |
| Directory Browsing | `list_directory` tool | ✅ Stable |
| Context Building | `build_context` tool | ✅ Stable |
| Recent Activity | `recent_activity` tool | ✅ Stable |

### 19.2 Project Management Capabilities

| Capability | Implementation | Status |
|------------|----------------|--------|
| Multiple Projects | Project configuration | ✅ Stable |
| Create Projects | `create_memory_project` tool | ✅ Stable |
| Switch Projects | CLI + tool support | ✅ Stable |
| Delete Projects | `delete_project` tool | ✅ Stable |
| Project Stats | `get_current_project` tool | ✅ Stable |
| Sync Status | `sync_status` tool | ✅ Stable |

### 19.3 Synchronization Capabilities

| Capability | Implementation | Status |
|------------|----------------|--------|
| Local Sync | watchfiles + sync service | ✅ Stable |
| Cloud Sync | rclone bisync (SPEC-20) | ✅ Stable |
| Conflict Detection | rclone bisync | ✅ Stable |
| Real-time Watch | `sync --watch` | ✅ Stable |
| Force Full Sync | `sync --force-full` | ✅ Stable |
| Background Sync | Async operations | ✅ Stable |
| Cloud Upload | WebDAV (SPEC-5) | ✅ Stable |
| Cloud Mount | rclone mount | ✅ Stable |

### 19.4 Import Capabilities

| Capability | Implementation | Status |
|------------|----------------|--------|
| Claude Conversations | `import claude` | ✅ Stable |
| ChatGPT Data | `import chatgpt` | ✅ Stable |
| Memory JSON | `import memory-json` | ✅ Stable |

### 19.5 Authentication & Authorization

| Capability | Implementation | Status |
|------------|----------------|--------|
| OAuth Login | Supabase (Google/GitHub) | ✅ Stable |
| JWT Tokens | PyJWT validation | ✅ Stable |
| Subscription Validation | Cloud API | ✅ Stable |
| Tenant Isolation | S3 prefixes | ✅ Stable |
| Token Refresh | Automatic renewal | ✅ Stable |

### 19.6 Experimental/Future Capabilities

| Capability | Implementation | Status |
|------------|----------------|--------|
| PostgreSQL Backend | Dual-backend arch | 🚧 Experimental |
| Semantic Search | ChromaDB (SPEC-17) | 📋 Planned |
| AI Memory Management | SPEC-18 | 📋 Planned |
| Multi-Tenant DB | SPEC-15 | 📋 Planned |
| Git Versioning | SPEC-14 | 📋 Planned |

---

## 20. Technical Debt & Known Issues

### 20.1 From GitHub Issues

- **Windows Compatibility:** Ongoing fixes for line endings, Unicode, path separators
- **PostgreSQL Maturity:** Experimental branch, not production-ready
- **Memory Usage:** Large projects can OOM (mitigated but not eliminated)
- **Conflict Resolution:** rclone bisync flags conflicts but doesn't auto-resolve

### 20.2 From CHANGELOG

- **Deprecations:** Module-level `client` → context manager pattern (SPEC-16)
- **Breaking Changes:** `entity_type` → `note_type` in v0.16.0
- **Migration Complexity:** 20+ Alembic migrations (requires careful upgrades)

---

## 21. Ecosystem Integration

### 21.1 Compatible Tools

- **Obsidian:** Full bidirectional compatibility
- **VS Code:** MCP + Markdown editing
- **Zed:** MCP support
- **Any Text Editor:** Direct Markdown editing
- **Git:** Version control for knowledge base

### 21.2 Cloud Providers

- **Tigris:** S3-compatible, primary cloud storage
- **AWS S3:** Compatible (via rclone)
- **Supabase:** OAuth authentication
- **WebDAV:** Upload protocol

---

## 22. Conclusion

Basic Memory implements a **Local-First Knowledge Graph** architecture that bridges **human-editable Markdown** and **AI-traversable structured data**. Its five-layer clean architecture, MCP integration, and bidirectional sync create a system where:

1. **Files are the source of truth** (human ownership)
2. **Database is an index** (AI performance)
3. **MCP is the interface** (universal compatibility)
4. **Bidirectional sync is reconciliation** (multi-device harmony)

The architecture is **specification-driven**, **async-first**, and **platform-agnostic**, with a clear separation between local-only and cloud-enabled modes. Its ~25k LOC Python codebase demonstrates mature engineering practices: clean architecture, comprehensive testing, type safety, and performance optimization.

**Core Innovation:** Treating Markdown files as a database that AIs can navigate via a knowledge graph, while humans edit the same files in their favorite tools.

---

**Status:** Complete  
**Confidence:** 95%  
**Next Steps:** Level 2 (Decision Forensics + Anti-Library Extraction)
