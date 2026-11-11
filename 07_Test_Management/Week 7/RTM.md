# Requirements Traceability Matrix — repaired Week 7

Derived requirements are not a signed baseline. Every master case is mapped. Historical status is separate from review disposition. Defect links identify case-specific canonical issues; aliases remain in the defect log and source records. A mapped case does not establish complete requirement coverage.

## R-01 — Registration validation and uniqueness

| Master case | Scenario | Technique | Historical result | Canonical defect | Review disposition |
|---|---|---|---|---|---|
| W1-REG-01 | Register with valid details | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-REG-02 | Username left empty | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-REG-03 | Password left empty | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-REG-04 | Both fields empty | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-REG-05 | Username below minimum length | BVA | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-REG-06 | Username at minimum length | BVA | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-REG-07 | Username at maximum length | BVA | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-REG-08 | Username above maximum length | BVA | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-REG-09 | Username contains spaces | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-REG-10 | Username contains hyphen | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-REG-11 | Password has 7 characters | BVA | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-REG-12 | Password has 8 characters | BVA | Fail | D-001 | Historical result retained; no new execution in this repair |
| W1-REG-13 | Password has 9 characters | BVA | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-REG-14 | Register using existing username | Decision Table | Fail | D-002 | Historical result retained; no new execution in this repair |
| W1-REG-15 | Username has leading/trailing spaces | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W2-WB-PWD-01 | Wrong type | White-box / Wrong type | Pass | None linked | Historical result retained; no new execution in this repair |
| W2-WB-PWD-02 | 7 characters | White-box / 7 characters | Pass | None linked | Historical result retained; no new execution in this repair |
| W2-WB-PWD-03 | 8 characters boundary | White-box / 8 characters boundary | Fail | D-001 | Historical result retained; no new execution in this repair |
| W2-WB-PWD-04 | 9 characters | White-box / 9 characters | Pass | None linked | Historical result retained; no new execution in this repair |
| W2-WB-USER-01 | Wrong type | White-box / Wrong type | Pass | None linked | Historical result retained; no new execution in this repair |
| W2-WB-USER-02 | 2 characters | White-box / 2 characters | Pass | None linked | Historical result retained; no new execution in this repair |
| W2-WB-USER-03 | 3 characters boundary | White-box / 3 characters boundary | Pass | None linked | Historical result retained; no new execution in this repair |
| W2-WB-USER-04 | 20 characters boundary | White-box / 20 characters boundary | Pass | None linked | Historical result retained; no new execution in this repair |
| W2-WB-USER-05 | 21 characters boundary | White-box / 21 characters boundary | Pass | None linked | Historical result retained; no new execution in this repair |
| W2-WB-USER-06 | Underscore allowed | White-box / Underscore allowed | Pass | None linked | Historical result retained; no new execution in this repair |
| W2-WB-USER-07 | Space disallowed | White-box / Space disallowed | Pass | None linked | Historical result retained; no new execution in this repair |
| W2-WB-USER-08 | Hyphen disallowed | White-box / Hyphen disallowed | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-WEB-01 | Register with a valid unique username and valid password. | Web functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-WEB-02 | Submit a username shorter than the minimum. | Web functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-WEB-03 | Submit a password shorter than the minimum. | Web functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-WEB-04 | Register using an existing username. | Web functional | Fail | D-002 | Historical result retained; no new execution in this repair |
| W4-API-02 | POST /api/register | API | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-API-03 | POST /api/register | API | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-API-04 | POST /api/register | API | Pass | None linked | Historical result retained; no new execution in this repair |
| W5-SEC-03 | Try registering a username that already exists, using a test account. | Security / TH-02 | Fail | D-002 | Historical result retained; no new execution in this repair |
| W5-SEC-07 | Submit a username shorter than the documented minimum using a fresh test value. | Security / TH-08 | Pass | None linked | Historical result retained; no new execution in this repair |
| W5-SEC-08 | Submit a password below the documented minimum using a test account. | Security / TH-08 | Pass | None linked | Historical result retained; no new execution in this repair |
| W6-AUTO-01 | test_registration_with_valid_details | API automation | Pass | None linked | Historical result retained; no new execution in this repair |
| W6-AUTO-02 | test_registration_rejects_username_below_minimum_length | API automation | Pass | None linked | Historical result retained; no new execution in this repair |
| W6-AUTO-03 | test_registration_rejects_short_password | API automation | Pass | None linked | Historical result retained; no new execution in this repair |
| W6-AUTO-04 | test_duplicate_registration_is_rejected | API automation | Fail | D-002 | Historical result retained; no new execution in this repair |

