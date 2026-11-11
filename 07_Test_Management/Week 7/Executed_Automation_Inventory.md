# Executed automation inventory and reconciliation
This supplement resolves the source registers at function level. Historical workbook counts remain unchanged. The API statuses below come from the supplied Week 6 log, not a new execution.
## Week 6: sixteen distinct executed functions
| Function | Historical status | Workbook alias / additional coverage |
|---|---|---|
| test_unauthenticated_user_cannot_access_tasks | PASSED | AUTO-13 |
| test_unauthenticated_user_cannot_access_dashboard | PASSED | Supplemental W6-EXTRA-01: dashboard authentication |
| test_blank_title_request_without_login_is_rejected | PASSED | Supplemental W6-EXTRA-02: authentication occurs before title validation |
| test_registration_with_valid_details | PASSED | AUTO-01 |
| test_api_login_with_valid_credentials | PASSED | AUTO-05 |
| test_authenticated_user_cannot_create_task_with_blank_title | PASSED | AUTO-08 AND AUTO-14 (one function) |
| test_api_login_rejects_incorrect_password | PASSED | AUTO-06 |
| test_authenticated_user_can_create_task | PASSED | AUTO-07 |
| test_authenticated_user_can_update_task | PASSED | AUTO-09 |
| test_authenticated_user_can_complete_task | PASSED | AUTO-10 |
| test_authenticated_user_can_delete_task | PASSED | AUTO-11 |
| test_duplicate_registration_is_rejected | FAILED | AUTO-04 / D-002 |
| test_registration_rejects_username_below_minimum_length | PASSED | AUTO-02 |
| test_registration_rejects_short_password | PASSED | AUTO-03 |
| test_authenticated_user_can_search_tasks_by_title | PASSED | AUTO-12 |
| test_api_rejects_invalid_category_id | FAILED | AUTO-15 / D-009 |

The 15 workbook aliases cover 14 distinct functions because AUTO-08 and AUTO-14 duplicate one function. The two supplemental authentication functions bring the executed total to 16. This reconciles the saved log exactly.
## Week 2: two supplemental default-argument cases
The 23 workbook case rows correspond to the named boundary/type tests. Two additional functions in test_helpers.py explain the 25-test run:

### W2-EXTRA-01
- Requirement: R-05 / R-06 as appropriate; technique: default-argument branch test.
- Objective: Verify omitted today uses the current date.
- Preconditions: local Python/pytest; no database or app needed.
- Steps: run `python -m pytest -p no:cacheprovider test_helpers.py::test_urg_06_uses_current_date_when_today_not_provided -v`.
- Expected: Tomorrow is Due Soon.
- Actual/status: Pass in the current 25-test run; earlier coverage screenshot supports the aggregate 22 Pass / 3 Fail.
- Evidence: `evidence/current_helpers_pytest.txt`; input and exact function in `test_helpers.py`.
- Defect: none linked.

### W2-EXTRA-02
- Requirement: R-05 / R-06 as appropriate; technique: default-argument branch test.
- Objective: Verify omitted now uses the current time.
- Preconditions: local Python/pytest; no database or app needed.
- Steps: run `python -m pytest -p no:cacheprovider test_helpers.py::test_day_07_uses_current_time_when_now_not_provided -v`.
- Expected: One-day-old completion counts as recent.
- Actual/status: Pass in the current 25-test run; earlier coverage screenshot supports the aggregate 22 Pass / 3 Fail.
- Evidence: `evidence/current_helpers_pytest.txt`; input and exact function in `test_helpers.py`.
- Defect: none linked.

## Executable assertions as detailed procedures
The following assertions are transcribed from the existing test sources as implementation evidence. They do not introduce new runs. Exact fixture and input setup remains in the referenced source files.

### test_helpers.py::test_urg_01_no_due_date
```python
assert compute_urgency(None, today=date(2026, 10, 19)) == "No due date"
```

