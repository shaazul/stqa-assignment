# Presentation content and speaker notes

Suggested duration: 10–12 minutes plus a 3–4 minute demo, subject to lecturer guidance. Suggested coordination: QA lead introduces scope and conclusion; test-design coordinator explains methods and quality mapping; automation coordinator presents results and demo; defect/metrics coordinator explains defects, limitations and process improvements. Assign actual names before presenting.

## Slide 1: PyTodo Pro

Software testing and quality assurance

Final presentation and quality evaluation

TEB3433 / TFB3433

September 2026 semester

01

Speaker notes: Explain that the group evaluates the supplied application without changing its source. Enter the four student names and IDs in the final group template or presenter introduction. Sources: Group Project.pdf, Week 7 Test_Plan_and_Strategy.md.

## Slide 2: QA investigation

Black-box design established input and date boundaries.

White-box testing examined selected helpers.

GUI, API, security and performance checks extended the evidence.

Week 7 reconciled cases and defects before final evaluation.

02

Speaker notes: Describe the progression, including how later API evidence contradicted an earlier authentication observation. Original records remain unchanged. Sources: Week 7 Source_Records.md and Week 8 Final_QA_Report.md.

## Slide 3: 44 automated tests: 38 passed, 6 failed

38 / 44 passed

86.4% pass rate

New automated run only

22 October 2026

03

Speaker notes: The 22 October 2026 run uses Python 3.12.14, Flask 3.0.3 and isolated temporary SQLite databases. These 44 functions differ from 198 historical documentation records. Do not add reused weekly evidence to the new execution count. Source: `../07_Test_Management/Week 7/evidence/verification_2026_10_22/results.xml`.

## Slide 4: Confirmed ownership failure

User A creates a disposable task.

User B deletes it through the task API and receives HTTP 200.

User A then requests the task and receives HTTP 404.

CR-001: proposed Major severity and High priority

04

Speaker notes: GET protection passes, but it does not establish DELETE protection. The code deletes by task ID without a user_id predicate. Demonstrate only with the included isolated test fixture. Source: test_week7_verification.py and pytest_full_log.txt.

## Slide 5: Other reproduced failures

Duplicate registration returns HTTP 201.

Invalid category IDs create tasks.

Due-today tasks appear as Overdue.

Eight-character passwords and the seven-day completion boundary fail.

05

Speaker notes: Map these to D-002, D-009, D-004, D-001 and D-006. Eleven canonical issues exist in the combined register: eight Confirmed, two Open and one Retest. D-010 SQL-like search remains historically confirmed but was not rerun in the new 44-test suite. Sources: Week 7 Defect_Log.md and verification results.

## Slide 6: Coverage and correctness

Helpers reach 100% statement and branch coverage.

Three helper assertions still fail.

app.py statement coverage is 60.5%, with 43.8% branch coverage.

Substantial web-route and browser behaviour remains outside the run.

06

Speaker notes: The combined coverage.py measure differs from statement coverage. app.py combined measure is 57.6%; app.py plus helpers.py combined measure is 62.6%. Do not describe 58% as statement coverage or 100% helper coverage as product correctness. Source: coverage.json.

## Slide 7: Historical UI and accessibility evidence

Chrome and Edge checks cover selected local configurations.

Label association and task-creation feedback need improvement.

Zoom evidence reaches 125%.

Screen readers, measured contrast and full mobile coverage remain gaps.

07

Speaker notes: These are primarily historical Week 3 findings and do not establish WCAG conformance. New UI evidence dated 23 October 2026 used Microsoft Edge 155.0.4283.62 at a 1920x1080 display/viewport and directly reproduced whitespace-title acceptance and missing creation feedback. Sources: `../03_Special_Testing/`, `../07_Test_Management/Week 7/UI_Evidence_2026_10_23.md` and its screenshots.

## Slide 8: Small local performance experiments

2 users: 41 task GETs in 30 seconds, p95 16 ms

5 users: 97 task GETs in 30 seconds, p95 15 ms

Both recorded zero task GET failures.

Short local runs cannot establish production capacity.

08

Speaker notes: Historical Week 5 observations only. Mean GET latency was 10.26 and 10.82 ms. For five users, the screenshot includes 102 aggregate requests including login, which must not be confused with 97 task GETs. No SLA was specified. Sources: PERF-02.png, PERF-03.png and Week 8 report.

## Slide 9: ISO/IEC 25010 quality mapping

Functional suitability: workflow and boundary failures

Security: authentication, ownership and input checks

Performance efficiency: limited local workload evidence

Interaction capability: GUI, usability and accessibility review

09

Speaker notes: Use ISO/IEC 25010:2023 terminology. A class using the 2011 model may use usability for interaction capability, and portability for flexibility. Mapping is the group’s interpretation of evidence, not a conformity claim. Official source: https://www.iso.org/standard/78176.html. Detailed mapping: Standards_Integration.md.

## Slide 10: Quality characteristics with evidence gaps

Compatibility: browser checks cover only selected configurations.

Maintainability: isolated tests offer limited indirect evidence.

Reliability and flexibility need longer runs and deployment testing.

Safety has no formal hazard assessment in this project.

10

Speaker notes: ISO/IEC 25010:2023 has nine product quality characteristics. Compatibility in the model includes coexistence/interoperability, so browser coverage is only a limited proxy. No formal maintainability evaluation, recovery test, portability/scalability study or safety analysis is claimed. Source: ISO page and Standards_Integration.md.

## Slide 11: ISO 9001 and CMMI process improvements

Documented cases and source hashes support repeatable review.

Canonical defect IDs preserve traceability across weeks.

Peer review should check ownership and boundary conditions.

Retest evidence must support every defect closure.

11

Speaker notes: Apply quality-management principles such as evidence-based decision making and continual improvement. For CMMI, relate documented and measured practices to improvement opportunities without assigning a maturity level. Sources: https://www.iso.org/publication/PUB100080.html and https://cmmiinstitute.com/learning/appraisals/levels. No certification or appraisal occurred.

## Slide 12: Regression testing in Agile and CI/CD

A pull request installs the recorded test dependencies.

Isolated helper and API tests produce JUnit and coverage evidence.

Known failing assertions keep the quality gate unsuccessful.

Browser and accessibility reviews remain additional checks.

12

Speaker notes: This is a proposed pipeline, not an implemented or executed CI workflow. Preserve failing assertions instead of marking them successful. A developer correction must pass retest and peer review. Continuous testing extends feedback through the lifecycle, including periodic browser and performance work. Source: https://docs.github.com/en/actions/tutorials/build-and-test-code/python.

## Slide 13: Live demonstration

Run the three isolated Week 7 verification cases.

Show two successful access checks and the failed DELETE check.

Trace the failure to CR-001 and its reproduction evidence.

Use the saved log if the local environment is unavailable.

13

Speaker notes: Target 3–4 minutes for the demonstration. The expected outcome on the supplied baseline is two passes and one failure. Do not claim a rehearsed team demo: the group still needs to allocate speakers and rehearse. See Live_Demo.md for commands, setup, failure interpretation and fallback.

## Slide 14: Quality conclusion

Common workflows succeed, but important defects remain.

Ownership, identity and category integrity take priority.

Historical manual findings and residual risks remain visible.

The evidence does not support production acceptance.

14

Speaker notes: Proposed group decision: continue educational demonstration with disposable data and withhold production acceptance. The assignment evaluates the application, so no source corrections are included. Team approval and identities remain pending. Sources: Week 8 Final_QA_Report.md and Week 7 Defect_Log.md.