## R-02 — Authentication and session access

| Master case | Scenario | Technique | Historical result | Canonical defect | Review disposition |
|---|---|---|---|---|---|
| W1-LOG-01 | Login with valid credentials | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LOG-02 | Login with incorrect password | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LOG-03 | Login with unknown username | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LOG-04 | Username left empty | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LOG-05 | Password left empty | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LOG-06 | Both fields empty | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LOG-07 | Username contains surrounding spaces | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LOG-08 | Access task list without login | State Transition | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LOG-10 | Access task list after logout | State Transition | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-API-02 | List tasks without login | Decision Table | Fail | D-005 | Historical result retained; no new execution in this repair |
| W1-API-03 | List tasks after login | Decision Table | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-API-11 | User B requests User A task | Access Control | Pass | None linked | Unverified historical Pass: recorded observation does not establish access denial; excluded from verified-pass claims; retest required |
| W4-WEB-05 | Log in with valid credentials. | Web functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-WEB-06 | Log in with incorrect password. | Web functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-API-05 | POST /api/login | API | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-API-06 | POST /api/login | API | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-API-08 | GET /api/tasks | API | Pass | D-005 | Historical result retained; no new execution in this repair |
| W5-SEC-01 | Send request without authentication/session. | Security / TH-01 | Pass | D-005 | Historical result retained; no new execution in this repair |
| W5-SEC-02 | Send request without authentication/session. | Security / TH-01 | Pass | None linked | Historical result retained; no new execution in this repair |
| W5-SEC-05 | If supported, log in as test account A and verify returned tasks belong to A; repeat with test account B. | Security / TH-05 | Pass | None linked | Historical result retained; no new execution in this repair |
| W6-AUTO-05 | Log in with valid credentials | API automation | Pass | None linked | Historical result retained; no new execution in this repair |
| W6-AUTO-06 | test_api_login_rejects_incorrect_password | API automation | Pass | None linked | Historical result retained; no new execution in this repair |
| W6-AUTO-07 | test_authenticated_user_can_create_task | API automation | Pass | None linked | Historical result retained; no new execution in this repair |
| W6-AUTO-08 | test_authenticated_user_cannot_create_task_with_blank_title | API automation | Pass | None linked | Historical result retained; no new execution in this repair |
| W6-AUTO-09 | test_authenticated_user_can_update_task | API automation | Pass | None linked | Historical result retained; no new execution in this repair |
| W6-AUTO-10 | test_authenticated_user_can_complete_task | API automation | Pass | None linked | Historical result retained; no new execution in this repair |
| W6-AUTO-11 | test_authenticated_user_can_delete_task | API automation | Pass | None linked | Historical result retained; no new execution in this repair |
| W6-AUTO-12 | test_authenticated_user_can_search_tasks_by_title | API automation | Pass | None linked | Historical result retained; no new execution in this repair |
| W6-AUTO-13 | GET /api/tasks without authentication returns 401 | API automation | Pass | D-005 | Historical result retained; no new execution in this repair |
| W6-EXTRA-01 | test_api_automation.py::test_unauthenticated_user_cannot_access_dashboard | API automation | Pass | None linked | Supplemental executed function added to register; does not add a historical run |
| W6-EXTRA-02 | test_api_automation.py::test_blank_title_request_without_login_is_rejected | API automation | Pass | None linked | Supplemental executed function added to register; does not add a historical run |

## R-03 — Task creation and title validation

