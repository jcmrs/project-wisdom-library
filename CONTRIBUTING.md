# Contributing Guidelines

## Who Contributes?
- **AI agents:** Perform analyses, syntheses, and catalogue results.
- **Strategic Owners (Vision Holders):** Provide context, review ripples, and validate alignment when prompted.
- **No manual code review or syntax checking required—automated by workflows and scripts.**

## For AI Agents: Automated Workflow

**Primary Workflow Guide:** [`AGENT_INTAKE_WORKFLOW.md`](AGENT_INTAKE_WORKFLOW.md)

This is your primary entry point for initiating new investigations. It provides a structured 9-step intake process:
1. Target Selection (Repository or Document)
2. Investigation Type (Atomic or Long-Form)
3. Analysis Menu Presentation
4. Strategic & Subjective Context Gathering
5. Automated Investigation Execution
6. Artifacts & Storage with Catalogue Updates
7. Post-Analysis Steps (Process Memory, Cross-linking)
8. Sensitive Materials Handling
9. Pull Request Preparation

**Detailed Operational Guide:** [`AGENT_PANEL_WORKFLOW.md`](AGENT_PANEL_WORKFLOW.md)

For comprehensive implementation details and advanced workflows, see the operational guide which provides:
- Detailed investigation protocols
- Analysis methodologies
- Artifact creation workflows
- Best practices and examples

**Quick Start:**
1. Follow the 9-step workflow in `AGENT_INTAKE_WORKFLOW.md` (primary intake)
2. Use analysis menu in `docs/ANALYSIS_MENU.md` to guide investigation
3. Reference `docs/MANIFEST_SCHEMA.md` for catalogue updates
4. Consult `AGENT_PANEL_WORKFLOW.md` for detailed operational guidance
5. Review `docs/AUTOMATION_GUIDE.md` for implementation patterns

## Standard Workflow (Summary)

1. Select whether your entry is atomic or long-form.
2. Use the correct template in `/templates/` (include process memory, analysis type, or distillation).
3. Place your entry in the correct folder.
4. Automated tools generate/update the index and catalogue.
5. If you have ideas for repository or process improvements, add them to `/backlog/` or `/ideas/`.

## Templates & Standards

- **Always use a submission template.**
- **Tag and link entries for automated catalogue update.**
- **Flag any sensitive materials; store them in `/sensitive/`.**

## Available Templates

- `templates/ATOMIC_ANALYSIS_TEMPLATE.md` - For quick, focused analyses
- `templates/DISTILLATION_TEMPLATE.md` - For comprehensive investigations
- `templates/PROCESS_MEMORY_TEMPLATE.md` - For strategic decision capture
- `templates/IDEA_NOTE_TEMPLATE.md` - For ideas and questions
- `templates/BACKLOG_ITEM_TEMPLATE.md` - For actionable improvements

## Documentation Resources

- **`AGENT_INTAKE_WORKFLOW.md`** - Structured 9-step intake workflow (START HERE)
- **`AGENT_PANEL_WORKFLOW.md`** - Detailed autonomous agent operational guide
- **`docs/ANALYSIS_MENU.md`** - Detailed analysis type descriptions
- **`docs/MANIFEST_SCHEMA.md`** - Catalogue metadata schema
- **`docs/AUTOMATION_GUIDE.md`** - Implementation patterns for agents
- **`FOUNDATION.md`** - Core principles and system thinking
- **`.github/PULL_REQUEST_TEMPLATE.md`** - PR submission format

---
