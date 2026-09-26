# Evaluation evidence

`cases.json` contains 19 scenario specifications with expected behavior. The three domains are generic corporate presentations, sports exhibitions, and non-visual assessments. Their examples do not include private project artifacts.

`results.json` preserves a historical authoring-session assessment. Field names beginning with `historical` distinguish those reported results from a newly executed or reproducible test run.

The original assessment used subagents to respond to scenarios. They shared prior conversation context, and one had helped design the suite. The assessment therefore does **not** establish independent blind performance. Two prompts were clarified and rerun because the stated evidence did not support the intended maturity classification.

The reported perfect scores were manually assigned in that conversation. Raw answers, per-assertion grading evidence, and complete model metadata are absent here. Do not quote the scores as certified accuracy, independent validation, or proof of production readiness.

## Reproducible checks

```sh
python3 scripts/validate_eval_suite.py evals/cases.json
python3 -m unittest discover -s skills/project-lifecycle-pep/scripts -p 'test_*.py'
```

The first command checks case metadata and domain/topic coverage. The second runs the small deterministic validator test suite. Neither executes the scenario prompts against a model.

## Future behavioral runs

For a new behavioral evaluation, provide only each scenario and its necessary raw artifacts to a fresh evaluator. Keep expected answers and prior case-design discussion out of its context. Retain the response, skill version, model/version, run date, assertion-level grade, and any rerun reason. Grade evidence-sensitive decisions against actual supplied sources or record them as `NOT_CHECKED`.

Use the suite's release criteria as proposed thresholds. A version label or a passed structural check alone does not establish that every project gate passed.
