# Live demonstration guide

Target duration: 3–4 minutes, subject to the lecturer's time allocation. The group must rehearse and assign speakers. No team rehearsal is claimed here.

## Preparation

Use the included application snapshot. It preserves the supplied source and uses test fixtures with a temporary SQLite database per test. Install dependencies before presentation day and confirm the command in your own environment. The runtime used for the verified run was Python 3.12.14, Flask 3.0.3, pytest 9.1.1 and pytest-cov 7.1.0. The tests must use disposable accounts, not the group's live application database.

From the 09_Presentation folder in PowerShell:

```powershell
cd application
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip install pytest==9.1.1 pytest-cov==7.1.0
python -m pytest -p no:cacheprovider test_week7_verification.py -v --tb=short
```

Expected on the supplied baseline: **2 passed, 1 failed**. Exit code 1 is expected because the ownership assertion fails. This is the observed product defect, not a reason to alter the expectation.

## Presenter sequence

1. Explain the requirement: a user may delete only their own task.
2. Show the fresh-client test passing with HTTP 401.
3. Show cross-user GET denial passing, with owner access preserved.
4. Show the DELETE test failure: B receives 200, and owner A then receives 404. Read the tuple (200, 404) from the failure output.
5. Open the CR-001 entry in evidence/Defect_Log.md. Explain the isolated prerequisites, expected versus actual result, proposed Major/High classification and confirmed status.
6. State that source review finds DELETE by ID without an ownership predicate. A future authorised correction must also preserve the task and pass this regression test.

## Full suite, if requested

```powershell
python -m pytest -p no:cacheprovider test_helpers.py test_api_automation.py test_week7_verification.py -v --tb=short --junitxml=demo-results.xml
```

Recorded reference: **38 passed, 6 failed** across 44 functions. Actual new output may differ if the build, dependencies or environment change. Save and investigate differences rather than claiming the old result as a live run.

## Fallback

If dependencies or the environment fail, show `../07_Test_Management/Week 7/evidence/verification_2026_10_22/pytest_full_log.txt` and `results.xml`. Label them clearly as the saved 22 October 2026 run. Use Presentation_Content.md for the narrative. Never present saved evidence as a new live execution.

## Questions to rehearse

- Why does 100% helper coverage still have failures? It measures executed structure, while assertions check expected behaviour.
- Why does GET pass while DELETE fails? Each endpoint must enforce ownership independently.
- Why are there 198 records but only 44 functions here? Weekly manual records and overlapping mappings are a different population.
- Can the group claim ISO compliance or a CMMI level? No certification or appraisal took place.
- Why withhold acceptance despite many passes? A reproduced data-deletion vulnerability has material impact that a pass percentage cannot cancel.

## Packaged demo check

The included three-case demo was executed from this package: 2 Pass / 1 Fail, confirming the expected DELETE failure. See evidence/demo_check_log.txt and demo_check_results.xml. This technical check does not replace the group rehearsal or change the earlier 44-test run totals.
