# Master test-case repository — repaired Week 7

Original results remain historical observations. Review dispositions qualify unsupported conclusions. Reviewed procedures and added supplemental rows do not claim new execution. Source workbooks remain unchanged. Application/test sources are in application/.

## Index

| Master ID | Feature | Historical status |
|---|---|---|
| W1-REG-01 | Registration | Pass |
| W1-REG-02 | Registration | Pass |
| W1-REG-03 | Registration | Pass |
| W1-REG-04 | Registration | Pass |
| W1-REG-05 | Registration | Pass |
| W1-REG-06 | Registration | Pass |
| W1-REG-07 | Registration | Pass |
| W1-REG-08 | Registration | Pass |
| W1-REG-09 | Registration | Pass |
| W1-REG-10 | Registration | Pass |
| W1-REG-11 | Registration | Pass |
| W1-REG-12 | Registration | Fail |
| W1-REG-13 | Registration | Pass |
| W1-REG-14 | Registration | Fail |
| W1-REG-15 | Registration | Pass |
| W1-LOG-01 | Login | Pass |
| W1-LOG-02 | Login | Pass |
| W1-LOG-03 | Login | Pass |
| W1-LOG-04 | Login | Pass |
| W1-LOG-05 | Login | Pass |
| W1-LOG-06 | Login | Pass |
| W1-LOG-07 | Login | Pass |
| W1-LOG-08 | Login / Access | Pass |
| W1-LOG-09 | Logout | Pass |
| W1-LOG-10 | Logout / Access | Pass |
| W1-TASK-01 | Create Task | Pass |
| W1-TASK-02 | Create Task | Pass |
| W1-TASK-03 | Create Task | Pass |
| W1-TASK-04 | Create Task | Fail |
| W1-TASK-05 | Create Task | Pass |
| W1-TASK-06 | Create Task | Pass |
| W1-TASK-07 | Create Task | Pass |
| W1-TASK-08 | Create Task | Pass |
| W1-TASK-09 | Create Task | Fail |
| W1-TASK-10 | Create Task | Pass |
| W1-TASK-11 | Edit Task | Pass |
| W1-TASK-12 | Edit Task | Pass |
| W1-TASK-13 | Edit Task | Pass |
| W1-TASK-14 | Edit Task | Pass |
| W1-TASK-15 | Edit Task | Pass |
| W1-TASK-16 | Task Status | Pass |
| W1-TASK-17 | Task Status | Pass |
| W1-TASK-18 | Delete Task | Pass |
| W1-TASK-19 | Delete Task | Pass |
| W1-TASK-20 | Persistence | Pass |
| W1-LIST-01 | Task List | Pass |
| W1-LIST-02 | Task List | Pass |
| W1-LIST-03 | Category Filter | Pass |
| W1-LIST-04 | Category Filter | Pass |
| W1-LIST-05 | Category Filter | Pass |
| W1-LIST-06 | Category Filter | Pass |
| W1-LIST-07 | Status Filter | Pass |
| W1-LIST-08 | Status Filter | Pass |
| W1-LIST-09 | Title Search | Pass |
| W1-LIST-10 | Title Search | Pass |
| W1-LIST-11 | Combined Filter | Pass |
| W1-LIST-12 | Title Search | Pass |
| W1-DASH-01 | Dashboard | Pass |
| W1-DASH-02 | Dashboard | Pass |
| W1-DASH-03 | Dashboard | Pass |
| W1-DASH-04 | Dashboard | Pass |
| W1-DASH-05 | Dashboard | Pass |
| W1-DASH-06 | Dashboard | Pass |
| W1-DASH-07 | Dashboard | Pass |
| W1-DASH-08 | Dashboard | Pass |
| W1-URG-01 | Task Urgency | Pass |
| W1-URG-02 | Task Urgency | Pass |
| W1-URG-03 | Task Urgency | Fail |
| W1-URG-04 | Task Urgency | Pass |
| W1-URG-05 | Task Urgency | Pass |
| W1-URG-06 | Task Urgency | Pass |
| W1-URG-07 | Task Urgency | Pass |
| W1-API-01 | API / Categories | Pass |
| W1-API-02 | API Authentication | Fail |
| W1-API-03 | API Authentication | Pass |
| W1-API-04 | API Create Task | Pass |
| W1-API-05 | API Create Task | Pass |
| W1-API-06 | API Task Detail | Pass |
| W1-API-07 | API Task Detail | Pass |
| W1-API-08 | API Update Task | Pass |
| W1-API-09 | API Delete Task | Pass |
| W1-API-10 | API Dashboard | Pass |
| W1-API-11 | User Data Isolation | Pass |
| W1-API-12 | User Data Isolation | Pass |
| W2-WB-URG-01 | compute_urgency | Pass |
| W2-WB-URG-02 | compute_urgency | Pass |
| W2-WB-URG-03 | compute_urgency | Fail |
| W2-WB-URG-04 | compute_urgency | Pass |
| W2-WB-URG-05 | compute_urgency | Pass |
| W2-WB-PWD-01 | is_valid_password | Pass |
| W2-WB-PWD-02 | is_valid_password | Pass |
| W2-WB-PWD-03 | is_valid_password | Fail |
| W2-WB-PWD-04 | is_valid_password | Pass |
| W2-WB-USER-01 | is_valid_username | Pass |
| W2-WB-USER-02 | is_valid_username | Pass |
| W2-WB-USER-03 | is_valid_username | Pass |
| W2-WB-USER-04 | is_valid_username | Pass |
| W2-WB-USER-05 | is_valid_username | Pass |
| W2-WB-USER-06 | is_valid_username | Pass |
| W2-WB-USER-07 | is_valid_username | Pass |
| W2-WB-USER-08 | is_valid_username | Pass |
| W2-WB-DAY-01 | completed_in_last_n_days | Pass |
| W2-WB-DAY-02 | completed_in_last_n_days | Pass |
| W2-WB-DAY-03 | completed_in_last_n_days | Fail |
| W2-WB-DAY-04 | completed_in_last_n_days | Pass |
| W2-WB-DAY-05 | completed_in_last_n_days | Pass |
| W2-WB-DAY-06 | completed_in_last_n_days | Pass |
| W3-GUI-01 | GUI Testing | Pass |
| W3-GUI-02 | GUI Testing | Pass |
| W3-GUI-03 | GUI Testing | Pass |
| W3-GUI-04 | GUI Testing | Pass |
| W3-GUI-05 | GUI Testing | Pass |
| W3-GUI-06 | GUI Testing | Fail |
| W3-GUI-07 | GUI Testing | Pass |
| W3-GUI-08 | GUI Testing | Pass |
| W3-COMP-01 | Compatibility / Configuration | Pass |
| W3-COMP-02 | Compatibility / Configuration | Pass |
| W3-COMP-03 | Compatibility / Configuration | Pass |
| W3-COMP-04 | Compatibility / Configuration | Pass |
| W3-USE-01 | Usability | Pass |
| W3-USE-02 | Usability | Fail |
| W3-USE-03 | Usability | Pass |
| W3-USE-04 | Usability | Fail |
| W3-USE-05 | Usability | Pass |
| W3-ACC-01 | Accessibility / Perceivable | N/A |
| W3-ACC-02 | Accessibility / Perceivable | Pass |
| W3-ACC-03 | Accessibility / Operable | Pass |
| W3-ACC-04 | Accessibility / Operable | Pass |
| W3-ACC-05 | Accessibility / Understandable | Pass |
| W3-ACC-06 | Accessibility / Understandable | Pass |
| W3-ACC-07 | Accessibility / Understandable | Pass |
| W3-ACC-08 | Accessibility / Robust | Fail |
| W3-ACC-09 | Accessibility / Robust | Pass |
| W4-WEB-01 | Registration | Pass |
| W4-WEB-02 | Registration validation | Pass |
| W4-WEB-03 | Registration validation | Pass |
| W4-WEB-04 | Duplicate registration | Fail |
| W4-WEB-05 | Login | Pass |
| W4-WEB-06 | Login validation | Pass |
| W4-WEB-07 | Task creation | Pass |
| W4-WEB-08 | Task validation | Pass |
| W4-WEB-09 | Task update | Pass |
| W4-WEB-10 | Task completion | Pass |
| W4-WEB-11 | Task deletion | Pass |
| W4-WEB-12 | Search/filter | Pass |
| W4-WEB-13 | Dashboard | Pass |
| W4-API-01 | /api/categories | Pass |
| W4-API-02 | /api/register | Pass |
| W4-API-03 | /api/register | Pass |
| W4-API-04 | /api/register | Pass |
| W4-API-05 | /api/login | Pass |
| W4-API-06 | /api/login | Pass |
| W4-API-07 | /api/tasks | Pass |
| W4-API-08 | /api/tasks | Pass |
| W4-API-09 | /api/tasks | Pass |
| W4-API-10 | /api/tasks | Pass |
| W4-API-11 | /api/tasks/999999 | Pass |
| W4-API-12 | /api/tasks/{task_id} | Pass |
| W4-API-13 | /api/tasks/{task_id} | Pass |
| W4-API-14 | /api/dashboard | Pass |
| W4-API-15 | /api/dashboard | Pass |
| W4-API-16 | /api/tasks | Pass |
| W4-API-17 | /api/tasks | Fail |
| W4-API-18 | /api/tasks?q=' OR 1=1 -- | Fail |
| W4-CMP-01 | Task creation | Pass |
| W4-CMP-02 | Blank task title | Pass |
| W4-CMP-03 | Task completion | Pass |
| W4-CMP-04 | Dashboard counts | Pass |
| W4-CMP-05 | Due-date urgency | Pass |
| W5-SEC-01 | GET /api/tasks | Pass |
| W5-SEC-02 | GET /api/dashboard | Pass |
| W5-SEC-03 | POST /api/register | Fail |
| W5-SEC-04 | POST /api/tasks | Fail |
| W5-SEC-05 | GET /api/tasks | Pass |
| W5-SEC-06 | GET /api/tasks?q=... | Fail |
| W5-SEC-07 | POST /api/register | Pass |
| W5-SEC-08 | POST /api/register | Pass |
| W5-SEC-09 | Privileged function (if any) | Not Applicable |
| W5-SEC-10 | Task activity history | Not Applicable |
| W6-AUTO-01 | WEB-01 | Pass |
| W6-AUTO-02 | WEB-02 | Pass |
| W6-AUTO-03 | WEB-03 | Pass |
| W6-AUTO-04 | WEB-04 | Fail |
| W6-AUTO-05 | WEB-05 | Pass |
| W6-AUTO-06 | WEB-06 | Pass |
| W6-AUTO-07 | WEB-07 | Pass |
| W6-AUTO-08 | WEB-08 | Pass |
| W6-AUTO-09 | WEB-09 | Pass |
| W6-AUTO-10 | WEB-10 | Pass |
| W6-AUTO-11 | WEB-11 | Pass |
| W6-AUTO-12 | WEB-12 | Pass |
| W6-AUTO-13 | API-08 | Pass |
| W6-AUTO-14 | API-10 | Pass |
| W6-AUTO-15 | API-17 | Fail |
| W2-EXTRA-01 | Urgency default date | Pass |
| W2-EXTRA-02 | Completion default time | Pass |
| W6-EXTRA-01 | Dashboard authentication | Pass |
| W6-EXTRA-02 | Authentication precedes validation | Pass |

## W1-REG-01

| Field | Record |
|---|---|
| id | REG-01 |
| feature | Registration |
| tech | EP |
| objective | Register with valid details |
| preconditions | Logged out; register page open |
| data | Username: farish01; Password: TestPass123 |
| steps | 1. Open Register. 2. Enter username/password. 3. Submit. |
| expected | Account is created; appropriate confirmation/navigation appears. |
| actual | Registration succeeded and the application displayed the task list with the logged-in username farish01 |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 5 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W1-REG-02

| Field | Record |
|---|---|
| id | REG-02 |
| feature | Registration |
| tech | EP |
| objective | Username left empty |
| preconditions | Register page open |
| data | Username: blank; Password: TestPass123 |
| steps | Leave username blank; submit. |
| expected | Registration is rejected; no account is created. |
| actual | The browser displayed the validation message "Please fill out this field" and prevented form submission. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 6 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W1-REG-03

| Field | Record |
|---|---|
| id | REG-03 |
| feature | Registration |
| tech | EP |
| objective | Password left empty |
| preconditions | Register page open |
| data | Username: farish02; Password: blank |
| steps | Leave password blank; submit. |
| expected | Registration is rejected; no account is created. |
| actual | The browser displayed “Please fill out this field” and prevented form submission when the password field was empty. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 7 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W1-REG-04

| Field | Record |
|---|---|
| id | REG-04 |
| feature | Registration |
| tech | EP |
| objective | Both fields empty |
| preconditions | Register page open |
| data | Username: blank; Password: blank |
| steps | Leave both fields blank; submit. |
| expected | Registration is rejected; no account is created. |
| actual | The browser displayed “Please fill out this field” and prevented submission when both fields were empty. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 8 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W1-REG-05

| Field | Record |
|---|---|
| id | REG-05 |
| feature | Registration |
| tech | BVA |
| objective | Username below minimum length |
| preconditions | Register page open |
| data | Username: ab (2 chars); Password: TestPass123 |
| steps | Submit registration. |
| expected | Registration rejected; username must be 3–20 characters. |
| actual | The application displayed “Username must be 3–20 characters (letters, numbers, underscore)” and rejected the username. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 9 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W1-REG-06

| Field | Record |
|---|---|
| id | REG-06 |
| feature | Registration |
| tech | BVA |
| objective | Username at minimum length |
| preconditions | Register page open |
| data | Username: abc (3 chars); Password: TestPass123 |
| steps | Submit registration. |
| expected | Username length is valid; account should be created if username is unique. |
| actual | The application accepted the username abc, created the account and redirected to the My Tasks page. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 10 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W1-REG-07

| Field | Record |
|---|---|
| id | REG-07 |
| feature | Registration |
| tech | BVA |
| objective | Username at maximum length |
| preconditions | Register page open |
| data | Username: abcdefghijklmnopqrst (20 chars); Password: TestPass123 |
| steps | Submit registration. |
| expected | Username length is valid; account should be created if unique. |
| actual | The application accepted the username and redirected to the My Tasks page. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 11 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W1-REG-08

| Field | Record |
|---|---|
| id | REG-08 |
| feature | Registration |
| tech | BVA |
| objective | Username above maximum length |
| preconditions | Register page open |
| data | Username: abcdefghijklmnopqrstu (21 chars); Password: TestPass123 |
| steps | Submit registration. |
| expected | Registration rejected; username must be 3–20 characters. |
| actual | The application displayed “Username must be 3–20 characters (letters, numbers, underscore)” and rejected the 21-character username. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 12 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W1-REG-09

