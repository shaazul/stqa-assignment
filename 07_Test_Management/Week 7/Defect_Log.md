# Consolidated defect log

Severity and priority below are proposed Week 7 triage decisions. Original classifications remain in Source_Records.md. Critical = catastrophic impact; Major = core function/security disruption; Moderate = incorrect behaviour with limited scope; Minor = low-impact presentation/feedback. High priority addresses identity, access, integrity or core failure first. Confirmed means supported by execution evidence or inspected screenshot, not fixed. Open means recorded but insufficient new confirmation; Retest means contradictory results need reconciliation; Closed requires verified correction and regression evidence. No fix is claimed.

## Register

| ID | Title | Feature | Severity | Priority | Status | Original IDs |
|---|---|---|---|---|---|---|
| D-001 | Eight-character password rejected | Registration | Moderate | Medium | Confirmed | DEF-01; DEF-W2-02 |
| D-002 | Duplicate username accepted | Registration | Moderate | High | Confirmed | DEF-02; BUG-W4-03; BUG-W5-01; BUG-W6-01 |
| D-003 | Whitespace-only title accepted through web form | Task creation | Moderate | Medium | Open | DEF-03 |
| D-004 | Due-today task classified as Overdue | Urgency | Moderate | High | Confirmed | DEF-04; DEF-W2-01 |
| D-005 | Historical unauthenticated task access conflicts with later evidence | API authentication | Major | High | Retest | DEF-05 |
| D-006 | Completion exactly N days ago excluded | Dashboard / helper | Moderate | Medium | Confirmed | DEF-W2-03 |
| D-007 | No task-creation confirmation | GUI feedback | Minor | Medium | Open | BUG-01 (Week 3) |
| D-008 | Form labels lack programmatic association | Accessibility | Moderate | Medium | Confirmed | BUG-02 (Week 3) |
| D-009 | Invalid category accepted | Task API validation | Moderate | High | Confirmed | BUG-W4-01; BUG-W5-02 |
| D-010 | SQL-like search causes server error | Task search | Major | High | Confirmed | BUG-W4-02; BUG-W5-03 |


## D-001

| Field | Detail |
|---|---|
| Title | Eight-character password rejected |
| Affected feature | Registration |
| Environment | Historical Windows 11 / local Flask / SQLite; helper retest uses current Python. Exact build hashes absent in historical evidence. |
| Preconditions | Disposable local test account; authenticated session where stated; fixed clock for helper boundaries. |
| Steps to reproduce | Register with a fresh valid username and password abc12345; or invoke is_valid_password("abc12345"). |
| Expected | At least eight characters accepted. |
| Actual | False / rejected. |
| Severity / priority | Moderate / Medium |
| Status | Confirmed |
| Original IDs | DEF-01; DEF-W2-02 |
| Related tests | W1-REG-12; W2-WB-PWD-03 |
| Evidence | Week 2 screenshots; current helper log |


## D-002

| Field | Detail |
|---|---|
| Title | Duplicate username accepted |
| Affected feature | Registration |
| Environment | Historical Windows 11 / local Flask / SQLite; helper retest uses current Python. Exact build hashes absent in historical evidence. |
| Preconditions | Disposable local test account; authenticated session where stated; fixed clock for helper boundaries. |
| Steps to reproduce | Register one test username, then register it again. |
| Expected | Second registration rejected; no additional account. |
| Actual | Second registration returns HTTP 201. |
| Severity / priority | Moderate / High |
| Status | Confirmed |
| Original IDs | DEF-02; BUG-W4-03; BUG-W5-01; BUG-W6-01 |
| Related tests | W1-REG-14; W4-WEB-04; W5-SEC-03; W6-AUTO-04 |
| Evidence | week6_pytest_log.txt; SEC-03.png |


## D-003

| Field | Detail |
|---|---|
| Title | Whitespace-only title accepted through web form |
| Affected feature | Task creation |
| Environment | Historical Windows 11 / local Flask / SQLite; helper retest uses current Python. Exact build hashes absent in historical evidence. |
| Preconditions | Disposable local test account; authenticated session where stated; fixed clock for helper boundaries. |
| Steps to reproduce | Log in; submit three spaces as Title on New Task. |
| Expected | Reject whitespace-only title server-side. |
| Actual | Blank-looking task created. |
| Severity / priority | Moderate / Medium |
| Status | Open |
| Original IDs | DEF-03 |
| Related tests | W1-TASK-04 |
| Evidence | Week 1 case and defect record; screenshot missing |


