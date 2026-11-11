# Source register and preserved workbook records

Prepared 22 October 2026. Sources are the six original weekly workbooks in `Group_Project_Collection_Weekly`. Original files are unchanged. Cell references below locate every extracted observation. Cached values were read from the XLSX XML; source formulas were not recalculated.

## Evidence inventory

| Relative source path | Bytes |
|---|---|
| STQA Data Collection (Week 1).xlsx | 30212 |
| STQA Data Collection (Week 2).xlsx | 18271 |
| STQA Data Collection (Week 3).xlsx | 23929 |
| STQA Data Collection (Week 4).xlsx | 24845 |
| STQA Data Collection (Week 5).xlsx | 32109 |
| STQA Data Collection (Week 6).xlsx | 20665 |
| week 2 evidence\branch_coverage_1.png | 236769 |
| week 2 evidence\branch_coverage_2.png | 245297 |
| week 2 evidence\CL-No-5-1.png | 287352 |
| week 2 evidence\CL-No-5-2.png | 265547 |
| week 2 evidence\CL-No-7-1.png | 254586 |
| week 2 evidence\CL-No-7-2.png | 259902 |
| week 2 evidence\CL-No-8-1.png | 250622 |
| week 2 evidence\CL-No-8-2.png | 259375 |
| week 2 evidence\coverage_report_proof_week2.png | 160138 |
| week 3 evidence\ACC-05_Empty_Title_Validation.png | 124368 |
| week 3 evidence\ACC-06_Label_Association.png | 219332 |
| week 3 evidence\ACC-08_Browser_Zoom_125.png | 129346 |
| week 3 evidence\COMP-02_Edge_Dashboard.png | 110821 |
| week 3 evidence\COMP-02_Edge_New_Task.png | 117652 |
| week 3 evidence\COMP-02_Edge_Tasks.png | 155279 |
| week 3 evidence\GUI-01_Empty_Title_Validation.png | 114777 |
| week 3 evidence\GUI-01_Valid_Title_Created.png | 153962 |
| week 3 evidence\GUI-02_Cancel_New_Task.png | 154075 |
| week 3 evidence\GUI-03_Dashboard_Navigation.png | 110204 |
| week 3 evidence\GUI-04_Form_Labels.png | 114629 |
| week 3 evidence\GUI-07_Dashboard.png.png | 111597 |
| week 3 evidence\GUI-07_My_Tasks.png | 153673 |
| week 3 evidence\GUI-08_Responsive_800px.png | 231455 |
| week 4 evidence\API-01.png | 222880 |
| week 4 evidence\API-02.png | 217174 |
| week 4 evidence\API-03.png | 234812 |
| week 4 evidence\API-04.png | 234562 |
| week 4 evidence\API-05.png | 235921 |
| week 4 evidence\API-06.png | 240904 |
| week 4 evidence\API-07.png | 285282 |
| week 4 evidence\API-08.png | 236838 |
| week 4 evidence\API-09-A.png | 244991 |
| week 4 evidence\API-09-B.png | 255090 |
| week 4 evidence\API-10.png | 242903 |
| week 4 evidence\API-11.png | 238131 |
| week 4 evidence\API-12.png | 259382 |
| week 4 evidence\API-13.png | 239865 |
| week 4 evidence\API-14.png | 244886 |
| week 4 evidence\API-15.png | 244315 |
| week 4 evidence\API-16-A.png | 255761 |
| week 4 evidence\API-16-B.png | 271095 |
| week 4 evidence\API-17.png | 272858 |
| week 4 evidence\API-18.png | 289933 |
| week 5 evidence\PERF-02.png | 167874 |
| week 5 evidence\PERF-03.png | 168725 |
| week 5 evidence\SEC-01.png | 239864 |
| week 5 evidence\SEC-02.png | 248160 |
| week 5 evidence\SEC-03.png | 275624 |
| week 5 evidence\SEC-04.png | 286323 |
| week 5 evidence\TH-01.png | 232038 |
| week 5 evidence\TH-05.png | 260089 |
| week 5 evidence\TH-06.png | 239440 |
| week 6 evidence\Pytest_Automation_Pass.png | 63235 |


## STQA Data Collection (Week 1).xlsx

### Feature Scope Matrix

| Cell | Source value |
|---|---|
| A1 | Feature / Test-Scope Matrix |
| A4 | Feature ID |
| B4 | Feature / area |
| C4 | What to test |
| D4 | Testing techniques |
| E4 | Priority |
| F4 | Notes |
| A5 | FS-01 |
| B5 | Create Account / Registration |
| C5 | Valid/invalid credentials, required fields, username rules, password boundaries, duplicate username, whitespace |
| D5 | EP, BVA, Decision Table, State Transition |
| E5 | High |
| F5 | Use unique usernames except duplicate test. |
| A6 | FS-02 |
| B6 | Login |
| C6 | Valid/invalid credentials, empty fields, username trimming, access after login |
| D6 | EP, Decision Table, State Transition |
| E6 | High |
| F6 | Create an account before login tests. |
| A7 | FS-03 |
| B7 | Logout / session |
| C7 | Logout and protected page access before/after logout |
| D7 | State Transition |
| E7 | High |
| F7 | Check redirect and session behaviour. |
| A8 | FS-04 |
| B8 | Task list / home |
| C8 | List loads, empty state, task visibility |
| D8 | Functional / EP |
| E8 | High |
| F8 | Use a logged-in account. |
| A9 | FS-05 |
| B9 | Create task |
| C9 | Title-only, full details, blank/space title, optional fields, dates |
| D9 | EP, BVA |
| E9 | High |
| F9 | Record actual behaviour for blank title. |
| A10 | FS-06 |
| B10 | Edit task |
| C10 | Edit title, description, category, date; nonexistent ID |
| D10 | EP, State Transition |
| E10 | High |
| F10 | Verify after refresh. |
| A11 | FS-07 |
| B11 | Complete / reopen task |
| C11 | Open → done → open; completion state persists |
| D11 | State Transition |
| E11 | High |
| F11 | Use an existing test task. |
| A12 | FS-08 |
| B12 | Delete task |
| C12 | Delete own task; nonexistent task; cross-user deletion |
| D12 | Decision Table, State Transition, access control |
| E12 | High |
| F12 | Cross-user test only with disposable test data. |
| A13 | FS-09 |
| B13 | Category filter |
| C13 | Work, Personal, Study, Urgent and no-match cases |
| D13 | EP |
| E13 | Medium |
| F13 | Seeded categories per README. |
| A14 | FS-10 |
| B14 | Status filter |
| C14 | Open and Done filters |
| D14 | EP |
| E14 | Medium |
| F14 | Have both open and completed tasks. |
| A15 | FS-11 |
| B15 | Title search |
| C15 | Matching title, partial title, no result |
| D15 | EP |
| E15 | Medium |
| F15 | Use distinct test titles. |
| A16 | FS-12 |
| B16 | Dashboard |
| C16 | Total, open, overdue, due soon, completed last 7 days |
| D16 | Functional, BVA |
| E16 | High |
| F16 | Compare counters against known tasks. |
| A17 | FS-13 |
| B17 | Task urgency |
| C17 | No date, yesterday, today, tomorrow, +2 days, +3 days, done |
| D17 | BVA, State Transition |
| E17 | High |
| F17 | Verify due-today behaviour. |
| A18 | FS-14 |
| B18 | API authentication |
| C18 | Protected endpoint with/without session |
| D18 | Decision Table, State Transition |
| E18 | High |
| F18 | API client or browser dev tools may be needed. |
| A19 | FS-15 |
| B19 | User data isolation |
| C19 | User B attempts to access/delete User A task |
| D19 | Access control / decision table |
| E19 | High |
| F19 | Use two test accounts you own. |


### Test Cases