| Field | Record |
|---|---|
| id | REG-09 |
| feature | Registration |
| tech | EP |
| objective | Username contains spaces |
| preconditions | Register page open |
| data | Username: test user; Password: TestPass123 |
| steps | Submit registration. |
| expected | Registration rejected because spaces are not allowed in username. |
| actual | The application displayed “Username must be 3–20 characters (letters, numbers, underscore)” and rejected the username containing a space. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 13 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W1-REG-10

| Field | Record |
|---|---|
| id | REG-10 |
| feature | Registration |
| tech | EP |
| objective | Username contains hyphen |
| preconditions | Register page open |
| data | Username: test-user; Password: TestPass123 |
| steps | Submit registration. |
| expected | Registration rejected because hyphen is not an allowed username character. |
| actual | Registration is rejected because hyphens are not allowed in usernames. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 14 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W1-REG-11

| Field | Record |
|---|---|
| id | REG-11 |
| feature | Registration |
| tech | BVA |
| objective | Password has 7 characters |
| preconditions | Register page open |
| data | Username: farish11; Password: abc1234 (7 chars) |
| steps | Submit registration. |
| expected | Registration rejected. |
| actual | The application displayed “Password must be at least 8 characters” and rejected the password. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 15 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W1-REG-12

| Field | Record |
|---|---|
| id | REG-12 |
| feature | Registration |
| tech | BVA |
| objective | Password has 8 characters |
| preconditions | Register page open |
| data | Username: farish12; Password: abc12345 (8 chars) |
| steps | Submit registration. |
| expected | Check actual behaviour; implementation may reject although message says at least 8 characters. |
| actual | The application rejected the password and displayed “Password must be at least 8 characters.” |
| status | Fail |
| evidence | Not recorded in source |
| defect | D-001 |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 16 |
| Original defect reference | DEF-01 |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W1-REG-13

| Field | Record |
|---|---|
| id | REG-13 |
| feature | Registration |
| tech | BVA |
| objective | Password has 9 characters |
| preconditions | Register page open |
| data | Username: farish13; Password: abc123456 (9 chars) |
| steps | Submit registration. |
| expected | Password passes length validation; account created if username is unique. |
| actual | The application accepted the credentials, created the account and redirected to the My Tasks page. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 17 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W1-REG-14

| Field | Record |
|---|---|
| id | REG-14 |
| feature | Registration |
| tech | Decision Table |
| objective | Register using existing username |
| preconditions | qauser01 already registered |
| data | Username: farish01; Password: TestPass123 |
| steps | Submit registration using the same username again. |
| expected | Check whether duplicate username is rejected or another account is created. |
| actual | The application displayed the My Tasks page with farish01 logged in instead of displaying a duplicate-username error. |
| status | Fail |
| evidence | Not recorded in source |
| defect | D-002 |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 18 |
| Original defect reference | DEF-02 |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W1-REG-15

| Field | Record |
|---|---|
| id | REG-15 |
| feature | Registration |
| tech | EP |
| objective | Username has leading/trailing spaces |
| preconditions | Register page open; use unused username |
| data | Username: ' farish15 '; Password: TestPass123 |
| steps | Enter username with spaces around it and submit. |
| expected | Spaces are trimmed before validation; observe the stored/accepted username. |
| actual | The application displayed the My Tasks page, with the logged-in username farish15 visible in the navigation bar. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 19 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W1-LOG-01

| Field | Record |
|---|---|
| id | LOG-01 |
| feature | Login |
| tech | EP |
| objective | Login with valid credentials |
| preconditions | Account exists; logged out |
| data | Username: farish01; Password: TestPass123 |
| steps | Open Login; enter credentials; submit. |
| expected | Login succeeds and user reaches authenticated page. |
| actual | The application displayed the My Tasks page, with the logged-in username farish01 visible in the navigation bar. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 20 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02 |

## W1-LOG-02

| Field | Record |
|---|---|
| id | LOG-02 |
| feature | Login |
| tech | EP |
| objective | Login with incorrect password |
| preconditions | Account exists; logged out |
| data | Username: farish01; Password: WrongPass123 |
| steps | Submit login. |
| expected | Login rejected. |
| actual | The application displayed “Invalid username or password” and remained on the Login page. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 21 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02 |

## W1-LOG-03

| Field | Record |
|---|---|
| id | LOG-03 |
| feature | Login |
| tech | EP |
| objective | Login with unknown username |
| preconditions | Logged out |
| data | Username: nobody987; Password: TestPass123 |
| steps | Submit login. |
| expected | Login rejected. |
| actual | The application displayed “Invalid username or password” and remained on the Login page. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 22 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02 |

## W1-LOG-04

| Field | Record |
|---|---|
| id | LOG-04 |
| feature | Login |
| tech | EP |
| objective | Username left empty |
| preconditions | Logged out |
| data | Username: blank; Password: TestPass123 |
| steps | Submit login. |
| expected | Login rejected. |
| actual | The browser displayed “Please fill out this field” and prevented form submission when the username field was empty. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 23 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02 |

## W1-LOG-05

| Field | Record |
|---|---|
| id | LOG-05 |
| feature | Login |
| tech | EP |
| objective | Password left empty |
| preconditions | Logged out |
| data | Username: farish01; Password: blank |
| steps | Submit login. |
| expected | Login rejected. |
| actual | The browser displayed “Please fill out this field” and prevented form submission when the password field was empty. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 24 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02 |

## W1-LOG-06

| Field | Record |
|---|---|
| id | LOG-06 |
| feature | Login |
| tech | EP |
| objective | Both fields empty |
| preconditions | Logged out |
| data | Username: blank; Password: blank |
| steps | Submit login. |
| expected | Login rejected. |
| actual | The browser displayed “Please fill out this field” and prevented form submission when both fields were empty. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 25 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02 |

## W1-LOG-07

| Field | Record |
|---|---|
| id | LOG-07 |
| feature | Login |
| tech | EP |
| objective | Username contains surrounding spaces |
| preconditions | Account exists; logged out |
| data | Username: ' farish01 '; Password: TestPass123 |
| steps | Enter username with surrounding spaces and submit. |
| expected | Check whether login succeeds after trimming. |
| actual | My Tasks page displayed with farish01 logged in; the screenshot does not confirm whether surrounding spaces were entered. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 26 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02 |

## W1-LOG-08

| Field | Record |
|---|---|
| id | LOG-08 |
| feature | Login / Access |
| tech | State Transition |
| objective | Access task list without login |
| preconditions | Logged out |
| data | URL: http://127.0.0.1:5000/ |
| steps | Open task list URL. |
| expected | Redirected to login. |
| actual | The application displayed the Login page at /login instead of showing the task list. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 27 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02 |

## W1-LOG-09

| Field | Record |
|---|---|
| id | LOG-09 |
| feature | Logout |
| tech | State Transition |
| objective | Logout |
| preconditions | Logged in |
| data | Click Logout |
| steps | Click Logout in the interface. |
| expected | Session ends and user is redirected to login or public page. |
| actual | The application logged the user out and displayed the Login page. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 28 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-14 |

## W1-LOG-10

| Field | Record |
|---|---|
| id | LOG-10 |
| feature | Logout / Access |
| tech | State Transition |
| objective | Access task list after logout |
| preconditions | Logged out after LOG-09 |
| data | URL: http://127.0.0.1:5000/ |
| steps | Enter task list URL after logout. |
| expected | Redirected to login; protected tasks are not displayed. |
| actual | The application displayed the Login page instead of the task list after logout. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 29 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02; R-14 |

## W1-TASK-01

| Field | Record |
|---|---|
| id | TASK-01 |
| feature | Create Task |
| tech | EP |
| objective | Create task with title only |
| preconditions | Logged in |
| data | Title: Complete STQA |
| steps | Open New Task; enter title; save. |
| expected | Task is created and appears in task list. |
| actual | The application created the task Complete STQA and displayed it in the task list with no category, no due date, and urgency shown as “No due date”. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 30 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-03 |

## W1-TASK-02

| Field | Record |
|---|---|
| id | TASK-02 |
| feature | Create Task |
| tech | EP |
| objective | Create task with all details |
| preconditions | Logged in |
| data | Title: STQA full task; Description: Testing practice; Category: Work; Due date: choose valid date |
| steps | Fill all available fields and save. |
| expected | Task is created with supplied details. |
| actual | The task STQA full task appears in the task list with category Work, due date 2026-10-31, and urgency Upcoming. The description is not visible in this screenshot. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 31 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-03 |

## W1-TASK-03

| Field | Record |
|---|---|
| id | TASK-03 |
| feature | Create Task |
| tech | EP |
| objective | Submit empty title |
| preconditions | Logged in |
| data | Title: blank |
| steps | Open New Task; leave title blank; submit. |
| expected | Observe whether an empty task is created; record exact result. |
| actual | The browser displayed “Please fill out this field” and prevented the form from being submitted. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 32 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-03 |

## W1-TASK-04

| Field | Record |
|---|---|
| id | TASK-04 |
| feature | Create Task |
| tech | EP |
| objective | Submit whitespace-only title |
| preconditions | Logged in |
| data | Title: three spaces |
| steps | Enter spaces as title; submit. |
| expected | Observe whether whitespace-only title is accepted. |
| actual | The application created a task with a blank-looking title and displayed it in the task list. |
| status | Fail |
| evidence | Not recorded in source |
| defect | D-003 |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 33 |
| Original defect reference | DEF-03 |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-03 |

## W1-TASK-05

| Field | Record |
|---|---|
| id | TASK-05 |
| feature | Create Task |
| tech | EP |
| objective | Create task without description |
| preconditions | Logged in |
| data | Title: No description; Description: blank |
| steps | Create and save task. |
| expected | Task is created if description is optional. |
| actual | The task Review STQA Notes appeared in the task list even though the description was blank. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 34 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-03 |

## W1-TASK-06

| Field | Record |
|---|---|
| id | TASK-06 |
| feature | Create Task |
| tech | EP |
| objective | Create task without category |
| preconditions | Logged in |
| data | Title: No category; category: blank/default |
| steps | Submit task form without selecting category. |
| expected | Record whether task is created and which category is used. |
| actual | The task No category was created successfully. The Category and Due Date columns display —. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 35 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-03; R-07 |

## W1-TASK-07

| Field | Record |
|---|---|
| id | TASK-07 |
| feature | Create Task |
| tech | EP |
| objective | Create task without due date |
| preconditions | Logged in |
| data | Title: No due date; Due date: blank |
| steps | Save task without due date. |
| expected | Task is created; urgency is No due date. |
| actual | The application created the task successfully. The Due Date column displays — and the Urgency column displays No due date. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 36 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-03 |

## W1-TASK-08

| Field | Record |
|---|---|
| id | TASK-08 |
| feature | Create Task |
| tech | BVA |
| objective | Create task with past due date |
| preconditions | Logged in |
| data | Title: Past due; Due date: yesterday |
| steps | Create task and inspect urgency. |
| expected | Task is created; urgency is Overdue. |
| actual | The application created the task with the due date 17/10/2026 and displayed the urgency as Overdue. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 37 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-03 |

## W1-TASK-09

| Field | Record |
|---|---|
| id | TASK-09 |
| feature | Create Task |
| tech | BVA |
| objective | Create task due today |
| preconditions | Logged in |
| data | Title: Due today; Due date: today's date |
| steps | Create task and inspect urgency. |
| expected | Expected label per stated spec: Due Today; record actual label. |
| actual | The task was created successfully, but the urgency label displayed was Overdue. |
| status | Fail |
| evidence | Not recorded in source |
| defect | D-004 |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 38 |
| Original defect reference | DEF-04 |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-03 |

## W1-TASK-10

| Field | Record |
|---|---|
| id | TASK-10 |
| feature | Create Task |
| tech | BVA |
| objective | Create task due in three days |
| preconditions | Logged in |
| data | Title: Upcoming; Due date: today + 3 days |
| steps | Create task and inspect urgency. |
| expected | Urgency is Upcoming. |
| actual | The task was created successfully with the due date 21/10/2026 and the urgency label Upcoming. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 39 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-03 |

## W1-TASK-11

| Field | Record |
|---|---|
| id | TASK-11 |
| feature | Edit Task |
| tech | Functional |
| objective | Edit task title |
| preconditions | Logged in; own task exists |
| data | Updated title: Updated STQA Task |
| steps | Open task edit form; change title; save. |
| expected | New title is saved. |
| actual | The task title was updated successfully and displayed as Updated STQA Task in the task list. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 40 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-04 |

## W1-TASK-12

| Field | Record |
|---|---|
| id | TASK-12 |
| feature | Edit Task |
| tech | Functional |
| objective | Edit task description |
| preconditions | Logged in; own task exists |
| data | Description: Updated description |
| steps | Edit description and save. |
| expected | New description is saved. |
| actual | The description was updated and saved successfully. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 41 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-04 |

## W1-TASK-13

| Field | Record |
|---|---|
| id | TASK-13 |
| feature | Edit Task |
| tech | Functional |
| objective | Change task category |
| preconditions | Logged in; own task exists |
| data | Category: Study |
| steps | Edit category and save. |
| expected | Category changes to Study. |
| actual | The task category was successfully changed to Study, and the task displayed the updated category. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 42 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-04; R-07 |

## W1-TASK-14

| Field | Record |
|---|---|
| id | TASK-14 |
| feature | Edit Task |
| tech | Functional |
| objective | Change due date |
| preconditions | Logged in; own task exists |
| data | Choose a different valid date |
| steps | Edit due date and save. |
| expected | New due date is saved. |
| actual | The task's due date changed from 2026-10-21 to 2026-10-22. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 43 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-04 |

## W1-TASK-15

| Field | Record |
|---|---|
| id | TASK-15 |
| feature | Edit Task |
| tech | Negative |
| objective | Edit nonexistent task |
| preconditions | Logged in |
| data | URL: /tasks/999999/edit (verify ID does not exist) |
| steps | Open URL. |
| expected | Application redirects or displays a not-found response; no other task is modified. |
| actual | The browser displayed the My Tasks page after the request for a nonexistent task's edit page. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 44 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-04 |

## W1-TASK-16

| Field | Record |
|---|---|
| id | TASK-16 |
| feature | Task Status |
| tech | State Transition |
| objective | Mark task as completed |
| preconditions | Logged in; open task exists |
| data | Select completion control for own task |
| steps | Mark task done. |
| expected | Task is marked Done. |
| actual | The task was marked completed. A check mark appeared, the title was crossed out, and the urgency changed to Done. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 45 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-04 |

## W1-TASK-17

