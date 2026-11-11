# Additional UI evidence - 23 October 2026

## Environment

- Application: unchanged copied PyTodo Pro snapshot
- Server: local Flask development server at `http://127.0.0.1:5000`
- Browser: Microsoft Edge 155.0.4283.62
- Display: 1920x1080
- Browser viewport: 1920x1080
- Account/data: disposable local account `audituser1023`; temporary copied database

## UI-EVID-01 - Whitespace-only task title accepted

Procedure:

1. Register and sign in with the disposable local account.
2. Open New Task.
3. Enter three spaces in Title.
4. Enter `Evidence: whitespace-only title accepted` in Description.
5. Select Create Task.

Expected result: server-side validation rejects the whitespace-only title and no task is created.

Actual result: the application returned to My Tasks and displayed a task row with an empty Title cell. The task received an ID and Edit/Delete controls. This directly confirms D-003 on the tested snapshot.

Evidence: `evidence/verification_2026_10_23/W7-UI-01_Whitespace_Title_Accepted_Edge.png`.

## UI-EVID-02 - No task-creation success confirmation

Procedure:

1. Open New Task while signed in.
2. Enter `Evidence Success Feedback Check` as the title.
3. Enter `Task created; verify no success message appears` as the description.
4. Select Create Task.

Expected result: the created task appears and the interface provides a clear success confirmation.

Actual result: the task appeared in My Tasks, but DOM inspection found no elements matching `[role=alert]`, `.alert`, `.flash` or `.message`. The visible page contained the task table and no success confirmation. This directly confirms D-007 on the tested snapshot.

Evidence: `evidence/verification_2026_10_23/W7-UI-02_No_Success_Message_Edge.png`.

## Requirement decision - completion exactly at the current time

The group project specification says a completion counts when it occurred within the last N days and explicitly includes the N-day boundary. A completion timestamp equal to the evaluation time has an age of zero and is within the interval. The adopted future oracle is therefore **True** for `completed_at == now`.

The historical `test_day_05_completed_now` expected False under the implementation's positive-age rule. Preserve that historical result, but treat its oracle as superseded for future test design. Add a corrected regression assertion when application fixes are authorised. This decision does not alter the saved 44-test run or its 38 Pass / 6 Fail figures.

## Authentication reconciliation

The verified Week 7 clean-session test returned HTTP 401 for unauthenticated task access, and the two-account GET test denied cross-user retrieval. The historical Week 1 result remains unexplained because its build/session state was not preserved. Keep D-005 in Retest rather than claiming a historical fix. The same verification run confirmed CR-001 because cross-user DELETE succeeded.
