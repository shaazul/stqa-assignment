# Additional verification — executed 22 October 2026

These three cases were executed in the new verification run and remain separate from historical results. Use the isolated temporary database fixture and record actual results, timestamp, dependency versions and source hashes after execution.

| Case | Requirement | Purpose / function | Expected | Status |
|---|---|---|---|---|
| W7-VERIFY-01 | R-02 | test_clean_session_task_access_is_denied | Fresh client receives 401 and authentication required; reconcile D-005 | Pass |
| W7-VERIFY-02 | R-02; R-12 | test_cross_user_get_is_denied | B receives 403/404; A retains access | Pass |
| W7-VERIFY-03 | R-04; R-12 | test_cross_user_delete_is_denied_and_owner_task_survives | B receives 403/404; A retrieves identical task | Fail: B received 200; A then received 404 |

Procedure: from application/, install WEEKS_7_TO_9_README.md dependencies and run python -m pytest -p no:cacheprovider test_week7_verification.py -v. Save full output. A current Pass does not establish a historical fix. On failure, retain both unauthorized response and owner verification in the log; triage CR-001 with the observed evidence. Do not repair app.py as part of this QA assignment.

## Verified run — 22 October 2026 (supersedes earlier execution-pending notes)

All three automated test files executed on the copied application using isolated temporary SQLite databases: 44 tests, 38 Pass, 6 Fail, no skips or setup errors. Helpers: 22 Pass/3 Fail; existing API suite: 14 Pass/2 Fail; Week 7 verification: 2 Pass/1 Fail. Evidence: [evidence/verification_2026_10_22/pytest_full_log.txt](evidence/verification_2026_10_22/pytest_full_log.txt); machine-readable results and environment are in the same folder. Source hashes match the included baseline.

D-001, D-002, D-004, D-006 and D-009 reproduced. CR-001 is now dynamically confirmed: B's DELETE returned HTTP 200 and A's subsequent GET returned HTTP 404. W7-VERIFY-01 and W7-VERIFY-02 passed. Current unauthenticated task access is blocked; D-005's historical discrepancy remains unresolved because historical builds are unknown. The historical W1-API-11/API-12 observations remain unchanged; new evidence establishes current GET protection and current DELETE failure.

This run does not execute all 198 documentation records. Manual GUI, browser compatibility, accessibility, historical web observations and performance experiments were not rerun. Structural coverage does not establish correctness: helpers have 100% measured statement/branch coverage while three assertions fail. Overall combined coverage of app.py/helpers.py is approximately 63%; this excludes browser templates, CSS and real browser behaviour.
