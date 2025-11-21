# Analysis of Project Needs

This document outlines the core needs of the `project-wisdom-library`, which inform the design of our development framework and methodology.

## 1. Decision Velocity vs. Rigor

The project is not a fast-moving production application but a framework for deep, structured analysis. Decisions made here have long-term consequences on the quality of the "wisdom" generated.

*   **Conclusion:** Rigor and the capturing of rationale ("Epistemic History") are more important than raw development speed. Our processes must prioritize clarity, review, and documentation over rapid, undocumented changes.

## 2. Core Product is Knowledge

The primary outputs of this project are structured knowledge artifacts (Markdown files), not compiled code. The "source code" for this knowledge includes not only the Python/YAML automation but, critically, the prompts used to guide the AI.

*   **Conclusion:** The development framework must treat prompts and documentation templates as first-class citizens, on par with application code. Changes to them must be subject to the same level of rigor and review.

## 3. GitHub-Native Workflow

The entire operational lifecycle exists within the GitHub ecosystem (Issues → Actions → Scripts → Pull Requests).

*   **Conclusion:** The development framework must be native to this environment, leveraging tools and processes that integrate seamlessly with GitHub (e.g., ADRs as Markdown files in the repo, specs using GitHub-compatible formats).

## 4. Separation of Concerns

There are two distinct workstreams required to contribute to this project:

*   **Conceptual Work:** The intellectual process of performing the "Wisdom Ladder" analyses.
*   **Technical Work:** The engineering task of maintaining and extending the automation that supports the conceptual work.

*   **Conclusion:** The framework must support both types of contributors. It should be clear and structured enough for technical contributors to implement changes, while also serving the needs of conceptual analysts who define the requirements.
