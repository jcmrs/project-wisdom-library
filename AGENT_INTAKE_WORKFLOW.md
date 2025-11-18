# Agent Panel: Conceptual Investigation & Intake – Project Wisdom Library

Welcome, Wisdom Agent!  
Please follow this step-by-step workflow to initiate a new conceptual distillation, atomic investigation, or process memory mapping.

---

## 1. Target Selection

**Question for user:**  
Is your investigation target a GitHub repository or a document?

### If Repository:
- Ask for the URL (e.g., `https://github.com/example/repo`)
- Confirm access and availability
- Note: You may need repository cloning capabilities or API access

### If Document:
- Request the upload or content paste
- Ask for format/type (e.g., session log, project memo, architecture document, meeting notes)
- Clarify the document's source and context

### If Other:
- Request clarification on the source type
- Determine the most appropriate approach for analysis

---

## 2. Investigation Type

**Question for user:**  
Is this an **Atomic Investigation** (quick, focused insight) or **Long-Form Distillation** (comprehensive, multi-step analysis)?

### Atomic Investigation:
- Focused, targeted investigation
- Single issue, pattern, or question
- Quick turnaround (minutes to hour)
- Uses `templates/ATOMIC_ANALYSIS_TEMPLATE.md`
- Stored in `/atomic/`

### Long-Form Distillation:
- Comprehensive, multi-faceted investigation
- System-wide patterns, architectural decisions
- Deeper synthesis (hours to days)
- Uses `templates/DISTILLATION_TEMPLATE.md`
- Stored in `/distillations/`

**Note:** You may start with an atomic investigation and escalate to long-form later if findings warrant deeper analysis.

---

## 3. Analysis Menu

**Present the following choices (user may select one or more):**

1. **Hard Architecture Mapping**
   - Map technical structure and dependencies
   - Identify architectural patterns and constraints
   - Document technology stack and integration points

2. **Decision Forensics**
   - Investigate why specific decisions were made
   - Trace decision history through commits, issues, PRs
   - Document trade-offs and alternatives considered