| Field | Record |
|---|---|
| id | TASK-17 |
| feature | Task Status |
| tech | State Transition |
| objective | Reopen completed task |
| preconditions | Logged in; done task exists |
| data | Select completion control for done task |
| steps | Mark task open again. |
| expected | Task returns to open state. |
| actual | The task was successfully reopened. The strikethrough disappeared, the completion circle became empty, and the urgency returned to Upcoming. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 46 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-04 |

## W1-TASK-18

| Field | Record |
|---|---|
| id | TASK-18 |
| feature | Delete Task |
| tech | State Transition |
| objective | Delete own task |
| preconditions | Logged in; own disposable task exists |
| data | Delete the selected task |
| steps | Use delete control if available; confirm if prompted. |
| expected | Task disappears from list. |
| actual | The task was successfully deleted and removed from the task list. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 47 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-04 |

## W1-TASK-19

| Field | Record |
|---|---|
| id | TASK-19 |
| feature | Delete Task |
| tech | Negative |
| objective | Delete nonexistent task |
| preconditions | Logged in |
| data | Task ID: 999999 |
| steps | Attempt deletion through available route/API if permitted. |
| expected | No unrelated task is deleted; appropriate not-found handling. |
| actual | The application returned a redirect to the task list. No unrelated task was deleted. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 48 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-04 |

## W1-TASK-20

| Field | Record |
|---|---|
| id | TASK-20 |
| feature | Persistence |
| tech | Functional |
| objective | Verify changes after refresh |
| preconditions | Task edited or completed |
| data | Refresh browser page |
| steps | Refresh and inspect the same task. |
| expected | Changes persist after refresh. |
| actual | The task changes remained saved and displayed correctly after refreshing the browser. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 49 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-14 |

## W1-LIST-01

| Field | Record |
|---|---|
| id | LIST-01 |
| feature | Task List |
| tech | Functional |
| objective | Open task list |
| preconditions | Logged in |
| data | URL: / |
| steps | Open task list. |
| expected | Current user's tasks are displayed. |
| actual | The My Tasks page opened successfully and displayed the current user's tasks with their details and filtering options. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 50 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-08 |

## W1-LIST-02

| Field | Record |
|---|---|
| id | LIST-02 |
| feature | Task List |
| tech | EP |
| objective | Open empty task list |
| preconditions | Use test account with no tasks |
| data | No tasks |
| steps | Open task list. |
| expected | Empty state shown without error. |
| actual | The empty task list displayed “No tasks match your filters.” without any error. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 51 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-08 |

## W1-LIST-03

| Field | Record |
|---|---|
| id | LIST-03 |
| feature | Category Filter |
| tech | EP |
| objective | Filter by Work category |
| preconditions | Logged in; tasks exist in multiple categories |
| data | Category: Work |
| steps | Select Work category filter. |
| expected | Only tasks in selected category appear. |
| actual | Only the task “STQA full task” with category Work was displayed after applying the filter. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 52 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-07; R-08 |

## W1-LIST-04

| Field | Record |
|---|---|
| id | LIST-04 |
| feature | Category Filter |
| tech | EP |
| objective | Filter by Personal category |
| preconditions | Logged in; tasks exist in multiple categories |
| data | Category: Personal |
| steps | Select Personal category filter. |
| expected | Only tasks in selected category appear. |
| actual | The Personal category filter was applied, but no tasks matched the selected category because no Personal-category tasks existed. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 53 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-07; R-08 |

## W1-LIST-05

| Field | Record |
|---|---|
| id | LIST-05 |
| feature | Category Filter |
| tech | EP |
| objective | Filter by Study category |
| preconditions | Logged in; tasks exist in multiple categories |
| data | Category: Study |
| steps | Select Study category filter. |
| expected | Only tasks in selected category appear. |
| actual | Only the task “Upcoming” with category Study was displayed after applying the filter. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 54 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-07; R-08 |

## W1-LIST-06

| Field | Record |
|---|---|
| id | LIST-06 |
| feature | Category Filter |
| tech | EP |
| objective | Filter by Urgent category |
| preconditions | Logged in; tasks exist in multiple categories |
| data | Category: Urgent |
| steps | Select Urgent category filter. |
| expected | Only tasks in selected category appear. |
| actual | Only the task “No category,” assigned to the Urgent category, was displayed after applying the filter. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 55 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-07; R-08 |

## W1-LIST-07

| Field | Record |
|---|---|
| id | LIST-07 |
| feature | Status Filter |
| tech | EP |
| objective | Filter open tasks |
| preconditions | Logged in; open and done tasks exist |
| data | Status: Open |
| steps | Select Open filter. |
| expected | Only incomplete tasks appear. |
| actual | The Open filter displayed incomplete tasks, including “Upcoming,” “Due today,” and “STQA full task.” |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 56 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-08 |

## W1-LIST-08

| Field | Record |
|---|---|
| id | LIST-08 |
| feature | Status Filter |
| tech | EP |
| objective | Filter completed tasks |
| preconditions | Logged in; open and done tasks exist |
| data | Status: Done |
| steps | Select Done filter. |
| expected | Only completed tasks appear. |
| actual | Only the completed task “Past Due Task” was displayed after applying the Done filter. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 57 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-08 |

## W1-LIST-09

| Field | Record |
|---|---|
| id | LIST-09 |
| feature | Title Search |
| tech | EP |
| objective | Search existing title |
| preconditions | Logged in; known task title exists |
| data | Search: STQA |
| steps | Enter STQA in search box. |
| expected | Matching tasks appear. |
| actual | Three matching tasks containing “STQA” appeared: “Review STQA Notes,” “STQA full task,” and “Updated STQA Task.” |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 58 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-08 |

## W1-LIST-10

| Field | Record |
|---|---|
| id | LIST-10 |
| feature | Title Search |
| tech | EP |
| objective | Search nonexistent title |
| preconditions | Logged in |
| data | Search: XYZ123NOTFOUND |
| steps | Search for the text. |
| expected | No matching tasks appear. |
| actual | No tasks matched the search text XYZ123NOTFOUND; the page displayed “No tasks match your filters.” |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 59 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-08 |

## W1-LIST-11

| Field | Record |
|---|---|
| id | LIST-11 |
| feature | Combined Filter |
| tech | Decision Table |
| objective | Combine category and status filters |
| preconditions | Logged in; open/done tasks in Work category |
| data | Category: Work; Status: Open |
| steps | Apply both filters. |
| expected | Only open Work tasks appear. |
| actual | Only the incomplete task “STQA full task” in the Work category was displayed after applying both filters. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 60 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-07; R-08 |

## W1-LIST-12

| Field | Record |
|---|---|
| id | LIST-12 |
| feature | Title Search |
| tech | EP |
| objective | Search using partial title |
| preconditions | Logged in; known title exists |
| data | Search a unique substring |
| steps | Enter partial title. |
| expected | Matching task appears. |
| actual | Searching for “Upcoming” displayed the matching task “Upcoming” with category Study and due date 2026-10-22. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 61 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-08 |

## W1-DASH-01

| Field | Record |
|---|---|
| id | DASH-01 |
| feature | Dashboard |
| tech | Functional |
| objective | Open dashboard |
| preconditions | Logged in |
| data | URL: /dashboard |
| steps | Open dashboard. |
| expected | Dashboard loads. |
| actual | The dashboard loaded successfully and displayed the task summary cards without an error. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 62 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-06 |

## W1-DASH-02

| Field | Record |
|---|---|
| id | DASH-02 |
| feature | Dashboard |
| tech | Functional |
| objective | Check total tasks |
| preconditions | Logged in; create exactly three tasks and no other tasks on test account |
| data | 3 tasks |
| steps | Open dashboard. |
| expected | Total counter equals 3. |
| actual | Dashboard displayed 3 total tasks, 3 open tasks, 0 overdue, 0 due soon, and 0 completed. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 63 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-06 |

## W1-DASH-03

| Field | Record |
|---|---|
| id | DASH-03 |
| feature | Dashboard |
| tech | Functional |
| objective | Check open tasks |
| preconditions | Logged in; exactly two open tasks exist |
| data | 2 open tasks |
| steps | Open dashboard. |
| expected | Open counter equals 2. |
| actual | Dashboard displayed 2 total tasks, 2 open tasks, 0 overdue, 0 due soon, and 0 completed. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 64 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-06 |

## W1-DASH-04

| Field | Record |
|---|---|
| id | DASH-04 |
| feature | Dashboard |
| tech | Functional |
| objective | Check overdue tasks |
| preconditions | Logged in; one overdue open task exists |
| data | Due date: yesterday |
| steps | Open dashboard. |
| expected | Overdue counter includes the overdue task. |
| actual | The dashboard displayed 2 overdue tasks, matching the two tasks marked overdue in the task list. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 65 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-06 |

## W1-DASH-05

| Field | Record |
|---|---|
| id | DASH-05 |
| feature | Dashboard |
| tech | Functional |
| objective | Check due-soon tasks |
| preconditions | Logged in; one open task due tomorrow |
| data | Due date: tomorrow |
| steps | Open dashboard. |
| expected | Due Soon counter includes the task. |
| actual | The task list showed “No category” due on 2026-10-19 with urgency Due Soon. The dashboard displayed Due Soon: 1. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 66 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-06 |

## W1-DASH-06

| Field | Record |
|---|---|
| id | DASH-06 |
| feature | Dashboard |
| tech | State Transition |
| objective | Check completed this week |
| preconditions | Logged in; complete a task today |
| data | Complete one task |
| steps | Open dashboard. |
| expected | Completed in last 7 days counter increases. |
| actual | After marking “Due today” as completed, the dashboard's Completed (last 7 days) counter increased from 0 to 1. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 67 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-06 |

## W1-DASH-07

| Field | Record |
|---|---|
| id | DASH-07 |
| feature | Dashboard |
| tech | Functional |
| objective | Check dashboard after deletion |
| preconditions | Logged in; known task exists |
| data | Delete one task |
| steps | Delete task; revisit dashboard. |
| expected | Relevant counters update. |
| actual | Dashboard total increased to 10 after adding a task and returned to 9 after deleting it. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 68 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-04; R-06 |

## W1-DASH-08

| Field | Record |
|---|---|
| id | DASH-08 |
| feature | Dashboard |
| tech | Functional |
| objective | Dashboard with no tasks |
| preconditions | Logged in with empty test account |
| data | No tasks |
| steps | Open dashboard. |
| expected | All counters are zero. |
| actual | All dashboard counters display 0. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 69 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-06 |

## W1-URG-01

| Field | Record |
|---|---|
| id | URG-01 |
| feature | Task Urgency |
| tech | BVA / State Transition |
| objective | No due date |
| preconditions | Logged in; can create task and set due date |
| data | Due date: blank |
| steps | Create or update task; inspect urgency label. |
| expected | No due date |
| actual | Task displays “No due date” as its urgency label. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 70 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-05 |

## W1-URG-02

| Field | Record |
|---|---|
| id | URG-02 |
| feature | Task Urgency |
| tech | BVA / State Transition |
| objective | Due yesterday |
| preconditions | Logged in; can create task and set due date |
| data | Due date: today - 1 day |
| steps | Create or update task; inspect urgency label. |
| expected | Overdue |
| actual | The task displays the urgency label “Overdue”. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 71 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-05 |

## W1-URG-03

| Field | Record |
|---|---|
| id | URG-03 |
| feature | Task Urgency |
| tech | BVA / State Transition |
| objective | Due today |
| preconditions | Logged in; can create task and set due date |
| data | Due date: today |
| steps | Create or update task; inspect urgency label. |
| expected | Due Today per stated specification; record actual label |
| actual | The task was created successfully, but the urgency label displayed Overdue instead of Due Today. |
| status | Fail |
| evidence | Not recorded in source |
| defect | D-004 |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 72 |
| Original defect reference | DEF-04 |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-05 |

## W1-URG-04

| Field | Record |
|---|---|
| id | URG-04 |
| feature | Task Urgency |
| tech | BVA / State Transition |
| objective | Due tomorrow |
| preconditions | Logged in; can create task and set due date |
| data | Due date: today + 1 day |
| steps | Create or update task; inspect urgency label. |
| expected | Due Soon |
| actual | The task displays “Due Soon”. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 73 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-05 |

## W1-URG-05

| Field | Record |
|---|---|
| id | URG-05 |
| feature | Task Urgency |
| tech | BVA / State Transition |
| objective | Due in two days |
| preconditions | Logged in; can create task and set due date |
| data | Due date: today + 2 days |
| steps | Create or update task; inspect urgency label. |
| expected | Due Soon |
| actual | The task displays “Due Soon”. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 74 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-05 |

## W1-URG-06

| Field | Record |
|---|---|
| id | URG-06 |
| feature | Task Urgency |
| tech | BVA / State Transition |
| objective | Due in three days |
| preconditions | Logged in; can create task and set due date |
| data | Due date: today + 3 days |
| steps | Create or update task; inspect urgency label. |
| expected | Upcoming |
| actual | The task displays “Upcoming”. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 75 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-05 |

## W1-URG-07

| Field | Record |
|---|---|
| id | URG-07 |
| feature | Task Urgency |
| tech | BVA / State Transition |
| objective | Completed task with due date |
| preconditions | Logged in; can create task and set due date |
| data | Mark task as completed |
| steps | Create or update task; inspect urgency label. |
| expected | Done |
| actual | The completed task displays the urgency label “Done”. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 76 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-05 |

## W1-API-01

| Field | Record |
|---|---|
| id | API-01 |
| feature | API / Categories |
| tech | Functional |
| objective | Retrieve categories |
| preconditions | Application running |
| data | GET /api/categories |
| steps | Use browser/API client to send request. |
| expected | Returns Work, Personal, Study and Urgent. |
| actual | The API returns all four categories in a JSON response. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 77 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-07 |

## W1-API-02

| Field | Record |
|---|---|
| id | API-02 |
| feature | API Authentication |
| tech | Decision Table |
| objective | List tasks without login |
| preconditions | No session cookie |
| data | GET /api/tasks |
| steps | Send request without logging in/session cookie. |
| expected | HTTP 401. |
| actual | The API returned a JSON list of tasks. |
| status | Fail |
| evidence | Not recorded in source |
| defect | D-005 |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 78 |
| Original defect reference | DEF-05 |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02 |

## W1-API-03

| Field | Record |
|---|---|
| id | API-03 |
| feature | API Authentication |
| tech | Decision Table |
| objective | List tasks after login |
| preconditions | Valid authenticated session cookie |
| data | GET /api/tasks |
| steps | Send request with session cookie. |
| expected | HTTP 200; only current user's tasks. |
| actual | The API returned a JSON list of tasks in the logged-in browser. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 79 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02 |

## W1-API-04

