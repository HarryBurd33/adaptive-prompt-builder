# Private prompt-builder evaluation suite

Frozen design for 9 behavioral cases and 6 independent activation cases. No runs have been performed by this package's designer.

- `inputs.json`: executor-safe synthetic inputs and orchestration protocol; no expected answers.
- `cases.json`: private checklists, question budgets, critical failures, and activation labels.
- `rubric.md`: private grading, comparison, evidence, and release gates.
- `FREEZE.json`: content hashes and design provenance.

Use an independent executor for each baseline/candidate case and an independent grader. Give executors only their selected input and assigned guidance. B01 is a controlled three-turn script; B03/B04 contain explicitly authored fixed history. Replace `{{CASE_OUTPUT_DIR}}` in B08/B09 with fresh isolated absolute directories inside the authorized run-output area. Read actual artifacts when grading.

Do not give private evaluator files to the candidate author or executor. “Held out” remains conditional on that separation. Keep the original frozen files intact; save later run outputs and any evaluation-design revision separately.