## D-004

| Field | Detail |
|---|---|
| Title | Due-today task classified as Overdue |
| Affected feature | Urgency |
| Environment | Historical Windows 11 / local Flask / SQLite; helper retest uses current Python. Exact build hashes absent in historical evidence. |
| Preconditions | Disposable local test account; authenticated session where stated; fixed clock for helper boundaries. |
| Steps to reproduce | Call compute_urgency with due date equal to injected today. |
| Expected | Due Today. |
| Actual | Overdue. |
| Severity / priority | Moderate / High |
| Status | Confirmed |
| Original IDs | DEF-04; DEF-W2-01 |
| Related tests | W1-TASK-09; W1-URG-03; W2-WB-URG-03 |
| Evidence | Current helper log; branch_coverage_2.png |


## D-005

| Field | Detail |
|---|---|
| Title | Historical unauthenticated task access conflicts with later evidence |
| Affected feature | API authentication |
| Environment | Historical Windows 11 / local Flask / SQLite; helper retest uses current Python. Exact build hashes absent in historical evidence. |
| Preconditions | Disposable local test account; authenticated session where stated; fixed clock for helper boundaries. |
| Steps to reproduce | Clear all cookies; GET /api/tasks with a fresh client; record build and session. |
| Expected | HTTP 401 without private data. |
| Actual | Week 1 records a task list; later evidence reports HTTP 401. |
| Severity / priority | Major / High |
| Status | Retest |
| Original IDs | DEF-05 |
| Related tests | W1-API-02; W4-API-08; W5-SEC-01; W6-AUTO-13 |
| Evidence | Week 1 record; SEC-01.png; supplied Week 6 log |


## D-006

| Field | Detail |
|---|---|
| Title | Completion exactly N days ago excluded |
| Affected feature | Dashboard / helper |
| Environment | Historical Windows 11 / local Flask / SQLite; helper retest uses current Python. Exact build hashes absent in historical evidence. |
| Preconditions | Disposable local test account; authenticated session where stated; fixed clock for helper boundaries. |
| Steps to reproduce | Invoke helper with n=7, now=2026-10-19 12:00:00, completed=2026-10-12 12:00:00. |
| Expected | True under inclusive N-day specification. |
| Actual | False. |
| Severity / priority | Moderate / Medium |
| Status | Confirmed |
| Original IDs | DEF-W2-03 |
| Related tests | W2-WB-DAY-03 |
| Evidence | Current helper log; branch_coverage_2.png |


## D-007

| Field | Detail |
|---|---|
| Title | No task-creation confirmation |
| Affected feature | GUI feedback |
| Environment | Historical Windows 11 / local Flask / SQLite; helper retest uses current Python. Exact build hashes absent in historical evidence. |
| Preconditions | Disposable local test account; authenticated session where stated; fixed clock for helper boundaries. |
| Steps to reproduce | Create a valid task in the web UI. |
| Expected | Clear success feedback. |
| Actual | Task created with no confirmation message. |
| Severity / priority | Minor / Medium |
| Status | Open |
| Original IDs | BUG-01 (Week 3) |
| Related tests | W3-GUI-06; W3-USE-02 |
| Evidence | Week 3 observation; separate screenshot absent |


## D-008

| Field | Detail |
|---|---|
| Title | Form labels lack programmatic association |
| Affected feature | Accessibility |
| Environment | Historical Windows 11 / local Flask / SQLite; helper retest uses current Python. Exact build hashes absent in historical evidence. |
| Preconditions | Disposable local test account; authenticated session where stated; fixed clock for helper boundaries. |
| Steps to reproduce | Inspect Title label/input on New Task. |
| Expected | Matching for/id attributes or correctly nested control. |
| Actual | Separate label/input have no association in screenshot. |
| Severity / priority | Moderate / Medium |
| Status | Confirmed |
| Original IDs | BUG-02 (Week 3) |
| Related tests | W3-ACC-08 |
| Evidence | week 3 evidence/ACC-06_Label_Association.png |


## D-009

