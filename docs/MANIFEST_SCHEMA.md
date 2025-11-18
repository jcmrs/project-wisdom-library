# Manifest Schema & Mapping Protocol

This document defines the schema for `/catalogue/manifest.json`, the machine-readable catalogue of the Project Wisdom Library. It includes the **Mapping Protocol** for translating internal Process Memory logic into external catalogue metadata.

---

## Root Schema

```json
{
  "atomic": [],
  "distillations": [],
  "process_memory": [],
  "analyses": [],
  "ideas": [],
  "backlog": [],
  "sensitive": []
}
```

---

## Artifact Entry Schema

All entries in the manifest must conform to this structure.

```json
{
  "id": "unique-kebab-id",
  "title": "Human-readable title",
  "date": "YYYY-MM-DD",
  "type": "atomic|distillation|process_memory|analysis|idea|backlog",
  "path": "/folder/filename.md",
  "description": "Brief summary",
  "tags": ["tag1", "tag2"],
  "author": "Agent or Human",
  "status": "complete|in-progress|deprecated",
  "related": ["id-1", "id-2"],
  "strategic_context": "The 'Why' or Rationale",
  "metadata": {
    "protocol_type": "StrategicDecision",
    "confidence": 0.95,
    "phase": "Design"
  }
}
```

---

## Process Memory Mapping Protocol

The **Process Memory Protocol** (used inside `templates/PROCESS_MEMORY_TEMPLATE.md`) creates rich, strict JSON data. The Agent must **map** that internal data to this Manifest Schema using the rules below.

| Protocol Field (Internal JSON) | Manifest Field (External Catalogue) | Mapping Logic |
| :--- | :--- | :--- |
| `id` | `id` | Direct copy. |
| `title` | `title` | Direct copy. |
| `timestamp_created` | `date` | Convert ISO to `YYYY-MM-DD`. |
| `summary` | `description` | Direct copy. |
| `rationale` | `strategic_context` | **Semantic Match:** The "Rationale" for a decision is the "Strategic Context" for the library. |
| `links` | `related` | **Merge:** Combine Protocol `links` with any other related artifact IDs. |
| `tags` | `tags` | Direct copy. |
| `provenance.author` | `author` | Flatten the nested object. |
| `type` (e.g., StrategicDecision) | `metadata.protocol_type` | Store the specific Protocol type in metadata to preserve granularity. |
| `confidence_level` | `metadata.confidence` | Store in metadata. |
| `phase` | `metadata.phase` | Store in metadata. |
| `source_adr` | `metadata.source_adr` | Store in metadata. |

---

## Field Definitions

### Core Fields
* **`id`**: Unique identifier (e.g., `auth-decision-2025-11-18`).
* **`type`**: High-level category matching the folder structure.
    * *Note:* For Process Memory, this is always `"process_memory"`. The specific *kind* (e.g., `MentalModels`) goes in `metadata.protocol_type`.
* **`strategic_context`**: The "Why". For investigations, this is the User's intent. For Process Memory, this is the Decision Rationale.

### Relationship Fields
* **`related`**: Bidirectional links. If Artifact A links to B, B must link to A.
* **`process_memory_refs`**: (Optional) Specific subset of `related` that points only to Process Memory entries.

---

## Example Entries

### 1. Process Memory Entry (Mapped from Protocol)
*Internal Protocol Type: `StrategicDecision`*

```json
{
  "id": "microservices-adoption-2025-11-10",
  "title": "Adopt Microservice Architecture",
  "date": "2025-11-10",
  "type": "process_memory",
  "path": "/process_memory/2025-11-10-session.md",
  "description": "Decision to adopt microservices to improve scalability.",
  "strategic_context": "Monolithic design limitations identified during load testing.",
  "tags": ["architecture", "scalability", "strategic"],
  "author": "Claude-3.5-Sonnet",
  "related": ["load-test-analysis-2025-11-09"],
  "metadata": {
    "protocol_type": "StrategicDecision",
    "confidence": 0.95,
    "phase": "Design",
    "source_adr": "[https://repo.company.com/docs/adr/001.md](https://repo.company.com/docs/adr/001.md)"
  }
}
```

### 2. Strategic Backlog Entry (Paradigm Shift)
*Generated from `templates/STRATEGIC_BACKLOG_TEMPLATE.md`*

```json
{
  "id": "culture-shift-automation-2025-11-18",
  "title": "Strategic Shift: From Manual Review to Automated Gates",
  "date": "2025-11-18",
  "type": "backlog",
  "path": "/backlog/2025-11-18-paradigm-shift-automation.md",
  "description": "Initiative to realign team culture around 'Automation is Culture' paradigm.",
  "strategic_context": "Current manual review process creates bottlenecks and ignores the 'AI-First' imperative.",
  "tags": ["paradigm-shift", "culture", "automation", "strategic-backlog"],
  "author": "System-Owner-Agent",
  "status": "open",
  "metadata": {
    "priority": "High",
    "type": "Strategic Realignment",
    "target_paradigm": "Automation is Culture"
  }
}
```