| Master case | Scenario | Technique | Historical result | Canonical defect | Review disposition |
|---|---|---|---|---|---|
| W1-TASK-01 | Create task with title only | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-TASK-02 | Create task with all details | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-TASK-03 | Submit empty title | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-TASK-04 | Submit whitespace-only title | EP | Fail | D-003 | Historical result retained; no new execution in this repair |
| W1-TASK-05 | Create task without description | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-TASK-06 | Create task without category | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-TASK-07 | Create task without due date | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-TASK-08 | Create task with past due date | BVA | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-TASK-09 | Create task due today | BVA | Fail | D-004 | Historical result retained; no new execution in this repair |
| W1-TASK-10 | Create task due in three days | BVA | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-API-04 | Create task through API | Functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-API-05 | Create task with blank title | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-WEB-07 | Create a task with a title and optional fields blank. | Web functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-WEB-08 | Attempt to create a task without a title. | Web functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-API-09 | POST /api/tasks | API | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-API-10 | POST /api/tasks | API | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-CMP-01 | Create equivalent task in browser and API. | UI/API comparison | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-CMP-02 | Submit blank title in UI and POST /api/tasks. | UI/API comparison | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-CMP-05 | Create a task due today and compare UI/API urgency. | UI/API comparison | Pass | None linked | Historical Pass measures UI/API agreement only; it does not prove correct due-today classification. D-004 remains unresolved. |
| W5-SEC-10 | Create/update/delete one disposable test task and check whether an audit/activity history is available. | Security / TH-04 | Not Applicable | None linked | Historical result retained; no new execution in this repair |
| W6-AUTO-07 | test_authenticated_user_can_create_task | API automation | Pass | None linked | Historical result retained; no new execution in this repair |
| W6-AUTO-08 | test_authenticated_user_cannot_create_task_with_blank_title | API automation | Pass | None linked | Historical result retained; no new execution in this repair |
| W6-AUTO-14 | POST /api/tasks with blank title returns 400 | API automation | Pass | None linked | Historical result retained; no new execution in this repair |
| W6-EXTRA-02 | test_api_automation.py::test_blank_title_request_without_login_is_rejected | API automation | Pass | None linked | Supplemental executed function added to register; does not add a historical run |

## R-04 — Task update, completion and deletion

| Master case | Scenario | Technique | Historical result | Canonical defect | Review disposition |
|---|---|---|---|---|---|
| W1-TASK-11 | Edit task title | Functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-TASK-12 | Edit task description | Functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-TASK-13 | Change task category | Functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-TASK-14 | Change due date | Functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-TASK-15 | Edit nonexistent task | Negative | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-TASK-16 | Mark task as completed | State Transition | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-TASK-17 | Reopen completed task | State Transition | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-TASK-18 | Delete own task | State Transition | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-TASK-19 | Delete nonexistent task | Negative | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-DASH-07 | Check dashboard after deletion | Functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-API-08 | Update task | Functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-API-09 | Delete own task | Functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-API-12 | User B attempts to delete User A task | Access Control | Pass | None linked | Unverified historical Pass: recorded observation does not establish access denial; excluded from verified-pass claims; retest required |
| W4-WEB-09 | Edit a task title or due date and save. | Web functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-WEB-10 | Mark a task complete. | Web functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-WEB-11 | Delete a disposable test task. | Web functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-API-12 | PUT /api/tasks/{task_id} | API | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-API-13 | DELETE /api/tasks/{task_id} | API | Pass | None linked | Historical result retained; no new execution in this repair |
| W5-SEC-09 | If roles/privileges exist, try the action as a non-privileged test user; otherwise mark Not Applicable. | Security / TH-07 | Not Applicable | None linked | Historical result retained; no new execution in this repair |
| W5-SEC-10 | Create/update/delete one disposable test task and check whether an audit/activity history is available. | Security / TH-04 | Not Applicable | None linked | Historical result retained; no new execution in this repair |
| W6-AUTO-09 | test_authenticated_user_can_update_task | API automation | Pass | None linked | Historical result retained; no new execution in this repair |
| W6-AUTO-10 | test_authenticated_user_can_complete_task | API automation | Pass | None linked | Historical result retained; no new execution in this repair |
| W6-AUTO-11 | test_authenticated_user_can_delete_task | API automation | Pass | None linked | Historical result retained; no new execution in this repair |