| Cell | Source value |
|---|---|
| A1 | Master Test Cases and Execution Record |
| A4 | Test ID |
| B4 | Feature |
| C4 | Technique |
| D4 | Test scenario |
| E4 | Preconditions |
| F4 | Example test data |
| G4 | Steps to execute |
| H4 | Expected result |
| I4 | Actual result (your notes) |
| J4 | Status (Pass/Fail) |
| K4 | Evidence / screenshot |
| L4 | Defect ID |
| M4 | Notes |
| A5 | REG-01 |
| B5 | Registration |
| C5 | EP |
| D5 | Register with valid details |
| E5 | Logged out; register page open |
| F5 | Username: farish01; Password: TestPass123 |
| G5 | 1. Open Register. 2. Enter username/password. 3. Submit. |
| H5 | Account is created; appropriate confirmation/navigation appears. |
| I5 | Registration succeeded and the application displayed the task list with the logged-in username farish01 |
| J5 | Pass |
| A6 | REG-02 |
| B6 | Registration |
| C6 | EP |
| D6 | Username left empty |
| E6 | Register page open |
| F6 | Username: blank; Password: TestPass123 |
| G6 | Leave username blank; submit. |
| H6 | Registration is rejected; no account is created. |
| I6 | The browser displayed the validation message "Please fill out this field" and prevented form submission. |
| J6 | Pass |
| A7 | REG-03 |
| B7 | Registration |
| C7 | EP |
| D7 | Password left empty |
| E7 | Register page open |
| F7 | Username: farish02; Password: blank |
| G7 | Leave password blank; submit. |
| H7 | Registration is rejected; no account is created. |
| I7 | The browser displayed “Please fill out this field” and prevented form submission when the password field was empty. |
| J7 | Pass |
| A8 | REG-04 |
| B8 | Registration |
| C8 | EP |
| D8 | Both fields empty |
| E8 | Register page open |
| F8 | Username: blank; Password: blank |
| G8 | Leave both fields blank; submit. |
| H8 | Registration is rejected; no account is created. |
| I8 | The browser displayed “Please fill out this field” and prevented submission when both fields were empty. |
| J8 | Pass |
| A9 | REG-05 |
| B9 | Registration |
| C9 | BVA |
| D9 | Username below minimum length |
| E9 | Register page open |
| F9 | Username: ab (2 chars); Password: TestPass123 |
| G9 | Submit registration. |
| H9 | Registration rejected; username must be 3–20 characters. |
| I9 | The application displayed “Username must be 3–20 characters (letters, numbers, underscore)” and rejected the username. |
| J9 | Pass |
| A10 | REG-06 |
| B10 | Registration |
| C10 | BVA |
| D10 | Username at minimum length |
| E10 | Register page open |
| F10 | Username: abc (3 chars); Password: TestPass123 |
| G10 | Submit registration. |
| H10 | Username length is valid; account should be created if username is unique. |
| I10 | The application accepted the username abc, created the account and redirected to the My Tasks page. |
| J10 | Pass |
| A11 | REG-07 |
| B11 | Registration |
| C11 | BVA |
| D11 | Username at maximum length |
| E11 | Register page open |
| F11 | Username: abcdefghijklmnopqrst (20 chars); Password: TestPass123 |
| G11 | Submit registration. |
| H11 | Username length is valid; account should be created if unique. |
| I11 | The application accepted the username and redirected to the My Tasks page. |
| J11 | Pass |
| A12 | REG-08 |
| B12 | Registration |
| C12 | BVA |
| D12 | Username above maximum length |
| E12 | Register page open |
| F12 | Username: abcdefghijklmnopqrstu (21 chars); Password: TestPass123 |
| G12 | Submit registration. |
| H12 | Registration rejected; username must be 3–20 characters. |
| I12 | The application displayed “Username must be 3–20 characters (letters, numbers, underscore)” and rejected the 21-character username. |
| J12 | Pass |
| A13 | REG-09 |
| B13 | Registration |
| C13 | EP |
| D13 | Username contains spaces |
| E13 | Register page open |
| F13 | Username: test user; Password: TestPass123 |
| G13 | Submit registration. |
| H13 | Registration rejected because spaces are not allowed in username. |
| I13 | The application displayed “Username must be 3–20 characters (letters, numbers, underscore)” and rejected the username containing a space. |
| J13 | Pass |
| A14 | REG-10 |
| B14 | Registration |
| C14 | EP |
| D14 | Username contains hyphen |
| E14 | Register page open |
| F14 | Username: test-user; Password: TestPass123 |
| G14 | Submit registration. |
| H14 | Registration rejected because hyphen is not an allowed username character. |
| I14 | Registration is rejected because hyphens are not allowed in usernames. |
| J14 | Pass |
| A15 | REG-11 |
| B15 | Registration |
| C15 | BVA |
| D15 | Password has 7 characters |
| E15 | Register page open |
| F15 | Username: farish11; Password: abc1234 (7 chars) |
| G15 | Submit registration. |
| H15 | Registration rejected. |
| I15 | The application displayed “Password must be at least 8 characters” and rejected the password. |
| J15 | Pass |
| A16 | REG-12 |
| B16 | Registration |
| C16 | BVA |
| D16 | Password has 8 characters |
| E16 | Register page open |
| F16 | Username: farish12; Password: abc12345 (8 chars) |
| G16 | Submit registration. |
| H16 | Check actual behaviour; implementation may reject although message says at least 8 characters. |
| I16 | The application rejected the password and displayed “Password must be at least 8 characters.” |
| J16 | Fail |
| L16 | DEF-01 |
| M16 | Potential validation boundary mismatch. |
| A17 | REG-13 |
| B17 | Registration |
| C17 | BVA |
| D17 | Password has 9 characters |
| E17 | Register page open |
| F17 | Username: farish13; Password: abc123456 (9 chars) |
| G17 | Submit registration. |
| H17 | Password passes length validation; account created if username is unique. |
| I17 | The application accepted the credentials, created the account and redirected to the My Tasks page. |
| J17 | Pass |
| A18 | REG-14 |
| B18 | Registration |
| C18 | Decision Table |
| D18 | Register using existing username |
| E18 | qauser01 already registered |
| F18 | Username: farish01; Password: TestPass123 |
| G18 | Submit registration using the same username again. |
| H18 | Check whether duplicate username is rejected or another account is created. |
| I18 | The application displayed the My Tasks page with farish01 logged in instead of displaying a duplicate-username error. |
| J18 | Fail |
| L18 | DEF-02 |
| M18 | Record actual behaviour; do not assume duplicate protection. |
| A19 | REG-15 |
| B19 | Registration |
| C19 | EP |
| D19 | Username has leading/trailing spaces |
| E19 | Register page open; use unused username |
| F19 | Username: ' farish15 '; Password: TestPass123 |
| G19 | Enter username with spaces around it and submit. |
| H19 | Spaces are trimmed before validation; observe the stored/accepted username. |
| I19 | The application displayed the My Tasks page, with the logged-in username farish15 visible in the navigation bar. |
| J19 | Pass |
| A20 | LOG-01 |
| B20 | Login |
| C20 | EP |
| D20 | Login with valid credentials |
| E20 | Account exists; logged out |
| F20 | Username: farish01; Password: TestPass123 |
| G20 | Open Login; enter credentials; submit. |
| H20 | Login succeeds and user reaches authenticated page. |
| I20 | The application displayed the My Tasks page, with the logged-in username farish01 visible in the navigation bar. |
| J20 | Pass |
| A21 | LOG-02 |
| B21 | Login |
| C21 | EP |
| D21 | Login with incorrect password |
| E21 | Account exists; logged out |
| F21 | Username: farish01; Password: WrongPass123 |
| G21 | Submit login. |
| H21 | Login rejected. |
| I21 | The application displayed “Invalid username or password” and remained on the Login page. |
| J21 | Pass |
| A22 | LOG-03 |
| B22 | Login |
| C22 | EP |
| D22 | Login with unknown username |
| E22 | Logged out |
| F22 | Username: nobody987; Password: TestPass123 |
| G22 | Submit login. |
| H22 | Login rejected. |
| I22 | The application displayed “Invalid username or password” and remained on the Login page. |
| J22 | Pass |
| A23 | LOG-04 |
| B23 | Login |
| C23 | EP |
| D23 | Username left empty |
| E23 | Logged out |
| F23 | Username: blank; Password: TestPass123 |
| G23 | Submit login. |
| H23 | Login rejected. |
| I23 | The browser displayed “Please fill out this field” and prevented form submission when the username field was empty. |
| J23 | Pass |
| A24 | LOG-05 |
| B24 | Login |
| C24 | EP |
| D24 | Password left empty |
| E24 | Logged out |
| F24 | Username: farish01; Password: blank |
| G24 | Submit login. |
| H24 | Login rejected. |
| I24 | The browser displayed “Please fill out this field” and prevented form submission when the password field was empty. |
| J24 | Pass |
| A25 | LOG-06 |
| B25 | Login |
| C25 | EP |
| D25 | Both fields empty |
| E25 | Logged out |
| F25 | Username: blank; Password: blank |
| G25 | Submit login. |
| H25 | Login rejected. |
| I25 | The browser displayed “Please fill out this field” and prevented form submission when both fields were empty. |
| J25 | Pass |
| A26 | LOG-07 |
| B26 | Login |
| C26 | EP |
| D26 | Username contains surrounding spaces |
| E26 | Account exists; logged out |
| F26 | Username: ' farish01 '; Password: TestPass123 |
| G26 | Enter username with surrounding spaces and submit. |
| H26 | Check whether login succeeds after trimming. |
| I26 | My Tasks page displayed with farish01 logged in; the screenshot does not confirm whether surrounding spaces were entered. |
| J26 | Pass |
| A27 | LOG-08 |
| B27 | Login / Access |
| C27 | State Transition |
| D27 | Access task list without login |
| E27 | Logged out |
| F27 | URL: http://127.0.0.1:5000/ |
| G27 | Open task list URL. |
| H27 | Redirected to login. |
| I27 | The application displayed the Login page at /login instead of showing the task list. |
| J27 | Pass |
| A28 | LOG-09 |
| B28 | Logout |
| C28 | State Transition |
| D28 | Logout |
| E28 | Logged in |
| F28 | Click Logout |
| G28 | Click Logout in the interface. |
| H28 | Session ends and user is redirected to login or public page. |
| I28 | The application logged the user out and displayed the Login page. |
| J28 | Pass |
| A29 | LOG-10 |
| B29 | Logout / Access |
| C29 | State Transition |
| D29 | Access task list after logout |
| E29 | Logged out after LOG-09 |
| F29 | URL: http://127.0.0.1:5000/ |
| G29 | Enter task list URL after logout. |
| H29 | Redirected to login; protected tasks are not displayed. |
| I29 | The application displayed the Login page instead of the task list after logout. |
| J29 | Pass |
| A30 | TASK-01 |
| B30 | Create Task |
| C30 | EP |
| D30 | Create task with title only |
| E30 | Logged in |
| F30 | Title: Complete STQA |
| G30 | Open New Task; enter title; save. |
| H30 | Task is created and appears in task list. |
| I30 | The application created the task Complete STQA and displayed it in the task list with no category, no due date, and urgency shown as “No due date”. |
| J30 | Pass |
| A31 | TASK-02 |
| B31 | Create Task |
| C31 | EP |
| D31 | Create task with all details |
| E31 | Logged in |
| F31 | Title: STQA full task; Description: Testing practice; Category: Work; Due date: choose valid date |
| G31 | Fill all available fields and save. |
| H31 | Task is created with supplied details. |
| I31 | The task STQA full task appears in the task list with category Work, due date 2026-10-31, and urgency Upcoming. The description is not visible in this screenshot. |
| J31 | Pass |
| A32 | TASK-03 |
| B32 | Create Task |
| C32 | EP |
| D32 | Submit empty title |
| E32 | Logged in |
| F32 | Title: blank |
| G32 | Open New Task; leave title blank; submit. |
| H32 | Observe whether an empty task is created; record exact result. |
| I32 | The browser displayed “Please fill out this field” and prevented the form from being submitted. |
| J32 | Pass |
| A33 | TASK-04 |
| B33 | Create Task |
| C33 | EP |
| D33 | Submit whitespace-only title |
| E33 | Logged in |
| F33 | Title: three spaces |
| G33 | Enter spaces as title; submit. |
| H33 | Observe whether whitespace-only title is accepted. |
| I33 | The application created a task with a blank-looking title and displayed it in the task list. |
| J33 | Fail |
| L33 | DEF-03 |
| A34 | TASK-05 |
| B34 | Create Task |
| C34 | EP |
| D34 | Create task without description |
| E34 | Logged in |
| F34 | Title: No description; Description: blank |
| G34 | Create and save task. |
| H34 | Task is created if description is optional. |
| I34 | The task Review STQA Notes appeared in the task list even though the description was blank. |
| J34 | Pass |
| A35 | TASK-06 |
| B35 | Create Task |
| C35 | EP |
| D35 | Create task without category |
| E35 | Logged in |
| F35 | Title: No category; category: blank/default |
| G35 | Submit task form without selecting category. |
| H35 | Record whether task is created and which category is used. |
| I35 | The task No category was created successfully. The Category and Due Date columns display —. |
| J35 | Pass |
| A36 | TASK-07 |
| B36 | Create Task |
| C36 | EP |
| D36 | Create task without due date |
| E36 | Logged in |
| F36 | Title: No due date; Due date: blank |
| G36 | Save task without due date. |
| H36 | Task is created; urgency is No due date. |
| I36 | The application created the task successfully. The Due Date column displays — and the Urgency column displays No due date. |
| J36 | Pass |
| A37 | TASK-08 |
| B37 | Create Task |
| C37 | BVA |
| D37 | Create task with past due date |
| E37 | Logged in |
| F37 | Title: Past due; Due date: yesterday |
| G37 | Create task and inspect urgency. |
| H37 | Task is created; urgency is Overdue. |
| I37 | The application created the task with the due date 17/10/2026 and displayed the urgency as Overdue. |
| J37 | Pass |
| A38 | TASK-09 |
| B38 | Create Task |
| C38 | BVA |
| D38 | Create task due today |
| E38 | Logged in |
| F38 | Title: Due today; Due date: today's date |
| G38 | Create task and inspect urgency. |
| H38 | Expected label per stated spec: Due Today; record actual label. |
| I38 | The task was created successfully, but the urgency label displayed was Overdue. |
| J38 | Fail |
| L38 | DEF-04 |
| A39 | TASK-10 |
| B39 | Create Task |
| C39 | BVA |
| D39 | Create task due in three days |
| E39 | Logged in |
| F39 | Title: Upcoming; Due date: today + 3 days |
| G39 | Create task and inspect urgency. |
| H39 | Urgency is Upcoming. |
| I39 | The task was created successfully with the due date 21/10/2026 and the urgency label Upcoming. |
| J39 | Pass |
| A40 | TASK-11 |
| B40 | Edit Task |
| C40 | Functional |
| D40 | Edit task title |
| E40 | Logged in; own task exists |
| F40 | Updated title: Updated STQA Task |
| G40 | Open task edit form; change title; save. |
| H40 | New title is saved. |
| I40 | The task title was updated successfully and displayed as Updated STQA Task in the task list. |
| J40 | Pass |
| A41 | TASK-12 |
| B41 | Edit Task |
| C41 | Functional |
| D41 | Edit task description |
| E41 | Logged in; own task exists |
| F41 | Description: Updated description |
| G41 | Edit description and save. |
| H41 | New description is saved. |
| I41 | The description was updated and saved successfully. |
| J41 | Pass |
| A42 | TASK-13 |
| B42 | Edit Task |
| C42 | Functional |
| D42 | Change task category |
| E42 | Logged in; own task exists |
| F42 | Category: Study |
| G42 | Edit category and save. |
| H42 | Category changes to Study. |
| I42 | The task category was successfully changed to Study, and the task displayed the updated category. |
| J42 | Pass |
| A43 | TASK-14 |
| B43 | Edit Task |
| C43 | Functional |
| D43 | Change due date |
| E43 | Logged in; own task exists |
| F43 | Choose a different valid date |
| G43 | Edit due date and save. |
| H43 | New due date is saved. |
| I43 | The task's due date changed from 2026-10-21 to 2026-10-22. |
| J43 | Pass |
| A44 | TASK-15 |
| B44 | Edit Task |
| C44 | Negative |
| D44 | Edit nonexistent task |
| E44 | Logged in |
| F44 | URL: /tasks/999999/edit (verify ID does not exist) |
| G44 | Open URL. |
| H44 | Application redirects or displays a not-found response; no other task is modified. |
| I44 | The browser displayed the My Tasks page after the request for a nonexistent task's edit page. |
| J44 | Pass |
| A45 | TASK-16 |
| B45 | Task Status |
| C45 | State Transition |
| D45 | Mark task as completed |
| E45 | Logged in; open task exists |
| F45 | Select completion control for own task |
| G45 | Mark task done. |
| H45 | Task is marked Done. |
| I45 | The task was marked completed. A check mark appeared, the title was crossed out, and the urgency changed to Done. |
| J45 | Pass |
| A46 | TASK-17 |
| B46 | Task Status |
| C46 | State Transition |
| D46 | Reopen completed task |
| E46 | Logged in; done task exists |
| F46 | Select completion control for done task |
| G46 | Mark task open again. |
| H46 | Task returns to open state. |
| I46 | The task was successfully reopened. The strikethrough disappeared, the completion circle became empty, and the urgency returned to Upcoming. |
| J46 | Pass |
| A47 | TASK-18 |
| B47 | Delete Task |
| C47 | State Transition |
| D47 | Delete own task |
| E47 | Logged in; own disposable task exists |
| F47 | Delete the selected task |
| G47 | Use delete control if available; confirm if prompted. |
| H47 | Task disappears from list. |
| I47 | The task was successfully deleted and removed from the task list. |
| J47 | Pass |
| A48 | TASK-19 |
| B48 | Delete Task |
| C48 | Negative |
| D48 | Delete nonexistent task |
| E48 | Logged in |
| F48 | Task ID: 999999 |
| G48 | Attempt deletion through available route/API if permitted. |
| H48 | No unrelated task is deleted; appropriate not-found handling. |
| I48 | The application returned a redirect to the task list. No unrelated task was deleted. |
| J48 | Pass |
| A49 | TASK-20 |
| B49 | Persistence |
| C49 | Functional |
| D49 | Verify changes after refresh |
| E49 | Task edited or completed |
| F49 | Refresh browser page |
| G49 | Refresh and inspect the same task. |
| H49 | Changes persist after refresh. |
| I49 | The task changes remained saved and displayed correctly after refreshing the browser. |
| J49 | Pass |
| A50 | LIST-01 |
| B50 | Task List |
| C50 | Functional |
| D50 | Open task list |
| E50 | Logged in |
| F50 | URL: / |
| G50 | Open task list. |
| H50 | Current user's tasks are displayed. |
| I50 | The My Tasks page opened successfully and displayed the current user's tasks with their details and filtering options. |
| J50 | Pass |
| A51 | LIST-02 |
| B51 | Task List |
| C51 | EP |
| D51 | Open empty task list |
| E51 | Use test account with no tasks |
| F51 | No tasks |
| G51 | Open task list. |
| H51 | Empty state shown without error. |
| I51 | The empty task list displayed “No tasks match your filters.” without any error. |
| J51 | Pass |
| A52 | LIST-03 |
| B52 | Category Filter |
| C52 | EP |
| D52 | Filter by Work category |
| E52 | Logged in; tasks exist in multiple categories |
| F52 | Category: Work |
| G52 | Select Work category filter. |
| H52 | Only tasks in selected category appear. |
| I52 | Only the task “STQA full task” with category Work was displayed after applying the filter. |
| J52 | Pass |
| A53 | LIST-04 |
| B53 | Category Filter |
| C53 | EP |
| D53 | Filter by Personal category |
| E53 | Logged in; tasks exist in multiple categories |
| F53 | Category: Personal |
| G53 | Select Personal category filter. |
| H53 | Only tasks in selected category appear. |
| I53 | The Personal category filter was applied, but no tasks matched the selected category because no Personal-category tasks existed. |
| J53 | Pass |
| A54 | LIST-05 |
| B54 | Category Filter |
| C54 | EP |
| D54 | Filter by Study category |
| E54 | Logged in; tasks exist in multiple categories |
| F54 | Category: Study |
| G54 | Select Study category filter. |
| H54 | Only tasks in selected category appear. |
| I54 | Only the task “Upcoming” with category Study was displayed after applying the filter. |
| J54 | Pass |
| A55 | LIST-06 |
| B55 | Category Filter |
| C55 | EP |
| D55 | Filter by Urgent category |
| E55 | Logged in; tasks exist in multiple categories |
| F55 | Category: Urgent |
| G55 | Select Urgent category filter. |
| H55 | Only tasks in selected category appear. |
| I55 | Only the task “No category,” assigned to the Urgent category, was displayed after applying the filter. |
| J55 | Pass |
| A56 | LIST-07 |
| B56 | Status Filter |
| C56 | EP |
| D56 | Filter open tasks |
| E56 | Logged in; open and done tasks exist |
| F56 | Status: Open |
| G56 | Select Open filter. |
| H56 | Only incomplete tasks appear. |
| I56 | The Open filter displayed incomplete tasks, including “Upcoming,” “Due today,” and “STQA full task.” |
| J56 | Pass |
| A57 | LIST-08 |
| B57 | Status Filter |
| C57 | EP |
| D57 | Filter completed tasks |
| E57 | Logged in; open and done tasks exist |
| F57 | Status: Done |
| G57 | Select Done filter. |
| H57 | Only completed tasks appear. |
| I57 | Only the completed task “Past Due Task” was displayed after applying the Done filter. |
| J57 | Pass |
| A58 | LIST-09 |
| B58 | Title Search |
| C58 | EP |
| D58 | Search existing title |
| E58 | Logged in; known task title exists |
| F58 | Search: STQA |
| G58 | Enter STQA in search box. |
| H58 | Matching tasks appear. |
| I58 | Three matching tasks containing “STQA” appeared: “Review STQA Notes,” “STQA full task,” and “Updated STQA Task.” |
| J58 | Pass |
| A59 | LIST-10 |
| B59 | Title Search |
| C59 | EP |
| D59 | Search nonexistent title |
| E59 | Logged in |
| F59 | Search: XYZ123NOTFOUND |
| G59 | Search for the text. |
| H59 | No matching tasks appear. |
| I59 | No tasks matched the search text XYZ123NOTFOUND; the page displayed “No tasks match your filters.” |
| J59 | Pass |
| A60 | LIST-11 |
| B60 | Combined Filter |
| C60 | Decision Table |
| D60 | Combine category and status filters |
| E60 | Logged in; open/done tasks in Work category |
| F60 | Category: Work; Status: Open |
| G60 | Apply both filters. |
| H60 | Only open Work tasks appear. |
| I60 | Only the incomplete task “STQA full task” in the Work category was displayed after applying both filters. |
| J60 | Pass |
| A61 | LIST-12 |
| B61 | Title Search |
| C61 | EP |
| D61 | Search using partial title |
| E61 | Logged in; known title exists |
| F61 | Search a unique substring |
| G61 | Enter partial title. |
| H61 | Matching task appears. |
| I61 | Searching for “Upcoming” displayed the matching task “Upcoming” with category Study and due date 2026-10-22. |
| J61 | Pass |
| A62 | DASH-01 |
| B62 | Dashboard |
| C62 | Functional |
| D62 | Open dashboard |
| E62 | Logged in |
| F62 | URL: /dashboard |
| G62 | Open dashboard. |
| H62 | Dashboard loads. |
| I62 | The dashboard loaded successfully and displayed the task summary cards without an error. |
| J62 | Pass |
| A63 | DASH-02 |
| B63 | Dashboard |
| C63 | Functional |
| D63 | Check total tasks |
| E63 | Logged in; create exactly three tasks and no other tasks on test account |
| F63 | 3 tasks |
| G63 | Open dashboard. |
| H63 | Total counter equals 3. |
| I63 | Dashboard displayed 3 total tasks, 3 open tasks, 0 overdue, 0 due soon, and 0 completed. |
| J63 | Pass |
| A64 | DASH-03 |
| B64 | Dashboard |
| C64 | Functional |
| D64 | Check open tasks |
| E64 | Logged in; exactly two open tasks exist |
| F64 | 2 open tasks |
| G64 | Open dashboard. |
| H64 | Open counter equals 2. |
| I64 | Dashboard displayed 2 total tasks, 2 open tasks, 0 overdue, 0 due soon, and 0 completed. |
| J64 | Pass |
| A65 | DASH-04 |
| B65 | Dashboard |
| C65 | Functional |
| D65 | Check overdue tasks |
| E65 | Logged in; one overdue open task exists |
| F65 | Due date: yesterday |
| G65 | Open dashboard. |
| H65 | Overdue counter includes the overdue task. |
| I65 | The dashboard displayed 2 overdue tasks, matching the two tasks marked overdue in the task list. |
| J65 | Pass |
| A66 | DASH-05 |
| B66 | Dashboard |
| C66 | Functional |
| D66 | Check due-soon tasks |
| E66 | Logged in; one open task due tomorrow |
| F66 | Due date: tomorrow |
| G66 | Open dashboard. |
| H66 | Due Soon counter includes the task. |
| I66 | The task list showed “No category” due on 2026-10-19 with urgency Due Soon. The dashboard displayed Due Soon: 1. |
| J66 | Pass |
| A67 | DASH-06 |
| B67 | Dashboard |
| C67 | State Transition |
| D67 | Check completed this week |
| E67 | Logged in; complete a task today |
| F67 | Complete one task |
| G67 | Open dashboard. |
| H67 | Completed in last 7 days counter increases. |
| I67 | After marking “Due today” as completed, the dashboard's Completed (last 7 days) counter increased from 0 to 1. |
| J67 | Pass |
| A68 | DASH-07 |
| B68 | Dashboard |
| C68 | Functional |
| D68 | Check dashboard after deletion |
| E68 | Logged in; known task exists |
| F68 | Delete one task |
| G68 | Delete task; revisit dashboard. |
| H68 | Relevant counters update. |
| I68 | Dashboard total increased to 10 after adding a task and returned to 9 after deleting it. |
| J68 | Pass |
| A69 | DASH-08 |
| B69 | Dashboard |
| C69 | Functional |
| D69 | Dashboard with no tasks |
| E69 | Logged in with empty test account |
| F69 | No tasks |
| G69 | Open dashboard. |
| H69 | All counters are zero. |
| I69 | All dashboard counters display 0. |
| J69 | Pass |
| A70 | URG-01 |
| B70 | Task Urgency |
| C70 | BVA / State Transition |
| D70 | No due date |
| E70 | Logged in; can create task and set due date |
| F70 | Due date: blank |
| G70 | Create or update task; inspect urgency label. |
| H70 | No due date |
| I70 | Task displays “No due date” as its urgency label. |
| J70 | Pass |
| M70 | Verify actual behaviour; URG-03 may reveal a mismatch. |
| A71 | URG-02 |
| B71 | Task Urgency |
| C71 | BVA / State Transition |
| D71 | Due yesterday |
| E71 | Logged in; can create task and set due date |
| F71 | Due date: today - 1 day |
| G71 | Create or update task; inspect urgency label. |
| H71 | Overdue |
| I71 | The task displays the urgency label “Overdue”. |
| J71 | Pass |
| M71 | Verify actual behaviour; URG-03 may reveal a mismatch. |
| A72 | URG-03 |
| B72 | Task Urgency |
| C72 | BVA / State Transition |
| D72 | Due today |
| E72 | Logged in; can create task and set due date |
| F72 | Due date: today |
| G72 | Create or update task; inspect urgency label. |
| H72 | Due Today per stated specification; record actual label |
| I72 | The task was created successfully, but the urgency label displayed Overdue instead of Due Today. |
| J72 | Fail |
| L72 | DEF-04 |
| M72 | Verify actual behaviour; URG-03 may reveal a mismatch. |
| A73 | URG-04 |
| B73 | Task Urgency |
| C73 | BVA / State Transition |
| D73 | Due tomorrow |
| E73 | Logged in; can create task and set due date |
| F73 | Due date: today + 1 day |
| G73 | Create or update task; inspect urgency label. |
| H73 | Due Soon |
| I73 | The task displays “Due Soon”. |
| J73 | Pass |
| M73 | Verify actual behaviour; URG-03 may reveal a mismatch. |
| A74 | URG-05 |
| B74 | Task Urgency |
| C74 | BVA / State Transition |
| D74 | Due in two days |
| E74 | Logged in; can create task and set due date |
| F74 | Due date: today + 2 days |
| G74 | Create or update task; inspect urgency label. |
| H74 | Due Soon |
| I74 | The task displays “Due Soon”. |
| J74 | Pass |
| M74 | Verify actual behaviour; URG-03 may reveal a mismatch. |
| A75 | URG-06 |
| B75 | Task Urgency |
| C75 | BVA / State Transition |
| D75 | Due in three days |
| E75 | Logged in; can create task and set due date |
| F75 | Due date: today + 3 days |
| G75 | Create or update task; inspect urgency label. |
| H75 | Upcoming |
| I75 | The task displays “Upcoming”. |
| J75 | Pass |
| M75 | Verify actual behaviour; URG-03 may reveal a mismatch. |
| A76 | URG-07 |
| B76 | Task Urgency |
| C76 | BVA / State Transition |
| D76 | Completed task with due date |
| E76 | Logged in; can create task and set due date |
| F76 | Mark task as completed |
| G76 | Create or update task; inspect urgency label. |
| H76 | Done |
| I76 | The completed task displays the urgency label “Done”. |
| J76 | Pass |
| M76 | Verify actual behaviour; URG-03 may reveal a mismatch. |
| A77 | API-01 |
| B77 | API / Categories |
| C77 | Functional |
| D77 | Retrieve categories |
| E77 | Application running |
| F77 | GET /api/categories |
| G77 | Use browser/API client to send request. |
| H77 | Returns Work, Personal, Study and Urgent. |
| I77 | The API returns all four categories in a JSON response. |
| J77 | Pass |
| A78 | API-02 |
| B78 | API Authentication |
| C78 | Decision Table |
| D78 | List tasks without login |
| E78 | No session cookie |
| F78 | GET /api/tasks |
| G78 | Send request without logging in/session cookie. |
| H78 | HTTP 401. |
| I78 | The API returned a JSON list of tasks. |
| J78 | Fail |
| L78 | DEF-05 |
| A79 | API-03 |
| B79 | API Authentication |
| C79 | Decision Table |
| D79 | List tasks after login |
| E79 | Valid authenticated session cookie |
| F79 | GET /api/tasks |
| G79 | Send request with session cookie. |
| H79 | HTTP 200; only current user's tasks. |
| I79 | The API returned a JSON list of tasks in the logged-in browser. |
| J79 | Pass |
| A80 | API-04 |
| B80 | API Create Task |
| C80 | Functional |
| D80 | Create task through API |
| E80 | Authenticated session cookie |
| F80 | POST /api/tasks; JSON title='API test task' |
| G80 | Send request with valid JSON body. |
| H80 | HTTP 201 and task is created. |
| I80 | HTTP 201 returned successfully. |
| J80 | Pass |
| A81 | API-05 |
| B81 | API Create Task |
| C81 | EP |
| D81 | Create task with blank title |
| E81 | Authenticated session cookie |
| F81 | POST /api/tasks; JSON title=' ' |
| G81 | Send request with whitespace-only title. |
| H81 | HTTP 400; title is required. |
| I81 | HTTP 400 returned. |
| J81 | Pass |
| A82 | API-06 |
| B82 | API Task Detail |
| C82 | Functional |
| D82 | Retrieve existing task |
| E82 | Logged in; own task exists |
| F82 | GET /api/tasks/{own_task_id} |
| G82 | Request existing own task ID. |
| H82 | Returns task details. |
| I82 | HTTP 200 returned for the existing task request. |
| J82 | Pass |
| A83 | API-07 |
| B83 | API Task Detail |
| C83 | Negative |
| D83 | Retrieve nonexistent task |
| E83 | Logged in; ID confirmed absent |
| F83 | GET /api/tasks/999999 |
| G83 | Request nonexistent ID. |
| H83 | HTTP 404. |
| I83 | HTTP 404 (NOT FOUND) returned. |
| J83 | Pass |
| A84 | API-08 |
| B84 | API Update Task |
| C84 | Functional |
| D84 | Update task |
| E84 | Logged in; own task exists |
| F84 | PUT /api/tasks/{own_task_id}; update title |
| G84 | Send partial update. |
| H84 | Updated task is returned and persists. |
| I84 | HTTP 200 returned after the update request. |
| J84 | Pass |
| A85 | API-09 |
| B85 | API Delete Task |
| C85 | Functional |
| D85 | Delete own task |
| E85 | Logged in; own disposable task exists |
| F85 | DELETE /api/tasks/{own_task_id} |
| G85 | Send DELETE request. |
| H85 | Task is deleted. |
| I85 | HTTP 200 returned, and a subsequent GET confirmed the title is API Updated Task. |
| J85 | Pass |
| A86 | API-10 |
| B86 | API Dashboard |
| C86 | Functional |
| D86 | Access dashboard API |
| E86 | Logged in with session cookie |
| F86 | GET /api/dashboard |
| G86 | Send request. |
| H86 | Returns dashboard counters. |
| I86 | HTTP 200 returned after the DELETE request. |
| J86 | Pass |
| A87 | API-11 |
| B87 | User Data Isolation |
| C87 | Access Control |
| D87 | User B requests User A task |
| E87 | Two test accounts; User A owns disposable task |
| F87 | As User B, GET /api/tasks/{A_task_id} |
| G87 | Log in as B and request A's task ID. |
| H87 | User B cannot view User A's task; expected not-found/denied. |
| I87 | HTTP 200 returned; verification confirmed task ID 15 no longer exists in the task list. |
| J87 | Pass |
| A88 | API-12 |
| B88 | User Data Isolation |
| C88 | Access Control |
| D88 | User B attempts to delete User A task |
| E88 | Two test accounts; User A owns disposable task |
| F88 | As User B, DELETE /api/tasks/{A_task_id} |
| G88 | Log in as B; attempt delete; verify as A. |
| H88 | User B must not be able to delete User A's task. |
| I88 | HTTP 200 returned. |
| J88 | Pass |


