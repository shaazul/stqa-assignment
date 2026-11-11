# Standards integration and final presentation

PyTodo Pro, TEB3433 / TFB3433. Week 9 integration corresponds to course Week 12. This document contextualises the completed investigation. It does not claim ISO certification, a CMMI appraisal, an implemented CI pipeline or a rehearsed group presentation.

## ISO/IEC 25010

The mapping below uses the 2023 product quality model. ISO identifies nine characteristics in that edition. If lecture material uses the 2011 edition, its terms usability and portability correspond broadly to interaction capability and flexibility in the newer model, but the revisions include more than renaming. Confirm the lecturer's preferred edition before presenting. The following coverage judgements are the group's interpretation, not a conformity assessment.

| Characteristic | Evaluation and evidence | Remaining limitation |
|---|---|---|
| Functional suitability | Direct: EP/BVA, workflows, selected helper and API assertions. Current boundary and validation failures include D-001/D-002/D-004/D-006/D-009. | Sampled features and incomplete oracles do not establish full functional completeness/correctness. |
| Performance efficiency | Direct but narrow: historical 2/5-user, 30-second local task-GET experiments. | No SLA, production topology, endurance study or resource-use profiling. |
| Compatibility | Limited indirect evidence: selected Chrome/Edge configurations and UI/API comparison. | Browser rendering agreement does not establish model-wide coexistence or interoperability. |
| Interaction capability | Direct basic review: navigation, feedback, keyboard checks, labels and zoom. D-007/D-008 remain. | No full assistive-technology evaluation, measured contrast or comprehensive user study. |
| Reliability | Limited indirect evidence: repeatable isolated tests and observed request errors. | No endurance, failure injection, recovery or availability measurement. |
| Security | Direct selected checks: fresh-client authentication, cross-user GET/DELETE, input validation and STRIDE-oriented cases. CR-001 confirms unauthorised deletion. | Not a comprehensive penetration assessment. Historical authentication disagreement remains unresolved. |
| Maintainability | Limited indirect evidence: pure helper tests, coverage and isolated API fixtures support repeatable analysis. | No change-effort study, modularity assessment or complete maintainability evaluation. |
| Flexibility | Limited indirect evidence: selected configurations and small workload changes. | No controlled installation/deployment matrix, migration or meaningful scalability assessment. |
| Safety | Not formally evaluated. | No hazard analysis or safety acceptance criteria. Application context does not justify inventing a safety pass. |

Important inadequately evaluated areas include reliability, flexibility, maintainability, safety and interoperability. Even directly examined areas have incomplete coverage. Prioritise CR-001 ownership correction and regression, followed by uniqueness, category integrity and query handling. Browser/accessibility work and longer performance/recovery experiments remain necessary.

## ISO 9001 concepts

Use quality-management principles to explain process improvements rather than claiming certification. Evidence-based decisions use raw logs and the defect register. A process approach links requirements, procedures, results and residual risks. Continual improvement uses defect causes and evidence gaps to revise future work. Engagement of people means all four students contribute and a second member reviews the conclusions.

Concrete improvements: agree expected results before running tests, record source hashes and environment versions, peer-review authorisation queries, require reproduction plus regression evidence before closure, and retain original records when later findings contradict them. These are proposed improvements, not proof of an audited quality management system.

## CMMI concepts

CMMI describes improvement of organisational capability and performance. Consistent planning, canonical defect IDs and measurement are useful practices to discuss. In this project, mismatched row/function counts and incomplete build history show opportunities for more consistent management. Establish controlled baselines, define metric populations, assign review ownership and use repeated measurements to improve test selection. No formal appraisal occurred, so do not assign the group or application a CMMI maturity level.

## Agile, DevOps and continuous testing

For each backlog item, write acceptance examples and link them to test IDs. In refinement, review identity, access and boundary risks. A proposed definition of done includes reviewed requirements, relevant passing tests and documented residual risks. Peer review of task ownership predicates would help prevent recurrence of CR-001. Retrospectives should discuss why previous cross-user Pass records lacked adequate proof.

A proposed pull-request pipeline checks out an identified build, selects a recorded Python version, installs controlled dependencies, and runs isolated helper/API/ownership tests. It saves JUnit results, coverage and environment metadata even on failure. Known failures keep the gate unsuccessful until authorised corrections pass retest. Do not hide them with unconditional success or unsupported expected-failure markers. Run browser/accessibility checks separately and controlled performance work on a suitable schedule. Deployment remains conditional on accepted residual risk and passing release criteria. This package documents a proposal, not an installed workflow.

Current baseline: 44 automated functions, 38 Pass and 6 Fail. The 198 master documentation rows contain historical and overlapping records, so they are not a distinct execution total. Eleven canonical issues comprise eight Confirmed, two Open and one Retest. The group's proposed conclusion withholds production acceptance while allowing an educational local demonstration using disposable data.

## References

- [ISO/IEC 25010:2023 official overview](https://www.iso.org/standard/78176.html)
- [GSO standards preview describing the 2023 model revision](https://gso-sims-preview-doc-aws.s3-eu-west-1.amazonaws.com/gso-iso-iec-25010-2025-en.html)
- [ISO quality management principles](https://www.iso.org/publication/PUB100080.html)
- [CMMI capability and maturity levels](https://cmmiinstitute.com/learning/appraisals/levels)
- [GitHub documentation: building and testing Python](https://docs.github.com/en/actions/tutorials/build-and-test-code/python)
- Internal: `../07_Test_Management/Week 7/Verification_Results.md`, `Defect_Log.md`, `evidence/verification_2026_10_22/`, and `../08_Final_QA_Report/08_Final_QA_Report.md`.