| Field | Record |
|---|---|
| id | API-04 |
| feature | API Create Task |
| tech | Functional |
| objective | Create task through API |
| preconditions | Authenticated session cookie |
| data | POST /api/tasks; JSON title='API test task' |
| steps | Send request with valid JSON body. |
| expected | HTTP 201 and task is created. |
| actual | HTTP 201 returned successfully. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 80 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-03 |

## W1-API-05

| Field | Record |
|---|---|
| id | API-05 |
| feature | API Create Task |
| tech | EP |
| objective | Create task with blank title |
| preconditions | Authenticated session cookie |
| data | POST /api/tasks; JSON title=' ' |
| steps | Send request with whitespace-only title. |
| expected | HTTP 400; title is required. |
| actual | HTTP 400 returned. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 81 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-03 |

## W1-API-06

| Field | Record |
|---|---|
| id | API-06 |
| feature | API Task Detail |
| tech | Functional |
| objective | Retrieve existing task |
| preconditions | Logged in; own task exists |
| data | GET /api/tasks/{own_task_id} |
| steps | Request existing own task ID. |
| expected | Returns task details. |
| actual | HTTP 200 returned for the existing task request. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 82 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-08 |

## W1-API-07

| Field | Record |
|---|---|
| id | API-07 |
| feature | API Task Detail |
| tech | Negative |
| objective | Retrieve nonexistent task |
| preconditions | Logged in; ID confirmed absent |
| data | GET /api/tasks/999999 |
| steps | Request nonexistent ID. |
| expected | HTTP 404. |
| actual | HTTP 404 (NOT FOUND) returned. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 83 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-08 |

## W1-API-08

| Field | Record |
|---|---|
| id | API-08 |
| feature | API Update Task |
| tech | Functional |
| objective | Update task |
| preconditions | Logged in; own task exists |
| data | PUT /api/tasks/{own_task_id}; update title |
| steps | Send partial update. |
| expected | Updated task is returned and persists. |
| actual | HTTP 200 returned after the update request. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 84 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-04 |

## W1-API-09

| Field | Record |
|---|---|
| id | API-09 |
| feature | API Delete Task |
| tech | Functional |
| objective | Delete own task |
| preconditions | Logged in; own disposable task exists |
| data | DELETE /api/tasks/{own_task_id} |
| steps | Send DELETE request. |
| expected | Task is deleted. |
| actual | HTTP 200 returned, and a subsequent GET confirmed the title is API Updated Task. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 85 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-04 |

## W1-API-10

| Field | Record |
|---|---|
| id | API-10 |
| feature | API Dashboard |
| tech | Functional |
| objective | Access dashboard API |
| preconditions | Logged in with session cookie |
| data | GET /api/dashboard |
| steps | Send request. |
| expected | Returns dashboard counters. |
| actual | HTTP 200 returned after the DELETE request. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 86 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-06 |

## W1-API-11

| Field | Record |
|---|---|
| id | API-11 |
| feature | User Data Isolation |
| tech | Access Control |
| objective | User B requests User A task |
| preconditions | Two test accounts; User A owns disposable task |
| data | As User B, GET /api/tasks/{A_task_id} |
| steps | Log in as B and request A's task ID. |
| expected | User B cannot view User A's task; expected not-found/denied. |
| actual | HTTP 200 returned; verification confirmed task ID 15 no longer exists in the task list. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 87 |
| Original defect reference | Not recorded in source |
| review disposition | Unverified historical Pass: recorded observation does not establish access denial; excluded from verified-pass claims; retest required |
| Requirement IDs | R-02; R-12 |

## W1-API-12

| Field | Record |
|---|---|
| id | API-12 |
| feature | User Data Isolation |
| tech | Access Control |
| objective | User B attempts to delete User A task |
| preconditions | Two test accounts; User A owns disposable task |
| data | As User B, DELETE /api/tasks/{A_task_id} |
| steps | Log in as B; attempt delete; verify as A. |
| expected | User B must not be able to delete User A's task. |
| actual | HTTP 200 returned. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 1).xlsx / Test Cases / row 88 |
| Original defect reference | Not recorded in source |
| review disposition | Unverified historical Pass: recorded observation does not establish access denial; excluded from verified-pass claims; retest required |
| Requirement IDs | R-04 |

## W2-WB-URG-01

| Field | Record |
|---|---|
| id | WB-URG-01 |
| feature | compute_urgency |
| tech | White-box / No due date |
| objective | No due date |
| preconditions | Pure helper function; fixed clock where supplied |
| data | None; today=date(2026,10,19) |
| steps | Invoke function with supplied input; compare result |
| expected | No due date |
| actual | No due date |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 4 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-05 |

## W2-WB-URG-02

| Field | Record |
|---|---|
| id | WB-URG-02 |
| feature | compute_urgency |
| tech | White-box / Past date |
| objective | Past date |
| preconditions | Pure helper function; fixed clock where supplied |
| data | '2026-10-18'; today=date(2026,10,19) |
| steps | Invoke function with supplied input; compare result |
| expected | Overdue |
| actual | Overdue |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 5 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-05 |

## W2-WB-URG-03

| Field | Record |
|---|---|
| id | WB-URG-03 |
| feature | compute_urgency |
| tech | White-box / Due today boundary |
| objective | Due today boundary |
| preconditions | Pure helper function; fixed clock where supplied |
| data | '2026-10-19'; today=date(2026,10,19) |
| steps | Invoke function with supplied input; compare result |
| expected | Due Today |
| actual | Overdue |
| status | Fail |
| evidence | Pytest confirmed: due-today date returns Overdue instead of Due Today. |
| defect | D-004 |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 6 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-05 |

## W2-WB-URG-04

| Field | Record |
|---|---|
| id | WB-URG-04 |
| feature | compute_urgency |
| tech | White-box / +2 days boundary |
| objective | +2 days boundary |
| preconditions | Pure helper function; fixed clock where supplied |
| data | '2026-10-21'; today=date(2026,10,19) |
| steps | Invoke function with supplied input; compare result |
| expected | Due Soon |
| actual | Due Soon |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 7 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-05 |

## W2-WB-URG-05

| Field | Record |
|---|---|
| id | WB-URG-05 |
| feature | compute_urgency |
| tech | White-box / +3 days boundary |
| objective | +3 days boundary |
| preconditions | Pure helper function; fixed clock where supplied |
| data | '2026-10-22'; today=date(2026,10,19) |
| steps | Invoke function with supplied input; compare result |
| expected | Upcoming |
| actual | Upcoming |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 8 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-05 |

## W2-WB-PWD-01

| Field | Record |
|---|---|
| id | WB-PWD-01 |
| feature | is_valid_password |
| tech | White-box / Wrong type |
| objective | Wrong type |
| preconditions | Pure helper function; fixed clock where supplied |
| data | None |
| steps | Invoke function with supplied input; compare result |
| expected | False |
| actual | 0 |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 9 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W2-WB-PWD-02

| Field | Record |
|---|---|
| id | WB-PWD-02 |
| feature | is_valid_password |
| tech | White-box / 7 characters |
| objective | 7 characters |
| preconditions | Pure helper function; fixed clock where supplied |
| data | 'abc1234' |
| steps | Invoke function with supplied input; compare result |
| expected | False |
| actual | 0 |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 10 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W2-WB-PWD-03

| Field | Record |
|---|---|
| id | WB-PWD-03 |
| feature | is_valid_password |
| tech | White-box / 8 characters boundary |
| objective | 8 characters boundary |
| preconditions | Pure helper function; fixed clock where supplied |
| data | 'abc12345' |
| steps | Invoke function with supplied input; compare result |
| expected | True: spec says at least 8 |
| actual | 0 |
| status | Fail |
| evidence | Pytest confirmed: 8-character password returns False instead of True. |
| defect | D-001 |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 11 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W2-WB-PWD-04

| Field | Record |
|---|---|
| id | WB-PWD-04 |
| feature | is_valid_password |
| tech | White-box / 9 characters |
| objective | 9 characters |
| preconditions | Pure helper function; fixed clock where supplied |
| data | 'abc123456' |
| steps | Invoke function with supplied input; compare result |
| expected | True |
| actual | 1 |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 12 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W2-WB-USER-01

| Field | Record |
|---|---|
| id | WB-USER-01 |
| feature | is_valid_username |
| tech | White-box / Wrong type |
| objective | Wrong type |
| preconditions | Pure helper function; fixed clock where supplied |
| data | None |
| steps | Invoke function with supplied input; compare result |
| expected | False |
| actual | 0 |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 13 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W2-WB-USER-02

| Field | Record |
|---|---|
| id | WB-USER-02 |
| feature | is_valid_username |
| tech | White-box / 2 characters |
| objective | 2 characters |
| preconditions | Pure helper function; fixed clock where supplied |
| data | 'ab' |
| steps | Invoke function with supplied input; compare result |
| expected | False |
| actual | 0 |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 14 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W2-WB-USER-03

| Field | Record |
|---|---|
| id | WB-USER-03 |
| feature | is_valid_username |
| tech | White-box / 3 characters boundary |
| objective | 3 characters boundary |
| preconditions | Pure helper function; fixed clock where supplied |
| data | 'abc' |
| steps | Invoke function with supplied input; compare result |
| expected | True |
| actual | 1 |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 15 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W2-WB-USER-04

| Field | Record |
|---|---|
| id | WB-USER-04 |
| feature | is_valid_username |
| tech | White-box / 20 characters boundary |
| objective | 20 characters boundary |
| preconditions | Pure helper function; fixed clock where supplied |
| data | 'abcdefghijklmnopqrst' |
| steps | Invoke function with supplied input; compare result |
| expected | True |
| actual | 1 |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 16 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W2-WB-USER-05

| Field | Record |
|---|---|
| id | WB-USER-05 |
| feature | is_valid_username |
| tech | White-box / 21 characters boundary |
| objective | 21 characters boundary |
| preconditions | Pure helper function; fixed clock where supplied |
| data | 'abcdefghijklmnopqrstu' |
| steps | Invoke function with supplied input; compare result |
| expected | False |
| actual | 0 |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 17 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W2-WB-USER-06

| Field | Record |
|---|---|
| id | WB-USER-06 |
| feature | is_valid_username |
| tech | White-box / Underscore allowed |
| objective | Underscore allowed |
| preconditions | Pure helper function; fixed clock where supplied |
| data | 'user_01' |
| steps | Invoke function with supplied input; compare result |
| expected | True |
| actual | 1 |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 18 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W2-WB-USER-07

| Field | Record |
|---|---|
| id | WB-USER-07 |
| feature | is_valid_username |
| tech | White-box / Space disallowed |
| objective | Space disallowed |
| preconditions | Pure helper function; fixed clock where supplied |
| data | 'user name' |
| steps | Invoke function with supplied input; compare result |
| expected | False |
| actual | 0 |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 19 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W2-WB-USER-08

| Field | Record |
|---|---|
| id | WB-USER-08 |
| feature | is_valid_username |
| tech | White-box / Hyphen disallowed |
| objective | Hyphen disallowed |
| preconditions | Pure helper function; fixed clock where supplied |
| data | 'user-name' |
| steps | Invoke function with supplied input; compare result |
| expected | False |
| actual | 0 |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 20 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W2-WB-DAY-01

| Field | Record |
|---|---|
| id | WB-DAY-01 |
| feature | completed_in_last_n_days |
| tech | White-box / Missing value |
| objective | Missing value |
| preconditions | Pure helper function; fixed clock where supplied |
| data | None; n=7; now=datetime(2026,10,19,12,0,0) |
| steps | Invoke function with supplied input; compare result |
| expected | False |
| actual | 0 |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 21 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-06 |

## W2-WB-DAY-02

| Field | Record |
|---|---|
| id | WB-DAY-02 |
| feature | completed_in_last_n_days |
| tech | White-box / Recent completion |
| objective | Recent completion |
| preconditions | Pure helper function; fixed clock where supplied |
| data | '2026-10-18 12:00:00'; n=7; now=datetime(2026,10,19,12,0,0) |
| steps | Invoke function with supplied input; compare result |
| expected | True |
| actual | 1 |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 22 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-06 |

## W2-WB-DAY-03

| Field | Record |
|---|---|
| id | WB-DAY-03 |
| feature | completed_in_last_n_days |
| tech | White-box / Exactly N days boundary |
| objective | Exactly N days boundary |
| preconditions | Pure helper function; fixed clock where supplied |
| data | '2026-10-12 12:00:00'; n=7; now=datetime(2026,10,19,12,0,0) |
| steps | Invoke function with supplied input; compare result |
| expected | True: docstring says inclusive |
| actual | 0 |
| status | Fail |
| evidence | Pytest confirmed: completion exactly 7 days ago returns False instead of True. |
| defect | D-006 |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 23 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-06 |

## W2-WB-DAY-04

| Field | Record |
|---|---|
| id | WB-DAY-04 |
| feature | completed_in_last_n_days |
| tech | White-box / Future completion |
| objective | Future completion |
| preconditions | Pure helper function; fixed clock where supplied |
| data | '2026-10-20 12:00:00'; n=7; now=datetime(2026,10,19,12,0,0) |
| steps | Invoke function with supplied input; compare result |
| expected | False |
| actual | 0 |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 24 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-06 |

## W2-WB-DAY-05

| Field | Record |
|---|---|
| id | WB-DAY-05 |
| feature | completed_in_last_n_days |
| tech | White-box / Exactly now |
| objective | Exactly now |
| preconditions | Pure helper function; fixed clock where supplied |
| data | '2026-10-19 12:00:00'; n=7; now=datetime(2026,10,19,12,0,0) |
| steps | Invoke function with supplied input; compare result |
| expected | False under positive-age rule |
| actual | 0 |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 25 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-06 |

## W2-WB-DAY-06

| Field | Record |
|---|---|
| id | WB-DAY-06 |
| feature | completed_in_last_n_days |
| tech | White-box / Older than N days |
| objective | Older than N days |
| preconditions | Pure helper function; fixed clock where supplied |
| data | '2026-10-11 12:00:00'; n=7; now=datetime(2026,10,19,12,0,0) |
| steps | Invoke function with supplied input; compare result |
| expected | False |
| actual | 0 |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 2).xlsx / Test Cases / row 26 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-06 |

## W3-GUI-01

| Field | Record |
|---|---|
| id | GUI-01 |
| feature | GUI Testing |
| tech | Manual review |
| objective | Check all forms and input fields. |
| preconditions | Local app; browser configuration in source |
| data | Not separately recorded |
| steps | Check all forms and input fields. |
| expected | Fields are visible, labelled, accept valid input and validate invalid input. |
| actual | Browser required-field validation prevents submission when Title is empty. <br>Required Title validation works task created successfully with optional fields left empty. |
| status | Pass |
| evidence | GUI-01_Empty_Title_Validation, GUI-01_Valid_Title_Created |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Task Checklist / row 5 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-09 |

## W3-GUI-02

