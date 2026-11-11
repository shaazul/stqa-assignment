# Software Test Plan and Test Strategy

Project: PyTodo Pro | Course: TEB3433 / TFB3433 | Version: Week 7 consolidation, 22 October 2026

## Purpose and objectives

Evaluate functional correctness, validation, access control, interface usability, selected accessibility and controlled response-time behaviour. Maintain a traceable chain from expected behaviour to test, observation, defect and residual risk. Consolidate Weeks 1–6 without modifying the application under test.

## Basis and scope

Test basis: Group Project.pdf, repository README, helper docstrings and six weekly workbooks. In scope: registration/login/logout, task CRUD, categories/search/filtering, urgency, dashboard, web/API parity, selected Chrome/Edge configurations, basic accessibility, safe local security checks and short Locust experiments. The RTM records derived requirements.

Out of scope for completed evidence: exhaustive penetration testing, production capacity certification, full WCAG conformance, all devices/operating systems, disaster recovery and exhaustive path testing. These are residual risks rather than implied passes.

## Risk-based strategy

Prioritise account identity, unauthenticated and cross-user operations, data integrity and query handling. Use EP/BVA for input and date boundaries; decision tables for authentication/validation combinations; state transitions for task completion; unit tests for pure helper branches; manual GUI/accessibility checks; API positive/negative cases; and short controlled load experiments. Regression protects common workflows and retains defect-revealing tests.

White-box testing deliberately selects four helpers. Their structural coverage cannot be extrapolated to app.py, templates or the entire application. API client tests bypass browser rendering and cannot replace UI checks.

## Environment, tools and data

Historical environment: Windows 11; local Flask/SQLite; Chrome version recorded in Week 3, Edge version missing. Repository dependency: Flask 3.0.3. Tools: Python, pytest, pytest-cov/coverage.py, browser developer tools, Postman and Locust. Screenshot coverage.py version: 7.16.2. Exact versions/build IDs were not consistently captured.

Use disposable accounts, isolated per-test SQLite databases and deterministic task titles. Inject dates for helper boundaries. Separate unauthenticated clients from logged-in sessions. Never reuse real-user records. Record command, timestamp, Python/tool versions, build hash, input and output for subsequent runs. Existing source test credentials are local test values.

## Roles and responsibilities

Roles confirmed in Team_and_Approval.md: QA/Test Lead Farisha Binti Mohamad Zulkefli (22001276) owns scope and release recommendation; Test Design Coordinator Muhammad Danial Hakim b. Jul Ikhram (22003590) reviews expected results and RTM; Automation/Tool Coordinator Elisa Filza Mizwan binti Lius (22002775) owns isolated runs/logs; Defect/Metrics Coordinator Nurfarhana Najihah binti Mohd Fadli (22003122) deduplicates defects and reconciles counts. Each deliverable receives a second-person review. All four members contribute across phases. Reviewer names and review dates are pending and must be entered before submission.

## Entry, suspension and resumption criteria

Enter testing when the selected build starts, dependencies are installed, a disposable database is available, test expectations are reviewable and the environment is recorded. Enter consolidation when weekly workbooks and evidence can be located. Suspend execution if the environment is unavailable, data isolation fails or unexpected destructive effects occur. Resume after restoring the environment/data and verifying a smoke test. Record a Blocked result when an intended test cannot run.

## Exit and acceptance criteria

Proposed product exit criteria: all applicable planned critical tests executed, no unresolved Critical/Major defects, high-priority access/identity/integrity cases passed, every failure linked to a triaged defect, and remaining risks explicitly accepted by the project owner. Present evidence does not meet this product gate because major and high-priority concerns remain.

Documentation exit criteria: master IDs unique, RTM links resolve, duplicates consolidated, execution populations reconciled, evidence gaps disclosed, report and presentation reviewed. Course submission can report failed tests honestly without claiming product acceptance.

## Defect management

Record reproducible expected/actual behaviour and evidence. Triage severity by impact and priority by urgency; preserve original IDs as aliases. Lifecycle: Open → Confirmed → Retest → Closed. A conflicting result returns to Retest with build/session details; a pass alone does not establish a fix. Duplicate records join the same canonical issue. Do not close issues without correction/build evidence and regression confirmation.

## Schedule and deliverables

Week 7: review test basis; formalise this plan; consolidate master cases, RTM, defects and execution status. Week 8: reconcile counts; integrate coverage, API/UI/security/performance findings; assess residual risks and prioritise recommendations. Week 9 integration (course Week 12): contextualise standards, review presentation, rehearse demo and complete submission checks. Exact calendar deadlines remain the lecturer's schedule.

## Control and limitations

Keep original workbooks unchanged and preserve sheet/row references in Source_Records.md. Proposed classifications and newly written procedures must remain distinguishable from historical observations. No complete build history is available, some evidence filenames disagree, and manual results include broad checks rather than atomic tests. See Reconciliation_and_Submission_Checklist.md for unresolved items.

## Controlled source baseline and repair addendum

The application and existing automated tests were located in the neighbouring stqa-assignment directory and copied unchanged into application/. SHA-256 hashes are recorded in evidence/application_sha256.json. This identifies the inspected source snapshot; it does not establish the build used by every historical run. The original application and weekly workbooks were not modified.

Requirements and procedures are derived from the assignment, existing sources and recorded expectations. Reviewed Week 4 negative API procedures are future execution specifications, not retrospectively established original oracles. Historical API access-control Pass conclusions require fresh evidence. CR-001 is a static finding awaiting execution.

Team approval, four coordination roles, reviewers and review dates are recorded in Team_and_Approval.md (approved 11 November 2026). Final deadline confirmed as 27 November 2026.

## Verified run — 22 October 2026 (supersedes earlier execution-pending notes)

All three automated test files executed on the copied application using isolated temporary SQLite databases: 44 tests, 38 Pass, 6 Fail, no skips or setup errors. Helpers: 22 Pass/3 Fail; existing API suite: 14 Pass/2 Fail; Week 7 verification: 2 Pass/1 Fail. Evidence: [evidence/verification_2026_10_22/pytest_full_log.txt](evidence/verification_2026_10_22/pytest_full_log.txt); machine-readable results and environment are in the same folder. Source hashes match the included baseline.

D-001, D-002, D-004, D-006 and D-009 reproduced. CR-001 is now dynamically confirmed: B's DELETE returned HTTP 200 and A's subsequent GET returned HTTP 404. W7-VERIFY-01 and W7-VERIFY-02 passed. Current unauthenticated task access is blocked; D-005's historical discrepancy remains unresolved because historical builds are unknown. The historical W1-API-11/API-12 observations remain unchanged; new evidence establishes current GET protection and current DELETE failure.

This run does not execute all 198 documentation records. Manual GUI, browser compatibility, accessibility, historical web observations and performance experiments were not rerun. Structural coverage does not establish correctness: helpers have 100% measured statement/branch coverage while three assertions fail. Overall combined coverage of app.py/helpers.py is approximately 63%; this excludes browser templates, CSS and real browser behaviour.