## R-05 — Urgency and due-date boundaries

| Master case | Scenario | Technique | Historical result | Canonical defect | Review disposition |
|---|---|---|---|---|---|
| W1-URG-01 | No due date | BVA / State Transition | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-URG-02 | Due yesterday | BVA / State Transition | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-URG-03 | Due today | BVA / State Transition | Fail | D-004 | Historical result retained; no new execution in this repair |
| W1-URG-04 | Due tomorrow | BVA / State Transition | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-URG-05 | Due in two days | BVA / State Transition | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-URG-06 | Due in three days | BVA / State Transition | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-URG-07 | Completed task with due date | BVA / State Transition | Pass | None linked | Historical result retained; no new execution in this repair |
| W2-WB-URG-01 | No due date | White-box / No due date | Pass | None linked | Historical result retained; no new execution in this repair |
| W2-WB-URG-02 | Past date | White-box / Past date | Pass | None linked | Historical result retained; no new execution in this repair |
| W2-WB-URG-03 | Due today boundary | White-box / Due today boundary | Fail | D-004 | Historical result retained; no new execution in this repair |
| W2-WB-URG-04 | +2 days boundary | White-box / +2 days boundary | Pass | None linked | Historical result retained; no new execution in this repair |
| W2-WB-URG-05 | +3 days boundary | White-box / +3 days boundary | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-CMP-05 | Create a task due today and compare UI/API urgency. | UI/API comparison | Pass | None linked | Historical Pass measures UI/API agreement only; it does not prove correct due-today classification. D-004 remains unresolved. |
| W2-EXTRA-01 | test_helpers.py::test_urg_06_uses_current_date_when_today_not_provided | Unit branch test | Pass | None linked | Supplemental executed function added to register; does not add a historical run |

## R-06 — Dashboard completion window

| Master case | Scenario | Technique | Historical result | Canonical defect | Review disposition |
|---|---|---|---|---|---|
| W1-DASH-01 | Open dashboard | Functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-DASH-02 | Check total tasks | Functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-DASH-03 | Check open tasks | Functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-DASH-04 | Check overdue tasks | Functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-DASH-05 | Check due-soon tasks | Functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-DASH-06 | Check completed this week | State Transition | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-DASH-07 | Check dashboard after deletion | Functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-DASH-08 | Dashboard with no tasks | Functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-API-10 | Access dashboard API | Functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W2-WB-DAY-01 | Missing value | White-box / Missing value | Pass | None linked | Historical result retained; no new execution in this repair |
| W2-WB-DAY-02 | Recent completion | White-box / Recent completion | Pass | None linked | Historical result retained; no new execution in this repair |
| W2-WB-DAY-03 | Exactly N days boundary | White-box / Exactly N days boundary | Fail | D-006 | Historical result retained; no new execution in this repair |
| W2-WB-DAY-04 | Future completion | White-box / Future completion | Pass | None linked | Historical result retained; no new execution in this repair |
| W2-WB-DAY-05 | Exactly now | White-box / Exactly now | Pass | None linked | Historical result retained; no new execution in this repair |
| W2-WB-DAY-06 | Older than N days | White-box / Older than N days | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-WEB-13 | Compare dashboard counts/urgency with task list. | Web functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-API-14 | GET /api/dashboard | API | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-API-15 | GET /api/dashboard | API | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-CMP-04 | Compare dashboard UI with GET /api/dashboard. | UI/API comparison | Pass | None linked | Historical result retained; no new execution in this repair |
| W5-SEC-02 | Send request without authentication/session. | Security / TH-01 | Pass | None linked | Historical result retained; no new execution in this repair |
| W2-EXTRA-02 | test_helpers.py::test_day_07_uses_current_time_when_now_not_provided | Unit branch test | Pass | None linked | Supplemental executed function added to register; does not add a historical run |
| W6-EXTRA-01 | test_api_automation.py::test_unauthenticated_user_cannot_access_dashboard | API automation | Pass | None linked | Supplemental executed function added to register; does not add a historical run |

