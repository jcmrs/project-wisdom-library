# Example: Atomic Analysis (Level 2)

**Type:** Atomic
**Date:** 2025-11-18
**Ladder Level:** Level 2 (Context & History)
**Target:** https://github.com/example/auth-service

## Quick Summary
Investigation of the decision to implement JWT-based authentication. Analysis reveals mobile requirements were the primary constraint that forced this architecture.

## Strategic Context
*From Intake:* "I am worried that our Auth service is becoming too complex for the new mobile team. I want to know if the original architects anticipated this pain."

## Investigation Findings
1.  **Mobile-First Driver:** PR #145 explicitly mentions "Cookies do not persist reliably in React Native WebViews."
2.  **Stateless Requirement:** Traffic spikes in 2024 forced a move away from sticky sessions (Commit `8f3a2b`).

## Constraints & Negative Knowledge (Critical)
*Why did we reject the alternatives?*
-   **Rejected Session Cookies:** Could not be shared securely between the Native App and the Web View without a proxy service (too expensive).
-   **Rejected Auth0:** Cost analysis in Issue #89 showed it would exceed budget at 100k MAU.

## Ripple Effects
-   **Complexity:** The "Refresh Token" dance is the direct cost of the "No Cookie" constraint.
-   **Drift:** New team members are trying to re-introduce cookies, unaware of the mobile constraint.

## Linked Artifacts
-   Process Memory: `jwt-decision-validation-2025-11-18`
-   Backlog: `paradigm-shift-documentation-2025-11-18`

## Tags
authentication, jwt, decision-forensics, mobile, constraints
