# Reconciliation and submission checklist

## Findings already handled in this consolidation

- Preserved original cells and observations in Source_Records.md; original workbooks unchanged.
- Prefixed master IDs with week numbers; REG-01/API-02 and similar identifiers are not globally unique in sources.
- Consolidated repeated defect aliases into D-001–D-010; triage classifications are explicitly proposed.
- Used the dedicated Week 3 Accessibility Review for ACC descriptions. Task Checklist ACC descriptions/expectations are shifted and ACC-08/09 wording does not align.
- Label-association screenshot exists as ACC-06_Label_Association.png; defect log references ACC-08_Label_Association. Zoom screenshot exists as ACC-08_Browser_Zoom_125.png. Preserve the mismatch and use actual evidence filename.
- Kept Week 5 reused security evidence separate from new executions; N/A checks excluded from applicable counts.
- Distinguished PERF-03 task GET statistics from aggregate login-plus-GET statistics.

## Group actions before final submission

- [ ] Enter team names/student IDs and assign the four coordination roles.
- [ ] Agree the proposed severity/priority decisions and sign off the test plan and quality conclusion.
- [x] Document the two missing helper cases in Executed_Automation_Inventory.md, retaining the original Week 2 register unchanged.
- [x] Reconcile all sixteen API functions in Executed_Automation_Inventory.md: fourteen distinct mapped functions plus two supplemental authentication tests.
- [ ] Resolve D-005 with a clean-session retest on a recorded build. Later passes do not establish when or why the historical observation changed.
- [x] Adopt True as the future oracle for completion exactly now because age zero is within the stated N-day interval. The historical contrary oracle remains identified in UI_Evidence_2026_10_23.md.
- [x] Capture direct Edge screenshots for whitespace-title acceptance and missing success feedback under evidence/verification_2026_10_23/.
- [x] Record Microsoft Edge 155.0.4283.62 and the 1920x1080 test display/viewport for the new UI evidence. Historical Week 3 Edge details remain qualified.
- [x] Execute the high-priority two-account DELETE ownership test on disposable data; CR-001 is confirmed.
- [x] Install the documented Flask/test dependencies in an isolated environment and rerun the full automated suite; preserve known failures.
- [x] Copy all 59 original workbooks/screenshots into evidence/weekly_sources without changing their contents. Source filenames resolve within that folder.
- [x] Retain Presentation_Content.md as the requested presentation deliverable; no `.pptx` file is required for this repository.
- [ ] Complete second-person review and verify the lecturer's final calendar deadline.

## Tool availability

No Ruflo MCP or ToolSearch tool was available in the session's exposed tool catalog. Consolidation used local read-only extraction and deterministic document generation instead. No swarm or external communication was invoked.

## Repair status

- [x] Add all 20 omitted original cases to RTM and map four supplemental functions.
- [x] Replace blanket RTM defects with case-specific canonical links.
- [x] Preserve historical statuses and qualify unsupported cross-user Pass claims.
- [x] Include unchanged application/test sources and hash manifest.
- [x] Add precise future procedures for API-17/API-18.
- [x] Include three isolated verification tests, clearly marked Not Run.
- [x] Execute verification tests and update defect/status records from actual results (38 Pass / 6 Fail across 44 tests).
- [ ] Complete Team_and_Approval.md and final group review.

Earlier completed checklist statements describe the supplied consolidation; this repair did not repeat those historical runs. Week 8/9 documents were outside the repair scope and must adopt the corrected Week 7 qualifications before final submission.

## Verified run — 22 October 2026 (supersedes earlier execution-pending notes)

All three automated test files executed on the copied application using isolated temporary SQLite databases: 44 tests, 38 Pass, 6 Fail, no skips or setup errors. Helpers: 22 Pass/3 Fail; existing API suite: 14 Pass/2 Fail; Week 7 verification: 2 Pass/1 Fail. Evidence: [evidence/verification_2026_10_22/pytest_full_log.txt](evidence/verification_2026_10_22/pytest_full_log.txt); machine-readable results and environment are in the same folder. Source hashes match the included baseline.

D-001, D-002, D-004, D-006 and D-009 reproduced. CR-001 is now dynamically confirmed: B's DELETE returned HTTP 200 and A's subsequent GET returned HTTP 404. W7-VERIFY-01 and W7-VERIFY-02 passed. Current unauthenticated task access is blocked; D-005's historical discrepancy remains unresolved because historical builds are unknown. The historical W1-API-11/API-12 observations remain unchanged; new evidence establishes current GET protection and current DELETE failure.

This run does not execute all 198 documentation records. Manual GUI, browser compatibility, accessibility, historical web observations and performance experiments were not rerun. Structural coverage does not establish correctness: helpers have 100% measured statement/branch coverage while three assertions fail. Overall combined coverage of app.py/helpers.py is approximately 63%; this excludes browser templates, CSS and real browser behaviour.