| Field | Detail |
|---|---|
| Title | Invalid category accepted |
| Affected feature | Task API validation |
| Environment | Historical Windows 11 / local Flask / SQLite; helper retest uses current Python. Exact build hashes absent in historical evidence. |
| Preconditions | Disposable local test account; authenticated session where stated; fixed clock for helper boundaries. |
| Steps to reproduce | Authenticate; POST task with category_id="invalid" or nonexistent 99999. |
| Expected | Controlled validation error; task not created. |
| Actual | HTTP 201 and invalid category stored. |
| Severity / priority | Moderate / High |
| Status | Confirmed |
| Original IDs | BUG-W4-01; BUG-W5-02 |
| Related tests | W4-API-17; W5-SEC-04; W6-AUTO-15 |
| Evidence | API-17.png; SEC-04.png; supplied Week 6 log |


## D-010

| Field | Detail |
|---|---|
| Title | SQL-like search causes server error |
| Affected feature | Task search |
| Environment | Historical Windows 11 / local Flask / SQLite; helper retest uses current Python. Exact build hashes absent in historical evidence. |
| Preconditions | Disposable local test account; authenticated session where stated; fixed clock for helper boundaries. |
| Steps to reproduce | Authenticate; GET /api/tasks with q=' OR 1=1 -- against local disposable data. |
| Expected | Controlled response without query interpretation or server error. |
| Actual | HTTP 500; SQLite binding error recorded. |
| Severity / priority | Major / High |
| Status | Confirmed |
| Original IDs | BUG-W4-02; BUG-W5-03 |
| Related tests | W4-API-18; W5-SEC-06 |
| Evidence | week 4 evidence/API-18.png |

## CR-001 — Cross-user API deletion: dynamically confirmed

| Field | Detail |
|---|---|
| Affected feature | DELETE /api/tasks/{task_id} |
| Evidence | application/app.py, api_delete_task: DELETE FROM tasks WHERE id = ? without user_id predicate |
| Classification | Confirmed access-control defect; reproduced by isolated two-account test |
| Proposed severity / priority | Major / High |
| Status | Confirmed — 22 October 2026 |
| Preconditions | Two separate authenticated clients; account A owns a disposable task; isolated database |
| Procedure | Run application/test_week7_verification.py::test_cross_user_delete_is_denied_and_owner_task_survives |
| Expected | B receives 403 or 404; A can still retrieve the unchanged task |
| Actual | B DELETE returned HTTP 200; subsequent owner A GET returned HTTP 404; see evidence/verification_2026_10_22/pytest_full_log.txt |
| Related requirement / case | R-04; R-12; W1-API-12; planned W7-VERIFY-03 |

## Evidence and reference clarification

Evidence names above resolve under evidence/weekly_sources/ unless they refer to evidence/current_helpers_pytest.txt or evidence/historical_week6_pytest_log.txt. week6_pytest_log.txt denotes the latter saved log. CR-001 is separate from the ten consolidated historical defects and is now confirmed in the new run; keep historical and current populations distinct. W3-USE-04 relates to D-004 based on the recorded urgency observation.

## Verified run — 22 October 2026 (supersedes earlier execution-pending notes)

All three automated test files executed on the copied application using isolated temporary SQLite databases: 44 tests, 38 Pass, 6 Fail, no skips or setup errors. Helpers: 22 Pass/3 Fail; existing API suite: 14 Pass/2 Fail; Week 7 verification: 2 Pass/1 Fail. Evidence: [evidence/verification_2026_10_22/pytest_full_log.txt](evidence/verification_2026_10_22/pytest_full_log.txt); machine-readable results and environment are in the same folder. Source hashes match the included baseline.

D-001, D-002, D-004, D-006 and D-009 reproduced. CR-001 is now dynamically confirmed: B's DELETE returned HTTP 200 and A's subsequent GET returned HTTP 404. W7-VERIFY-01 and W7-VERIFY-02 passed. Current unauthenticated task access is blocked; D-005's historical discrepancy remains unresolved because historical builds are unknown. The historical W1-API-11/API-12 observations remain unchanged; new evidence establishes current GET protection and current DELETE failure.

This run does not execute all 198 documentation records. Manual GUI, browser compatibility, accessibility, historical web observations and performance experiments were not rerun. Structural coverage does not establish correctness: helpers have 100% measured statement/branch coverage while three assertions fail. Overall combined coverage of app.py/helpers.py is approximately 63%; this excludes browser templates, CSS and real browser behaviour.