| Field | Record |
|---|---|
| id | GUI-02 |
| feature | GUI Testing |
| tech | Manual review |
| objective | Check buttons and their actions. |
| preconditions | Local app; browser configuration in source |
| data | Not separately recorded |
| steps | Check buttons and their actions. |
| expected | Each button is visible, clickable and performs the expected action. |
| actual | Cancel returns to My Tasks without creating a task. |
| status | Pass |
| evidence | GUI-02_Cancel_New_Task |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Task Checklist / row 6 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-09 |

## W3-GUI-03

| Field | Record |
|---|---|
| id | GUI-03 |
| feature | GUI Testing |
| tech | Manual review |
| objective | Check links and navigation links. |
| preconditions | Local app; browser configuration in source |
| data | Not separately recorded |
| steps | Check links and navigation links. |
| expected | Links open the correct page or destination; no broken links. |
| actual | Dashboard link opens the Dashboard page successfully. No navigation error observed. |
| status | Pass |
| evidence | GUI-03_Dashboard_Navigation |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Task Checklist / row 7 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-09 |

## W3-GUI-04

| Field | Record |
|---|---|
| id | GUI-04 |
| feature | GUI Testing |
| tech | Manual review |
| objective | Check labels and instructions. |
| preconditions | Local app; browser configuration in source |
| data | Not separately recorded |
| steps | Check labels and instructions. |
| expected | Labels are clear, correctly associated with fields and free from spelling errors. |
| actual | All four form labels are clear, readable and positioned correctly above their corresponding fields. |
| status | Pass |
| evidence | GUI-04_Form_Labels |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Task Checklist / row 8 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-09 |

## W3-GUI-05

| Field | Record |
|---|---|
| id | GUI-05 |
| feature | GUI Testing |
| tech | Manual review |
| objective | Check page navigation and menu items. |
| preconditions | Local app; browser configuration in source |
| data | Not separately recorded |
| steps | Check page navigation and menu items. |
| expected | Users can move between pages and return without unexpected errors. |
| actual | Navigation between My Tasks and Dashboard works successfully without errors. |
| status | Pass |
| evidence | - |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Task Checklist / row 9 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-09 |

## W3-GUI-06

| Field | Record |
|---|---|
| id | GUI-06 |
| feature | GUI Testing |
| tech | Manual review |
| objective | Check success, warning and error messages. |
| preconditions | Local app; browser configuration in source |
| data | Not separately recorded |
| steps | Check success, warning and error messages. |
| expected | Messages appear at the right time and explain the outcome clearly. |
| actual | Task is created successfully, but no success message or confirmation feedback is displayed. See BUG-01 in the Defect Log. |
| status | Fail |
| evidence | - |
| defect | D-007 |
| Source | STQA Data Collection (Week 3).xlsx / Task Checklist / row 10 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-09 |

## W3-GUI-07

| Field | Record |
|---|---|
| id | GUI-07 |
| feature | GUI Testing |
| tech | Manual review |
| objective | Check visual consistency. |
| preconditions | Local app; browser configuration in source |
| data | Not separately recorded |
| steps | Check visual consistency. |
| expected | Fonts, colours, spacing, alignment and component styles are consistent. |
| actual | Overall design is consistent. Page headings appear at different horizontal positions. Minor visual alignment improvement may be considered. |
| status | Pass |
| evidence | GUI-07_Dashboard<br>GUI-07_My_Tasks |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Task Checklist / row 11 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-09 |

## W3-GUI-08

| Field | Record |
|---|---|
| id | GUI-08 |
| feature | GUI Testing |
| tech | Manual review |
| objective | Check layout at a narrower browser-window width. |
| preconditions | Local app; browser configuration in source |
| data | Not separately recorded |
| steps | Check layout at a narrower browser-window width. |
| expected | Content remains readable; controls do not overlap or disappear. |
| actual | At 800 px responsive width, the task list and controls appear readable. No obvious overlap observed in the visible area. |
| status | Pass |
| evidence | GUI-08_Responsive_800px |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Task Checklist / row 12 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-09 |

## W3-COMP-01

| Field | Record |
|---|---|
| id | COMP-01 |
| feature | Compatibility / Configuration |
| tech | Manual review |
| objective | Test the application in the group's primary browser. |
| preconditions | Local app; browser configuration in source |
| data | Not separately recorded |
| steps | Test the application in the group's primary browser. |
| expected | Record browser name/version, OS and whether key functions work. |
| actual | Tested on Google Chrome 155.0.8059.85 and Windows 11. My Tasks, New Task, Dashboard, task creation and navigation worked. Due-today tasks showed Overdue; linked to existing defect DEF-04. |
| status | Pass |
| evidence | - |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Task Checklist / row 13 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-10 |

## W3-COMP-02

| Field | Record |
|---|---|
| id | COMP-02 |
| feature | Compatibility / Configuration |
| tech | Manual review |
| objective | Test the application in a second available browser, if available. |
| preconditions | Local app; browser configuration in source |
| data | Not separately recorded |
| steps | Test the application in a second available browser, if available. |
| expected | Compare layout and core functions with the primary browser. |
| actual | All three pages opened successfully in Microsoft Edge. Task list, New Task form and Dashboard were accessible without navigation errors. |
| status | Pass |
| evidence | COMP-02_Edge_Tasks<br>COMP-02_Edge_New_Task<br>COMP-02_Edge_Dashboard |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Task Checklist / row 14 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-10 |

## W3-COMP-03

| Field | Record |
|---|---|
| id | COMP-03 |
| feature | Compatibility / Configuration |
| tech | Manual review |
| objective | Test a different screen/window configuration available to the group. |
| preconditions | Local app; browser configuration in source |
| data | Not separately recorded |
| steps | Test a different screen/window configuration available to the group. |
| expected | Record screen resolution or window size and any layout differences. |
| actual | Tested at 800 px responsive width. Task list and controls remained readable, with no obvious overlap in the visible area. |
| status | Pass |
| evidence | - |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Task Checklist / row 15 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-10 |

## W3-COMP-04

| Field | Record |
|---|---|
| id | COMP-04 |
| feature | Compatibility / Configuration |
| tech | Manual review |
| objective | Compare key pages across tested configurations. |
| preconditions | Local app; browser configuration in source |
| data | Not separately recorded |
| steps | Compare key pages across tested configurations. |
| expected | Record pass/fail and environment-specific defects in the matrix. |
| actual | Compared the desktop and 800 px responsive layouts. No obvious layout issue was observed in the areas checked. |
| status | Pass |
| evidence | - |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Task Checklist / row 16 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-10 |

## W3-USE-01

| Field | Record |
|---|---|
| id | USE-01 |
| feature | Usability |
| tech | Manual review |
| objective | Evaluate ease of navigation. |
| preconditions | Local app; browser configuration in source |
| data | Not separately recorded |
| steps | Evaluate ease of navigation. |
| expected | Record whether users can locate main pages and complete common tasks easily. |
| actual | USE-OBS-01: Main navigation works between My Tasks, New Task and Dashboard. |
| status | Pass |
| evidence | - |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Task Checklist / row 17 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-09 |

## W3-USE-02

| Field | Record |
|---|---|
| id | USE-02 |
| feature | Usability |
| tech | Manual review |
| objective | Evaluate feedback and system responses. |
| preconditions | Local app; browser configuration in source |
| data | Not separately recorded |
| steps | Evaluate feedback and system responses. |
| expected | Record whether the application clearly confirms actions and explains failures. |
| actual | USE-OBS-02: Task creation succeeds but no confirmation message appears. See BUG-01. |
| status | Fail |
| evidence | - |
| defect | D-007 |
| Source | STQA Data Collection (Week 3).xlsx / Task Checklist / row 18 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-09 |

## W3-USE-03

| Field | Record |
|---|---|
| id | USE-03 |
| feature | Usability |
| tech | Manual review |
| objective | Evaluate consistency across pages. |
| preconditions | Local app; browser configuration in source |
| data | Not separately recorded |
| steps | Evaluate consistency across pages. |
| expected | Record consistent wording, controls, layout and interaction patterns. |
| actual | USE-OBS-03: Consistent colours and card styles; minor heading alignment difference. |
| status | Pass |
| evidence | - |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Task Checklist / row 19 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-09 |

## W3-USE-04

| Field | Record |
|---|---|
| id | USE-04 |
| feature | Usability |
| tech | Manual review |
| objective | Evaluate error prevention and recovery. |
| preconditions | Local app; browser configuration in source |
| data | Not separately recorded |
| steps | Evaluate error prevention and recovery. |
| expected | Check validation, helpful error messages and whether users can correct mistakes. |
| actual | USE-OBS-04: Empty Title is blocked, but tasks due today are displayed as Overdue.  |
| status | Fail |
| evidence | - |
| defect | D-004 |
| Source | STQA Data Collection (Week 3).xlsx / Task Checklist / row 20 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-09 |

## W3-USE-05

| Field | Record |
|---|---|
| id | USE-05 |
| feature | Usability |
| tech | Manual review |
| objective | Evaluate understandability. |
| preconditions | Local app; browser configuration in source |
| data | Not separately recorded |
| steps | Evaluate understandability. |
| expected | Record unclear labels, instructions, terminology or confusing workflows. |
| actual | USE-OBS-05: Page headings, field labels, buttons and task information are clear. |
| status | Pass |
| evidence | - |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Task Checklist / row 21 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-09 |

## W3-ACC-01

| Field | Record |
|---|---|
| id | ACC-01 |
| feature | Accessibility / Perceivable |
| tech | Basic accessibility review |
| objective | Meaningful images have alternative text where applicable. |
| preconditions | Local browser; manual review |
| data | Not separately recorded |
| steps | Meaningful images have alternative text where applicable. |
| expected | Satisfy check: Meaningful images have alternative text where applicable. |
| actual | No meaningful images or logos requiring alternative text were found in the application. |
| status | N/A |
| evidence | See source checklist; filename discrepancies in reconciliation |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Accessibility Review / row 4 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-11 |

## W3-ACC-02

| Field | Record |
|---|---|
| id | ACC-02 |
| feature | Accessibility / Perceivable |
| tech | Basic accessibility review |
| objective | Text and background have readable contrast. |
| preconditions | Local browser; manual review |
| data | Not separately recorded |
| steps | Text and background have readable contrast. |
| expected | Satisfy check: Text and background have readable contrast. |
| actual | Text on the navigation bar, form labels, and buttons appears readable against the background. |
| status | Pass |
| evidence | See source checklist; filename discrepancies in reconciliation |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Accessibility Review / row 5 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-11 |

## W3-ACC-03

| Field | Record |
|---|---|
| id | ACC-03 |
| feature | Accessibility / Operable |
| tech | Basic accessibility review |
| objective | All main interactive elements can be reached by keyboard. |
| preconditions | Local browser; manual review |
| data | Not separately recorded |
| steps | All main interactive elements can be reached by keyboard. |
| expected | Satisfy check: All main interactive elements can be reached by keyboard. |
| actual | Navigation links, buttons, search, filters, and task controls can be reached using Tab and Shift+Tab. |
| status | Pass |
| evidence | See source checklist; filename discrepancies in reconciliation |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Accessibility Review / row 6 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-11 |

## W3-ACC-04

| Field | Record |
|---|---|
| id | ACC-04 |
| feature | Accessibility / Operable |
| tech | Basic accessibility review |
| objective | Keyboard focus is visible and follows a logical order. |
| preconditions | Local browser; manual review |
| data | Not separately recorded |
| steps | Keyboard focus is visible and follows a logical order. |
| expected | Satisfy check: Keyboard focus is visible and follows a logical order. |
| actual | Keyboard navigation works using Tab and Shift+Tab. Interactive elements show a visible focus outline, and the navigation order is logical. |
| status | Pass |
| evidence | See source checklist; filename discrepancies in reconciliation |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Accessibility Review / row 7 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-11 |

## W3-ACC-05

| Field | Record |
|---|---|
| id | ACC-05 |
| feature | Accessibility / Understandable |
| tech | Basic accessibility review |
| objective | Labels and instructions are clear and readable. |
| preconditions | Local browser; manual review |
| data | Not separately recorded |
| steps | Labels and instructions are clear and readable. |
| expected | Satisfy check: Labels and instructions are clear and readable. |
| actual | Title, Description, Category, and Due Date labels are clearly visible and easy to understand. |
| status | Pass |
| evidence | See source checklist; filename discrepancies in reconciliation |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Accessibility Review / row 8 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-11 |

## W3-ACC-06

| Field | Record |
|---|---|
| id | ACC-06 |
| feature | Accessibility / Understandable |
| tech | Basic accessibility review |
| objective | Validation and error messages explain how to correct mistakes. |
| preconditions | Local browser; manual review |
| data | Not separately recorded |
| steps | Validation and error messages explain how to correct mistakes. |
| expected | Satisfy check: Validation and error messages explain how to correct mistakes. |
| actual | When the Title field is left empty, the browser displays “Please fill out this field.” |
| status | Pass |
| evidence | See source checklist; filename discrepancies in reconciliation |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Accessibility Review / row 9 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-11 |

## W3-ACC-07

| Field | Record |
|---|---|
| id | ACC-07 |
| feature | Accessibility / Understandable |
| tech | Basic accessibility review |
| objective | Navigation and controls behave consistently. |
| preconditions | Local browser; manual review |
| data | Not separately recorded |
| steps | Navigation and controls behave consistently. |
| expected | Satisfy check: Navigation and controls behave consistently. |
| actual | Navigation links and buttons behave consistently and take users to the expected pages. |
| status | Pass |
| evidence | See source checklist; filename discrepancies in reconciliation |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Accessibility Review / row 10 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-11 |

## W3-ACC-08

| Field | Record |
|---|---|
| id | ACC-08 |
| feature | Accessibility / Robust |
| tech | Basic accessibility review |
| objective | Page structure and controls have meaningful names/semantics where inspectable. |
| preconditions | Local browser; manual review |
| data | Not separately recorded |
| steps | Page structure and controls have meaningful names/semantics where inspectable. |
| expected | Satisfy check: Page structure and controls have meaningful names/semantics where inspectable. |
| actual | The form contains visible labels, but the Title label and input do not show a clear programmatic association in the inspected HTML. |
| status | Fail |
| evidence | See source checklist; filename discrepancies in reconciliation |
| defect | D-008 |
| Source | STQA Data Collection (Week 3).xlsx / Accessibility Review / row 11 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-11 |

## W3-ACC-09