## R-07 — Category integrity

| Master case | Scenario | Technique | Historical result | Canonical defect | Review disposition |
|---|---|---|---|---|---|
| W1-TASK-06 | Create task without category | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-TASK-13 | Change task category | Functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LIST-03 | Filter by Work category | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LIST-04 | Filter by Personal category | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LIST-05 | Filter by Study category | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LIST-06 | Filter by Urgent category | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LIST-11 | Combine category and status filters | Decision Table | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-API-01 | Retrieve categories | Functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-WEB-12 | Search by title and use category/status filters. | Web functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-API-01 | GET /api/categories | API | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-API-17 | POST /api/tasks | API | Fail | D-009 | Historical result retained; no new execution in this repair |
| W5-SEC-04 | Submit a test task with an invalid category_id type/value. | Security / TH-03 | Fail | D-009 | Historical result retained; no new execution in this repair |
| W6-AUTO-15 | test_api_rejects_invalid_category_id | API automation | Fail | D-009 | Historical result retained; no new execution in this repair |

## R-08 — Search, filtering and task retrieval

| Master case | Scenario | Technique | Historical result | Canonical defect | Review disposition |
|---|---|---|---|---|---|
| W1-LIST-01 | Open task list | Functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LIST-02 | Open empty task list | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LIST-03 | Filter by Work category | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LIST-04 | Filter by Personal category | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LIST-05 | Filter by Study category | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LIST-06 | Filter by Urgent category | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LIST-07 | Filter open tasks | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LIST-08 | Filter completed tasks | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LIST-09 | Search existing title | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LIST-10 | Search nonexistent title | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LIST-11 | Combine category and status filters | Decision Table | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LIST-12 | Search using partial title | EP | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-API-06 | Retrieve existing task | Functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-API-07 | Retrieve nonexistent task | Negative | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-WEB-12 | Search by title and use category/status filters. | Web functional | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-API-07 | GET /api/tasks | API | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-API-11 | GET /api/tasks/999999 | API | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-API-16 | GET /api/tasks | API | Pass | None linked | Historical result retained; no new execution in this repair |
| W4-API-18 | GET /api/tasks?q=' OR 1=1 -- | API | Fail | D-010 | Historical result retained; no new execution in this repair |
| W4-CMP-03 | Complete task in UI and inspect via GET /api/tasks. | UI/API comparison | Pass | None linked | Historical result retained; no new execution in this repair |
| W5-SEC-06 | Send one SQL-like search string once, using a test session. | Security / TH-06 | Fail | D-010 | Historical result retained; no new execution in this repair |
| W6-AUTO-12 | test_authenticated_user_can_search_tasks_by_title | API automation | Pass | None linked | Historical result retained; no new execution in this repair |

## R-09 — GUI consistency, feedback and navigation

