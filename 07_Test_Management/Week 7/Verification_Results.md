# Automated verification results — 22 October 2026

44 tests executed: **38 passed, 6 failed**. No application source was changed. Temporary isolated databases were used, and all 14 copied source hashes still match the baseline.

| Suite | Pass | Fail |
|---|---:|---:|
| Helpers | 22 | 3 |
| Existing API automation | 14 | 2 |
| Week 7 verification | 2 | 1 |
| Total | 38 | 6 |

| Defect | Reproduced failure |
|---|---|
| D-004 | Due today classified as Overdue |
| D-001 | Exactly eight password characters rejected |
| D-006 | Completion exactly seven days ago excluded |
| D-002 | Duplicate username accepted, HTTP 201 |
| D-009 | Invalid category accepted, HTTP 201 |
| CR-001 | User B deletes A's task, HTTP 200; A subsequently receives 404 |

Unauthenticated task access and cross-user GET denial passed on this baseline. Historical observations are preserved; a current pass does not prove when or why earlier behaviour differed. The new run confirms CR-001 as Major/High under the proposed triage scheme.

Helpers achieved 100% measured statement/branch coverage despite three failing assertions. app.py measured approximately 58% combined coverage; combined app/helpers coverage was approximately 63%. These are structural measures for this run, not proof of whole-product quality.

[Full execution log](evidence/verification_2026_10_22/pytest_full_log.txt) · [Individual results](evidence/verification_2026_10_22/results.xml) · [Coverage](evidence/verification_2026_10_22/coverage.json) · [Environment](evidence/verification_2026_10_22/environment.json)

The 198 documentation records include historical manual and overlapping tests. This automated run does not re-execute every manual, UI, accessibility or performance record. Those require separate procedures and fresh evidence. No application defects were fixed because the assignment evaluates the supplied application.