| Field | Record |
|---|---|
| id | ACC-09 |
| feature | Accessibility / Robust |
| tech | Basic accessibility review |
| objective | Content remains usable with browser zoom/text enlargement. |
| preconditions | Local browser; manual review |
| data | Not separately recorded |
| steps | Content remains usable with browser zoom/text enlargement. |
| expected | Satisfy check: Content remains usable with browser zoom/text enlargement. |
| actual | At 125% browser zoom, all form fields and both buttons remain accessible. The page can be scrolled to reach content below the visible area. |
| status | Pass |
| evidence | See source checklist; filename discrepancies in reconciliation |
| defect | None linked |
| Source | STQA Data Collection (Week 3).xlsx / Accessibility Review / row 12 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-11 |

## W4-WEB-01

| Field | Record |
|---|---|
| id | WEB-01 |
| feature | Registration |
| tech | Web functional |
| objective | Register with a valid unique username and valid password. |
| preconditions | Local app; login where required |
| data | See scenario |
| steps | Register with a valid unique username and valid password. |
| expected | Account is created and user is redirected/logged in as designed. |
| actual | Registration successful; redirected to the Tasks page and logged in as farisha0000. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / Web Test Scenarios / row 5 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W4-WEB-02

| Field | Record |
|---|---|
| id | WEB-02 |
| feature | Registration validation |
| tech | Web functional |
| objective | Submit a username shorter than the minimum. |
| preconditions | Local app; login where required |
| data | See scenario |
| steps | Submit a username shorter than the minimum. |
| expected | Validation appears; account is not created. |
| actual | The system rejected the username "ab" and displayed a validation message. No account was created. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / Web Test Scenarios / row 6 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W4-WEB-03

| Field | Record |
|---|---|
| id | WEB-03 |
| feature | Registration validation |
| tech | Web functional |
| objective | Submit a password shorter than the minimum. |
| preconditions | Local app; login where required |
| data | See scenario |
| steps | Submit a password shorter than the minimum. |
| expected | Validation appears; account is not created. |
| actual | The system displayed “Password must be at least 8 characters” and rejected the registration. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / Web Test Scenarios / row 7 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W4-WEB-04

| Field | Record |
|---|---|
| id | WEB-04 |
| feature | Duplicate registration |
| tech | Web functional |
| objective | Register using an existing username. |
| preconditions | Local app; login where required |
| data | See scenario |
| steps | Register using an existing username. |
| expected | Duplicate username is rejected; no unintended login/account duplication. |
| actual | Registration was successful using an existing username, even when the other details were different and when the name was the same. |
| status | Fail |
| evidence | Not recorded in source |
| defect | D-002 |
| Source | STQA Data Collection (Week 4).xlsx / Web Test Scenarios / row 8 |
| Original defect reference | Duplicate username is not rejected.  |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W4-WEB-05

| Field | Record |
|---|---|
| id | WEB-05 |
| feature | Login |
| tech | Web functional |
| objective | Log in with valid credentials. |
| preconditions | Local app; login where required |
| data | See scenario |
| steps | Log in with valid credentials. |
| expected | Login succeeds and task page opens. |
| actual | Login successful using valid credentials; redirected to the Tasks page. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / Web Test Scenarios / row 9 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02 |

## W4-WEB-06

| Field | Record |
|---|---|
| id | WEB-06 |
| feature | Login validation |
| tech | Web functional |
| objective | Log in with incorrect password. |
| preconditions | Local app; login where required |
| data | See scenario |
| steps | Log in with incorrect password. |
| expected | Login is rejected with an error. |
| actual | Login rejected with the error message “Invalid username or password.” |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / Web Test Scenarios / row 10 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02 |

## W4-WEB-07

| Field | Record |
|---|---|
| id | WEB-07 |
| feature | Task creation |
| tech | Web functional |
| objective | Create a task with a title and optional fields blank. |
| preconditions | Local app; login where required |
| data | See scenario |
| steps | Create a task with a title and optional fields blank. |
| expected | Task is created and appears in the list. |
| actual | Task was created successfully and appeared in the task list with optional fields left blank. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / Web Test Scenarios / row 11 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-03 |

## W4-WEB-08

| Field | Record |
|---|---|
| id | WEB-08 |
| feature | Task validation |
| tech | Web functional |
| objective | Attempt to create a task without a title. |
| preconditions | Local app; login where required |
| data | See scenario |
| steps | Attempt to create a task without a title. |
| expected | Creation is blocked and validation is shown. |
| actual | Task creation was blocked by browser validation. The message “Please fill out this field” |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / Web Test Scenarios / row 12 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-03 |

## W4-WEB-09

| Field | Record |
|---|---|
| id | WEB-09 |
| feature | Task update |
| tech | Web functional |
| objective | Edit a task title or due date and save. |
| preconditions | Local app; login where required |
| data | See scenario |
| steps | Edit a task title or due date and save. |
| expected | Updated values appear in the list. |
| actual | Task updated successfully and the new changes appeared in the task list. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / Web Test Scenarios / row 13 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-04 |

## W4-WEB-10

| Field | Record |
|---|---|
| id | WEB-10 |
| feature | Task completion |
| tech | Web functional |
| objective | Mark a task complete. |
| preconditions | Local app; login where required |
| data | See scenario |
| steps | Mark a task complete. |
| expected | Completion state changes correctly. |
| actual | Task marked as completed successfully. The task title was crossed out and the urgency |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / Web Test Scenarios / row 14 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-04 |

## W4-WEB-11

| Field | Record |
|---|---|
| id | WEB-11 |
| feature | Task deletion |
| tech | Web functional |
| objective | Delete a disposable test task. |
| preconditions | Local app; login where required |
| data | See scenario |
| steps | Delete a disposable test task. |
| expected | Task is removed from the list. |
| actual | Task deleted successfully and disappeared from the task list. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / Web Test Scenarios / row 15 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-04 |

## W4-WEB-12

| Field | Record |
|---|---|
| id | WEB-12 |
| feature | Search/filter |
| tech | Web functional |
| objective | Search by title and use category/status filters. |
| preconditions | Local app; login where required |
| data | See scenario |
| steps | Search by title and use category/status filters. |
| expected | Only matching tasks are displayed. |
| actual | Search and filters worked correctly; only tasks matching the search criteria and selected filters were displayed. |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / Web Test Scenarios / row 16 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-07; R-08 |

## W4-WEB-13

| Field | Record |
|---|---|
| id | WEB-13 |
| feature | Dashboard |
| tech | Web functional |
| objective | Compare dashboard counts/urgency with task list. |
| preconditions | Local app; login where required |
| data | See scenario |
| steps | Compare dashboard counts/urgency with task list. |
| expected | Dashboard values are consistent with task data. |
| actual | Dashboard displays 17 total tasks, 16 open, 5 overdue, 1 due soon, and 1 completed in the last 7 days. However, tasks due today are incorrectly labelled “Overdue.” |
| status | Pass |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / Web Test Scenarios / row 17 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-06 |

## W4-API-01

| Field | Record |
|---|---|
| id | API-01 |
| feature | /api/categories |
| tech | API |
| objective | GET /api/categories |
| preconditions | Authentication required: No |
| data | None |
| steps | Send request and verify HTTP status and response |
| expected | 200; JSON array of category objects with id/name |
| actual | Returned HTTP 200 OK with four categories: Personal, Study, Urgent, Work; - |
| status | Pass |
| evidence | API-01.png |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / API Test Suite / row 5 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-07 |

## W4-API-02

| Field | Record |
|---|---|
| id | API-02 |
| feature | /api/register |
| tech | API |
| objective | POST /api/register |
| preconditions | Authentication required: No |
| data | {"username":"week4_farisha00","password":"Week4Pass123"} |
| steps | Send request and verify HTTP status and response |
| expected | 201; JSON includes id and username |
| actual | HTTP 201 Created; returned id: 11 and username week4_farisha00; - |
| status | Pass |
| evidence | API-02.png |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / API Test Suite / row 6 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W4-API-03

| Field | Record |
|---|---|
| id | API-03 |
| feature | /api/register |
| tech | API |
| objective | POST /api/register |
| preconditions | Authentication required: No |
| data | Missing/invalid username |
| steps | Send request and verify HTTP status and response |
| expected | 400; JSON error: "invalid username" |
| actual | HTTP 400 Bad Request; JSON response: {"error":"invalid username"}; - |
| status | Pass |
| evidence | API-03.png |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / API Test Suite / row 7 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W4-API-04

| Field | Record |
|---|---|
| id | API-04 |
| feature | /api/register |
| tech | API |
| objective | POST /api/register |
| preconditions | Authentication required: No |
| data | Password below minimum |
| steps | Send request and verify HTTP status and response |
| expected | 400; JSON error: "invalid password" |
| actual | HTTP 400 Bad Request; JSON response: {"error":"invalid password"}; - |
| status | Pass |
| evidence | API-04.png |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / API Test Suite / row 8 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W4-API-05

| Field | Record |
|---|---|
| id | API-05 |
| feature | /api/login |
| tech | API |
| objective | POST /api/login |
| preconditions | Authentication required: No |
| data | Valid username/password |
| steps | Send request and verify HTTP status and response |
| expected | 200; JSON includes id and username |
| actual | HTTP 200 OK; JSON returned id: 11 and username week4_farisha00; - |
| status | Pass |
| evidence | API-05.png |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / API Test Suite / row 9 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02 |

## W4-API-06

| Field | Record |
|---|---|
| id | API-06 |
| feature | /api/login |
| tech | API |
| objective | POST /api/login |
| preconditions | Authentication required: No |
| data | Incorrect credentials |
| steps | Send request and verify HTTP status and response |
| expected | 401; JSON error: "invalid credentials" |
| actual | HTTP 401 Unauthorized; JSON response: {"error":"invalid credentials"}; - |
| status | Pass |
| evidence | API-06.png |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / API Test Suite / row 10 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02 |

## W4-API-07

| Field | Record |
|---|---|
| id | API-07 |
| feature | /api/tasks |
| tech | API |
| objective | GET /api/tasks |
| preconditions | Authentication required: Yes |
| data | Authenticated session |
| steps | Send request and verify HTTP status and response |
| expected | 200; JSON array of tasks |
| actual | HTTP 200 OK; returned an empty JSON array []; - |
| status | Pass |
| evidence | API-07.png |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / API Test Suite / row 11 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-08 |

## W4-API-08

| Field | Record |
|---|---|
| id | API-08 |
| feature | /api/tasks |
| tech | API |
| objective | GET /api/tasks |
| preconditions | Authentication required: No |
| data | No authenticated session |
| steps | Send request and verify HTTP status and response |
| expected | 401; JSON error: "authentication required" |
| actual | HTTP 401 Unauthorized; JSON response: {"error":"authentication required"}; - |
| status | Pass |
| evidence | API-08.png |
| defect | D-005 |
| Source | STQA Data Collection (Week 4).xlsx / API Test Suite / row 12 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02 |

## W4-API-09

| Field | Record |
|---|---|
| id | API-09 |
| feature | /api/tasks |
| tech | API |
| objective | POST /api/tasks |
| preconditions | Authentication required: Yes |
| data | {"title":"Week 4 API test task"} |
| steps | Send request and verify HTTP status and response |
| expected | 201; Created task JSON includes id/title/urgency |
| actual | HTTP 201 Created; task ID 22, title Week 4 API test task, urgency No due date; - |
| status | Pass |
| evidence | API-09-A.png<br>API-09-B.png |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / API Test Suite / row 13 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-03 |

## W4-API-10

| Field | Record |
|---|---|
| id | API-10 |
| feature | /api/tasks |
| tech | API |
| objective | POST /api/tasks |
| preconditions | Authentication required: Yes |
| data | {"title":"   "} |
| steps | Send request and verify HTTP status and response |
| expected | 400; JSON error: "title is required" |
| actual | HTTP 400 Bad Request; JSON response: {"error":"title is required"}; - |
| status | Pass |
| evidence | API-10.png |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / API Test Suite / row 14 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-03 |

## W4-API-11

| Field | Record |
|---|---|
| id | API-11 |
| feature | /api/tasks/999999 |
| tech | API |
| objective | GET /api/tasks/999999 |
| preconditions | Authentication required: Yes |
| data | ID confirmed not to exist |
| steps | Send request and verify HTTP status and response |
| expected | 404; JSON error: "not found" |
| actual | Postman returned 404 Not Found for GET /api/tasks/999999 with JSON error "not found".; - |
| status | Pass |
| evidence | API-11.png |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / API Test Suite / row 15 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-08 |

## W4-API-12

| Field | Record |
|---|---|
| id | API-12 |
| feature | /api/tasks/{task_id} |
| tech | API |
| objective | PUT /api/tasks/{task_id} |
| preconditions | Authentication required: Yes |
| data | {"title":"Week 4 updated task"} |
| steps | Send request and verify HTTP status and response |
| expected | 200; Updated task JSON reflects change |
| actual | Postman returned 200 OK. Task 22 title changed to "Week 4 updated task".; - |
| status | Pass |
| evidence | API-12.png |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / API Test Suite / row 16 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-04 |

## W4-API-13

| Field | Record |
|---|---|
| id | API-13 |
| feature | /api/tasks/{task_id} |
| tech | API |
| objective | DELETE /api/tasks/{task_id} |
| preconditions | Authentication required: Yes |
| data | No body |
| steps | Send request and verify HTTP status and response |
| expected | 200; JSON result: "ok" |
| actual | Postman returned 200 OK and {"result":"ok"} when deleting disposable test task ID 22.; - |
| status | Pass |
| evidence | API-13.png |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / API Test Suite / row 17 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-04 |

## W4-API-14

| Field | Record |
|---|---|
| id | API-14 |
| feature | /api/dashboard |
| tech | API |
| objective | GET /api/dashboard |
| preconditions | Authentication required: Yes |
| data | Authenticated session |
| steps | Send request and verify HTTP status and response |
| expected | 200; JSON dashboard counts |
| actual | Postman returned 200 OK with total=1, open=1, overdue=0, due_soon=0, completed_this_week=0.; - |
| status | Pass |
| evidence | API-14.png |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / API Test Suite / row 18 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-06 |

## W4-API-15

| Field | Record |
|---|---|
| id | API-15 |
| feature | /api/dashboard |
| tech | API |
| objective | GET /api/dashboard |
| preconditions | Authentication required: No |
| data | No authenticated session |
| steps | Send request and verify HTTP status and response |
| expected | 401; JSON error: "authentication required" |
| actual | Postman returned 401 Unauthorized with the expected authentication-required error when no valid session cookie was provided.; - |
| status | Pass |
| evidence | API-15.png |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / API Test Suite / row 19 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-06 |

## W4-API-16

| Field | Record |
|---|---|
| id | API-16 |
| feature | /api/tasks |
| tech | API |
| objective | GET /api/tasks |
| preconditions | Authentication required: Yes |
| data | Invalid page/per_page values (e.g. text) |
| steps | Send request and verify HTTP status and response |
| expected | Record observed behaviour; Check pagination and response content |
| actual | 200 OK; returned a JSON array containing the Week 4 API test task despite invalid pagination values.; - |
| status | Pass |
| evidence | API-16.png |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / API Test Suite / row 20 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-08 |