### Execution Summary

| Cell | Source value |
|---|---|
| A1 | Execution Summary |
| A4 | Metric |
| B4 | Value |
| A5 | Total test cases |
| B5 | 84 |
| A6 | Passed |
| B6 | 78 |
| A7 | Failed |
| B7 | 6 |
| A8 | Blocked |
| B8 | 0 |
| A9 | Not Run |
| B9 | 0 |
| A10 | Execution rate |
| B10 | 1 |
| A11 | Pass rate among executed |
| B11 | 0.9285714285714286 |


### Defect Log

| Cell | Source value |
|---|---|
| A1 | Defect Log |
| A4 | Defect ID |
| B4 | Title |
| C4 | Related Test ID |
| D4 | Feature |
| E4 | Environment |
| F4 | Preconditions |
| G4 | Steps to reproduce |
| H4 | Expected result |
| I4 | Actual result |
| J4 | Severity |
| K4 | Priority |
| L4 | Evidence / Status |
| A5 | DEF-01 |
| B5 | 8-character password rejected |
| C5 | REG-12 |
| D5 | Registration |
| E5 | Windows 11 / Chrome / Local Flask app |
| F5 | Register page open |
| G5 | Enter username farish12 and password abc12345, then submit |
| H5 | Password with 8 characters should be accepted if the minimum is 8 |
| I5 | Application rejected the password and displayed a message requiring at least 8 characters |
| J5 | Moderate |
| K5 | Medium |
| A6 | DEF-02 |
| B6 | Duplicate username accepted |
| C6 | REG-14 |
| D6 | Registration |
| E6 | Windows 11 / Chrome / Local Flask app |
| F6 | Username farish01 already registered |
| G6 | Attempt to register again using username farish01 and password TestPass123 |
| H6 | Registration should be rejected with a duplicate-username error |
| I6 | Application displayed My Tasks and logged in as farish01 instead of displaying a duplicate-username error |
| J6 | Moderate |
| K6 | High |
| A7 | DEF-03 |
| B7 | Whitespace-only task title accepted |
| C7 | TASK-04 |
| D7 | Create Task |
| E7 | Windows 11 / Chrome / Local Flask app |
| F7 | Logged in |
| G7 | Enter three spaces as the task title and submit |
| H7 | Whitespace-only title should be rejected |
| I7 | A task with a blank-looking title was created |
| J7 | Moderate |
| K7 | Medium |
| A8 | DEF-04 |
| B8 | Task due today marked Overdue |
| C8 | URG-03, TASK-09 |
| D8 | Task Urgency |
| E8 | Windows 11 / Chrome / Local Flask app |
| F8 | Logged in; task can be created |
| G8 | 1. Log in. 2. Create a task with today's due date. 3. View the task list and check its urgency label. |
| H8 | Urgency label displays Due Today. |
| I8 | Task is created successfully, but the urgency label displays Overdue instead of Due Today. |
| J8 | Minor |
| K8 | Medium |
| A9 | DEF-05 |
| B9 | API tasks accessible without authentication |
| C9 | API-02 |
| D9 | API Authentication |
| E9 | Windows 11 / Chrome / Local Flask app |
| F9 | No authenticated session cookie |
| G9 | Send GET /api/tasks without logging in or sending a session cookie |
| H9 | HTTP 401 Unauthorized |
| I9 | API returned a JSON list of tasks |
| J9 | Major |
| K9 | High |


## STQA Data Collection (Week 2).xlsx

### Test Cases

| Cell | Source value |
|---|---|
| A1 | Week 2 White-Box Test Cases |
| A3 | Test ID |
| B3 | Function |
| C3 | Technique / focus |
| D3 | Test input |
| E3 | Expected result (spec) |
| F3 | Code behaviour to verify |
| G3 | Actual result |
| H3 | Status |
| I3 | Evidence / notes |
| A4 | WB-URG-01 |
| B4 | compute_urgency |
| C4 | No due date |
| D4 | None; today=date(2026,10,19) |
| E4 | No due date |
| F4 | Expected No due date |
| G4 | No due date |
| H4 | Pass |
| A5 | WB-URG-02 |
| B5 | compute_urgency |
| C5 | Past date |
| D5 | '2026-10-18'; today=date(2026,10,19) |
| E5 | Overdue |
| F5 | Expected Overdue |
| G5 | Overdue |
| H5 | Pass |
| A6 | WB-URG-03 |
| B6 | compute_urgency |
| C6 | Due today boundary |
| D6 | '2026-10-19'; today=date(2026,10,19) |
| E6 | Due Today |
| F6 | Code likely returns Overdue |
| G6 | Overdue |
| H6 | Fail |
| I6 | Pytest confirmed: due-today date returns Overdue instead of Due Today. |
| A7 | WB-URG-04 |
| B7 | compute_urgency |
| C7 | +2 days boundary |
| D7 | '2026-10-21'; today=date(2026,10,19) |
| E7 | Due Soon |
| F7 | Expected Due Soon |
| G7 | Due Soon |
| H7 | Pass |
| A8 | WB-URG-05 |
| B8 | compute_urgency |
| C8 | +3 days boundary |
| D8 | '2026-10-22'; today=date(2026,10,19) |
| E8 | Upcoming |
| F8 | Expected Upcoming |
| G8 | Upcoming |
| H8 | Pass |
| A9 | WB-PWD-01 |
| B9 | is_valid_password |
| C9 | Wrong type |
| D9 | None |
| E9 | False |
| F9 | Expected False |
| G9 | 0 |
| H9 | Pass |
| A10 | WB-PWD-02 |
| B10 | is_valid_password |
| C10 | 7 characters |
| D10 | 'abc1234' |
| E10 | False |
| F10 | Expected False |
| G10 | 0 |
| H10 | Pass |
| A11 | WB-PWD-03 |
| B11 | is_valid_password |
| C11 | 8 characters boundary |
| D11 | 'abc12345' |
| E11 | True: spec says at least 8 |
| F11 | Code likely returns False |
| G11 | 0 |
| H11 | Fail |
| I11 | Pytest confirmed: 8-character password returns False instead of True. |
| A12 | WB-PWD-04 |
| B12 | is_valid_password |
| C12 | 9 characters |
| D12 | 'abc123456' |
| E12 | True |
| F12 | Expected True |
| G12 | 1 |
| H12 | Pass |
| A13 | WB-USER-01 |
| B13 | is_valid_username |
| C13 | Wrong type |
| D13 | None |
| E13 | False |
| F13 | Expected False |
| G13 | 0 |
| H13 | Pass |
| A14 | WB-USER-02 |
| B14 | is_valid_username |
| C14 | 2 characters |
| D14 | 'ab' |
| E14 | False |
| F14 | Expected False |
| G14 | 0 |
| H14 | Pass |
| A15 | WB-USER-03 |
| B15 | is_valid_username |
| C15 | 3 characters boundary |
| D15 | 'abc' |
| E15 | True |
| F15 | Expected True |
| G15 | 1 |
| H15 | Pass |
| A16 | WB-USER-04 |
| B16 | is_valid_username |
| C16 | 20 characters boundary |
| D16 | 'abcdefghijklmnopqrst' |
| E16 | True |
| F16 | Expected True |
| G16 | 1 |
| H16 | Pass |
| A17 | WB-USER-05 |
| B17 | is_valid_username |
| C17 | 21 characters boundary |
| D17 | 'abcdefghijklmnopqrstu' |
| E17 | False |
| F17 | Expected False |
| G17 | 0 |
| H17 | Pass |
| A18 | WB-USER-06 |
| B18 | is_valid_username |
| C18 | Underscore allowed |
| D18 | 'user_01' |
| E18 | True |
| F18 | Expected True |
| G18 | 1 |
| H18 | Pass |
| A19 | WB-USER-07 |
| B19 | is_valid_username |
| C19 | Space disallowed |
| D19 | 'user name' |
| E19 | False |
| F19 | Expected False |
| G19 | 0 |
| H19 | Pass |
| A20 | WB-USER-08 |
| B20 | is_valid_username |
| C20 | Hyphen disallowed |
| D20 | 'user-name' |
| E20 | False |
| F20 | Expected False |
| G20 | 0 |
| H20 | Pass |
| A21 | WB-DAY-01 |
| B21 | completed_in_last_n_days |
| C21 | Missing value |
| D21 | None; n=7; now=datetime(2026,10,19,12,0,0) |
| E21 | False |
| F21 | Expected False |
| G21 | 0 |
| H21 | Pass |
| A22 | WB-DAY-02 |
| B22 | completed_in_last_n_days |
| C22 | Recent completion |
| D22 | '2026-10-18 12:00:00'; n=7; now=datetime(2026,10,19,12,0,0) |
| E22 | True |
| F22 | Expected True |
| G22 | 1 |
| H22 | Pass |
| A23 | WB-DAY-03 |
| B23 | completed_in_last_n_days |
| C23 | Exactly N days boundary |
| D23 | '2026-10-12 12:00:00'; n=7; now=datetime(2026,10,19,12,0,0) |
| E23 | True: docstring says inclusive |
| F23 | Code likely returns False |
| G23 | 0 |
| H23 | Fail |
| I23 | Pytest confirmed: completion exactly 7 days ago returns False instead of True. |
| A24 | WB-DAY-04 |
| B24 | completed_in_last_n_days |
| C24 | Future completion |
| D24 | '2026-10-20 12:00:00'; n=7; now=datetime(2026,10,19,12,0,0) |
| E24 | False |
| F24 | Expected False |
| G24 | 0 |
| H24 | Pass |
| A25 | WB-DAY-05 |
| B25 | completed_in_last_n_days |
| C25 | Exactly now |
| D25 | '2026-10-19 12:00:00'; n=7; now=datetime(2026,10,19,12,0,0) |
| E25 | False under positive-age rule |
| F25 | Expected False |
| G25 | 0 |
| H25 | Pass |
| A26 | WB-DAY-06 |
| B26 | completed_in_last_n_days |
| C26 | Older than N days |
| D26 | '2026-10-11 12:00:00'; n=7; now=datetime(2026,10,19,12,0,0) |
| E26 | False |
| F26 | Expected False |
| G26 | 0 |
| H26 | Pass |


### Coverage Guide

