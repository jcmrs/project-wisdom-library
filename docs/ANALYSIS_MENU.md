# Analysis Menu: The Wisdom Ladder

This document defines the hierarchy of investigation types available in the Project Wisdom Library. It is structured as a **Wisdom Ladder**—a progression from raw technical data to high-level philosophical abstraction.

---

## The Wisdom Ladder (Distillation Hierarchy)

To achieve high-level conceptual distillation, analyses should ideally proceed in this sequence:

1.  **The "What" (Data/Reality):** Mapping the physical truth of the system.
2.  **The "How & Why" (Information/Context):** Understanding history, decisions, and failures.
3.  **The "Meaning" (Knowledge/Epistemology):** Aligning rationale, intent, and human experience.
4.  **The "Wisdom" (Abstraction/Paradigms):** Synthesizing universal laws, mental models, and paradigms.

---

## Level 1: The "What" (Data & Reality)

### 1. Hard Architecture Mapping
**Purpose:** Map the technical architecture, dependencies, and structural patterns.
**Methodology:**
- Identify system layers and component dependencies.
- Analyze data flow and communication patterns.
- Document technology stack and integration points.
**Best For:** Establishing the "Ground Truth" before asking "Why".

---

## Level 2: The "How & Why" (Information & Context)

### 2. Decision Forensics
**Purpose:** Investigate *why* specific decisions were made (traceability).
**Methodology:**
- Review git history, PRs, and issues.
- Trace trade-offs and alternatives considered.
- Document implicit vs explicit decisions.
**Best For:** Understanding the rationale behind the current architecture.

### 3. Anti-Library Extraction
**Purpose:** Document "Negative Knowledge"—discarded approaches, failed experiments, and "roads not taken."
**Methodology:**
- Identify abandoned branches and closed-without-merge PRs.
- Extract lessons from failed experiments.
- Document constraints that forced specific choices.
**Best For:** Preventing repeated mistakes and understanding boundaries.

---

## Level 3: The "Meaning" (Knowledge & Epistemology)

### 4. Process Memory & Epistemic History
**Purpose:** Document the *evolution of thought*, strategic pivots, and the subjective "Why".
**Methodology:**
- Capture real-time strategic context during analysis.
- Document "The Pivot" (what changed our mind).
- Record uncertainties and how they were resolved.
**Best For:** Preserving institutional wisdom and the "Spirit" of the project.

### 5. Vision Alignment
**Purpose:** Assess alignment between stated goals/vision and actual implementation.
**Methodology:**
- Extract stated vision from documentation/intake.
- Map actual implementation patterns against intent.
- Identify drift or misalignment.
**Best For:** Strategic planning and course correction.

### 6. Sentiment Analysis
**Purpose:** Analyze team dynamics, friction points, and emotional health.
**Methodology:**
- Analyze tone in commits and comments.
- Identify frustration hot-spots or burnout signals.
**Best For:** Understanding the human element of the system.

---

## Level 4: The "Wisdom" (Abstraction & Paradigms)

### 7. Meta-Pattern Synthesis
**Purpose:** Identify recurring patterns *across* multiple investigations or projects.
**Methodology:**
- Connect disparate findings into coherent frameworks.
- Extract universal lessons that transcend specific code.
**Best For:** Building the organizational "Brain" and shared vocabulary.

### 8. Paradigm Extraction
**Purpose:** Identify the core **Mental Models**, **System Archetypes**, and **Root Metaphors** governing the system.
**Methodology:**
- **Abstraction:** Move from "Code handles retries" $\to$ "System favors Eventual Consistency."
- **Archetype ID:** Identify systems thinking patterns (e.g., "Shifting the Burden").
- **Paradigm Shift:** Define the *From/To* shift in worldview (e.g., "From Monolith to Microservices").
**Best For:** Long-Form Distillations and Strategic Realignment.

---

## Action & Utilities

### 9. Backlog/Idea Capture
**Purpose:** Extract actionable improvements and future concepts.
- **Tactical:** Technical debt, bug fixes.
- **Strategic:** Cultural changes, paradigm shifts (use Strategic Backlog).

### 10. Custom Analysis
**Purpose:** User-defined investigation for specific needs not covered above.

---

**Selection Strategy:**
* For **Atomic** requests, pick from Level 1 or 2.
* For **Long-Form Distillations**, you must climb the ladder: Level 1 $\to$ 2 $\to$ 3 $\to$ 4.