| Master case | Scenario | Technique | Historical result | Canonical defect | Review disposition |
|---|---|---|---|---|---|
| W3-GUI-01 | Check all forms and input fields. | Manual review | Pass | None linked | Historical result retained; no new execution in this repair |
| W3-GUI-02 | Check buttons and their actions. | Manual review | Pass | None linked | Historical result retained; no new execution in this repair |
| W3-GUI-03 | Check links and navigation links. | Manual review | Pass | None linked | Historical result retained; no new execution in this repair |
| W3-GUI-04 | Check labels and instructions. | Manual review | Pass | None linked | Historical result retained; no new execution in this repair |
| W3-GUI-05 | Check page navigation and menu items. | Manual review | Pass | None linked | Historical result retained; no new execution in this repair |
| W3-GUI-06 | Check success, warning and error messages. | Manual review | Fail | D-007 | Historical result retained; no new execution in this repair |
| W3-GUI-07 | Check visual consistency. | Manual review | Pass | None linked | Historical result retained; no new execution in this repair |
| W3-GUI-08 | Check layout at a narrower browser-window width. | Manual review | Pass | None linked | Historical result retained; no new execution in this repair |
| W3-USE-01 | Evaluate ease of navigation. | Manual review | Pass | None linked | Historical result retained; no new execution in this repair |
| W3-USE-02 | Evaluate feedback and system responses. | Manual review | Fail | D-007 | Historical result retained; no new execution in this repair |
| W3-USE-03 | Evaluate consistency across pages. | Manual review | Pass | None linked | Historical result retained; no new execution in this repair |
| W3-USE-04 | Evaluate error prevention and recovery. | Manual review | Fail | D-004 | Historical result retained; no new execution in this repair |
| W3-USE-05 | Evaluate understandability. | Manual review | Pass | None linked | Historical result retained; no new execution in this repair |

## R-10 — Supported browser configurations

| Master case | Scenario | Technique | Historical result | Canonical defect | Review disposition |
|---|---|---|---|---|---|
| W3-COMP-01 | Test the application in the group's primary browser. | Manual review | Pass | None linked | Historical result retained; no new execution in this repair |
| W3-COMP-02 | Test the application in a second available browser, if available. | Manual review | Pass | None linked | Historical result retained; no new execution in this repair |
| W3-COMP-03 | Test a different screen/window configuration available to the group. | Manual review | Pass | None linked | Historical result retained; no new execution in this repair |
| W3-COMP-04 | Compare key pages across tested configurations. | Manual review | Pass | None linked | Historical result retained; no new execution in this repair |

## R-11 — Basic accessibility

| Master case | Scenario | Technique | Historical result | Canonical defect | Review disposition |
|---|---|---|---|---|---|
| W3-ACC-01 | Meaningful images have alternative text where applicable. | Basic accessibility review | N/A | None linked | Historical result retained; no new execution in this repair |
| W3-ACC-02 | Text and background have readable contrast. | Basic accessibility review | Pass | None linked | Historical result retained; no new execution in this repair |
| W3-ACC-03 | All main interactive elements can be reached by keyboard. | Basic accessibility review | Pass | None linked | Historical result retained; no new execution in this repair |
| W3-ACC-04 | Keyboard focus is visible and follows a logical order. | Basic accessibility review | Pass | None linked | Historical result retained; no new execution in this repair |
| W3-ACC-05 | Labels and instructions are clear and readable. | Basic accessibility review | Pass | None linked | Historical result retained; no new execution in this repair |
| W3-ACC-06 | Validation and error messages explain how to correct mistakes. | Basic accessibility review | Pass | None linked | Historical result retained; no new execution in this repair |
| W3-ACC-07 | Navigation and controls behave consistently. | Basic accessibility review | Pass | None linked | Historical result retained; no new execution in this repair |
| W3-ACC-08 | Page structure and controls have meaningful names/semantics where inspectable. | Basic accessibility review | Fail | D-008 | Historical result retained; no new execution in this repair |
| W3-ACC-09 | Content remains usable with browser zoom/text enlargement. | Basic accessibility review | Pass | None linked | Historical result retained; no new execution in this repair |

## R-12 — Security-oriented behaviour