### test_helpers.py::test_urg_02_past_due_date
```python
assert compute_urgency("2026-10-18", today=date(2026, 10, 19)) == "Overdue"
```

### test_helpers.py::test_urg_03_due_today
```python
assert compute_urgency("2026-10-19", today=date(2026, 10, 19)) == "Due Today"
```

### test_helpers.py::test_urg_04_due_in_two_days
```python
assert compute_urgency("2026-10-21", today=date(2026, 10, 19)) == "Due Soon"
```

### test_helpers.py::test_urg_05_due_in_three_days
```python
assert compute_urgency("2026-10-22", today=date(2026, 10, 19)) == "Upcoming"
```

### test_helpers.py::test_pwd_01_wrong_type
```python
assert is_valid_password(None) is False
```

### test_helpers.py::test_pwd_02_seven_characters
```python
assert is_valid_password("abc1234") is False
```

### test_helpers.py::test_pwd_03_eight_characters
```python
assert is_valid_password("abc12345") is True
```

### test_helpers.py::test_pwd_04_nine_characters
```python
assert is_valid_password("abc123456") is True
```

### test_helpers.py::test_user_01_wrong_type
```python
assert is_valid_username(None) is False
```

### test_helpers.py::test_user_02_two_characters
```python
assert is_valid_username("ab") is False
```

### test_helpers.py::test_user_03_three_characters
```python
assert is_valid_username("abc") is True
```

### test_helpers.py::test_user_04_twenty_characters
```python
assert is_valid_username("abcdefghijklmnopqrst") is True
```

### test_helpers.py::test_user_05_twenty_one_characters
```python
assert is_valid_username("abcdefghijklmnopqrstu") is False
```

### test_helpers.py::test_user_06_underscore_allowed
```python
assert is_valid_username("user_01") is True
```

### test_helpers.py::test_user_07_space_disallowed
```python
assert is_valid_username("user name") is False
```

### test_helpers.py::test_user_08_hyphen_disallowed
```python
assert is_valid_username("user-name") is False
```

### test_helpers.py::test_day_01_missing_value
```python
assert completed_in_last_n_days(
        None, n=7, now=datetime(2026, 10, 19, 12, 0, 0)
    ) is False
```

### test_helpers.py::test_day_02_recent_completion
```python
assert completed_in_last_n_days(
        "2026-10-18 12:00:00",
        n=7,
        now=datetime(2026, 10, 19, 12, 0, 0),
    ) is True
```

### test_helpers.py::test_day_03_exactly_seven_days_ago
```python
assert completed_in_last_n_days(
        "2026-10-12 12:00:00",
        n=7,
        now=datetime(2026, 10, 19, 12, 0, 0),
    ) is True
```

### test_helpers.py::test_day_04_future_completion
```python
assert completed_in_last_n_days(
        "2026-10-20 12:00:00",
        n=7,
        now=datetime(2026, 10, 19, 12, 0, 0),
    ) is False
```

### test_helpers.py::test_day_05_completed_now
```python
assert completed_in_last_n_days(
        "2026-10-19 12:00:00",
        n=7,
        now=datetime(2026, 10, 19, 12, 0, 0),
    ) is False
```

### test_helpers.py::test_day_06_older_than_seven_days
```python
assert completed_in_last_n_days(
        "2026-10-11 12:00:00",
        n=7,
        now=datetime(2026, 10, 19, 12, 0, 0),
    ) is False
```

### test_helpers.py::test_urg_06_uses_current_date_when_today_not_provided
```python
assert compute_urgency(tomorrow) == "Due Soon"
```

### test_helpers.py::test_day_07_uses_current_time_when_now_not_provided
```python
assert completed_in_last_n_days(recent_completion) is True
```

### test_api_automation.py::test_unauthenticated_user_cannot_access_tasks
```python
assert response.status_code == 401
assert response.get_json()["error"] == "authentication required"
```

### test_api_automation.py::test_unauthenticated_user_cannot_access_dashboard
```python
assert response.status_code == 401
assert response.get_json()["error"] == "authentication required"
```