## W4-API-17

| Field | Record |
|---|---|
| id | API-17 |
| feature | /api/tasks |
| tech | API |
| objective | POST /api/tasks |
| preconditions | Authentication required: Yes |
| data | Wrong type/invalid category_id |
| steps | Send request and verify HTTP status and response |
| expected | Record observed behaviour; Controlled response; no server crash or inconsistent data |
| actual | HTTP 201 Created; task ID 27 was created with category_id "invalid" and category null.; - |
| status | Fail |
| evidence | API-17.png |
| defect | D-009 |
| Source | STQA Data Collection (Week 4).xlsx / API Test Suite / row 21 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Reviewed test data | JSON {"title":"W7-invalid-category","category_id":"invalid"}; repeat with category_id 99999 after confirming it does not exist |
| Reviewed numbered procedure | 1. Authenticate a disposable account. 2. Save baseline task IDs. 3. POST /api/tasks with application/json and the stated payload. 4. Record status/body. 5. GET /api/tasks and verify neither payload created a task. |
| Reviewed expected result | HTTP 400 validation error; no task created. This reviewed expectation follows the automated category-validation contract; historical oracle was less precise. |
| Requirement IDs | R-07 |

## W4-API-18

| Field | Record |
|---|---|
| id | API-18 |
| feature | /api/tasks?q=' OR 1=1 -- |
| tech | API |
| objective | GET /api/tasks?q=' OR 1=1 -- |
| preconditions | Authentication required: Yes |
| data | Search query with SQL-like characters |
| steps | Send request and verify HTTP status and response |
| expected | Record observed behaviour; No data leakage or SQL error; only own user's tasks |
| actual | 500 Internal Server Error. SQLite reported an incorrect number of bindings supplied when SQL-like search input was submitted.; - |
| status | Fail |
| evidence | API-18.png |
| defect | D-010 |
| Source | STQA Data Collection (Week 4).xlsx / API Test Suite / row 22 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Reviewed test data | Query q=' OR 1=1 --; disposable authenticated account |
| Reviewed numbered procedure | 1. Authenticate. 2. Send GET /api/tasks using a URL-encoded q parameter with the stated value. 3. Record status, body and server log. 4. Verify no other user records are disclosed. |
| Reviewed expected result | HTTP 200 with literal-search results limited to the current user, or a documented HTTP 400 validation response; never HTTP 500, SQL error disclosure, or cross-user data. |
| Requirement IDs | R-08; R-12 |

## W4-CMP-01

| Field | Record |
|---|---|
| id | CMP-01 |
| feature | Task creation |
| tech | UI/API comparison |
| objective | Create equivalent task in browser and API. |
| preconditions | Equivalent user and task state |
| data | See scenario |
| steps | Create equivalent task in browser and API. |
| expected | Task should appear in UI and be returned by API for the same user. |
| actual | UI: Task "CMP-01 Comparison Task" was created and appeared in the task list.; API: GET /api/tasks returned HTTP 200 OK and included the task in the JSON response. |
| status | Pass |
| evidence | Task created in UI and verified through API; API-07. |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / UI vs API Comparison / row 5 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-03 |

## W4-CMP-02

| Field | Record |
|---|---|
| id | CMP-02 |
| feature | Blank task title |
| tech | UI/API comparison |
| objective | Submit blank title in UI and POST /api/tasks. |
| preconditions | Equivalent user and task state |
| data | See scenario |
| steps | Submit blank title in UI and POST /api/tasks. |
| expected | Both paths reject blank title; record differences in validation/message/status. |
| actual | UI: The browser rejected the blank task title and displayed a validation message. No task was created.; API: POST /api/tasks returned HTTP 400 Bad Request with {"error":"title is required"}. |
| status | Pass |
| evidence | API result verified using API-10. |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / UI vs API Comparison / row 6 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-03 |

## W4-CMP-03

| Field | Record |
|---|---|
| id | CMP-03 |
| feature | Task completion |
| tech | UI/API comparison |
| objective | Complete task in UI and inspect via GET /api/tasks. |
| preconditions | Equivalent user and task state |
| data | See scenario |
| steps | Complete task in UI and inspect via GET /api/tasks. |
| expected | API done field and UI state agree. |
| actual | UI: The browser showed “Due + 2 day” as completed. The task was crossed out and displayed a check mark.; API: GET /api/tasks returned the completed task with "done": true and "urgency": "Done". |
| status | Pass |
| evidence | Completed task state matches between UI and API. |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / UI vs API Comparison / row 7 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-08 |

## W4-CMP-04

| Field | Record |
|---|---|
| id | CMP-04 |
| feature | Dashboard counts |
| tech | UI/API comparison |
| objective | Compare dashboard UI with GET /api/dashboard. |
| preconditions | Equivalent user and task state |
| data | See scenario |
| steps | Compare dashboard UI with GET /api/dashboard. |
| expected | Counts match the same user's task data. |
| actual | UI: Dashboard displayed Total Tasks: 15, Open: 14, Overdue: 4, Due Soon: 1, Completed (last 7 days): 1.; API: GET /api/dashboard returned HTTP 200 OK with total: 15, open: 14, overdue: 4, due_soon: 1, completed_this_week: 1. |
| status | Pass |
| evidence | UI dashboard counts match API dashboard response. |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / UI vs API Comparison / row 8 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-06 |

## W4-CMP-05

| Field | Record |
|---|---|
| id | CMP-05 |
| feature | Due-date urgency |
| tech | UI/API comparison |
| objective | Create a task due today and compare UI/API urgency. |
| preconditions | Equivalent user and task state |
| data | See scenario |
| steps | Create a task due today and compare UI/API urgency. |
| expected | UI/API should be consistent; compare with existing DEF-04 rather than duplicating it. |
| actual | UI: Task CMP-05 Due Today Test with due date 2026-10-21 displayed urgency as Overdue.; API: GET /api/tasks returned HTTP 200 OK. Task ID 26 had due date 2026-10-21 and urgency Overdue. |
| status | Pass |
| evidence | UI and API urgency values match, but both show the known incorrect result. Refer to DEF-04. |
| defect | None linked |
| Source | STQA Data Collection (Week 4).xlsx / UI vs API Comparison / row 9 |
| Original defect reference | Not recorded in source |
| review disposition | Historical Pass measures UI/API agreement only; it does not prove correct due-today classification. D-004 remains unresolved. |
| Requirement IDs | R-03; R-05 |

## W5-SEC-01

| Field | Record |
|---|---|
| id | SEC-01 |
| feature | GET /api/tasks |
| tech | Security / TH-01 |
| objective | Send request without authentication/session. |
| preconditions | Local disposable test accounts; see source |
| data | See steps |
| steps | Send request without authentication/session. |
| expected | 401/403 or documented redirect; no private task data returned. |
| actual | HTTP 401 Unauthorized returned with "authentication required". No task data was returned. |
| status | Pass |
| evidence | SEC-01.png |
| defect | D-005 |
| Source | STQA Data Collection (Week 5).xlsx / Security Test Cases / row 5 |
| Original defect reference | Unauthenticated access correctly blocked. |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02; R-12 |

## W5-SEC-02

| Field | Record |
|---|---|
| id | SEC-02 |
| feature | GET /api/dashboard |
| tech | Security / TH-01 |
| objective | Send request without authentication/session. |
| preconditions | Local disposable test accounts; see source |
| data | See steps |
| steps | Send request without authentication/session. |
| expected | 401/403 or documented redirect; no private dashboard data returned. |
| actual | HTTP 401 Unauthorized returned with "authentication required". No private dashboard data was returned. |
| status | Pass |
| evidence | SEC-02.png |
| defect | None linked |
| Source | STQA Data Collection (Week 5).xlsx / Security Test Cases / row 6 |
| Original defect reference | Unauthenticated dashboard access correctly blocked. |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02; R-06; R-12 |

## W5-SEC-03

| Field | Record |
|---|---|
| id | SEC-03 |
| feature | POST /api/register |
| tech | Security / TH-02 |
| objective | Try registering a username that already exists, using a test account. |
| preconditions | Local disposable test accounts; see source |
| data | See steps |
| steps | Try registering a username that already exists, using a test account. |
| expected | Registration rejected with a clear message; no unintended login or duplicate account. |
| actual | HTTP 201 Created returned. Duplicate username was accepted and a new user ID (19) was created. |
| status | Fail |
| evidence | SEC-03.png |
| defect | D-002 |
| Source | STQA Data Collection (Week 5).xlsx / Security Test Cases / row 7 |
| Original defect reference | BUG-W4-03 persists. Duplicate username registration is accepted. |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01; R-12 |

## W5-SEC-04

| Field | Record |
|---|---|
| id | SEC-04 |
| feature | POST /api/tasks |
| tech | Security / TH-03 |
| objective | Submit a test task with an invalid category_id type/value. |
| preconditions | Local disposable test accounts; see source |
| data | See steps |
| steps | Submit a test task with an invalid category_id type/value. |
| expected | Controlled validation response; no inconsistent task record is created. |
| actual | HTTP 201 Created returned. Task ID 29 was created with an invalid category_id value; category was returned as null. |
| status | Fail |
| evidence | SEC-04.png |
| defect | D-009 |
| Source | STQA Data Collection (Week 5).xlsx / Security Test Cases / row 8 |
| Original defect reference | BUG-W4-01 persists. Invalid category value was accepted. |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-07; R-12 |

## W5-SEC-05

| Field | Record |
|---|---|
| id | SEC-05 |
| feature | GET /api/tasks |
| tech | Security / TH-05 |
| objective | If supported, log in as test account A and verify returned tasks belong to A; repeat with test account B. |
| preconditions | Local disposable test accounts; see source |
| data | See steps |
| steps | If supported, log in as test account A and verify returned tasks belong to A; repeat with test account B. |
| expected | Each account sees only its own tasks; no cross-account task disclosure. |
| actual | Account B received HTTP 404 Not Found when requesting Account A's task (ID 28). The endpoint did not return the task. |
| status | Pass |
| evidence | TH-05.png |
| defect | None linked |
| Source | STQA Data Collection (Week 5).xlsx / Security Test Cases / row 9 |
| Original defect reference | Existing Week 4/Week 5 evidence reused; no new test executed. |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02; R-12 |

## W5-SEC-06

| Field | Record |
|---|---|
| id | SEC-06 |
| feature | GET /api/tasks?q=... |
| tech | Security / TH-06 |
| objective | Send one SQL-like search string once, using a test session. |
| preconditions | Local disposable test accounts; see source |
| data | See steps |
| steps | Send one SQL-like search string once, using a test session. |
| expected | Safe response (e.g. empty results or validation error); no HTTP 500 or data leakage. |
| actual | Week 4 testing showed that an SQL-like search string caused HTTP 500 Internal Server Error due to a SQLite binding error. |
| status | Fail |
| evidence | API-18.png |
| defect | D-010 |
| Source | STQA Data Collection (Week 5).xlsx / Security Test Cases / row 10 |
| Original defect reference | BUG-W4-02 persists based on existing Week 4 evidence. No new test executed. |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-08; R-12 |

## W5-SEC-07

| Field | Record |
|---|---|
| id | SEC-07 |
| feature | POST /api/register |
| tech | Security / TH-08 |
| objective | Submit a username shorter than the documented minimum using a fresh test value. |
| preconditions | Local disposable test accounts; see source |
| data | See steps |
| steps | Submit a username shorter than the documented minimum using a fresh test value. |
| expected | Registration rejected with a validation message; account is not created. |
| actual | Week 4 API-03 returned HTTP 400 Bad Request with "invalid username" for the 2-character username "ab". |
| status | Pass |
| evidence | API-03.png |
| defect | None linked |
| Source | STQA Data Collection (Week 5).xlsx / Security Test Cases / row 11 |
| Original defect reference | Existing Week 4 evidence reused; username below the minimum length was rejected. |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01; R-12 |

## W5-SEC-08

| Field | Record |
|---|---|
| id | SEC-08 |
| feature | POST /api/register |
| tech | Security / TH-08 |
| objective | Submit a password below the documented minimum using a test account. |
| preconditions | Local disposable test accounts; see source |
| data | See steps |
| steps | Submit a password below the documented minimum using a test account. |
| expected | Registration rejected with a validation message; account is not created. |
| actual | Week 4 API-04 returned HTTP 400 Bad Request for a password below the minimum length, with an invalid-password response. |
| status | Pass |
| evidence | API-04.png |
| defect | None linked |
| Source | STQA Data Collection (Week 5).xlsx / Security Test Cases / row 12 |
| Original defect reference | Existing Week 4 evidence reused; short password was rejected. |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01; R-12 |

## W5-SEC-09

| Field | Record |
|---|---|
| id | SEC-09 |
| feature | Privileged function (if any) |
| tech | Security / TH-07 |
| objective | If roles/privileges exist, try the action as a non-privileged test user; otherwise mark Not Applicable. |
| preconditions | Local disposable test accounts; see source |
| data | See steps |
| steps | If roles/privileges exist, try the action as a non-privileged test user; otherwise mark Not Applicable. |
| expected | Unauthorized action is blocked; no protected state changes. |
| actual | No administrator roles or privileged functions were identified in the application. |
| status | Not Applicable |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 5).xlsx / Security Test Cases / row 13 |
| Original defect reference | Application has no role-based access control or administrator functions to test. |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-04; R-12 |

## W5-SEC-10

| Field | Record |
|---|---|
| id | SEC-10 |
| feature | Task activity history |
| tech | Security / TH-04 |
| objective | Create/update/delete one disposable test task and check whether an audit/activity history is available. |
| preconditions | Local disposable test accounts; see source |
| data | See steps |
| steps | Create/update/delete one disposable test task and check whether an audit/activity history is available. |
| expected | Activity is traceable if feature exists; if not, document missing audit trail as a limitation, not a failed functional test. |
| actual | No task activity history or audit log was found in the application. |
| status | Not Applicable |
| evidence | Not recorded in source |
| defect | None linked |
| Source | STQA Data Collection (Week 5).xlsx / Security Test Cases / row 14 |
| Original defect reference | No audit trail feature was identified; recorded as a limitation based on code review, not a newly executed test. |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-03; R-04; R-12 |

## W6-AUTO-01

| Field | Record |
|---|---|
| id | AUTO-01 |
| feature | WEB-01 |
| tech | API automation |
| objective | test_registration_with_valid_details |
| preconditions | Isolated temporary database; test client |
| data | See test_api_automation.py |
| steps | Run pytest test_api_automation.py; inspect named test |
| expected | HTTP 201; registration succeeds with valid username and password |
| actual | HTTP 201 CREATED; registration successful |
| status | Pass |
| evidence | evidence/historical_week6_pytest_log.txt |
| defect | None linked |
| Source | STQA Data Collection (Week 6).xlsx / Automated Test Results / row 2 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W6-AUTO-02