3. **Anti-Library (Discarded Approaches)**
   - Identify abandoned experiments and failed approaches
   - Document "roads not taken" and why
   - Extract negative knowledge (what doesn't work)

4. **Vision Alignment**
   - Assess alignment with stated goals/vision
   - Identify drift or misalignment
   - Recommend realignment strategies

5. **Sentiment Analysis**
   - Analyze tone in commits, comments, issues
   - Identify friction points or areas of frustration
   - Detect team dynamics and collaboration patterns

6. **Meta-Pattern Synthesis**
   - Identify recurring patterns across investigations
   - Synthesize higher-order insights
   - Extract philosophical/strategic lessons

7. **Process Memory Mapping** (Request as Output)
   - Document strategic decisions and context
   - Capture pivots, uncertainties, learning moments
   - Uses `templates/PROCESS_MEMORY_TEMPLATE.md`

8. **Backlog/Idea Capture**
   - Extract improvement opportunities
   - Identify technical debt and enhancement ideas
   - Document risks or concerns

9. **Custom** (Describe)
   - User-defined investigation type
   - Request specific methodology or focus
   - Adapt existing templates or create new approach

**See [`docs/ANALYSIS_MENU.md`](docs/ANALYSIS_MENU.md) for detailed descriptions of each analysis type.**

---

## 4. Strategic & Subjective Context

**Prompt user:**  
Please provide any subjective context, uncertainty, strategic vision, relevant background, or key questions driving this investigation.

### Important Context Questions:
- What is your primary goal with this analysis?
- Are there specific patterns or issues you want to understand?
- What decision or insight are you hoping to gain?
- What excites or frustrates you about this project/topic?
- Are there uncertainties or open questions you're grappling with?
- What is the strategic intent? (What are you trying to learn/achieve?)
- Are there specific focus areas or concerns?
- Is there any prior work or related analyses?
- Is there context that isn't captured in the repository/document?

**Never infer intent—always ask for clarification when context is unclear.**

---

## 5. Automated Investigation Execution

Once you have gathered the necessary information:

1. **Gather Source Materials:**
   - Clone or access repository (if applicable)
   - Parse and review documents
   - Collect relevant artifacts

2. **Apply Analysis Methodology:**
   - Use appropriate investigation techniques for each selected analysis type
   - Review code, commits, issues, PRs, documentation as needed
   - Apply domain-specific analysis tools if available
   - Extract patterns, decisions, sentiments, or structures

3. **Handle Ambiguity:**
   - If context is missing: **prompt user for clarification**
   - If findings are ambiguous: document uncertainty
   - If additional artifacts needed: request them
   - Document all assumptions made

4. **Generate Output:**
   - Use the appropriate template from `/templates/`
   - Atomic: `ATOMIC_ANALYSIS_TEMPLATE.md`
   - Long-form: `DISTILLATION_TEMPLATE.md`
   - Process memory: `PROCESS_MEMORY_TEMPLATE.md`
   - Ideas: `IDEA_NOTE_TEMPLATE.md`
   - Backlog: `BACKLOG_ITEM_TEMPLATE.md`

5. **Quality Check:**
   - Ensure all template sections are completed
   - Verify findings are well-supported
   - Check for clarity and coherence

**If context/artifact is ambiguous or missing, prompt user for more detail before proceeding.**

---

## 6. Artifacts & Storage

Save each output artifact to the correct folder and update the catalogue:

### Storage Locations:

| Artifact Type | Folder | Naming Convention |
|---------------|--------|-------------------|
| Atomic Analyses | `/atomic/` | `YYYY-MM-DD-short-descriptor.md` |
| Long-Form Distillations | `/distillations/` | `YYYY-MM-DD-project-theme.md` |
| Specialized Analyses | `/analyses/` | `YYYY-MM-DD-analysis-type-subject.md` |
| Process Memory | `/process_memory/` | `YYYY-MM-DD-session-context.md` + `.json` |
| Ideas | `/ideas/` | `YYYY-MM-DD-idea-brief-description.md` |
| Backlog Items | `/backlog/` | `YYYY-MM-DD-item-brief-description.md` |
| Sensitive Materials | `/sensitive/` | `YYYY-MM-DD-sensitive-descriptor.md` |

### Catalogue Update Process:

1. **Update `/catalogue/index.md`:**
   - Add entry under appropriate section
   - Include title, date, brief description
   - Add link to artifact
   - Include relevant tags

2. **Update `/catalogue/manifest.json`:**
   - Add entry to appropriate array with metadata:
   ```json
   {
     "id": "unique-id",
     "title": "Analysis Title",
     "date": "YYYY-MM-DD",
     "type": "atomic|distillation|process_memory|analysis|idea|backlog",
     "path": "/atomic/YYYY-MM-DD-descriptor.md",
     "tags": ["tag1", "tag2"],
     "related": ["id1", "id2"],
     "description": "Brief description"
   }
   ```

3. **Cross-Link Related Artifacts:**
   - Link to related analyses in artifact files
   - Update related artifacts to point back
   - Create bidirectional references
   - Build knowledge graph

**See [`docs/MANIFEST_SCHEMA.md`](docs/MANIFEST_SCHEMA.md) for detailed schema information.**

---

## 7. Post-Analysis Steps

### Process Memory Synthesis

When applicable, synthesize process memory entries using the protocol in `/templates/PROCESS_MEMORY_TEMPLATE.md`.

**Create process memory when:**
- Strategic decisions are made
- Notable insights emerge
- Context significantly changes
- Investigation reveals pivots or shifts
- User expresses uncertainty that gets resolved
- Patterns connect across multiple analyses

**Process memory should capture:**
- Strategic context and vision
- Decisions made and rationale
- Frustrations or uncertainties
- Ripple effects noted
- Artifacts created
- Recommended next steps

### Cross-Linking

- Link analyses to related distillations
- Connect to process memory entries
- Reference backlog items spawned from findings
- Link to related ideas captured during investigation
- Create bidirectional references for easy navigation

### Backlog & Ideas

If the analysis surfaces new items:
- Create backlog items for actionable improvements
- Create idea notes for future enhancements
- Link back to the originating analysis
- Prompt user: "This analysis identified [N] potential improvements. Should I create backlog items?"

---

## 8. Sensitive Materials

**If any output or artifact is sensitive:**

### Detection Criteria:
- User explicitly flags as sensitive
- Agent detects credentials, keys, private data
- Proprietary information or trade secrets
- Personal/confidential information

### Handling Protocol:
1. Store in `/sensitive/` directory
2. Add `.gitignore` entry if needed
3. Sanitize public-facing references
4. Document sensitivity reason
5. Flag for human review
6. Consider creating redacted public version if appropriate

### Alternative Approaches:
- Create redacted public version in standard folder
- Store only metadata in public catalogue
- Reference by ID without details in public artifacts

---

## 9. Prepare Review

Generate summary/template for pull request using `.github/PULL_REQUEST_TEMPLATE.md`.

### PR Should Include:

**Title Format:**
```
[Atomic/Long-Form] [Project/Theme]: [Short Description]
```

**Example:** `[Atomic] Auth System: Decision Forensics on JWT Implementation`

### Required Sections:

1. **Investigation/Analysis Summary:**
   - Investigation type performed
   - Core insights, metaphors, meta-patterns
   - Key findings and recommendations

2. **Strategic/Subjective Context:**
   - User-provided context
   - Uncertainties addressed
   - Vision alignment notes

3. **Analysis Performed & Rationale:**
   - Menu selections made
   - Analysis methodology
   - Sources examined

4. **Process Memory Entries (if any):**
   - Strategic decisions documented
   - Context pivots noted
   - Learning moments captured

5. **Ripple Effects and Recommendations:**
   - Broader implications
   - Recommended actions or risks
   - Follow-up suggestions

6. **Index/Manifest Updates:**
   - List catalogue changes
   - New entries added
   - Cross-links created

7. **Linked Files/Artifacts:**
   - All added files with paths
   - Modified files listed
   - Related artifacts referenced

### Pre-PR Checklist:
- [ ] All artifacts use proper templates
- [ ] Files saved in correct directories
- [ ] Catalogue index updated
- [ ] Manifest JSON updated and valid
- [ ] Cross-links created where appropriate
- [ ] Process memory created if applicable
- [ ] Backlog/ideas captured if surfaced
- [ ] Sensitive materials properly handled
- [ ] PR description complete and accurate

---

## Best Practices

### Always:
- ✅ **Prompt for context, never infer intent**
- ✅ Use templates for all outputs
- ✅ Label and link artifacts
- ✅ Update catalogue and manifest after every analysis
- ✅ Document assumptions and uncertainties
- ✅ Create process memory for significant insights
- ✅ Handle sensitive materials appropriately

### Consider:
- 💡 Allow atomic-to-long-form escalation when findings warrant
- 💡 Suggest related analyses that might provide additional value
- 💡 Identify patterns across multiple investigations
- 💡 Review backlog and ideas for system improvement
- 💡 Build on prior investigations when relevant

### Never:
- ❌ Infer strategic intent without confirmation
- ❌ Skip template usage
- ❌ Forget to update catalogue and manifest
- ❌ Ignore sensitive materials protocols
- ❌ Create artifacts without cross-linking
- ❌ Miss documenting process memory for key decisions

---

## Quick Reference Workflow

```
┌─────────────────────────────────────────────┐
│ 1. Target Selection                         │
│    → Repository or Document?                │
└────────────────┬────────────────────────────┘
                 │
┌────────────────▼────────────────────────────┐
│ 2. Investigation Type                       │
│    → Atomic or Long-Form?                   │
└────────────────┬────────────────────────────┘
                 │
┌────────────────▼────────────────────────────┐
│ 3. Analysis Menu                            │
│    → Select analysis type(s)                │
└────────────────┬────────────────────────────┘
                 │
┌────────────────▼────────────────────────────┐
│ 4. Strategic Context                        │
│    → Gather user context & goals            │
└────────────────┬────────────────────────────┘
                 │
┌────────────────▼────────────────────────────┐
│ 5. Execute Investigation                    │
│    → Analyze & generate findings            │
└────────────────┬────────────────────────────┘
                 │
┌────────────────▼────────────────────────────┐
│ 6. Save Artifacts & Update Catalogue        │
│    → Store in correct folders               │
└────────────────┬────────────────────────────┘
                 │
┌────────────────▼────────────────────────────┐
│ 7. Post-Analysis                            │
│    → Process memory, cross-link, backlog    │
└────────────────┬────────────────────────────┘
                 │
┌────────────────▼────────────────────────────┐
│ 8. Handle Sensitive Materials               │
│    → Flag and secure if needed              │
└────────────────┬────────────────────────────┘
                 │
┌────────────────▼────────────────────────────┐
│ 9. Prepare Pull Request                     │
│    → Complete PR template & submit          │
└─────────────────────────────────────────────┘
```

---

## Additional Resources

- **[`AGENT_PANEL_WORKFLOW.md`](AGENT_PANEL_WORKFLOW.md)** - Detailed autonomous agent workflow guide
- **[`docs/ANALYSIS_MENU.md`](docs/ANALYSIS_MENU.md)** - Comprehensive analysis type descriptions
- **[`docs/MANIFEST_SCHEMA.md`](docs/MANIFEST_SCHEMA.md)** - Catalogue metadata schema
- **[`docs/AUTOMATION_GUIDE.md`](docs/AUTOMATION_GUIDE.md)** - Implementation patterns
- **[`FOUNDATION.md`](FOUNDATION.md)** - Core principles and system thinking
- **[`CONTRIBUTING.md`](CONTRIBUTING.md)** - Contribution guidelines

---

**End of Agent Intake Workflow**

*This workflow is designed to be agent-executable while maintaining "human in the loop" for strategic validation and context provision. Follow each step sequentially for optimal results.*
