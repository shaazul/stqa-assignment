# Execution and regression status

| Week | Population | Applicable planned | Assessed Pass+Fail | Pass | Fail | Blocked | Not Run | N/A | Assessment rate | Pass rate |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Black-box | 84 | 84 | 78 | 6 | 0 | 0 | 0 | 100.0% | 92.9% |
| 2 | White-box case records | 23 | 23 | 20 | 3 | 0 | 0 | 0 | 100.0% | 87.0% |
| 3 | GUI / compatibility / usability / accessibility | 25 | 25 | 21 | 4 | 0 | 0 | 1 | 100.0% | 84.0% |
| 4 | Web / API / comparisons | 36 | 36 | 33 | 3 | 0 | 0 | 0 | 100.0% | 91.7% |
| 5 | Security assessments (includes reused evidence) | 8 | 8 | 5 | 3 | 0 | 0 | 2 | 100.0% | 62.5% |
| 6 | Automation mapping rows | 15 | 15 | 13 | 2 | 0 | 0 | 0 | 100.0% | 86.7% |

## Interpretation

These are source-record counts, not a sum of independent executions. Assessment rate = (Pass + Fail) / applicable planned; pass rate = Pass / (Pass + Fail). N/A is excluded. Blocked and Not Run counts describe source statuses and do not mean no gaps exist.

Week 2 has 23 detailed case rows, but its summary, screenshots and current test_helpers.py contain 25 executed tests: 22 passed and 3 failed. The two additional tests cover default current-date/current-time arguments. Use 25 / 22 / 3 for the executed suite and 23 / 20 / 3 for the detailed case register until the missing rows are added.

Week 6 has 15 mapping/result rows (13 Pass, 2 Fail), but the saved pytest log reports 16 collected tests (14 Pass, 2 Fail). AUTO-08 and AUTO-14 both map to the same authenticated blank-title test, so 15 mapping rows are not 15 distinct functions. The focused Regression Suite has 10 rows: 8 Pass and 2 Fail. Its rows are a subset, not extra executions.

Week 5 SEC-05, SEC-06, SEC-07 and SEC-08 explicitly reuse earlier evidence. No new execution is asserted for these rows. Performance request counts are workload measurements, not functional test-case counts.

## Previously supplied validation log, 22 October 2026

`python -m pytest -p no:cacheprovider test_helpers.py -q` reproduces 22 Pass and 3 Fail. See `evidence/current_helpers_pytest.txt`. The three failures concern due today, exactly eight password characters, and completion exactly seven days ago. This is a new verification run and is kept separate from historical weekly counts. API automation was not rerun in this environment because Flask is absent; its status comes from the supplied log. No application code was changed.

## Repair reconciliation

The master register now contains 198 records: 194 original rows plus two Week 2 and two Week 6 supplemental functions previously documented only in the inventory. This does not add four new executions. Week 6 still contains one duplicate alias (AUTO-08/AUTO-14). Use 25 functions (22 Pass/3 Fail) for the saved helper run and 16 functions (14 Pass/2 Fail) for the saved API run. Do not sum those figures with overlapping workbook rows.

Week 1 has 78 source-record Pass statuses, but W1-API-11 and W1-API-12 are unverified after review. Of 84 source rows, 76 Pass claims are not challenged by this review, 6 are Fail, and 2 require retest. This is an evidence qualification, not a new execution or a claim that every other Pass has direct evidence.

Before the subsequent verification run, no tests had been executed during the document repair. Previously supplied logs remain evidence of their recorded runs only. Three additional verification cases were initially planned in Verification_Plan.md; keep these separate from the 198 historical/supplemental records.

## Verified run — 22 October 2026 (supersedes earlier execution-pending notes)

All three automated test files executed on the copied application using isolated temporary SQLite databases: 44 tests, 38 Pass, 6 Fail, no skips or setup errors. Helpers: 22 Pass/3 Fail; existing API suite: 14 Pass/2 Fail; Week 7 verification: 2 Pass/1 Fail. Evidence: [evidence/verification_2026_10_22/pytest_full_log.txt](evidence/verification_2026_10_22/pytest_full_log.txt); machine-readable results and environment are in the same folder. Source hashes match the included baseline.

D-001, D-002, D-004, D-006 and D-009 reproduced. CR-001 is now dynamically confirmed: B's DELETE returned HTTP 200 and A's subsequent GET returned HTTP 404. W7-VERIFY-01 and W7-VERIFY-02 passed. Current unauthenticated task access is blocked; D-005's historical discrepancy remains unresolved because historical builds are unknown. The historical W1-API-11/API-12 observations remain unchanged; new evidence establishes current GET protection and current DELETE failure.

This run does not execute all 198 documentation records. Manual GUI, browser compatibility, accessibility, historical web observations and performance experiments were not rerun. Structural coverage does not establish correctness: helpers have 100% measured statement/branch coverage while three assertions fail. Overall combined coverage of app.py/helpers.py is approximately 63%; this excludes browser templates, CSS and real browser behaviour.