| Field | Record |
|---|---|
| id | AUTO-02 |
| feature | WEB-02 |
| tech | API automation |
| objective | test_registration_rejects_username_below_minimum_length |
| preconditions | Isolated temporary database; test client |
| data | See test_api_automation.py |
| steps | Run pytest test_api_automation.py; inspect named test |
| expected | HTTP 400 or 422; short username rejected |
| actual | Username was rejected; test passed |
| status | Pass |
| evidence | evidence/historical_week6_pytest_log.txt |
| defect | None linked |
| Source | STQA Data Collection (Week 6).xlsx / Automated Test Results / row 3 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W6-AUTO-03

| Field | Record |
|---|---|
| id | AUTO-03 |
| feature | WEB-03 |
| tech | API automation |
| objective | test_registration_rejects_short_password |
| preconditions | Isolated temporary database; test client |
| data | See test_api_automation.py |
| steps | Run pytest test_api_automation.py; inspect named test |
| expected | HTTP 400 or 422; short password rejected |
| actual | Password "1" was rejected; test passed |
| status | Pass |
| evidence | evidence/historical_week6_pytest_log.txt |
| defect | None linked |
| Source | STQA Data Collection (Week 6).xlsx / Automated Test Results / row 4 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W6-AUTO-04

| Field | Record |
|---|---|
| id | AUTO-04 |
| feature | WEB-04 |
| tech | API automation |
| objective | test_duplicate_registration_is_rejected |
| preconditions | Isolated temporary database; test client |
| data | See test_api_automation.py |
| steps | Run pytest test_api_automation.py; inspect named test |
| expected | HTTP 400 or 409; duplicate username rejected |
| actual | HTTP 201 CREATED; duplicate username accepted |
| status | Fail |
| evidence | evidence/historical_week6_pytest_log.txt |
| defect | D-002 |
| Source | STQA Data Collection (Week 6).xlsx / Automated Test Results / row 5 |
| Original defect reference | BUG-W6-01 |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-01 |

## W6-AUTO-05

| Field | Record |
|---|---|
| id | AUTO-05 |
| feature | WEB-05 |
| tech | API automation |
| objective | Log in with valid credentials |
| preconditions | Isolated temporary database; test client |
| data | See test_api_automation.py |
| steps | Run pytest test_api_automation.py; inspect named test |
| expected | HTTP 200; valid login succeeds |
| actual | HTTP 200; valid login succeeded |
| status | Pass |
| evidence | evidence/historical_week6_pytest_log.txt |
| defect | None linked |
| Source | STQA Data Collection (Week 6).xlsx / Automated Test Results / row 6 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02 |

## W6-AUTO-06

| Field | Record |
|---|---|
| id | AUTO-06 |
| feature | WEB-06 |
| tech | API automation |
| objective | test_api_login_rejects_incorrect_password |
| preconditions | Isolated temporary database; test client |
| data | See test_api_automation.py |
| steps | Run pytest test_api_automation.py; inspect named test |
| expected | HTTP 401; invalid credentials |
| actual | HTTP 401; invalid credentials |
| status | Pass |
| evidence | evidence/historical_week6_pytest_log.txt |
| defect | None linked |
| Source | STQA Data Collection (Week 6).xlsx / Automated Test Results / row 7 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02 |

## W6-AUTO-07

| Field | Record |
|---|---|
| id | AUTO-07 |
| feature | WEB-07 |
| tech | API automation |
| objective | test_authenticated_user_can_create_task |
| preconditions | Isolated temporary database; test client |
| data | See test_api_automation.py |
| steps | Run pytest test_api_automation.py; inspect named test |
| expected | HTTP 201; task created successfully with id, title and urgency |
| actual | HTTP 201; task created successfully with id, title and urgency |
| status | Pass |
| evidence | evidence/historical_week6_pytest_log.txt |
| defect | None linked |
| Source | STQA Data Collection (Week 6).xlsx / Automated Test Results / row 8 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02; R-03 |

## W6-AUTO-08

| Field | Record |
|---|---|
| id | AUTO-08 |
| feature | WEB-08 |
| tech | API automation |
| objective | test_authenticated_user_cannot_create_task_with_blank_title |
| preconditions | Isolated temporary database; test client |
| data | See test_api_automation.py |
| steps | Run pytest test_api_automation.py; inspect named test |
| expected | HTTP 400; blank task title is rejected |
| actual | HTTP 400; title is required |
| status | Pass |
| evidence | evidence/historical_week6_pytest_log.txt |
| defect | None linked |
| Source | STQA Data Collection (Week 6).xlsx / Automated Test Results / row 9 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02; R-03 |

## W6-AUTO-09

| Field | Record |
|---|---|
| id | AUTO-09 |
| feature | WEB-09 |
| tech | API automation |
| objective | test_authenticated_user_can_update_task |
| preconditions | Isolated temporary database; test client |
| data | See test_api_automation.py |
| steps | Run pytest test_api_automation.py; inspect named test |
| expected | HTTP 200; updated task title is returned |
| actual | HTTP 200; Updated task title returned |
| status | Pass |
| evidence | evidence/historical_week6_pytest_log.txt |
| defect | None linked |
| Source | STQA Data Collection (Week 6).xlsx / Automated Test Results / row 10 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02; R-04 |

## W6-AUTO-10

| Field | Record |
|---|---|
| id | AUTO-10 |
| feature | WEB-10 |
| tech | API automation |
| objective | test_authenticated_user_can_complete_task |
| preconditions | Isolated temporary database; test client |
| data | See test_api_automation.py |
| steps | Run pytest test_api_automation.py; inspect named test |
| expected | HTTP 200;  Task completion request returns and done is True |
| actual | HTTP 200; done is True |
| status | Pass |
| evidence | evidence/historical_week6_pytest_log.txt |
| defect | None linked |
| Source | STQA Data Collection (Week 6).xlsx / Automated Test Results / row 11 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02; R-04 |

## W6-AUTO-11

| Field | Record |
|---|---|
| id | AUTO-11 |
| feature | WEB-11 |
| tech | API automation |
| objective | test_authenticated_user_can_delete_task |
| preconditions | Isolated temporary database; test client |
| data | See test_api_automation.py |
| steps | Run pytest test_api_automation.py; inspect named test |
| expected | HTTP 404; task is deleted successfully and subsequent retrieval returns  |
| actual | HTTP retrieval returned; 404 Deletion successful |
| status | Pass |
| evidence | evidence/historical_week6_pytest_log.txt |
| defect | None linked |
| Source | STQA Data Collection (Week 6).xlsx / Automated Test Results / row 12 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02; R-04 |

## W6-AUTO-12

| Field | Record |
|---|---|
| id | AUTO-12 |
| feature | WEB-12 |
| tech | API automation |
| objective | test_authenticated_user_can_search_tasks_by_title |
| preconditions | Isolated temporary database; test client |
| data | See test_api_automation.py |
| steps | Run pytest test_api_automation.py; inspect named test |
| expected | HTTP 200; matching task is returned and unrelated task is excluded |
| actual | HTTP 200; matching task found and unrelated task excluded |
| status | Pass |
| evidence | evidence/historical_week6_pytest_log.txt |
| defect | None linked |
| Source | STQA Data Collection (Week 6).xlsx / Automated Test Results / row 13 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02; R-08 |

## W6-AUTO-13

| Field | Record |
|---|---|
| id | AUTO-13 |
| feature | API-08 |
| tech | API automation |
| objective | GET /api/tasks without authentication returns 401 |
| preconditions | Isolated temporary database; test client |
| data | See test_api_automation.py |
| steps | Run pytest test_api_automation.py; inspect named test |
| expected | HTTP 401; authentication required |
| actual | HTTP 401; authentication required |
| status | Pass |
| evidence | evidence/historical_week6_pytest_log.txt |
| defect | D-005 |
| Source | STQA Data Collection (Week 6).xlsx / Automated Test Results / row 14 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-02 |

## W6-AUTO-14

| Field | Record |
|---|---|
| id | AUTO-14 |
| feature | API-10 |
| tech | API automation |
| objective | POST /api/tasks with blank title returns 400 |
| preconditions | Isolated temporary database; test client |
| data | See test_api_automation.py |
| steps | Run pytest test_api_automation.py; inspect named test |
| expected | HTTP 400; title is required |
| actual | HTTP 400; title is required |
| status | Pass |
| evidence | evidence/historical_week6_pytest_log.txt |
| defect | None linked |
| Source | STQA Data Collection (Week 6).xlsx / Automated Test Results / row 15 |
| Original defect reference | Not recorded in source |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-03 |

## W6-AUTO-15

| Field | Record |
|---|---|
| id | AUTO-15 |
| feature | API-17 |
| tech | API automation |
| objective | test_api_rejects_invalid_category_id |
| preconditions | Isolated temporary database; test client |
| data | See test_api_automation.py |
| steps | Run pytest test_api_automation.py; inspect named test |
| expected | HTTP 400; invalid category_id is rejected and no task is created |
| actual | HTTP 201 CREATED; task created with invalid category_id |
| status | Fail |
| evidence | evidence/historical_week6_pytest_log.txt |
| defect | D-009 |
| Source | STQA Data Collection (Week 6).xlsx / Automated Test Results / row 16 |
| Original defect reference | BUG-W4-01 |
| review disposition | Historical result retained; no new execution in this repair |
| Requirement IDs | R-07 |

## W2-EXTRA-01

| Field | Record |
|---|---|
| id | W2-EXTRA-01 |
| feature | Urgency default date |
| tech | Unit branch test |
| objective | test_helpers.py::test_urg_06_uses_current_date_when_today_not_provided |
| preconditions | Dependencies installed; use copied application; API fixtures isolate database |
| data | Tomorrow relative to system date |
| steps | 1. Open application directory. 2. Run python -m pytest -p no:cacheprovider test_helpers.py::test_urg_06_uses_current_date_when_today_not_provided -v. 3. Inspect assertion and result. |
| expected | Due Soon |
| actual | PASSED in supplied saved log; not rerun during this repair |
| status | Pass |
| evidence | evidence/current_helpers_pytest.txt |
| defect | None linked |
| Source | Executed_Automation_Inventory.md; copied test function; saved execution log |
| review disposition | Supplemental executed function added to register; does not add a historical run |
| Requirement IDs | R-05 |

## W2-EXTRA-02

| Field | Record |
|---|---|
| id | W2-EXTRA-02 |
| feature | Completion default time |
| tech | Unit branch test |
| objective | test_helpers.py::test_day_07_uses_current_time_when_now_not_provided |
| preconditions | Dependencies installed; use copied application; API fixtures isolate database |
| data | Completion one day before system time |
| steps | 1. Open application directory. 2. Run python -m pytest -p no:cacheprovider test_helpers.py::test_day_07_uses_current_time_when_now_not_provided -v. 3. Inspect assertion and result. |
| expected | True |
| actual | PASSED in supplied saved log; not rerun during this repair |
| status | Pass |
| evidence | evidence/current_helpers_pytest.txt |
| defect | None linked |
| Source | Executed_Automation_Inventory.md; copied test function; saved execution log |
| review disposition | Supplemental executed function added to register; does not add a historical run |
| Requirement IDs | R-06 |

## W6-EXTRA-01

| Field | Record |
|---|---|
| id | W6-EXTRA-01 |
| feature | Dashboard authentication |
| tech | API automation |
| objective | test_api_automation.py::test_unauthenticated_user_cannot_access_dashboard |
| preconditions | Dependencies installed; use copied application; API fixtures isolate database |
| data | Fresh client; GET /api/dashboard |
| steps | 1. Open application directory. 2. Run python -m pytest -p no:cacheprovider test_api_automation.py::test_unauthenticated_user_cannot_access_dashboard -v. 3. Inspect assertion and result. |
| expected | HTTP 401; authentication required |
| actual | PASSED in supplied saved log; not rerun during this repair |
| status | Pass |
| evidence | evidence/historical_week6_pytest_log.txt |
| defect | None linked |
| Source | Executed_Automation_Inventory.md; copied test function; saved execution log |
| review disposition | Supplemental executed function added to register; does not add a historical run |
| Requirement IDs | R-02; R-06 |

## W6-EXTRA-02

| Field | Record |
|---|---|
| id | W6-EXTRA-02 |
| feature | Authentication precedes validation |
| tech | API automation |
| objective | test_api_automation.py::test_blank_title_request_without_login_is_rejected |
| preconditions | Dependencies installed; use copied application; API fixtures isolate database |
| data | Fresh client; POST /api/tasks with title empty |
| steps | 1. Open application directory. 2. Run python -m pytest -p no:cacheprovider test_api_automation.py::test_blank_title_request_without_login_is_rejected -v. 3. Inspect assertion and result. |
| expected | HTTP 401; authentication required |
| actual | PASSED in supplied saved log; not rerun during this repair |
| status | Pass |
| evidence | evidence/historical_week6_pytest_log.txt |
| defect | None linked |
| Source | Executed_Automation_Inventory.md; copied test function; saved execution log |
| review disposition | Supplemental executed function added to register; does not add a historical run |
| Requirement IDs | R-02; R-03 |

## Verified run — 22 October 2026 (supersedes earlier execution-pending notes)

All three automated test files executed on the copied application using isolated temporary SQLite databases: 44 tests, 38 Pass, 6 Fail, no skips or setup errors. Helpers: 22 Pass/3 Fail; existing API suite: 14 Pass/2 Fail; Week 7 verification: 2 Pass/1 Fail. Evidence: [evidence/verification_2026_10_22/pytest_full_log.txt](evidence/verification_2026_10_22/pytest_full_log.txt); machine-readable results and environment are in the same folder. Source hashes match the included baseline.

D-001, D-002, D-004, D-006 and D-009 reproduced. CR-001 is now dynamically confirmed: B's DELETE returned HTTP 200 and A's subsequent GET returned HTTP 404. W7-VERIFY-01 and W7-VERIFY-02 passed. Current unauthenticated task access is blocked; D-005's historical discrepancy remains unresolved because historical builds are unknown. The historical W1-API-11/API-12 observations remain unchanged; new evidence establishes current GET protection and current DELETE failure.

This run does not execute all 198 documentation records. Manual GUI, browser compatibility, accessibility, historical web observations and performance experiments were not rerun. Structural coverage does not establish correctness: helpers have 100% measured statement/branch coverage while three assertions fail. Overall combined coverage of app.py/helpers.py is approximately 63%; this excludes browser templates, CSS and real browser behaviour.