| Cell | Source value |
|---|---|
| A1 | Run Unit Tests and Coverage |
| A3 | Step |
| B3 | Command / action |
| C3 | What to check |
| A4 | 1. Open terminal |
| B4 | VS Code → Terminal → New Terminal |
| C4 | Terminal is in project folder. |
| A5 | 2. Install if needed |
| B5 | python -m pip install pytest pytest-cov |
| C5 | Install testing tools. |
| A6 | 3. Run tests |
| B6 | python -m pytest -v |
| C6 | Review pass/fail output and save screenshot. |
| A7 | 4. Coverage summary |
| B7 | python -m pytest --cov=helpers --cov-branch --cov-report=term-missing |
| C7 | Shows coverage and missing lines/branches where supported. |
| A8 | 5. HTML report |
| B8 | python -m pytest --cov=helpers --cov-branch --cov-report=html |
| C8 | Creates htmlcov; open htmlcov/index.html. |
| A9 | 6. Save evidence |
| B9 | Capture terminal output and coverage summary. |
| C9 | Do not report a coverage percentage before running. |
| A13 | Statement Coverage Summary |
| B13 | old value  |
| C13 | new value |
| A14 | File |
| B14 | helpers.py |
| C14 | helpers.py |
| A15 | Total statements |
| B15 | 31 |
| C15 | 31 |
| A16 | Statements missed |
| B16 | 2 |
| C16 | 0 |
| A17 | Code coverage |
| B17 | 0.94 |
| C17 | 1 |
| A18 | Missing lines |
| B18 | 27, 72 |
| C18 | None |
| A19 | Tests passed |
| B19 | 20 |
| C19 | 22 |
| A20 | Tests failed |
| B20 | 3 |
| C20 | 3 |
| B21 | The tests achieved 100% statement coverage, with all 31 statements executed and no statements missed. However, three tests failed because the implementation did not match the specified behaviour. Therefore, 100% statement coverage does not guarantee correctness. |
| A23 | Branch Coverage |
| A24 | Total branches |
| B24 | 18 |
| A25 | Partial branches |
| B25 | 0 |
| A26 | Branch coverage |
| B26 | 1 |
| A29 | Function-selection |
| A30 | Function |
| B30 | Justfification for selection |
| A31 | compute_urgency() |
| B31 | Selected because it contains multiple date-based decisions and boundary conditions, including past dates, today's date, and upcoming due dates. Incorrect results may cause tasks to display the wrong urgency. |
| A32 | is_valid_password() |
| B32 | Selected because it contains input-type validation and a password-length boundary. Boundary testing can reveal whether the minimum password length is implemented correctly. |
| A33 | is_valid_username() |
| B33 | Selected because it contains several conditions, including input type, minimum and maximum length, and permitted characters. |
| A34 | completed_in_last_n_days() |
| B34 | Selected because it contains date-time calculations, optional parameters, and time-boundary conditions. Incorrect results may affect task-completion statistics. |
| A37 | Control-Flow Analysis |
| A38 | Function |
| B38 | Control-flow and decisions |
| A39 | compute_urgency() |
| B39 | Checks whether today is missing, whether a due date is provided, whether the date is past or today, and whether the date is within two days. Each condition leads to a different execution path. |
| A40 | is_valid_password() |
| B40 | First checks whether the input is a string. If it is, the function checks whether its length is greater than eight characters. |
| A41 | is_valid_username() |
| B41 | Checks input type, minimum and maximum length, and whether every character is alphanumeric or an underscore. |
| A42 | completed_in_last_n_days() |
| B42 | Checks for a missing completion date and missing now value, parses the timestamp, calculates its age, and checks whether the completion is in the past and within the specified number of days. |
| A45 | Path/Data-Flow Considerations |
| A46 | Function |
| B46 | Path/Data-Flow Considerations |
| A47 | compute_urgency() |
| B47 | Test different paths for missing dates, past dates, today's date, dates 1–2 days away, and dates 3 or more days away. Check how due_date_str, today, and delta_days affect the returned urgency label. |
| A48 | is_valid_password() |
| B48 | Test non-string inputs and passwords below, at, and above the eight-character boundary. Check how the input type and password length affect the Boolean result. |
| A49 | is_valid_username() |
| B49 | Test non-string inputs, usernames below the minimum length, at the minimum and maximum lengths, above the maximum length, and usernames containing invalid characters. |
| A50 | completed_in_last_n_days() |
| B50 | Test missing completion dates, recent completions, completions exactly seven days ago, older completions, and future timestamps. Check how completed_at_str, n, now, and age affect the result. |


### Execution Summary

| Cell | Source value |
|---|---|
| A1 | Execution Summary |
| A3 | Metric |
| B3 | Value |
| A4 | Total test cases |
| B4 | 25 |
| A5 | Passed |
| B5 | 22 |
| A6 | Failed |
| B6 | 3 |
| A7 | Blocked |
| B7 | 0 |
| A8 | Not Run |
| B8 | 0 |
| A9 | Execution rate |
| B9 | 1 |
| A10 | Pass rate among executed |
| B10 | 0.88 |


### Defect Log

| Cell | Source value |
|---|---|
| A1 | Week 2 Defect Log |
| A3 | Defect ID |
| B3 | Related Test ID |
| C3 | Title |
| D3 | Function |
| E3 | Environment |
| F3 | Preconditions / input |
| G3 | Expected result |
| H3 | Actual result |
| I3 | Severity |
| J3 | Priority |
| K3 | Evidence / status |
| A4 | DEF-W2-01 |
| B4 | WB-URG-03 |
| C4 | Due-today task classified as Overdue |
| D4 | compute_urgency() |
| E4 | Python / local project |
| F4 | today=2026-10-19; due='2026-10-19' |
| G4 | Due Today |
| H4 | Overdue instead of Due Today |
| I4 | Moderate |
| J4 | High |
| K4 | Confirmed by Pytest — WB-URG-03 failed; due-today date returned Overdue instead of Due Today. |
| A5 | DEF-W2-02 |
| B5 | WB-PWD-03 |
| C5 | 8-character password rejected |
| D5 | is_valid_password() |
| E5 | Python / local project |
| F5 | password='abc12345' |
| G5 | True: at least 8 characters |
| H5 | False instead of True |
| I5 | Moderate |
| J5 | Medium |
| K5 | Confirmed by Pytest — WB-PWD-03 failed; 8-character password returned False instead of True. |
| A6 | DEF-W2-03 |
| B6 | WB-DAY-03 |
| C6 | Completion exactly N days ago excluded |
| D6 | completed_in_last_n_days() |
| E6 | Python / local project |
| F6 | n=7; now=2026-10-19 12:00:00; completed=2026-10-12 12:00:00 |
| G6 | True: spec says inclusive |
| H6 | False instead of True |
| I6 | Moderate |
| J6 | Medium |
| K6 | Confirmed by Pytest — WB-DAY-03 failed; completion exactly 7 days ago returned False instead of True. |


## STQA Data Collection (Week 3).xlsx

### Task Checklist

| Cell | Source value |
|---|---|
| A1 | PROJECT WEEK 3 – GUI, COMPATIBILITY, USABILITY & ACCESSIBILITY TESTING |
| A4 | Task ID |
| B4 | Testing Area |
| C4 | Task / Check |
| D4 | Expected Result / What to Record |
| E4 | Status |
| F4 | Evidence / Screenshot Filename |
| G4 | Notes / Defect ID |
| A5 | GUI-01 |
| B5 | GUI Testing |
| C5 | Check all forms and input fields. |
| D5 | Fields are visible, labelled, accept valid input and validate invalid input. |
| E5 | Pass |
| F5 | GUI-01_Empty_Title_Validation, GUI-01_Valid_Title_Created |
| G5 | Browser required-field validation prevents submission when Title is empty. <br>Required Title validation works task created successfully with optional fields left empty. |
| A6 | GUI-02 |
| B6 | GUI Testing |
| C6 | Check buttons and their actions. |
| D6 | Each button is visible, clickable and performs the expected action. |
| E6 | Pass |
| F6 | GUI-02_Cancel_New_Task |
| G6 | Cancel returns to My Tasks without creating a task. |
| A7 | GUI-03 |
| B7 | GUI Testing |
| C7 | Check links and navigation links. |
| D7 | Links open the correct page or destination; no broken links. |
| E7 | Pass |
| F7 | GUI-03_Dashboard_Navigation |
| G7 | Dashboard link opens the Dashboard page successfully. No navigation error observed. |
| A8 | GUI-04 |
| B8 | GUI Testing |
| C8 | Check labels and instructions. |
| D8 | Labels are clear, correctly associated with fields and free from spelling errors. |
| E8 | Pass |
| F8 | GUI-04_Form_Labels |
| G8 | All four form labels are clear, readable and positioned correctly above their corresponding fields. |
| A9 | GUI-05 |
| B9 | GUI Testing |
| C9 | Check page navigation and menu items. |
| D9 | Users can move between pages and return without unexpected errors. |
| E9 | Pass |
| F9 | - |
| G9 | Navigation between My Tasks and Dashboard works successfully without errors. |
| A10 | GUI-06 |
| B10 | GUI Testing |
| C10 | Check success, warning and error messages. |
| D10 | Messages appear at the right time and explain the outcome clearly. |
| E10 | Fail |
| F10 | - |
| G10 | Task is created successfully, but no success message or confirmation feedback is displayed. See BUG-01 in the Defect Log. |
| A11 | GUI-07 |
| B11 | GUI Testing |
| C11 | Check visual consistency. |
| D11 | Fonts, colours, spacing, alignment and component styles are consistent. |
| E11 | Pass |
| F11 | GUI-07_Dashboard<br>GUI-07_My_Tasks |
| G11 | Overall design is consistent. Page headings appear at different horizontal positions. Minor visual alignment improvement may be considered. |
| A12 | GUI-08 |
| B12 | GUI Testing |
| C12 | Check layout at a narrower browser-window width. |
| D12 | Content remains readable; controls do not overlap or disappear. |
| E12 | Pass |
| F12 | GUI-08_Responsive_800px |
| G12 | At 800 px responsive width, the task list and controls appear readable. No obvious overlap observed in the visible area. |
| A13 | COMP-01 |
| B13 | Compatibility / Configuration |
| C13 | Test the application in the group's primary browser. |
| D13 | Record browser name/version, OS and whether key functions work. |
| E13 | Pass |
| F13 | - |
| G13 | Tested on Google Chrome 155.0.8059.85 and Windows 11. My Tasks, New Task, Dashboard, task creation and navigation worked. Due-today tasks showed Overdue; linked to existing defect DEF-04. |
| A14 | COMP-02 |
| B14 | Compatibility / Configuration |
| C14 | Test the application in a second available browser, if available. |
| D14 | Compare layout and core functions with the primary browser. |
| E14 | Pass |
| F14 | COMP-02_Edge_Tasks<br>COMP-02_Edge_New_Task<br>COMP-02_Edge_Dashboard |
| G14 | All three pages opened successfully in Microsoft Edge. Task list, New Task form and Dashboard were accessible without navigation errors. |
| A15 | COMP-03 |
| B15 | Compatibility / Configuration |
| C15 | Test a different screen/window configuration available to the group. |
| D15 | Record screen resolution or window size and any layout differences. |
| E15 | Pass |
| F15 | - |
| G15 | Tested at 800 px responsive width. Task list and controls remained readable, with no obvious overlap in the visible area. |
| A16 | COMP-04 |
| B16 | Compatibility / Configuration |
| C16 | Compare key pages across tested configurations. |
| D16 | Record pass/fail and environment-specific defects in the matrix. |
| E16 | Pass |
| F16 | - |
| G16 | Compared the desktop and 800 px responsive layouts. No obvious layout issue was observed in the areas checked. |
| A17 | USE-01 |
| B17 | Usability |
| C17 | Evaluate ease of navigation. |
| D17 | Record whether users can locate main pages and complete common tasks easily. |
| E17 | Pass |
| F17 | - |
| G17 | USE-OBS-01: Main navigation works between My Tasks, New Task and Dashboard. |
| A18 | USE-02 |
| B18 | Usability |
| C18 | Evaluate feedback and system responses. |
| D18 | Record whether the application clearly confirms actions and explains failures. |
| E18 | Fail |
| F18 | - |
| G18 | USE-OBS-02: Task creation succeeds but no confirmation message appears. See BUG-01. |
| A19 | USE-03 |
| B19 | Usability |
| C19 | Evaluate consistency across pages. |
| D19 | Record consistent wording, controls, layout and interaction patterns. |
| E19 | Pass |
| F19 | - |
| G19 | USE-OBS-03: Consistent colours and card styles; minor heading alignment difference. |
| A20 | USE-04 |
| B20 | Usability |
| C20 | Evaluate error prevention and recovery. |
| D20 | Check validation, helpful error messages and whether users can correct mistakes. |
| E20 | Fail |
| F20 | - |
| G20 | USE-OBS-04: Empty Title is blocked, but tasks due today are displayed as Overdue.  |
| A21 | USE-05 |
| B21 | Usability |
| C21 | Evaluate understandability. |
| D21 | Record unclear labels, instructions, terminology or confusing workflows. |
| E21 | Pass |
| F21 | - |
| G21 | USE-OBS-05: Page headings, field labels, buttons and task information are clear. |
| A22 | ACC-01 |
| B22 | Accessibility (WCAG / POUR) |
| C22 | Perceivable: check meaningful images for alternative text. |
| D22 | Record whether information is perceivable; check meaningful images for alternative text where applicable. |
| E22 | N/A |
| F22 | - |
| G22 | No meaningful images or logos requiring alternative text were found. |
| A23 | ACC-02 |
| B23 | Accessibility (WCAG / POUR) |
| C23 | Perceivable: check meaningful images for alternative text. |
| D23 | Interactive elements can be reached in a logical order and show visible focus. |
| E23 | Pass |
| F23 | - |
| G23 | Record whether text is readable against its background and note any contrast-checking tool used. |
| A24 | ACC-03 |
| B24 | Accessibility (WCAG / POUR) |
| C24 | Operable: check keyboard access to interactive elements. |
| D24 | Main functions can be used without requiring a mouse, where applicable. |
| E24 | Pass |
| F24 | - |
| G24 | Main navigation links, buttons and form controls can be accessed using the keyboard. |
| A25 | ACC-04 |
| B25 | Accessibility (WCAG / POUR) |
| C25 | Operable: check visible keyboard focus and logical navigation order. |
| D25 | Text and actions are understandable; form instructions are clear. |
| E25 | Pass |
| F25 | - |
| G25 | Interactive elements show visible focus and follow a logical order. |
| A26 | ACC-05 |
| B26 | Accessibility (WCAG / POUR) |
| C26 | Understandable: check form labels and instructions. |
| D26 | Errors identify the issue and explain how to correct it. |
| E26 | Pass |
| F26 | - |
| G26 | Labels and instructions are clear, readable and easy to understand. |
| A27 | ACC-06 |
| B27 | Accessibility (WCAG / POUR) |
| C27 | Understandable: check validation and error messages. |
| D27 | Controls and structure are interpretable by browsers and assistive technologies; note manual limitations. |
| E27 | Pass |
| F27 | ACC-05_Empty_Title_Validation<br> |
| G27 | Validation messages explain errors and help users correct mistakes. |
| A28 | ACC-07 |
| B28 | Accessibility (WCAG / POUR) |
| C28 | Understandable: check consistent navigation and control behaviour. |
| D28 | Record tool or visual method used and any low-contrast text; use a contrast checker if available. |
| E28 | Pass |
| F28 | - |
| G28 | Navigation links and controls behave consistently across pages. |
| A29 | ACC-08 |
| B29 | Accessibility (WCAG / POUR) |
| C29 | Robust: inspect page structure and programmatic label associations. |
| D29 | Content remains readable and usable when zoomed, without major clipping or overlap. |
| E29 | Fail |
| F29 | ACC-06_Label_Association |
| G29 | Controls have meaningful names and labels are associated with their inputs where applicable. |
| A30 | ACC-09 |
| B30 | Accessibility (WCAG / POUR) |
| C30 | Robust: check usability at increased browser zoom or text size. |
| D30 | Record missing alternative text or links whose purpose is unclear. |
| E30 | Pass |
| F30 | ACC-08_Browser_Zoom_125 |
| G30 | At 125% zoom, all form fields and both buttons remain accessible. Scrolling is needed to view lower content. |
| A31 | DEF-01 |
| B31 | Defect & Improvement Log |
| C31 | Document each issue with reproducible steps. |
| D31 | Record expected vs actual result, severity/priority, environment and evidence. |
| E31 | Completed |
| F31 | - |
| G31 | BUG-01 and BUG-02 are documented with reproduction steps, expected and actual results, severity/priority, and recommendations. |
| A32 | DEF-02 |
| B32 | Defect & Improvement Log |
| C32 | Capture screenshot or other reproducible evidence. |
| D32 | Use a filename and reference it in the task or defect log. |
| E32 | Completed |
| F32 | - |
| G32 | Evidence references are recorded in the Defect Log |
| A33 | DEF-03 |
| B33 | Defect & Improvement Log |
| C33 | Write an improvement recommendation for each important issue. |
| D33 | Recommend a practical change and link it to the related defect ID. |
| E33 | Completed |
| F33 | - |
| G33 | Recommendations are recorded for BUG-01 and BUG-02. |
| A34 | DEL-01 |
| B34 | Deliverables |
| C34 | Complete the GUI testing checklist/results. |
| D34 | Ensure test result and notes are filled for each GUI check. |
| E34 | Completed |
| F34 | - |
| G34 | GUI-01 to GUI-08 tested and recorded. |
| A35 | DEL-02 |
| B35 | Deliverables |
| C35 | Complete the compatibility/configuration matrix. |
| D35 | Include each browser/configuration tested and its result. |
| E35 | Completed |
| F35 | - |
| G35 | Chrome, Edge and the 800 px configuration have been tested and recorded. |
| A36 | DEL-03 |
| B36 | Deliverables |
| C36 | Complete usability observations. |
| D36 | Summarize strengths, confusion points and recommendations. |
| E36 | Completed |
| F36 | - |
| G36 | USE-OBS-01 to USE-OBS-05 recorded. |
| A37 | DEL-04 |
| B37 | Deliverables |
| C37 | Complete basic accessibility findings. |
| D37 | Summarize checks against the POUR principles and any limitations. |
| E37 | Completed |
| F37 | - |
| G37 | ACC-01 to ACC-09 are recorded. |
| A38 | DEL-05 |
| B38 | Deliverables |
| C38 | Prepare the final defects and improvement recommendations. |
| D38 | Ensure defects have evidence and clear reproduction steps. |
| E38 | Completed |
| F38 | - |
| G38 | Both defects and their recommended fixes are documented. |