| Master case | Scenario | Technique | Historical result | Canonical defect | Review disposition |
|---|---|---|---|---|---|
| W1-API-11 | User B requests User A task | Access Control | Pass | None linked | Unverified historical Pass: recorded observation does not establish access denial; excluded from verified-pass claims; retest required |
| W4-API-18 | GET /api/tasks?q=' OR 1=1 -- | API | Fail | D-010 | Historical result retained; no new execution in this repair |
| W5-SEC-01 | Send request without authentication/session. | Security / TH-01 | Pass | D-005 | Historical result retained; no new execution in this repair |
| W5-SEC-02 | Send request without authentication/session. | Security / TH-01 | Pass | None linked | Historical result retained; no new execution in this repair |
| W5-SEC-03 | Try registering a username that already exists, using a test account. | Security / TH-02 | Fail | D-002 | Historical result retained; no new execution in this repair |
| W5-SEC-04 | Submit a test task with an invalid category_id type/value. | Security / TH-03 | Fail | D-009 | Historical result retained; no new execution in this repair |
| W5-SEC-05 | If supported, log in as test account A and verify returned tasks belong to A; repeat with test account B. | Security / TH-05 | Pass | None linked | Historical result retained; no new execution in this repair |
| W5-SEC-06 | Send one SQL-like search string once, using a test session. | Security / TH-06 | Fail | D-010 | Historical result retained; no new execution in this repair |
| W5-SEC-07 | Submit a username shorter than the documented minimum using a fresh test value. | Security / TH-08 | Pass | None linked | Historical result retained; no new execution in this repair |
| W5-SEC-08 | Submit a password below the documented minimum using a test account. | Security / TH-08 | Pass | None linked | Historical result retained; no new execution in this repair |
| W5-SEC-09 | If roles/privileges exist, try the action as a non-privileged test user; otherwise mark Not Applicable. | Security / TH-07 | Not Applicable | None linked | Historical result retained; no new execution in this repair |
| W5-SEC-10 | Create/update/delete one disposable test task and check whether an audit/activity history is available. | Security / TH-04 | Not Applicable | None linked | Historical result retained; no new execution in this repair |

## R-14 — Logout and persistence

| Master case | Scenario | Technique | Historical result | Canonical defect | Review disposition |
|---|---|---|---|---|---|
| W1-LOG-09 | Logout | State Transition | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-LOG-10 | Access task list after logout | State Transition | Pass | None linked | Historical result retained; no new execution in this repair |
| W1-TASK-20 | Verify changes after refresh | Functional | Pass | None linked | Historical result retained; no new execution in this repair |

## R-13 — Controlled performance

| Experiment | Workload | Evidence | Result |
|---|---|---|---|
| PERF-01 | 10 sequential requests / 97 s | Week 5 Performance Result row 5 | 10 success; p95 unavailable |
| PERF-02 | 2 users / 30 s | PERF-02.png | 41 task GETs; p95 16 ms; zero failures |
| PERF-03 | 5 users / 30 s | PERF-03.png | 97 task GETs; p95 15 ms; zero failures |



## Unresolved coverage

W1-API-11 and W1-API-12 remain unverified historical passes. Cross-user DELETE failed in the new test_week7_verification.py run; see CR-001 and Verification_Plan.md. Malformed types, recovery, long-term reliability, screen-reader operation and production capacity remain incomplete.

## Verified run — 22 October 2026 (supersedes earlier execution-pending notes)

All three automated test files executed on the copied application using isolated temporary SQLite databases: 44 tests, 38 Pass, 6 Fail, no skips or setup errors. Helpers: 22 Pass/3 Fail; existing API suite: 14 Pass/2 Fail; Week 7 verification: 2 Pass/1 Fail. Evidence: [evidence/verification_2026_10_22/pytest_full_log.txt](evidence/verification_2026_10_22/pytest_full_log.txt); machine-readable results and environment are in the same folder. Source hashes match the included baseline.

D-001, D-002, D-004, D-006 and D-009 reproduced. CR-001 is now dynamically confirmed: B's DELETE returned HTTP 200 and A's subsequent GET returned HTTP 404. W7-VERIFY-01 and W7-VERIFY-02 passed. Current unauthenticated task access is blocked; D-005's historical discrepancy remains unresolved because historical builds are unknown. The historical W1-API-11/API-12 observations remain unchanged; new evidence establishes current GET protection and current DELETE failure.

This run does not execute all 198 documentation records. Manual GUI, browser compatibility, accessibility, historical web observations and performance experiments were not rerun. Structural coverage does not establish correctness: helpers have 100% measured statement/branch coverage while three assertions fail. Overall combined coverage of app.py/helpers.py is approximately 63%; this excludes browser templates, CSS and real browser behaviour.
