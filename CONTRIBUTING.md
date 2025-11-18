# Contributing to Project Wisdom

## The Workflow: Issue-Driven Autonomous Distillation

We do not use "Interactive PRs" or "Chat-based" investigations. The workflow is **Asynchronous** and **Issue-Driven**.

### For Humans (Vision Owners)
1.  **Submit an Issue:** Use the `Conceptual Investigation Intake` form.
2.  **Provide Context:** The "Subjective Context" field is the most important part of your submission. It tells the agent *why* to care.
3.  **Review Results:** You will receive a Pull Request containing the analysis. Your role is "On the Loop" validation.

### For AI Agents (System Owners)
**You are the System Owner.** You must enforce the protocol.

1.  **Read the Manual:**
    * `AGENT_PANEL_WORKFLOW.md`: Your operational script.
    * `docs/AUTOMATION_GUIDE.md`: Your logic implementation guide.
    * `docs/MANIFEST_SCHEMA.md`: Your database schema.

2.  **Enforce the Standards:**
    * **Never** create a Process Memory file without a valid JSON Protocol block.
    * **Never** create a Distillation without an Abstraction Layer (Mental Models).
    * **Always** map your internal protocol data to the external Manifest schema.

3.  **Training Data:**
    * Use the files in `/examples/` as your one-shot learning prompts. They represent the "Ground Truth" of a correct output.

---
**Imperative:** Holistic System Thinking. Do not just generate files; build the Knowledge Graph.