### Compatibility Matrix

| Cell | Source value |
|---|---|
| A1 | COMPATIBILITY / CONFIGURATION MATRIX |
| A3 | Config ID |
| B3 | Browser & Version |
| C3 | Operating System |
| D3 | Screen / Window Size |
| E3 | Pages / Functions Tested |
| F3 | Expected Result |
| G3 | Actual Result / Status |
| H3 | Evidence / Notes |
| A4 | CFG-01 |
| B4 | Google Chrome 155.0.8059.85 |
| C4 | Windows 11 |
| D4 | 1920 × 1080 desktop |
| E4 | My Tasks, New Task, Dashboard, task creation and navigation |
| F4 | Pages display correctly and key functions work without layout or navigation errors |
| G4 | Pass — My Tasks, New Task, Dashboard, task creation and navigation worked correctly in Chrome on Windows 11 |
| H4 | The application worked correctly on Chrome and Windows 11. Empty task titles were blocked by required-field validation. Tasks due today were displayed as Overdue, which is linked to the existing Week 1 defect DEF-04. |
| A5 | CFG-02 |
| B5 | Microsoft Edge |
| C5 | Windows 11 |
| D5 | 1920 × 1080 desktop |
| E5 | My Tasks, New Task, Dashboard and navigation |
| F5 | Pages display correctly and key functions work without layout or navigation errors. |
| G5 | Pass — all three pages opened successfully. |
| H5 | Basic compatibility check completed in Microsoft Edge. Version and exact resolution were not recorded. |
| A6 | CFG-03 |
| A7 | CFG-04 |
| A8 | CFG-05 |
| A9 | CFG-06 |
| A10 | CFG-07 |
| A11 | CFG-08 |
| A12 | CFG-09 |
| A13 | CFG-10 |


### Defect Log

| Cell | Source value |
|---|---|
| A1 | DEFECT & IMPROVEMENT LOG |
| A3 | Defect ID |
| B3 | Testing Area |
| C3 | Page / Feature |
| D3 | Steps to Reproduce |
| E3 | Expected Result |
| F3 | Actual Result |
| G3 | Severity / Priority |
| H3 | Screenshot / Evidence |
| I3 | Recommendation / Status |
| A4 | BUG-01 |
| B4 | GUI Testing |
| C4 | Create Task |
| D4 | Open New Task, enter a valid Title, click Create Task. |
| E4 | Task is created and a clear success confirmation is displayed. |
| F4 | Task is created, but no confirmation message appears. |
| G4 | Low / Medium |
| H4 | Observed in Chrome Inspect; no separate screenshot attached. |
| I4 | Add a success message after task creation. Open — not fixed. |
| A5 | BUG-02 |
| B5 | Accessibility |
| C5 | New Task — Title field |
| D5 | Open New Task, press F12, expand the form element in the Elements panel and inspect the Title label and input. |
| E5 | The Title label should be programmatically associated with its input. |
| F5 | The inspected HTML shows a label and input but no visible matching for and id attributes. |
| G5 | Medium / Medium |
| H5 | ACC-08_Label_Association |
| I5 | Associate the label and input using matching for and id attributes, or nest the input inside the label. Open — not fixed. |
| A6 | BUG-03 |
| A7 | BUG-04 |
| A8 | BUG-05 |
| A9 | BUG-06 |
| A10 | BUG-07 |
| A11 | BUG-08 |
| A12 | BUG-09 |
| A13 | BUG-10 |


### Usability Observations

| Cell | Source value |
|---|---|
| A1 | USABILITY OBSERVATIONS |
| A3 | Observation ID |
| B3 | Dimension |
| C3 | Task / Page |
| D3 | Observation (Actual) |
| E3 | Impact on User |
| F3 | Recommendation |
| A4 | USE-OBS-01 |
| B4 | Ease of navigation |
| C4 | My Tasks, New Task and Dashboard |
| D4 | Navigation links work correctly. Users can move between My Tasks and Dashboard, and return to the task list. |
| E4 | Users can navigate between the main pages without difficulty. |
| F4 | Maintain clear navigation links and consistent placement across pages. |
| A5 | USE-OBS-02 |
| B5 | Feedback |
| C5 | New Task — task creation |
| D5 | The task was created successfully, but no success message or confirmation was displayed. |
| E5 | Users may be unsure whether their task was created successfully. |
| F5 | Display a clear success message after a task is created. |
| A6 | USE-OBS-03 |
| B6 | Consistency |
| C6 | My Tasks and Dashboard |
| D6 | The pages use consistent colours, card styles, spacing and text formatting. However, the page headings appear at slightly different horizontal positions. |
| E6 | The interface is generally easy to recognise, although the heading alignment difference slightly reduces visual consistency. |
| F6 | Align page headings consistently across the main pages. |
| A7 | USE-OBS-04 |
| B7 | Error prevention / recovery |
| C7 | New Task form and task urgency |
| D7 | The application prevents submission when the Title field is empty. However, a task due today is displayed as Overdue. |
| E7 | Required-field validation prevents incomplete tasks, but incorrect urgency information may confuse users. |
| F7 | Maintain required-field validation and correct the urgency label for tasks due today. |
| A8 | USE-OBS-05 |
| B8 | Understandability |
| C8 | My Tasks and New Task |
| D8 | Page headings, field labels, buttons and task information are clear and easy to understand. |
| E8 | Users can understand the main functions and enter task information without difficulty. |
| F8 | Maintain clear labels and simple instructions throughout the application. |


### Accessibility Review

| Cell | Source value |
|---|---|
| A1 | BASIC ACCESSIBILITY REVIEW – WCAG / POUR |
| A3 | Check ID |
| B3 | POUR Principle |
| C3 | Check |
| D3 | Result (Pass/Fail/N/A) |
| E3 | Evidence / Finding |
| F3 | Recommendation |
| A4 | ACC-01 |
| B4 | Perceivable |
| C4 | Meaningful images have alternative text where applicable. |
| D4 | N/A |
| E4 | No meaningful images or logos requiring alternative text were found in the application. |
| F4 | Provide appropriate alternative text if meaningful images are added in the future. |
| A5 | ACC-02 |
| B5 | Perceivable |
| C5 | Text and background have readable contrast. |
| D5 | Pass |
| E5 | Text on the navigation bar, form labels, and buttons appears readable against the background. |
| F5 | Verify text and background colour contrast using a tool such as WebAIM Contrast Checker. |
| A6 | ACC-03 |
| B6 | Operable |
| C6 | All main interactive elements can be reached by keyboard. |
| D6 | Pass |
| E6 | Navigation links, buttons, search, filters, and task controls can be reached using Tab and Shift+Tab. |
| F6 | Maintain keyboard accessibility for all interactive elements. |
| A7 | ACC-04 |
| B7 | Operable |
| C7 | Keyboard focus is visible and follows a logical order. |
| D7 | Pass |
| E7 | Keyboard navigation works using Tab and Shift+Tab. Interactive elements show a visible focus outline, and the navigation order is logical. |
| F7 | No immediate improvement required. |
| A8 | ACC-05 |
| B8 | Understandable |
| C8 | Labels and instructions are clear and readable. |
| D8 | Pass |
| E8 | Title, Description, Category, and Due Date labels are clearly visible and easy to understand. |
| F8 | Maintain clear and readable form labels. |
| A9 | ACC-06 |
| B9 | Understandable |
| C9 | Validation and error messages explain how to correct mistakes. |
| D9 | Pass |
| E9 | When the Title field is left empty, the browser displays “Please fill out this field.” |
| F9 | Consider providing a more specific message identifying the Title field. |
| A10 | ACC-07 |
| B10 | Understandable |
| C10 | Navigation and controls behave consistently. |
| D10 | Pass |
| E10 | Navigation links and buttons behave consistently and take users to the expected pages. |
| F10 | Maintain consistent navigation and button behaviour across pages. |
| A11 | ACC-08 |
| B11 | Robust |
| C11 | Page structure and controls have meaningful names/semantics where inspectable. |
| D11 | Fail |
| E11 | The form contains visible labels, but the Title label and input do not show a clear programmatic association in the inspected HTML. |
| F11 | Associate each label with its input using matching for and id attributes, or use a properly nested label. |
| A12 | ACC-09 |
| B12 | Robust |
| C12 | Content remains usable with browser zoom/text enlargement. |
| D12 | Pass |
| E12 | At 125% browser zoom, all form fields and both buttons remain accessible. The page can be scrolled to reach content below the visible area. |
| F12 | Maintain usability when browser zoom is increased. |


### Deliverables

| Cell | Source value |
|---|---|
| A1 | PROJECT WEEK 3 – DELIVERABLES TRACKER |
| A3 | Deliverable |
| B3 | Required Content |
| C3 | Status |
| D3 | Notes / File Reference |
| A4 | GUI testing checklist/results |
| B4 | Results for forms, buttons, links, labels, navigation, messages and visual consistency. |
| C4 | Completed |
| D4 | GUI-01 to GUI-08 tested; results and evidence recorded. |
| A5 | Compatibility/configuration matrix |
| B5 | Browsers/configurations actually tested, environment details and results. |
| C5 | Completed |
| D5 | Chrome 155 on Windows 11; desktop and application checks recorded. |
| A6 | Usability observations |
| B6 | Ease of navigation, feedback, consistency, error prevention and understandability. |
| C6 | Completed |
| D6 | USE-OBS-01 to USE-OBS-05 recorded. |
| A7 | Basic accessibility findings |
| B7 | Checks guided by WCAG POUR principles, findings and limitations. |
| C7 | Completed |
| D7 | ACC-01 to ACC-09 recorded, including one failure. |
| A8 | Defects and improvement recommendations |
| B8 | Reproducible steps, expected/actual results, screenshots and recommended fixes. |
| C8 | Completed |
| D8 | Includes missing task-creation feedback and accessibility label association finding. |


## STQA Data Collection (Week 4).xlsx

### Web Test Scenarios

| Cell | Source value |
|---|---|
| A1 | WEEK 4 — WEB WORKFLOW TEST SCENARIOS |
| A4 | Test ID |
| B4 | Area |
| C4 | Steps / Scenario |
| D4 | Expected Result |
| E4 | Actual Result |
| F4 | Evidence Filename |
| G4 | Status |
| H4 | Notes / Defect ID |
| A5 | WEB-01 |
| B5 | Registration |
| C5 | Register with a valid unique username and valid password. |
| D5 | Account is created and user is redirected/logged in as designed. |
| E5 | Registration successful; redirected to the Tasks page and logged in as farisha0000. |
| G5 | Pass |
| A6 | WEB-02 |
| B6 | Registration validation |
| C6 | Submit a username shorter than the minimum. |
| D6 | Validation appears; account is not created. |
| E6 | The system rejected the username "ab" and displayed a validation message. No account was created. |
| G6 | Pass |
| A7 | WEB-03 |
| B7 | Registration validation |
| C7 | Submit a password shorter than the minimum. |
| D7 | Validation appears; account is not created. |
| E7 | The system displayed “Password must be at least 8 characters” and rejected the registration. |
| G7 | Pass |
| A8 | WEB-04 |
| B8 | Duplicate registration |
| C8 | Register using an existing username. |
| D8 | Duplicate username is rejected; no unintended login/account duplication. |
| E8 | Registration was successful using an existing username, even when the other details were different and when the name was the same. |
| G8 | Fail |
| H8 | Duplicate username is not rejected.  |
| A9 | WEB-05 |
| B9 | Login |
| C9 | Log in with valid credentials. |
| D9 | Login succeeds and task page opens. |
| E9 | Login successful using valid credentials; redirected to the Tasks page. |
| G9 | Pass |
| A10 | WEB-06 |
| B10 | Login validation |
| C10 | Log in with incorrect password. |
| D10 | Login is rejected with an error. |
| E10 | Login rejected with the error message “Invalid username or password.” |
| G10 | Pass |
| A11 | WEB-07 |
| B11 | Task creation |
| C11 | Create a task with a title and optional fields blank. |
| D11 | Task is created and appears in the list. |
| E11 | Task was created successfully and appeared in the task list with optional fields left blank. |
| G11 | Pass |
| A12 | WEB-08 |
| B12 | Task validation |
| C12 | Attempt to create a task without a title. |
| D12 | Creation is blocked and validation is shown. |
| E12 | Task creation was blocked by browser validation. The message “Please fill out this field” |
| G12 | Pass |
| A13 | WEB-09 |
| B13 | Task update |
| C13 | Edit a task title or due date and save. |
| D13 | Updated values appear in the list. |
| E13 | Task updated successfully and the new changes appeared in the task list. |
| G13 | Pass |
| A14 | WEB-10 |
| B14 | Task completion |
| C14 | Mark a task complete. |
| D14 | Completion state changes correctly. |
| E14 | Task marked as completed successfully. The task title was crossed out and the urgency |
| G14 | Pass |
| A15 | WEB-11 |
| B15 | Task deletion |
| C15 | Delete a disposable test task. |
| D15 | Task is removed from the list. |
| E15 | Task deleted successfully and disappeared from the task list. |
| G15 | Pass |
| A16 | WEB-12 |
| B16 | Search/filter |
| C16 | Search by title and use category/status filters. |
| D16 | Only matching tasks are displayed. |
| E16 | Search and filters worked correctly; only tasks matching the search criteria and selected filters were displayed. |
| G16 | Pass |
| A17 | WEB-13 |
| B17 | Dashboard |
| C17 | Compare dashboard counts/urgency with task list. |
| D17 | Dashboard values are consistent with task data. |
| E17 | Dashboard displays 17 total tasks, 16 open, 5 overdue, 1 due soon, and 1 completed in the last 7 days. However, tasks due today are incorrectly labelled “Overdue.” |
| G17 | Pass |


### API Test Suite

