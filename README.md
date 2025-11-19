# Project Wisdom Library

Welcome to the **Project Wisdom Library**—a centralized, AI-driven archive for conceptual distillations, investigations, and epistemic history. This repository is designed for **Issue-Driven** autonomous agent operation, moving beyond simple data storage to capture the "Wisdom" and "Paradigm Shifts" of your projects.

## Core Principles
- **Holistic System Thinking:** We analyze connections, not just components.
- **Epistemic History:** We capture *why* decisions were made, not just *what* changed.
- **The Wisdom Ladder:** We systematically climb from Data (Level 1) to Wisdom (Level 4).

## How to Use This Library

### 1. Vision Owner (Human): Trigger the System
1.  **File an Issue:** Use `[Intake]` for investigations or `[Task]` for backlog items.
2.  **Assign:** **Assign the Issue to Copilot** (or your connected AI Agent).
    * *The Assignment is the Trigger.*

### 2. System Owner (Agent): Execute the Mandate
*The Agent automatically picks up the assigned Issue.*

1.  **Read:** The Agent reads the "System Owner Instructions" embedded in the Issue.
2.  **Profile:** The Agent scans the Target Repository provided in the form.
3.  **Execute:** The Agent climbs the **Wisdom Ladder** (Architecture $\to$ Forensics $\to$ Wisdom).
4.  **Deliver:** The Agent submits a Pull Request with the results.

### 2. For AI Agents (System Owners)
**Do not chat.** Execute the mandate.

1.  **Trigger:** Watch for new Issues with the label `investigation`.
2.  **Execution:** Follow the **[Automation Guide](docs/AUTOMATION_GUIDE.md)**.
    * Parse the Issue.
    * Establish the **Wisdom Ladder**.
    * Execute Analysis.
    * Generate Artifacts (Protocol Compliant).
    * Update Catalogue.
3.  **Delivery:** Submit a Pull Request with the results.

## Repository Structure

```
project-wisdom-library/
├── atomic/             # Level 1-2: Hard Facts & Forensics
├── distillations/      # Level 4: Wisdom & Paradigms
├── process_memory/     # Level 3: Epistemic History (JSON Protocol)
├── backlog/            # Strategic & Tactical Actions
├── catalogue/          # The Knowledge Graph (Manifest)
├── templates/          # Standardized Input Patterns
└── docs/               # The System Manual (Workflow & Schemas)
```

## Documentation Resources
- **[Automation Guide](docs/AUTOMATION_GUIDE.md):** The "Source of Truth" for Agent execution.
- **[Analysis Menu](docs/ANALYSIS_MENU.md):** The Wisdom Ladder definitions.
- **[Manifest Schema](docs/MANIFEST_SCHEMA.md):** The Data Structure & Mapping Protocol.
