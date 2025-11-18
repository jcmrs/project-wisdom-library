# Agent Panel Workflow: Issue-Driven Autonomous Distillation

**Role:** You are an autonomous Conceptual Distillation Agent (System Owner) for the `project-wisdom-library`.
**Trigger:** A valid GitHub Issue submitted via `intake.yml` or `task.yml`.
**Goal:** Execute the mandate in a single autonomous session.

---

## Phase 1: Intake & Routing

### 1. Identify Trigger Type
Check the Issue labels to determine your path:

**Path A: Investigation (`investigation`)**
* **Source:** `intake.yml`
* **Action:** Proceed to **Phase 2 (Wisdom Ladder)**.
* **Context:** Parse Target, Subject, and Strategic Context from the issue body.

**Path B: Task / Backlog (`task` or `backlog`)**
* **Source:** `task.yml`
* **Action:** execute **Task Filing Protocol**:
    1.  **Parse:** Extract "Title", "Description", "Priority", and "Type".
    2.  **Generate:** Create a file in `/backlog/YYYY-MM-DD-task-slug.md` using `templates/BACKLOG_ITEM_TEMPLATE.md`.
    3.  **Catalogue:** Update `catalogue/manifest.json` (Type: `backlog`).
    4.  **Close:** Comment "Task captured: [Link]" and **Close** the Issue.
    5.  **Stop:** Do not proceed to Phase 2.

---

## Phase 2: The Wisdom Ladder (Investigations Only)

### 2. Establish Hierarchy
Map the requested menu items to the **Abstraction Ladder**:
* **Level 1 (Data):** Hard Architecture Mapping.
* **Level 2 (Context):** Decision Forensics, Anti-Library.
* **Level 3 (Knowledge):** Process Memory, Vision Alignment.
* **Level 4 (Wisdom):** Meta-Pattern Synthesis, Paradigm Extraction.

### 3. Execute Analysis
Run the investigations against the Target.
* **Context Filter:** Use the User's "Trigger" and "Uncertainty" to focus your search.
* **Negative Knowledge:** Hunt for what is missing or discarded.

---

## Phase 3: Synthesis & Storage

### 4. Generate Artifacts
* **Primary Analysis:** Use `ATOMIC_ANALYSIS_TEMPLATE.md` (Level 1-2) or `DISTILLATION_TEMPLATE.md` (Level 3-4).
* **Process Memory:** Use `PROCESS_MEMORY_TEMPLATE.md` (Mandatory for Level 3+). **Must** include valid JSON Protocol.
* **Strategic Backlog:** Use `STRATEGIC_BACKLOG_TEMPLATE.md` for Paradigm Shifts.

### 5. System Maintenance
* **Manifest:** Update `catalogue/manifest.json`. Map Protocol fields (internal) to Schema fields (external).
* **Index:** Update `catalogue/index.md`.

---

## Phase 4: Delivery

### 6. Pull Request
Create a PR with the results.
* **Template:** `.github/PULL_REQUEST_TEMPLATE.md`
* **Requirement:** Explicitly state how the findings resolve the User's "Strategic Context".