| Cell | Source value |
|---|---|
| A1 | WEEK 4 — REST API TEST SUITE |
| A4 | Test ID |
| B4 | Method |
| C4 | Endpoint |
| D4 | Auth Required? |
| E4 | Request / Test Data |
| F4 | Expected HTTP Status |
| G4 | Expected Response / Check |
| H4 | Actual HTTP Result |
| I4 | Notes |
| J4 | Status |
| K4 | Evidence / Defect ID |
| A5 | API-01 |
| B5 | GET |
| C5 | /api/categories |
| D5 | No |
| E5 | None |
| F5 | 200 |
| G5 | JSON array of category objects with id/name |
| H5 | Returned HTTP 200 OK with four categories: Personal, Study, Urgent, Work |
| I5 | - |
| J5 | Pass |
| K5 | API-01.png |
| A6 | API-02 |
| B6 | POST |
| C6 | /api/register |
| D6 | No |
| E6 | {"username":"week4_farisha00","password":"Week4Pass123"} |
| F6 | 201 |
| G6 | JSON includes id and username |
| H6 | HTTP 201 Created; returned id: 11 and username week4_farisha00 |
| I6 | - |
| J6 | Pass |
| K6 | API-02.png |
| A7 | API-03 |
| B7 | POST |
| C7 | /api/register |
| D7 | No |
| E7 | Missing/invalid username |
| F7 | 400 |
| G7 | JSON error: "invalid username" |
| H7 | HTTP 400 Bad Request; JSON response: {"error":"invalid username"} |
| I7 | - |
| J7 | Pass |
| K7 | API-03.png |
| A8 | API-04 |
| B8 | POST |
| C8 | /api/register |
| D8 | No |
| E8 | Password below minimum |
| F8 | 400 |
| G8 | JSON error: "invalid password" |
| H8 | HTTP 400 Bad Request; JSON response: {"error":"invalid password"} |
| I8 | - |
| J8 | Pass |
| K8 | API-04.png |
| A9 | API-05 |
| B9 | POST |
| C9 | /api/login |
| D9 | No |
| E9 | Valid username/password |
| F9 | 200 |
| G9 | JSON includes id and username |
| H9 | HTTP 200 OK; JSON returned id: 11 and username week4_farisha00 |
| I9 | - |
| J9 | Pass |
| K9 | API-05.png |
| A10 | API-06 |
| B10 | POST |
| C10 | /api/login |
| D10 | No |
| E10 | Incorrect credentials |
| F10 | 401 |
| G10 | JSON error: "invalid credentials" |
| H10 | HTTP 401 Unauthorized; JSON response: {"error":"invalid credentials"} |
| I10 | - |
| J10 | Pass |
| K10 | API-06.png |
| A11 | API-07 |
| B11 | GET |
| C11 | /api/tasks |
| D11 | Yes |
| E11 | Authenticated session |
| F11 | 200 |
| G11 | JSON array of tasks |
| H11 | HTTP 200 OK; returned an empty JSON array [] |
| I11 | - |
| J11 | Pass |
| K11 | API-07.png |
| A12 | API-08 |
| B12 | GET |
| C12 | /api/tasks |
| D12 | No |
| E12 | No authenticated session |
| F12 | 401 |
| G12 | JSON error: "authentication required" |
| H12 | HTTP 401 Unauthorized; JSON response: {"error":"authentication required"} |
| I12 | - |
| J12 | Pass |
| K12 | API-08.png |
| A13 | API-09 |
| B13 | POST |
| C13 | /api/tasks |
| D13 | Yes |
| E13 | {"title":"Week 4 API test task"} |
| F13 | 201 |
| G13 | Created task JSON includes id/title/urgency |
| H13 | HTTP 201 Created; task ID 22, title Week 4 API test task, urgency No due date |
| I13 | - |
| J13 | Pass |
| K13 | API-09-A.png<br>API-09-B.png |
| A14 | API-10 |
| B14 | POST |
| C14 | /api/tasks |
| D14 | Yes |
| E14 | {"title":"   "} |
| F14 | 400 |
| G14 | JSON error: "title is required" |
| H14 | HTTP 400 Bad Request; JSON response: {"error":"title is required"} |
| I14 | - |
| J14 | Pass |
| K14 | API-10.png |
| A15 | API-11 |
| B15 | GET |
| C15 | /api/tasks/999999 |
| D15 | Yes |
| E15 | ID confirmed not to exist |
| F15 | 404 |
| G15 | JSON error: "not found" |
| H15 | Postman returned 404 Not Found for GET /api/tasks/999999 with JSON error "not found". |
| I15 | - |
| J15 | Pass |
| K15 | API-11.png |
| A16 | API-12 |
| B16 | PUT |
| C16 | /api/tasks/{task_id} |
| D16 | Yes |
| E16 | {"title":"Week 4 updated task"} |
| F16 | 200 |
| G16 | Updated task JSON reflects change |
| H16 | Postman returned 200 OK. Task 22 title changed to "Week 4 updated task". |
| I16 | - |
| J16 | Pass |
| K16 | API-12.png |
| A17 | API-13 |
| B17 | DELETE |
| C17 | /api/tasks/{task_id} |
| D17 | Yes |
| E17 | No body |
| F17 | 200 |
| G17 | JSON result: "ok" |
| H17 | Postman returned 200 OK and {"result":"ok"} when deleting disposable test task ID 22. |
| I17 | - |
| J17 | Pass |
| K17 | API-13.png |
| A18 | API-14 |
| B18 | GET |
| C18 | /api/dashboard |
| D18 | Yes |
| E18 | Authenticated session |
| F18 | 200 |
| G18 | JSON dashboard counts |
| H18 | Postman returned 200 OK with total=1, open=1, overdue=0, due_soon=0, completed_this_week=0. |
| I18 | - |
| J18 | Pass |
| K18 | API-14.png |
| A19 | API-15 |
| B19 | GET |
| C19 | /api/dashboard |
| D19 | No |
| E19 | No authenticated session |
| F19 | 401 |
| G19 | JSON error: "authentication required" |
| H19 | Postman returned 401 Unauthorized with the expected authentication-required error when no valid session cookie was provided. |
| I19 | - |
| J19 | Pass |
| K19 | API-15.png |
| A20 | API-16 |
| B20 | GET |
| C20 | /api/tasks |
| D20 | Yes |
| E20 | Invalid page/per_page values (e.g. text) |
| F20 | Record observed behaviour |
| G20 | Check pagination and response content |
| H20 | 200 OK; returned a JSON array containing the Week 4 API test task despite invalid pagination values. |
| I20 | - |
| J20 | Pass |
| K20 | API-16.png |
| A21 | API-17 |
| B21 | POST |
| C21 | /api/tasks |
| D21 | Yes |
| E21 | Wrong type/invalid category_id |
| F21 | Record observed behaviour |
| G21 | Controlled response; no server crash or inconsistent data |
| H21 | HTTP 201 Created; task ID 27 was created with category_id "invalid" and category null. |
| I21 | - |
| J21 | Fail |
| K21 | API-17.png |
| A22 | API-18 |
| B22 | GET |
| C22 | /api/tasks?q=' OR 1=1 -- |
| D22 | Yes |
| E22 | Search query with SQL-like characters |
| F22 | Record observed behaviour |
| G22 | No data leakage or SQL error; only own user's tasks |
| H22 | 500 Internal Server Error. SQLite reported an incorrect number of bindings supplied when SQL-like search input was submitted. |
| I22 | - |
| J22 | Fail |
| K22 | API-18.png |


### Request Test Data

| Cell | Source value |
|---|---|
| A1 | REQUEST / TEST DATA |
| A4 | Data ID |
| B4 | Endpoint |
| C4 | Scenario |
| D4 | Body Type |
| E4 | Example Body |
| F4 | Expected Status |
| G4 | Notes / Safety |
| A5 | DATA-01 |
| B5 | POST /api/register |
| C5 | Valid registration |
| D5 | JSON |
| E5 | {"username":"week4_user01","password":"Week4Pass123"} |
| F5 | 201 |
| G5 | Use a fresh username and a dedicated test account. |
| A6 | DATA-02 |
| B6 | POST /api/register |
| C6 | Missing username |
| D6 | JSON |
| E6 | {"password":"Week4Pass123"} |
| F6 | 400 |
| G6 | Expected: "invalid username". |
| A7 | DATA-03 |
| B7 | POST /api/register |
| C7 | Missing password |
| D7 | JSON |
| E7 | {"username":"week4_user02"} |
| F7 | 400 |
| G7 | Expected: "invalid password". |
| A8 | DATA-04 |
| B8 | POST /api/login |
| C8 | Invalid credentials |
| D8 | JSON |
| E8 | {"username":"week4_user01","password":"WrongPass123"} |
| F8 | 401 |
| G8 | Expected: "invalid credentials". |
| A9 | DATA-05 |
| B9 | POST /api/tasks |
| C9 | Valid task |
| D9 | JSON |
| E9 | {"title":"Week 4 API test task","description":"Temporary test data"} |
| F9 | 201 |
| G9 | Requires authenticated session. |
| A10 | DATA-06 |
| B10 | POST /api/tasks |
| C10 | Blank title |
| D10 | JSON |
| E10 | {"title":"   "} |
| F10 | 400 |
| G10 | Expected: "title is required"; requires authenticated session. |
| A11 | DATA-07 |
| B11 | PUT /api/tasks/{task_id} |
| C11 | Update a test task |
| D11 | JSON |
| E11 | {"title":"Week 4 updated task"} |
| F11 | 200 |
| G11 | Replace task ID with a task created for testing. |
| A12 | DATA-08 |
| B12 | DELETE /api/tasks/{task_id} |
| C12 | Delete a test task |
| D12 | No body |
| E12 | — |
| F12 | 200 |
| G12 | Delete only a disposable task created for testing. |


### UI vs API Comparison

| Cell | Source value |
|---|---|
| A1 | WEEK 4 — UI AND API BEHAVIOUR COMPARISON |
| A4 | Compare ID |
| B4 | Feature |
| C4 | UI/API Steps |
| D4 | Expected Result |
| E4 | UI Actual Result |
| F4 | API Actual Result |
| G4 | Status |
| H4 | Notes / Defect ID |
| A5 | CMP-01 |
| B5 | Task creation |
| C5 | Create equivalent task in browser and API. |
| D5 | Task should appear in UI and be returned by API for the same user. |
| E5 | Task "CMP-01 Comparison Task" was created and appeared in the task list. |
| F5 | GET /api/tasks returned HTTP 200 OK and included the task in the JSON response. |
| G5 | Pass |
| H5 | Task created in UI and verified through API; API-07. |
| A6 | CMP-02 |
| B6 | Blank task title |
| C6 | Submit blank title in UI and POST /api/tasks. |
| D6 | Both paths reject blank title; record differences in validation/message/status. |
| E6 | The browser rejected the blank task title and displayed a validation message. No task was created. |
| F6 | POST /api/tasks returned HTTP 400 Bad Request with {"error":"title is required"}. |
| G6 | Pass |
| H6 | API result verified using API-10. |
| A7 | CMP-03 |
| B7 | Task completion |
| C7 | Complete task in UI and inspect via GET /api/tasks. |
| D7 | API done field and UI state agree. |
| E7 | The browser showed “Due + 2 day” as completed. The task was crossed out and displayed a check mark. |
| F7 | GET /api/tasks returned the completed task with "done": true and "urgency": "Done". |
| G7 | Pass |
| H7 | Completed task state matches between UI and API. |
| A8 | CMP-04 |
| B8 | Dashboard counts |
| C8 | Compare dashboard UI with GET /api/dashboard. |
| D8 | Counts match the same user's task data. |
| E8 | Dashboard displayed Total Tasks: 15, Open: 14, Overdue: 4, Due Soon: 1, Completed (last 7 days): 1. |
| F8 | GET /api/dashboard returned HTTP 200 OK with total: 15, open: 14, overdue: 4, due_soon: 1, completed_this_week: 1. |
| G8 | Pass |
| H8 | UI dashboard counts match API dashboard response. |
| A9 | CMP-05 |
| B9 | Due-date urgency |
| C9 | Create a task due today and compare UI/API urgency. |
| D9 | UI/API should be consistent; compare with existing DEF-04 rather than duplicating it. |
| E9 | Task CMP-05 Due Today Test with due date 2026-10-21 displayed urgency as Overdue. |
| F9 | GET /api/tasks returned HTTP 200 OK. Task ID 26 had due date 2026-10-21 and urgency Overdue. |
| G9 | Pass |
| H9 | UI and API urgency values match, but both show the known incorrect result. Refer to DEF-04. |


### Defect Log

| Cell | Source value |
|---|---|
| A1 | WEEK 4 — DEFECT AND IMPROVEMENT LOG |
| A4 | Defect ID |
| B4 | Related Test ID |
| C4 | Feature / Endpoint |
| D4 | Expected Result |
| E4 | Actual Result |
| F4 | Steps to Reproduce |
| G4 | Severity |
| H4 | Status |
| I4 | Evidence Filename |
| J4 | Recommended Fix |
| A5 | BUG-W4-01 |
| B5 | API-17 |
| C5 | POST /api/tasks — category validation |
| D5 | Reject the invalid category_id with a controlled validation response. |
| E5 | 201 Created. Task ID 24 was created with category_id "invalid" and category null. |
| F5 | Log in and send POST /api/tasks with title "API-17 Invalid Category Test" and category_id "invalid". |
| G5 | Low |
| H5 | Open |
| I5 | API-17.png |
| J5 | Validate category_id type and existence before creating the task. |
| A6 | BUG-W4-02 |
| B6 | API-18 |
| C6 | GET /api/tasks — search |
| D6 | API should safely handle search input and return a controlled response without a server error. |
| E6 | 500 Internal Server Error. SQLite reported an incorrect number of bindings supplied. |
| F6 | Log in, then send GET /api/tasks?q=' OR 1=1 -- in Postman. |
| G6 | Medium |
| H6 | Open |
| I6 | API-18.png |
| J6 | Use parameterized SQL queries and handle search input safely. |
| A7 | BUG-W4-03 |
| B7 | WEB-04 |
| C7 | Registration — duplicate username validation |
| D7 | Registration should reject an existing username and display an appropriate error message. |
| E7 | Registration succeeded using an existing username, even when the other details were different and when the name and password were the same. |
| F7 | Attempt to register using an existing username. Repeat with different details and with the same name and password. |
| G7 | Medium |
| H7 | Open |
| J7 | Check whether the username already exists before creating an account. Reject duplicate usernames and display a clear validation message. |


### Execution Summary

| Cell | Source value |
|---|---|
| A1 | WEEK 4 — EXECUTION SUMMARY |
| A4 | Metric |
| B4 | Count |
| C4 | Notes |
| A5 | Web tests planned |
| B5 | 13 |
| C5 | Planned cases. |
| A6 | Web tests executed |
| B6 | 13 |
| C6 | Pass + Fail. |
| A7 | Web tests passed |
| B7 | 12 |
| A8 | Web tests failed |
| B8 | 1 |
| A9 | API tests planned |
| B9 | 18 |
| C9 | Planned cases. |
| A10 | API tests executed |
| B10 | 18 |
| C10 | Pass + Fail. |
| A11 | API tests passed |
| B11 | 16 |
| A12 | API tests failed |
| B12 | 2 |
| A13 | UI/API comparisons planned |
| B13 | 5 |
| A14 | UI/API comparisons executed |
| B14 | 5 |


## STQA Data Collection (Week 5).xlsx

### STRIDE Threads

| Cell | Source value |
|---|---|
| A1 | WEEK 5 — STRIDE THREAT TABLE |
| A4 | Threat ID |
| B4 | Asset / Function |
| C4 | STRIDE Category |
| D4 | Threat Scenario |
| E4 | Potential Impact |
| F4 | Safe Test / Check |
| G4 | Priority |
| H4 | Column1 |
| I4 | Evidence / Notes |
| A5 | TH-01 |
| B5 | Login / session |
| C5 | Spoofing |
| D5 | An unauthenticated user may try to access a protected page or API endpoint without a valid session. |
| E5 | Unauthorized access to user tasks or dashboard. |
| F5 | Request GET /api/tasks and /api/dashboard without a session; expect an authentication-required response and no private data. |
| G5 | High |
| H5 | Pass |
| I5 | TH-01.png<br>API returned 401 Unauthorized with authentication-required message; no task data returned. |
| A6 | TH-02 |
| B6 | Registration |
| C6 | Spoofing |
| D6 | Registration may allow duplicate usernames, causing identity confusion or account collision. |
| E6 | Wrong account association or unintended access. |
| F6 | Attempt registration with an existing username using a safe test account; expect rejection and no unintended login. |
| G6 | High |
| H6 | Fail |
| I6 | WEB-04.png <br>Duplicate username was accepted; registration succeeded instead of displaying a validation error. |
| A7 | TH-03 |
| B7 | Task creation / update |
| C7 | Tampering |
| D7 | Invalid or unexpected field values may be stored without validation. |
| E7 | Inconsistent task data and broken UI/API behaviour. |
| F7 | Submit a benign invalid category_id using a test task; expect a controlled validation response and no inconsistent record. |
| G7 | Medium |
| H7 | Fail |
| I7 | API-17.png — API returned HTTP 201 Created for an invalid category_id; task was created with inconsistent category data. Related defect: BUG-W4-01. |
| A8 | TH-04 |
| B8 | Task operations |
| C8 | Repudiation |
| D8 | Important task changes may not leave an activity trail. |
| E8 | Difficult to investigate unexpected edits/deletions. |
| F8 | Check whether the app provides an activity/audit history for a disposable test task; record if unavailable. |
| G8 | Low |
| H8 | Not Applicable |
| I8 | Code review of app.py found no activity log or audit history for task creation, updates, or deletions. This limits traceability of task changes. |
| A9 | TH-05 |
| B9 | Task data / API responses |
| C9 | Information Disclosure |
| D9 | An API response may expose another user's task data or private fields. |
| E9 | Privacy breach. |
| F9 | If multi-user accounts are supported, verify each account sees only its own tasks and inspect responses for unnecessary sensitive fields. |
| G9 | High |
| H9 | Pass |
| I9 | TH-05.png <br>Account B received HTTP 404 Not Found when requesting Account A's task (ID 28). The endpoint did not return the task details. |
| A10 | TH-06 |
| B10 | Search endpoint |
| C10 | Denial of Service |
| D10 | Malformed search input may trigger an unhandled server error or excessive work. |
| E10 | Endpoint instability or failed requests. |
| F10 | Send one controlled SQL-like search string to GET /api/tasks; expect safe handling without HTTP 500. Do not loop or flood requests. |
| G10 | High |
| H10 | Pass |
| I10 | TH-06.png<br>The search endpoint returned HTTP 200 OK with an empty result array for SQL-like input during Week 5. Week 4 API-18 previously returned HTTP 500 for similar input.  |
| A11 | TH-07 |
| B11 | Role / account permissions |
| C11 | Elevation of Privilege |
| D11 | A user may access functions or records beyond their intended permissions. |
| E11 | Unauthorized changes or data access. |
| F11 | If roles exist, verify a lower-privileged test account cannot use privileged actions; otherwise mark Not Applicable. |
| G11 | Low |
| H11 | Not Applicable |
| I11 | Code review of app.py found no administrator roles or admin-only functions. Privilege escalation testing is not applicable to the current application scope. |
| A12 | TH-08 |
| B12 | Registration validation |
| C12 | Tampering |
| D12 | Boundary inputs may bypass validation rules. |
| E12 | Invalid accounts or inconsistent validation. |
| F12 | Use harmless boundary inputs (e.g. username shorter than 3 characters) and verify a clear validation response. |
| G12 | Medium |
| H12 | Pass |
| I12 | API-03.png  <br>Registration API returned HTTP 400 Bad Request with "invalid username" for a two-character username, confirming that minimum username length validation is enforced. |


### Security Test Cases

