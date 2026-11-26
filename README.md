# PyTodo Pro - Software Testing and Quality Assurance Project

Course: TEB3433 / TFB3433  
Semester: September 2026  
Application under test: PyTodo Pro

## Team details
This project was completed by the following group members:

1. **Farisha Binti Mohamad Zulkefli**
   - Student ID: 22001276
2. **Muhammad Danial Hakim bin Jul Ikhram**
   - Student ID: 22003590
3. **Elisa Filza Mizwan binti Lius**
   - Student ID: 22002775 
4. **Nurfarhana Najihah binti Mohd Fadli**
   - Student ID: 22003122 

## Project overview

This repository contains a progressive quality evaluation of PyTodo Pro, a Flask and SQLite task-management application. The project evaluates the supplied application rather than developing or repairing it. Testing covers functional behaviour, validation boundaries, selected white-box paths, GUI and accessibility observations, REST API behaviour, controlled security checks, short local performance experiments, automated regression, traceability, defect management and final quality evaluation.

The current verified automated run contains 44 tests: 38 passed and 6 failed. The failures reproduce incorrect date/password boundaries, duplicate registration, invalid category acceptance and a cross-user deletion defect. These results are evidence for the tested source snapshot and do not prove the whole product is defect-free.

## Repository structure

| Folder | Contents |
|---|---|
| `01_Black_Box` | Week 1 application analysis, black-box cases, execution results and defects |
| `02_White_Box_Coverage` | Week 2 helper tests, coverage analysis and screenshots |
| `03_Special_Testing` | Week 3 GUI, compatibility, usability and accessibility evidence |
| `04_Web_API` | Week 4 web/API scenarios, responses and defects |
| `05_Security_Performance` | Week 5 STRIDE, security checks and controlled performance results |
| `06_Automation_Regression` | Week 6 automation mapping, regression results and pytest evidence |
| `07_Test_Management` | Formal test plan, RTM, master cases, consolidated defects and verified execution evidence |
| `08_Final_QA_Report` | Integrated QA report, metrics tables and charts |
| `09_Presentation` | Written presentation content, standards integration, live-demo runbook and final checklist |

## Team details

Enter the four names and student IDs in `07_Test_Management/Week 7/Team_and_Approval.md`. The group must also record the reviewer, review date, approved quality conclusion and lecturer-confirmed deadline.

## Tools and environment

- Windows 11
- Python 3.12.14 for the verified 22 October 2026 run
- Flask 3.0.3 and Werkzeug 3.1.9
- pytest 9.1.1, pytest-cov 7.1.0 and coverage.py 7.16.2
- Postman for historical API work
- Locust for historical performance experiments
- Microsoft Edge 155.0.4283.62 and Google Chrome for selected GUI checks

Browser evidence is limited to the recorded configurations. The new UI evidence dated 23 October 2026 used Microsoft Edge 155.0.4283.62 with a 1920x1080 display and a 1920x1080 browser viewport.

## Setup

From `07_Test_Management/Week 7/application`:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip install pytest pytest-cov
```

Run the application:

```powershell
python app.py
```

Open `http://127.0.0.1:5000/` and register a disposable local account.

## Automated tests

Run all included suites:

```powershell
python -m pytest -p no:cacheprovider test_helpers.py test_api_automation.py test_week7_verification.py -v
```

Run coverage for the measured Python modules:

```powershell
python -m pytest -p no:cacheprovider test_helpers.py test_api_automation.py test_week7_verification.py --cov=helpers --cov=app --cov-branch --cov-report=term-missing
```

Known failures must remain visible until authorised development fixes are implemented and verified. Do not change expected results simply to make the suite pass.

## Current evidence summary

- Automated run: 38 passed, 6 failed, 44 total.
- Canonical issues: 11 total - 8 Confirmed, 2 Open and 1 Retest.
- Proposed severity: 3 Major, 7 Moderate and 1 Minor.
- `helpers.py`: 100% statement and branch coverage while three assertions fail.
- Combined measured `app.py` and `helpers.py` coverage.py result: approximately 62.6%.
- Short local performance experiments recorded zero task-GET failures at two and five users, but do not establish production capacity.
- Accessibility work is a basic review and does not establish WCAG conformance.

## Final submission

The Week 9 deliverable is maintained as written presentation content; a PowerPoint file is intentionally not required for this repository. Before submission, complete the personal/team fields, obtain group approval, confirm the deadline and rehearse the live demonstration. Follow `09_Presentation/Submission_Checklist.md`.