### test_api_automation.py::test_blank_title_request_without_login_is_rejected
```python
assert response.status_code == 401
assert response.get_json()["error"] == "authentication required"
```

### test_api_automation.py::test_registration_with_valid_details
```python
assert response.status_code == 201
```

### test_api_automation.py::test_api_login_with_valid_credentials
```python
assert registration.status_code == 201
assert response.status_code == 200
assert response.get_json()["username"] == "week6tester"
```

### test_api_automation.py::test_authenticated_user_cannot_create_task_with_blank_title
```python
assert registration.status_code == 201
assert response.status_code == 400
assert response.get_json()["error"] == "title is required"
```

### test_api_automation.py::test_api_login_rejects_incorrect_password
```python
assert registration.status_code == 201
assert response.status_code == 401
assert response.get_json()["error"] == "invalid credentials"
```

### test_api_automation.py::test_authenticated_user_can_create_task
```python
assert registration.status_code == 201
assert response.status_code == 201
assert task["title"] == "Week 6 automated task"
assert "id" in task
assert "urgency" in task
```

### test_api_automation.py::test_authenticated_user_can_update_task
```python
assert registration.status_code == 201
assert creation.status_code == 201
assert response.status_code == 200
assert response.get_json()["title"] == "Updated task title"
```

### test_api_automation.py::test_authenticated_user_can_complete_task
```python
assert registration.status_code == 201
assert creation.status_code == 201
assert response.status_code == 200
assert response.get_json()["done"] is True
```

### test_api_automation.py::test_authenticated_user_can_delete_task
```python
assert registration.status_code == 201
assert creation.status_code == 201
assert response.status_code in (200, 204)
assert check.status_code == 404
```

### test_api_automation.py::test_duplicate_registration_is_rejected
```python
assert first_registration.status_code == 201
assert second_registration.status_code in (400, 409)
```

### test_api_automation.py::test_registration_rejects_username_below_minimum_length
```python
assert response.status_code in (400, 422)
```

### test_api_automation.py::test_registration_rejects_short_password
```python
assert response.status_code in (400, 422)
```

### test_api_automation.py::test_authenticated_user_can_search_tasks_by_title
```python
assert registration.status_code == 201
assert first_task.status_code == 201
assert second_task.status_code == 201
assert response.status_code == 200
assert "STQA Search Target" in titles
assert "Unrelated Assignment" not in titles
```

### test_api_automation.py::test_api_rejects_invalid_category_id
```python
assert registration.status_code == 201
assert response.status_code == 400
```

## Verified run — 22 October 2026 (supersedes earlier execution-pending notes)

All three automated test files executed on the copied application using isolated temporary SQLite databases: 44 tests, 38 Pass, 6 Fail, no skips or setup errors. Helpers: 22 Pass/3 Fail; existing API suite: 14 Pass/2 Fail; Week 7 verification: 2 Pass/1 Fail. Evidence: [evidence/verification_2026_10_22/pytest_full_log.txt](evidence/verification_2026_10_22/pytest_full_log.txt); machine-readable results and environment are in the same folder. Source hashes match the included baseline.

D-001, D-002, D-004, D-006 and D-009 reproduced. CR-001 is now dynamically confirmed: B's DELETE returned HTTP 200 and A's subsequent GET returned HTTP 404. W7-VERIFY-01 and W7-VERIFY-02 passed. Current unauthenticated task access is blocked; D-005's historical discrepancy remains unresolved because historical builds are unknown. The historical W1-API-11/API-12 observations remain unchanged; new evidence establishes current GET protection and current DELETE failure.

This run does not execute all 198 documentation records. Manual GUI, browser compatibility, accessibility, historical web observations and performance experiments were not rerun. Structural coverage does not establish correctness: helpers have 100% measured statement/branch coverage while three assertions fail. Overall combined coverage of app.py/helpers.py is approximately 63%; this excludes browser templates, CSS and real browser behaviour.