| Cell | Source value |
|---|---|
| A1 | WEEK 5 — SECURITY TEST CASES |
| A4 | Test ID |
| B4 | Related Threat ID |
| C4 | Feature / Endpoint |
| D4 | Test Scenario / Steps |
| E4 | Expected Result |
| F4 | Actual Result |
| G4 | Status |
| H4 | Severity if Failed |
| I4 | Evidence Filename |
| J4 | Finding ID / Notes |
| A5 | SEC-01 |
| B5 | TH-01 |
| C5 | GET /api/tasks |
| D5 | Send request without authentication/session. |
| E5 | 401/403 or documented redirect; no private task data returned. |
| F5 | HTTP 401 Unauthorized returned with "authentication required". No task data was returned. |
| G5 | Pass |
| H5 | High |
| I5 | SEC-01.png |
| J5 | Unauthenticated access correctly blocked. |
| A6 | SEC-02 |
| B6 | TH-01 |
| C6 | GET /api/dashboard |
| D6 | Send request without authentication/session. |
| E6 | 401/403 or documented redirect; no private dashboard data returned. |
| F6 | HTTP 401 Unauthorized returned with "authentication required". No private dashboard data was returned. |
| G6 | Pass |
| H6 | High |
| I6 | SEC-02.png |
| J6 | Unauthenticated dashboard access correctly blocked. |
| A7 | SEC-03 |
| B7 | TH-02 |
| C7 | POST /api/register |
| D7 | Try registering a username that already exists, using a test account. |
| E7 | Registration rejected with a clear message; no unintended login or duplicate account. |
| F7 | HTTP 201 Created returned. Duplicate username was accepted and a new user ID (19) was created. |
| G7 | Fail |
| H7 | High |
| I7 | SEC-03.png |
| J7 | BUG-W4-03 persists. Duplicate username registration is accepted. |
| A8 | SEC-04 |
| B8 | TH-03 |
| C8 | POST /api/tasks |
| D8 | Submit a test task with an invalid category_id type/value. |
| E8 | Controlled validation response; no inconsistent task record is created. |
| F8 | HTTP 201 Created returned. Task ID 29 was created with an invalid category_id value; category was returned as null. |
| G8 | Fail |
| H8 | Medium |
| I8 | SEC-04.png |
| J8 | BUG-W4-01 persists. Invalid category value was accepted. |
| A9 | SEC-05 |
| B9 | TH-05 |
| C9 | GET /api/tasks |
| D9 | If supported, log in as test account A and verify returned tasks belong to A; repeat with test account B. |
| E9 | Each account sees only its own tasks; no cross-account task disclosure. |
| F9 | Account B received HTTP 404 Not Found when requesting Account A's task (ID 28). The endpoint did not return the task. |
| G9 | Pass |
| H9 | High |
| I9 | TH-05.png |
| J9 | Existing Week 4/Week 5 evidence reused; no new test executed. |
| A10 | SEC-06 |
| B10 | TH-06 |
| C10 | GET /api/tasks?q=... |
| D10 | Send one SQL-like search string once, using a test session. |
| E10 | Safe response (e.g. empty results or validation error); no HTTP 500 or data leakage. |
| F10 | Week 4 testing showed that an SQL-like search string caused HTTP 500 Internal Server Error due to a SQLite binding error. |
| G10 | Fail |
| H10 | Medium |
| I10 | API-18.png |
| J10 | BUG-W4-02 persists based on existing Week 4 evidence. No new test executed. |
| A11 | SEC-07 |
| B11 | TH-08 |
| C11 | POST /api/register |
| D11 | Submit a username shorter than the documented minimum using a fresh test value. |
| E11 | Registration rejected with a validation message; account is not created. |
| F11 | Week 4 API-03 returned HTTP 400 Bad Request with "invalid username" for the 2-character username "ab". |
| G11 | Pass |
| H11 | Medium |
| I11 | API-03.png |
| J11 | Existing Week 4 evidence reused; username below the minimum length was rejected. |
| A12 | SEC-08 |
| B12 | TH-08 |
| C12 | POST /api/register |
| D12 | Submit a password below the documented minimum using a test account. |
| E12 | Registration rejected with a validation message; account is not created. |
| F12 | Week 4 API-04 returned HTTP 400 Bad Request for a password below the minimum length, with an invalid-password response. |
| G12 | Pass |
| H12 | Medium |
| I12 | API-04.png |
| J12 | Existing Week 4 evidence reused; short password was rejected. |
| A13 | SEC-09 |
| B13 | TH-07 |
| C13 | Privileged function (if any) |
| D13 | If roles/privileges exist, try the action as a non-privileged test user; otherwise mark Not Applicable. |
| E13 | Unauthorized action is blocked; no protected state changes. |
| F13 | No administrator roles or privileged functions were identified in the application. |
| G13 | Not Applicable |
| H13 | Medium |
| J13 | Application has no role-based access control or administrator functions to test. |
| A14 | SEC-10 |
| B14 | TH-04 |
| C14 | Task activity history |
| D14 | Create/update/delete one disposable test task and check whether an audit/activity history is available. |
| E14 | Activity is traceable if feature exists; if not, document missing audit trail as a limitation, not a failed functional test. |
| F14 | No task activity history or audit log was found in the application. |
| G14 | Not Applicable |
| H14 | Low |
| J14 | No audit trail feature was identified; recorded as a limitation based on code review, not a newly executed test. |


### Security Findings

| Cell | Source value |
|---|---|
| A1 | WEEK 5 — SECURITY FINDINGS |
| A4 | Finding ID |
| B4 | Related Test ID |
| C4 | Title / Finding |
| D4 | Observed Evidence |
| E4 | Impact / Risk |
| F4 | Severity |
| G4 | Status |
| H4 | Recommended Fix |
| I4 | Evidence Filename |
| A5 | BUG-W5-01 |
| B5 | SEC-03 |
| C5 | Duplicate username registration |
| D5 | Week 4 testing confirmed that duplicate username registration succeeded and created another user account. |
| E5 | Potential account identity confusion if duplicate registration is accepted. |
| F5 | Medium |
| G5 | Open |
| H5 | Enforce unique username at server/database level; return a clear validation error for duplicates. |
| I5 | SEC-03.png |
| A6 | BUG-W5-02 |
| B6 | SEC-04 |
| C6 | Invalid category value accepted |
| D6 | Known Week 4 observation: API returned 201 and stored category_id as "invalid" with category null. |
| E6 | Inconsistent task data and possible downstream errors. |
| F6 | Low |
| G6 | Open |
| H6 | Validate category_id type and existence before creating/updating a task. |
| I6 | API-17.png |
| A7 | BUG-W5-03 |
| B7 | SEC-06 |
| C7 | Search input causes server error |
| D7 | Known Week 4 observation: SQL-like search input returned HTTP 500 and SQLite binding error. |
| E7 | Unhandled exception can disrupt search and reveal implementation details. |
| F7 | Medium |
| G7 | Open |
| H7 | Use correct parameter binding, validate search input, and return controlled errors. |
| I7 | API-18.png |


### Performance Plan

| Cell | Source value |
|---|---|
| A1 | WEEK 5 — PERFORMANCE TEST PLAN |
| A4 | Plan ID |
| B4 | Item |
| C4 | Planned Definition |
| D4 | Actual / Confirmed Value |
| E4 | Notes |
| A5 | PERF-PLAN-01 |
| B5 | Objective |
| C5 | Check whether PyTodo Pro responds more slowly when it receives more requests. Also observe the number of requests handled and any failed requests. |
| D5 | Compare results across workloads. |
| E5 | Assess response time, throughput, and error rate as request load increases. |
| A6 | PERF-PLAN-02 |
| B6 | Target endpoint |
| C6 | Use GET /api/tasks as the main endpoint because it retrieves the logged-in user's task list. |
| D6 | Use the same endpoint throughout the test. |
| E6 | GET /api/tasks with an authenticated test session. |
| A7 | PERF-PLAN-03 |
| B7 | Environment |
| C7 | Run the tests on the local development server. Record the application setup, database, testing tool, and test date. |
| D7 | Results apply to the local development environment only. |
| E7 | Local PyTodo Pro server on Windows, Flask application, SQLite database, Python 3.14.8, and Postman. |
| A8 | PERF-PLAN-04 |
| B8 | Test data |
| C8 | Use a test account and sample tasks created for testing. Do not use real users' information. |
| D8 | Record all 10 response times in Performance Results. |
| E8 | Existing test account and synthetic task data. No personal or production data used. |
| A9 | PERF-PLAN-05 |
| B9 | Baseline workload |
| C9 | Send 10 requests one after another using one client and record each response time. |
| D9 | Run only if a suitable tool is available. |
| E9 | One client sending 10 sequential requests. |
| A10 | PERF-PLAN-06 |
| B10 | Moderate workload |
| C10 | If a suitable tool is available, send requests from two clients at the same time for 30 seconds and observe the results. |
| D10 | Two concurrent clients for 30 seconds, if the selected tool supports it. |
| E10 | Two concurrent clients for 30 seconds, if supported by the selected load-testing tool. |
| A11 | PERF-PLAN-07 |
| B11 | Higher workload |
| C11 | If the application remains stable, gradually increase the number of concurrent clients to a maximum of five for a short test. |
| D11 | Stop if errors or instability occur. |
| E11 | Up to five concurrent clients for a short run, only if the application remains stable and the tool supports it. |
| A12 | PERF-PLAN-08 |
| B12 | Metrics |
| C12 | Record the average response time, 95th-percentile response time if available, requests per second, and percentage of failed requests. |
| D12 | Mark unavailable metrics as N/A and explain why. |
| E12 | Average response time, 95th-percentile response time (if available), throughput, and error rate. |
| A13 | PERF-PLAN-09 |
| B13 | Stop conditions |
| C13 | Stop the test if the application stops responding, errors increase significantly, or the test interferes with normal computer use. |
| D13 | Keep each run short and controlled. |
| E13 | Stop if the server becomes unresponsive, errors increase sharply, or testing affects other work. |
| A14 | PERF-PLAN-10 |
| B14 | Tool / method |
| C14 | Use Postman to measure individual request times. Use a load-testing tool for concurrent requests only if one is available. |
| D14 | Record the tool and settings used. |
| E14 | Postman for baseline measurements; a bounded load-testing tool for concurrent requests, if available. |


### Performance Result

| Cell | Source value |
|---|---|
| A1 | WEEK 5 — PERFORMANCE RESULTS |
| A4 | Run ID |
| B4 | Endpoint |
| C4 | Workload / Concurrency |
| D4 | Duration (s) |
| E4 | Requests Sent |
| F4 | Successful |
| G4 | Failed |
| H4 | p95 Response (ms) |
| I4 | Throughput (req/s) |
| J4 | Error Rate (%) |
| K4 | Evidence |
| L4 | Observation / Interpretation |
| A5 | PERF-01 |
| B5 | GET /api/tasks |
| C5 | Baseline: 1 client, 10 sequential requests |
| D5 | 97 |
| E5 | 10 |
| F5 | 10 |
| G5 | 0 |
| H5 | N/A |
| I5 | 0.1 |
| J5 | 0 |
| L5 | Postman completed 10 sequential GET /api/tasks requests. All 10 requests succeeded, with no failures. The measured duration was 97 seconds in total, giving a throughput of approximately 0.10 requests per second. The p95 response time was not available from the recorded measurements. |
| A6 | PERF-02 |
| B6 | GET /api/tasks |
| C6 | Baseline: 2 Locust users |
| D6 | 30 |
| E6 | 41 |
| F6 | 41 |
| G6 | 0 |
| H6 | 16 |
| I6 | 1.37 |
| J6 | 0 |
| K6 | PERF-02.png |
| L6 | Two concurrent Locust users sent 41 GET /api/tasks requests during the 30-second test. All requests succeeded with no failures. Average response time was 10.26 ms and p95 response time was 16 ms. |
| A7 | PERF-03 |
| B7 | GET /api/tasks |
| C7 | Higher workload: 5 concurrent Locust users |
| D7 | 30 |
| E7 | 97 |
| F7 | 97 |
| G7 | 0 |
| H7 | 15 |
| I7 | 3.23 |
| J7 | 0 |
| K7 | PERF-03.png |
| L7 | Five concurrent Locust users generated 97 GET /api/tasks requests with no failures. Average response time was 10.82 ms and p95 response time was 15 ms. The application remained responsive during this short test. |


### Limit & Recommendations

| Cell | Source value |
|---|---|
| A1 | WEEK 5 — LIMITATIONS AND RECOMMENDATIONS |
| A4 | ID |
| B4 | Area |
| C4 | Limitation / Observation |
| D4 | Risk / Meaning |
| E4 | Recommendation |
| F4 | Priority |
| G4 | Status |
| A5 | LIM-01 |
| B5 | Environment |
| C5 | Testing was carried out on a local development server using a local database. |
| D5 | Results may differ from a production environment because of differences in hardware, network conditions, database size, and configuration. |
| E5 | Repeat the tests in an authorised staging environment, if one is available. |
| F5 | Medium |
| G5 | Documented |
| A6 | LIM-02 |
| B6 | Workload |
| C6 | Performance testing covered a 10-request manual baseline and short Locust runs with 2 and 5 simulated users. Each Locust run lasted 30 seconds. |
| D6 | The small workload and short test duration are insufficient to determine maximum system capacity or predict performance under real-world traffic. |
| E6 | Test with a larger workload and longer duration only when authorised and when the application remains stable. |
| F6 | Medium |
| G6 | Documented |
| A7 | LIM-03 |
| B7 | Metrics |
| C7 | Performance measurements depended on the metrics available in the selected testing tools. |
| D7 | Missing measurements may limit the accuracy of comparisons between test runs. |
| E7 | Record the tool version and use consistent metrics across all runs. Mark unsupported metrics as N/A and explain why. |
| F7 | Low |
| G7 | Documented |
| A8 | LIM-04 |
| B8 | Security scope |
| C8 | Security testing focused on controlled, non-destructive checks. Uncontrolled penetration testing was not performed. |
| D8 | Some security vulnerabilities may remain undiscovered. |
| E8 | Conduct a more comprehensive security assessment in an authorised test environment if required. |
| F8 | Medium |
| G8 | Documented |
| A9 | REC-01 |
| B9 | Authentication |
| C9 | Authentication and access-control checks should cover both unauthenticated requests and access to another user's data. |
| D9 | Weak access controls could allow unauthorised users to view or modify tasks. |
| E9 | Add automated tests for unauthenticated requests and cross-user access to task records. |
| F9 | High |
| G9 | Recommended |
| A10 | REC-02 |
| B10 | Input validation |
| C10 | API inputs should be validated on the server, including category IDs and username/password boundaries. |
| D10 | Invalid inputs may create inconsistent data or bypass expected validation rules. |
| E10 | Validate input types, lengths, and referenced IDs on the server, and add regression tests for invalid values. |
| F10 | High |
| G10 | Recommended |
| A11 | REC-03 |
| B11 | Search safety |
| C11 | SQL-like search input caused an HTTP 500 error during Week 4 testing. |
| D11 | Unhandled exceptions can interrupt search and expose implementation details. |
| E11 | Use parameterised database queries and return a controlled error response. Add regression tests for unusual search input. |
| F11 | High |
| G11 | Recommended |
| A12 | REC-04 |
| B12 | Duplicate usernames |
| C12 | Registration accepted a username that already existed during Week 4 testing. |
| D12 | Duplicate usernames can cause account identity conflicts and unexpected login behaviour. |
| E12 | Enforce username uniqueness in the database and return a clear validation message when a duplicate is submitted. |
| F12 | High |
| G12 | Recommended |
| A13 | REC-05 |
| B13 | Performance |
| C13 | Performance testing covered only the specific workloads recorded in the Performance Results sheet. |
| D13 | The results cannot establish performance under all possible workloads or prove production-scale capacity. |
| E13 | Compare response times, throughput, and error rates across the baseline and higher-load runs. Record the test conditions and explain the observed differences. |
| F13 | Medium |
| G13 | Completed |


## STQA Data Collection (Week 6).xlsx

### Automation Candidates

| Cell | Source value |
|---|---|
| A1 | Candidate ID |
| B1 | Manual Test ID |
| C1 | Feature / Endpoint |
| D1 | Manual Test Scenario |
| E1 | Automation Rationale |
| F1 | Priority |
| G1 | Selection Decision |
| H1 | Notes / Evidence |
| A2 | AUTO-01 |
| B2 | WEB-01 |
| C2 | Registration |
| D2 | Register with valid details |
| E2 | Repeated core workflow; suitable for stable end-to-end regression. |
| F2 | High |
| G2 | Selected |
| H2 | Use a dedicated test account or reset test data between runs. |
| A3 | AUTO-02 |
| B3 | WEB-02 |
| C3 | Registration validation |
| D3 | Reject username below minimum length |
| E3 | Stable validation boundary; protects registration rules. |
| F3 | Medium |
| G3 | Selected |
| H3 | Reuse existing manual test data and expected validation. |
| A4 | AUTO-03 |
| B4 | WEB-03 |
| C4 | Registration validation |
| D4 | Reject password below minimum length |
| E4 | Stable validation boundary; protects password rules. |
| F4 | Medium |
| G4 | Selected |
| H4 | Do not store real credentials in scripts. |
| A5 | AUTO-04 |
| B5 | WEB-04 |
| C5 | Duplicate registration |
| D5 | Reject an existing username |
| E5 | High regression value, but currently known to fail in manual testing. |
| F5 | High |
| G5 | Selected |
| H5 | Keep as a regression test; expect it to fail until the application defect is fixed. |
| A6 | AUTO-05 |
| B6 | WEB-05 |
| C6 | Login |
| D6 | Log in with valid credentials |
| E6 | Critical and frequently repeated authentication workflow. |
| F6 | High |
| G6 | Selected |
| H6 | Use a dedicated test account. |
| A7 | AUTO-06 |
| B7 | WEB-06 |
| C7 | Login validation |
| D7 | Reject incorrect password |
| E7 | Critical security-related behaviour and stable negative test. |
| F7 | High |
| G7 | Selected |
| H7 | Do not print passwords in logs. |
| A8 | AUTO-07 |
| B8 | WEB-07 |
| C8 | Task creation |
| D8 | Create a task with optional fields blank |
| E8 | Common core workflow; useful for repeated regression checks. |
| F8 | High |
| G8 | Selected |
| H8 | Use unique test titles or clean up test data. |
| A9 | AUTO-08 |
| B9 | WEB-08 |
| C9 | Task validation |
| D9 | Reject a blank task title |
| E9 | Stable required-field validation check. |
| F9 | High |
| G9 | Selected |
| H9 | UI browser validation may be used if UI automation is in scope. |
| A10 | AUTO-09 |
| B10 | WEB-09 |
| C10 | Task update |
| D10 | Edit an existing task |
| E10 | Core workflow that should remain stable across changes. |
| F10 | High |
| G10 | Selected |
| H10 | Create a disposable task before editing. |
| A11 | AUTO-10 |
| B11 | WEB-10 |
| C11 | Task completion |
| D11 | Mark a task complete |
| E11 | Core workflow; verify completion state and visual status. |
| F11 | High |
| G11 | Selected |
| H11 | Use a disposable task. |
| A12 | AUTO-11 |
| B12 | WEB-11 |
| C12 | Task deletion |
| D12 | Delete a task |
| E12 | Important regression workflow; verify only the test task is removed. |
| F12 | High |
| G12 | Selected |
| H12 | Use a disposable task only. |
| A13 | AUTO-12 |
| B13 | WEB-12 |
| C13 | Search / filter |
| D13 | Search or filter tasks |
| E13 | Repeated user workflow; suitable for regression when test data is controlled. |
| F13 | Medium |
| G13 | Selected |
| H13 | Make expected results deterministic with known task titles. |
| A14 | AUTO-13 |
| B14 | API-08 |
| C14 | API authentication |
| D14 | GET /api/tasks without authentication returns 401 |
| E14 | Stable access-control check; fast and repeatable API regression. |
| F14 | High |
| G14 | Selected |
| H14 | Use API-level automation if approved. |
| A15 | AUTO-14 |
| B15 | API-10 |
| C15 | API validation |
| D15 | POST /api/tasks with blank title returns 400 |
| E15 | Stable server-side validation check. |
| F15 | High |
| G15 | Selected |
| H15 | Use a test session and disposable data. |
| A16 | AUTO-15 |
| B16 | API-17 |
| C16 | Category validation |
| D16 | Reject invalid category_id |
| E16 | Known defect: API accepted invalid category_id in Week 4. |
| F16 | High |
| G16 | Selected |
| H16 | Expected to fail until fixed; track BUG-W4-01. |


### Test Traceability

| Cell | Source value |
|---|---|
| A1 | Manual Test ID |
| B1 | Automated Test ID |
| C1 | Requirement / Behaviour |
| D1 | Proposed Script Filename |
| E1 | Automation Level |
| F1 | Coverage Status |
| G1 | Notes |
| A2 | WEB-01 |
| B2 | AUTO-01 |
| C2 | Valid registration succeeds |
| D2 | test_api_automation.py |
| E2 | API |
| F2 | Automated and executed |
| G2 | Registration with a valid username and password returned HTTP 201 CREATED. Automated test passed. |
| A3 | WEB-02 |
| B3 | AUTO-02 |
| C3 | Short username is rejected |
| D3 | test_api_automation.py |
| E3 | API |
| F3 | Automated and executed |
| G3 | Registration with a one-character username was rejected successfully. Automated test passed. |
| A4 | WEB-03 |
| B4 | AUTO-03 |
| C4 | Short password is rejected |
| D4 | test_api_automation.py |
| E4 | API |
| F4 | Automated and executed |
| G4 | Registration using a one-character password was rejected successfully. Automated test passed. |
| A5 | WEB-04 |
| B5 | AUTO-04 |
| C5 | Duplicate username is rejected |
| D5 | test_api_automation.py |
| E5 | API |
| F5 | Automated and executed |
| G5 | Duplicate registration test failed. The second registration using an existing username returned HTTP 201 CREATED instead of rejecting the duplicate. Defect ID: BUG-W6-01. |
| A6 | WEB-05 |
| B6 | AUTO-05 |
| C6 | Valid login succeeds |
| D6 | test_api_automation.py |
| E6 | API |
| F6 | Automated and executed |
| G6 | Valid login test passed; HTTP 200 returned. |
| A7 | WEB-06 |
| B7 | AUTO-06 |
| C7 | Incorrect password is rejected |
| D7 | test_api_automation.py |
| E7 | API |
| F7 | Automated and executed |
| G7 | incorrect password was rejected with HTTP 401 |
| A8 | WEB-07 |
| B8 | AUTO-07 |
| C8 | Task creation with optional fields blank succeeds |
| D8 | test_api_automation.py |
| E8 | API |
| F8 | Automated and executed |
| G8 | Authenticated task creation returned HTTP 201; task ID, title and urgency were verified. |
| A9 | WEB-08 |
| B9 | AUTO-08 |
| C9 | Blank task title is rejected |
| D9 | test_api_automation.py |
| E9 | API |
| F9 | Automated and executed |
| G9 | Authenticated request with a blank task title returned HTTP 400 with the message "title is required". Automated test passed. |
| A10 | WEB-09 |
| B10 | AUTO-09 |
| C10 | Task update succeeds |
| D10 | test_api_automation.py |
| E10 | API |
| F10 | Automated and executed |
| G10 | Authenticated task update returned HTTP 200 and the updated title |
| A11 | WEB-10 |
| B11 | AUTO-10 |
| C11 | Task completion state changes |
| D11 | test_api_automation.py |
| E11 | API |
| F11 | Automated and executed |
| A12 | WEB-11 |
| B12 | AUTO-11 |
| C12 | Verify authenticated user can delete a task |
| D12 | test_api_automation.py |
| E12 | API |
| F12 | Automated and executed |
| G12 | The authenticated user successfully deleted a task. The deletion request returned HTTP 200, and subsequent retrieval returned HTTP 404, confirming that the task was deleted. |
| A13 | WEB-12 |
| B13 | AUTO-12 |
| C13 | Search/filter returns matching tasks |
| D13 | test_api_automation.py |
| E13 | API |
| F13 | Automated and executed |
| G13 | The API returned HTTP 200 and included the matching task while excluding the unrelated task. Automated test passed. |
| A14 | API-08 |
| B14 | AUTO-13 |
| C14 | Unauthenticated task listing is rejected |
| D14 | test_api_automation.py |
| E14 | API |
| F14 | Automated and executed |
| G14 | Unauthenticated GET /api/tasks returned HTTP 401. |
| A15 | API-10 |
| B15 | AUTO-14 |
| C15 | Blank task title is rejected by API |
| D15 | test_api_automation.py |
| E15 | API |
| F15 | Automated and executed |
| G15 | Authenticated blank-title request returned HTTP 400. |
| A16 | API-17 |
| B16 | AUTO-15 |
| C16 | Invalid category_id is rejected |
| D16 | test_api_automation.py |
| E16 | API |
| F16 | Automated and executed |
| G16 | Automated test failed: POST /api/tasks accepted category_id 99999 and returned HTTP 201 CREATED. Known defect BUG-W4-01. |


### Automated Test Results

| Cell | Source value |
|---|---|
| A1 | Run ID |
| B1 | Automated Test ID |
| C1 | Manual Test ID |
| D1 | Script / Test Name |
| E1 | Expected Result |
| F1 | Actual Result |
| G1 | Status |
| H1 | Evidence / Log Filename |
| I1 | Defect ID |
| J1 | Comments |
| A2 | RUN-01 |
| B2 | AUTO-01 |
| C2 | WEB-01 |
| D2 | test_registration_with_valid_details |
| E2 | HTTP 201; registration succeeds with valid username and password |
| F2 | HTTP 201 CREATED; registration successful |
| G2 | Pass |
| H2 | week6_pytest_log.txt |
| A3 | RUN-02 |
| B3 | AUTO-02 |
| C3 | WEB-02 |
| D3 | test_registration_rejects_username_below_minimum_length |
| E3 | HTTP 400 or 422; short username rejected |
| F3 | Username was rejected; test passed |
| G3 | Pass |
| H3 | week6_pytest_log.txt |
| A4 | RUN-03 |
| B4 | AUTO-03 |
| C4 | WEB-03 |
| D4 | test_registration_rejects_short_password |
| E4 | HTTP 400 or 422; short password rejected |
| F4 | Password "1" was rejected; test passed |
| G4 | Pass |
| H4 | week6_pytest_log.txt |
| A5 | RUN-04 |
| B5 | AUTO-04 |
| C5 | WEB-04 |
| D5 | test_duplicate_registration_is_rejected |
| E5 | HTTP 400 or 409; duplicate username rejected |
| F5 | HTTP 201 CREATED; duplicate username accepted |
| G5 | Fail |
| H5 | week6_pytest_log.txt |
| I5 | BUG-W6-01 |
| J5 | Duplicate username was accepted; registration endpoint should reject an existing username. |
| A6 | RUN-05 |
| B6 | AUTO-05 |
| C6 | WEB-05 |
| D6 | Log in with valid credentials |
| E6 | HTTP 200; valid login succeeds |
| F6 | HTTP 200; valid login succeeded |
| G6 | Pass |
| H6 | week6_pytest_log.txt |
| A7 | RUN-06 |
| B7 | AUTO-06 |
| C7 | WEB-06 |
| D7 | test_api_login_rejects_incorrect_password |
| E7 | HTTP 401; invalid credentials |
| F7 | HTTP 401; invalid credentials |
| G7 | Pass |
| H7 | week6_pytest_log.txt |
| A8 | RUN-07 |
| B8 | AUTO-07 |
| C8 | WEB-07 |
| D8 | test_authenticated_user_can_create_task |
| E8 | HTTP 201; task created successfully with id, title and urgency |
| F8 | HTTP 201; task created successfully with id, title and urgency |
| G8 | Pass |
| H8 | week6_pytest_log.txt |
| A9 | RUN-08 |
| B9 | AUTO-08 |
| C9 | WEB-08 |
| D9 | test_authenticated_user_cannot_create_task_with_blank_title |
| E9 | HTTP 400; blank task title is rejected |
| F9 | HTTP 400; title is required |
| G9 | Pass |
| H9 | week6_pytest_log.txt |
| A10 | RUN-09 |
| B10 | AUTO-09 |
| C10 | WEB-09 |
| D10 | test_authenticated_user_can_update_task |
| E10 | HTTP 200; updated task title is returned |
| F10 | HTTP 200; Updated task title returned |
| G10 | Pass |
| H10 | week6_pytest_log.txt |
| A11 | RUN-10 |
| B11 | AUTO-10 |
| C11 | WEB-10 |
| D11 | test_authenticated_user_can_complete_task |
| E11 | HTTP 200;  Task completion request returns and done is True |
| F11 | HTTP 200; done is True |
| G11 | Pass |
| H11 | week6_pytest_log.txt |
| A12 | RUN-11 |
| B12 | AUTO-11 |
| C12 | WEB-11 |
| D12 | test_authenticated_user_can_delete_task |
| E12 | HTTP 404; task is deleted successfully and subsequent retrieval returns  |
| F12 | HTTP retrieval returned; 404 Deletion successful |
| G12 | Pass |
| H12 | week6_pytest_log.txt |
| A13 | RUN-12 |
| B13 | AUTO-12 |
| C13 | WEB-12 |
| D13 | test_authenticated_user_can_search_tasks_by_title |
| E13 | HTTP 200; matching task is returned and unrelated task is excluded |
| F13 | HTTP 200; matching task found and unrelated task excluded |
| G13 | Pass |
| H13 | week6_pytest_log.txt |
| A14 | RUN-13 |
| B14 | AUTO-13 |
| C14 | API-08 |
| D14 | GET /api/tasks without authentication returns 401 |
| E14 | HTTP 401; authentication required |
| F14 | HTTP 401; authentication required |
| G14 | Pass |
| H14 | week6_pytest_log.txt |
| A15 | RUN-14 |
| B15 | AUTO-14 |
| C15 | API-10 |
| D15 | POST /api/tasks with blank title returns 400 |
| E15 | HTTP 400; title is required |
| F15 | HTTP 400; title is required |
| G15 | Pass |
| H15 | week6_pytest_log.txt |
| A16 | RUN-15 |
| B16 | AUTO-15 |
| C16 | API-17 |
| D16 | test_api_rejects_invalid_category_id |
| E16 | HTTP 400; invalid category_id is rejected and no task is created |
| F16 | HTTP 201 CREATED; task created with invalid category_id |
| G16 | Fail |
| H16 | week6_pytest_log.txt |
| I16 | BUG-W4-01 |
| J16 | API accepts a nonexistent category_id without validation. |


### Regression Suite

| Cell | Source value |
|---|---|
| A1 | Regression ID |
| B1 | Automated Test ID |
| C1 | Feature |
| D1 | Test Objective |
| E1 | Execution Order |
| F1 | Expected Result |
| G1 | Latest Status |
| H1 | Defect / Notes |
| A2 | REG-01 |
| B2 | AUTO-05 |
| C2 | Login |
| D2 | Valid user can log in |
| E2 | 1 |
| F2 | Login succeeds |
| G2 | Pass |
| H2 | week6_pytest_log.txt<br>Valid login test passed; HTTP 200 returned. |
| A3 | REG-02 |
| B3 | AUTO-06 |
| C3 | Login |
| D3 | Incorrect password is rejected |
| E3 | 2 |
| F3 | Authentication is denied |
| G3 | Pass |
| H3 | week6_pytest_log.txt<br>incorrect password was rejected with HTTP 401 |
| A4 | REG-03 |
| B4 | AUTO-13 |
| C4 | API authentication |
| D4 | Unauthenticated task listing is denied |
| E4 | 3 |
| F4 | HTTP 401 Unauthorized |
| G4 | Pass |
| H4 | week6_pytest_log.txt<br>Unauthenticated GET /api/tasks returned HTTP 401. |
| A5 | REG-04 |
| B5 | AUTO-07 |
| C5 | Task creation |
| D5 | Task can be created with optional fields blank |
| E5 | 4 |
| F5 | Task is created successfully |
| G5 | Pass |
| H5 | week6_pytest_log.txt<br>authenticated task creation test passed; HTTP 201 returned. |
| A6 | REG-05 |
| B6 | AUTO-08 |
| C6 | Task validation |
| D6 | Blank task title is rejected |
| E6 | 5 |
| F6 | Validation prevents creation |
| G6 | Pass |
| H6 | week6_pytest_log.txt <br>blank task title was rejected with HTTP 400. |
| A7 | REG-06 |
| B7 | AUTO-09 |
| C7 | Task update |
| D7 | Existing disposable task can be edited |
| E7 | 6 |
| F7 | Updated values are saved |
| G7 | Pass |
| H7 | week6_pytest_log.txt<br>task update test passed; HTTP 200 and updated title verified. |
| A8 | REG-07 |
| B8 | AUTO-10 |
| C8 | Task completion |
| D8 | Task can be marked complete |
| E8 | 7 |
| F8 | Completion state changes |
| G8 | Pass |
| A9 | REG-08 |
| B9 | AUTO-11 |
| C9 | Task deletion |
| D9 | Disposable task can be deleted |
| E9 | 8 |
| F9 | Only the test task is deleted |
| G9 | Pass |
| H9 | week6_pytest_log.txt<br>Automated regression test passed. |
| A10 | REG-09 |
| B10 | AUTO-04 |
| C10 | Duplicate registration |
| D10 | Duplicate username is rejected |
| E10 | 9 |
| F10 | Registration is rejected |
| G10 | Fail |
| H10 | BUG-W6-01: duplicate registration returned HTTP 201 instead of rejection. |
| A11 | REG-10 |
| B11 | AUTO-15 |
| C11 | Category validation |
| D11 | Invalid category_id is rejected |
| E11 | 10 |
| F11 | HTTP 400 validation response; no task created |
| G11 | Fail |
| H11 | BUG-W4-01: API returned HTTP 201 and accepted a nonexistent category_id. |


### Automation Reflection

| Cell | Source value |
|---|---|
| A1 | Area |
| B1 | Reflection / Observation |
| C1 | Evidence / Example |
| D1 | Recommendation |
| A2 | Benefits |
| B2 | Automation can repeat stable tests quickly and consistently. |
| C2 | Login, validation, task CRUD, unauthenticated API checks. |
| D2 | Run the focused suite after code changes. |
| A3 | Regression value |
| B3 | Core workflows and known defects should be retested after fixes. |
| C3 | Duplicate registration (WEB-04) and invalid category_id (API-17). |
| D3 | Keep defect-linked tests until fixes are verified. |
| A4 | Limitations |
| B4 | Automated tests can be brittle if UI selectors or test data change. |
| C4 | UI workflows need stable selectors and predictable test accounts. |
| D4 | Prefer stable selectors and isolated test data. |
| A5 | Environment |
| B5 | Results depend on local app, database state, browser and tool versions. |
| C5 | PyTodo Pro local Flask/SQLite environment. |
| D5 | Record versions and use dedicated test data. |
| A6 | Known defects |
| B6 | Some tests may fail because the application has existing defects, not because the script is wrong. |
| C6 | WEB-04 duplicate username; API-17 invalid category_id. |
| D6 | Report defect-related failures clearly; do not hide them. |
| A7 | Scope |
| B7 | Only tests actually implemented and executed can be reported as automated. |
| C7 | Candidate list and traceability are planning records until scripts run. |
| D7 | Fill results from real execution logs; never invent pass/fail. |
| A8 | Execution results |
| B8 | The latest test run collected 16 tests: 14 passed and 2 failed. The suite covers registration validation, login, task creation, task update, task completion, task deletion, task search, blank-title validation, and unauthenticated API access. The duplicate-registration test failed because the application accepted an existing username with HTTP 201 instead of rejecting it. The invalid-category test also failed because the API accepted a nonexistent category_id and returned HTTP 201. These failures identify application defects rather than successful validation. |
| C8 | test_api_automation.py and week6_pytest_log.txt |
| D8 | Expand automation to registration validation, task CRUD, and regression tests for known defects. |
